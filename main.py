import logging
import os
# from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram import Bot, Dispatcher, executor, types
import apimethod

# load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')

# Настройка ведения журнала логирования
logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class Get_Rates(StatesGroup):
    pair = State()

class Get_Stat(StatesGroup):
    pair = State()   


# Опрашиваем юзера
@dp.message_handler(commands=['pair'])
async def q1(message: types.Message):
    await message.answer(
        'Введите название пары'
    )
    await Get_Rates.pair.set()

# Даём ответ
@dp.message_handler(state=Get_Rates.pair)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer(apimethod.get_price(answer))

    await state.finish()


# Опрашиваем юзера
@dp.message_handler(commands=['24stat'])
async def q2(message: types.Message):
    await message.answer(
        'Введите название пары'
    )
    await Get_Stat.pair.set()

# Даём ответ
@dp.message_handler(state=Get_Stat.pair)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await message.answer(apimethod.get_24h_statistic(answer))

    await state.finish() 


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer(
        '✅Вызовите в меню команду /pair\n'
        '✅Введите название пары торгуемой\nна Binance\n'
        '✅Формат ввода: btcusdt'
    )


@dp.message_handler(commands=['btc'])
async def get_btc(message: types.Message):
    await message.answer(apimethod.get_price('btcusdt'))


@dp.message_handler(commands=['eth'])
async def get_eth(message: types.Message):
    await message.answer(apimethod.get_price('ethusdt'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
