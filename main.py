from aiogram import Bot, Dispatcher, executor, types
import logging
from bot.api.films import Film
from bot.utils.telegram import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.channel_post_handler(content_types=['video'])
async def channel_post(message: types.Message):
    if message.video:
        film = Film()
        message_id = message.message_id
        file_unique_id = message.video.file_unique_id
        film.update_film_message_id(message_id, file_unique_id)


if '__main__' == __name__:
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
