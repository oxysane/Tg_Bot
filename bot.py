import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Get token from environment variable
TOKEN = os.getenv('BOT_TOKEN')


if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables!")


# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start_command(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("FoFNews Channel", url="https://t.me/FoFNews"),
            InlineKeyboardButton("Trust Test Bot", url="http://t.me/trust_Test88_Bot/Trusts"),
            InlineKeyboardButton("X.com", url="https://x.com")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome to our Telegram Bot! 🚀\n\n"
        "Discover our channels and resources:\n\n"
        "• FoFNews: Stay updated with the latest news\n"
        "• Trust Test Bot: Explore our trusted services\n"
        "• X.com: Visit our main platform\n\n"
        "Click the buttons below to explore!",
        reply_markup=reply_markup
    )


async def handle_image(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("FoFNews Channel", url="https://t.me/FoFNews"),
            InlineKeyboardButton("Trust Test Bot", url="http://t.me/trust_Test88_Bot/Trusts"),
            InlineKeyboardButton("X.com", url="https://x.com")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Thanks for sending an image! 📸\n\n"
        "Check out our channels and resources:",
        reply_markup=reply_markup
    )


def create_app():
    """Initialize bot application"""
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))
    
    return application


app = create_app()


if __name__ == '__main__':
    logger.info("Starting bot...")
    app.run_polling(drop_pending_updates=True)