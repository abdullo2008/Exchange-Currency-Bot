from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Cовершить обмен', callback_data='exchange'),
        ],
        [
            InlineKeyboardButton(text='Получить инструкции', callback_data="instructions")
        ],
        [
            InlineKeyboardButton(text='Посмотреть видео инструкцию', callback_data="instruction_vid")
        ],
        [
            InlineKeyboardButton(text='Гарантии', url="https://t.me/PhuketRealEst")
        ],
    ]
)

# all_currencies = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='RUB 🇷🇺 на')
#         ],
#         [
#             KeyboardButton(text='USDT 💲 на')
#         ],
#         # [
#         #     KeyboardButton(text="Назад 🔙", callback_data='all_currencies_back')
#         # ]
#     ], resize_keyboard=True
# )

all_currencies = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Обменять Рубли на Баты'),
        ],
        [
            KeyboardButton(text='Обменять Рубли на USDT'),
        ],
        [
            KeyboardButton(text='Обменять USDT на Баты'),
        ],
        [
            KeyboardButton(text='Обменять USDT на Рубли'),
        ],
    ], resize_keyboard=True
)

