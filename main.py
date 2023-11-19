import os
import logging
from uuid import uuid4
from telegram import Update, InlineQueryResultCachedVoice, InlineQueryResultCachedVideo
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text("Hi!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text("Help!")


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query

    if not query:  # empty query should not be handled
        return

    results = [
        InlineQueryResultCachedVoice(
            id=str(uuid4()),
            voice_file_id="AwACAgIAAxkBAAMPZTlTkqT6jQsoYVLOcGXsrhSwqNYAArA7AALecMlJHZIG-3NJc9owBA",
            title="about suicide",
        ),
        InlineQueryResultCachedVoice(
            id=str(uuid4()),
            voice_file_id="AwACAgIAAxkBAAMUZTlUtWZGCgNj98vJayw2Cwwo1zsAAg0uAAIoqnBI2wEZSO8mmtEwBA",
            title="Alina",
        ),
        InlineQueryResultCachedVoice(
            id=str(uuid4()),
            voice_file_id="AwACAgIAAxkBAAMVZTlZkndjljECJTqABPnlyS4XMLUAAr8-AAIUeqBJC5xpM0hXJdUwBA",
            title="уУУуУууууу",
        ),
        InlineQueryResultCachedVoice(
            id=str(uuid4()),
            voice_file_id="AwACAgIAAxkBAAMWZTlZtPNsZyxjWesxk8qk0LS9jNgAAjo0AAKkyMBLTtOCd6Rr5UUwBA",
            title="Кіріл Прігожін",
        ),
        InlineQueryResultCachedVoice(
            id=str(uuid4()),
            voice_file_id="AwACAgIAAxkBAAMXZTlZ4jsBMUXPvPsVo6Ji89HKun4AAjstAAKUTMFLEnaG8GtG-88wBA",
            title="Хіхоньки та хахоньки",
        ),
        InlineQueryResultCachedVoice(
            id=str(uuid4()),
            voice_file_id="AwACAgIAAxkBAAMYZTlaFceLlwiJZE0za2JtJuoVotsAAmA_AALc_olL0hAUBtJFctowBA",
            title="Концерт Мазелова",
        ),
        InlineQueryResultCachedVoice(
            id=str(uuid4()),
            voice_file_id="AwACAgIAAxkBAAMZZTlaPP0Y68g3Yrzt4bXwuDCGx10AAtA0AAKHPFlLcHyK2NZFP7owBA",
            title="Тілі-тілі-бом",
        ),
        InlineQueryResultCachedVideo(
            id=str(uuid4()),
            video_file_id="DQACAgIAAxkBAAMaZTlbB8d5ECvg9H5r7B4PJJyl_D0AAto6AAL2GNBJIvg7_hFyKDIwBA",
            title="Пук",
            caption="Пук",
        ),
        InlineQueryResultCachedVideo(
            id=str(uuid4()),
            video_file_id="DQACAgIAAxkBAAMbZTlbSquti1BETuvEOKc6vFz-YFIAArY1AAKea_BICLjtxOasKAcwBA",
            title="Важко",
            caption="Важко",
        ),
        InlineQueryResultCachedVideo(
            id=str(uuid4()),
            video_file_id="DQACAgIAAxkBAAMcZTlgJFtXqjz2lRjGPecxc67n8lwAAgQ7AAL2GNBJ1voUoIPI2U8wBA",
            title="Будьмо",
            caption="Будьмо",
        ),
        InlineQueryResultCachedVideo(
            id=str(uuid4()),
            video_file_id="DQACAgIAAxkBAAMdZTlgNEbXhf4fzDiy55wHJ4wgrY0AAhcIAAILP2FIXF611GL3wL4wBA",
            title="Ага",
            caption="Ага",
        ),
        InlineQueryResultCachedVideo(
            id=str(uuid4()),
            video_file_id="DQACAgIAAxkBAAMeZTlgZn5p0WAWv-Bfc2VCDN5vKl0AAhIDAAKVnXFJNfjApbfLwjYwBA",
            title="Лесная братва",
            caption="Лесная братва",
            description="Діди пють пиво"
        ),
        InlineQueryResultCachedVideo(
            id=str(uuid4()),
            video_file_id="DQACAgIAAxkBAAM7ZVp2hIU4s3QIm9TchaLXUV3VzLgAAsY4AAIrg9FK2nWjy01ZO3wzBA",
            title="Фейс палм",
            caption="Фейс палм",
            description="Фейс палм"
        ),
        InlineQueryResultCachedVideo(
            id=str(uuid4()),
            video_file_id="DQACAgIAAxkBAAM6ZVp2e3dWR5qwKM-JWN88izleeacAAsk4AAIrg9FKNFLccIHIwAQzBA",
            title="Чисті зуби",
            caption="Чисті зуби",
            description="Чисті зуби"
        ),
    ]

    await update.inline_query.answer(results)


def main() -> None:

    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on inline queries - show corresponding inline results
    application.add_handler(InlineQueryHandler(inline_query))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
