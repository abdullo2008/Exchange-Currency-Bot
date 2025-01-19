from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile
from app.keyboards import start_kb, all_currencies

from config import BOT_ADMINS

router = Router()


class AddOperator(StatesGroup):
    add = State()


class DeleteOperator(StatesGroup):
    delete = State()


@router.message(Command("start"))
async def cmd_start(message: Message):
    user_name = message.from_user.full_name
    if message.chat.id not in BOT_ADMINS:
        for admin_id in BOT_ADMINS:
            await message.bot.send_message(admin_id, f"User {message.from_user.id} sent: {message.text}")

    await message.answer(f'Добрый день, <b>{message.from_user.full_name}</b>!\n\n'
                         f'✨ Рады приветствовать вас в нашем надежном обменном боте! 💸🔄\n\n'
                         f'Здесь вы можете быстро, выгодно и качественно обменивать валюты 💵🌍\n\n',
                         parse_mode="HTML", reply_markup=start_kb)

    await message.answer(
        f"Добро пожаловать, {user_name}!\n"
        "Наш менеджер скоро свяжется с вами!"
    )


@router.callback_query(F.data == "all_currencies_back")
async def all_currencies_back(callback: CallbackQuery):
    await callback.message.edit_text(f'Добрый день, <b>{callback.message.from_user.full_name}</b>!\n\n'
                                     f'✨ Рады приветствовать вас в нашем надежном обменном боте! 💸🔄\n\n'
                                     f'Здесь вы можете быстро, выгодно и качественно обменивать валюты 💵🌍\n\n',
                                     parse_mode="HTML", reply_markup=start_kb)


@router.callback_query(F.data == 'instructions')
async def instructions(callback: CallbackQuery):
    await callback.answer()
    photo = FSInputFile("static\IMG_6947.jpeg")
    await (callback.message.
           answer_photo(photo=photo,
                        caption="🔍- методом сканирования\n"
                                "🔢 - по пин-коду\n\n"
                                "Банкоматы можно найти возле магазинов seven eleven \n\n"
                                "🗺 - через приложение «google maps» написав название банкомата\n\n"
                                "💬 Так же вы можете прислать нам в чат вашу геолокацию и мы найдем ближайший "
                                "подходящий банкомат\n\n\n"
                                "👇Инструкция по ссылке👇\n\n"
                                "[🟩ATM K-Bank 🔍](https://t.me/PhuketRealEst/975)\n\n"
                                "[🟦ATM Bangkok Bank 🔍](https://t.me/PhuketRealEst/976)\n\n"
                                "[🟨ATM Krungsri Bank 🔢](https://t.me/PhuketRealEst/977)\n\n"
                                "[🟪АTM SCB bank 🔢](https://t.me/PhuketRealEst/978)\n\n"
                                "[🔹ATM Krungthai bank 🔢](https://t.me/PhuketRealEst/979)\n\n"
                                "[Суточные лимиты на наличные из банкоматов](https://t.me/PhuketRealEst/980)",
                        parse_mode="Markdown"
                        )
           )


@router.callback_query(F.data == 'instruction_vid')
async def instruction_vid(callback: CallbackQuery):
    await callback.answer()
    video = FSInputFile("static\\tut_video.mp4")
    await callback.message.answer_video(video=video,
                                        caption="<b>Trust Exchange | Проверенный сервис обмена и перестановки "
                                                "денег</b>\n"
                                                "Процесс получения наличных бат без карты  через банкомат "
                                                "Kasikorn Bank 😀", parse_mode="HTML")


request_id = 31493


@router.callback_query(F.data == "exchange")
async def exchange(callback: CallbackQuery):
    await callback.answer()
    global request_id
    request_id += 1
    await callback.message.answer(
        f"Ваша заявка создана: <b>#{request_id}</b>\n"
        f"ДОБРОГО ВРЕМЕНИ СУТОК, КАКУЮ СУММУ ВЫ БЫ ХОТЕЛИ ОБМЕНЯТЬ?:",
        parse_mode="HTML", reply_markup=all_currencies
    )


@router.message(F.text == "Обменять Рубли на Баты")
async def rub_to_thb(message: Message):
    user_id = message.from_user.id
    if message.chat.id not in BOT_ADMINS:
        for admin_id in BOT_ADMINS:
            await message.bot.send_message(admin_id,
                                           f"Пользователь {user_id}\nОтправил(а): {message.text}")
    await message.answer(f"Укажите сумму которую вы хотите обменять 🇷🇺 🔄 🇹🇭:")


@router.message(F.text == "Обменять Рубли на USDT")
async def rub_to_usdt(message: Message):
    user_id = message.from_user.id
    if message.chat.id not in BOT_ADMINS:
        for admin_id in BOT_ADMINS:
            await message.bot.send_message(admin_id,
                                           f"Пользователь {user_id}\nОтправил(а): {message.text}")
    await message.answer(f"Укажите сумму которую вы хотите обменять 🇷🇺 🔄 💲:")


@router.message(F.text == "Обменять USDT на Баты")
async def usdt_to_thb(message: Message):
    user_id = message.from_user.id
    if message.chat.id not in BOT_ADMINS:
        for admin_id in BOT_ADMINS:
            await message.bot.send_message(admin_id,
                                           f"Пользователь {user_id}\nОтправил(а): {message.text}")
    await message.answer(f"Укажите сумму которую вы хотите обменять 💲 🔄 🇹🇭:")


@router.message(F.text == "Обменять USDT на Рубли")
async def usdt_to_rub(message: Message):
    user_id = message.from_user.id
    if message.chat.id not in BOT_ADMINS:
        for admin_id in BOT_ADMINS:
            await message.bot.send_message(admin_id,
                                           f"Пользователь {user_id}\nОтправил(а): {message.text}")
    await message.answer(f"Укажите сумму которую вы хотите обменять 💲 🔄 🇷🇺:")


def setup_handlers(dp, bot):
    @router.message(lambda message: message.from_user.id == BOT_ADMINS)
    async def admin_answers(message: Message):
        try:
            user_test = message.reply_to_message.text
            user_id = user_test.split('\n')[0]
            await bot.send_message(chat_id=user_id, text=message.text)
        except:
            pass

    @router.message()
    async def user_message_handler(message: Message):
        if message.chat.id not in BOT_ADMINS:
            for admin_id in BOT_ADMINS:
                await message.bot.send_message(admin_id, f"ID пользователя {message.from_user.id}\n"
                                                         f"Сообщение: {message.text}")
        elif message.from_user.id in BOT_ADMINS:
            try:
                parts = message.text.split(": ", 1)
                if len(parts) == 2:
                    user_id_str, user_message = parts
                    try:
                        user_id = int(user_id_str)
                        await bot.send_message(user_id, user_message)

                        for admin_id in BOT_ADMINS:
                            if admin_id != message.from_user.id:
                                await bot.send_message(admin_id,
                                                       f"Admin {message.from_user.id} sent this to user {user_id}: {message.text}")

                        await message.answer(f"Сообщение отправлено пользователю {user_id}.")
                    except ValueError:
                        await message.answer("ID пользователя должен быть действительным целым числом.")
                else:
                    await message.answer("Пожалуйста, укажите как ID пользователя, так и текст сообщения.\n"
                                         "Пример, 1234567890: и сообщение.")
            except Exception as e:
                await message.answer(f"Не удалось отправить сообщение: {e}")
