import os
import logging
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ConversationHandler,
)
from telegram.error import TelegramError, NetworkError, TimedOut

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define states as integers
START, TELL_MORE, READY = range(3)

# Define the handlers for each state
async def start(update: Update, context) -> int:
    """Sends a welcome message with options."""
    try:
        keyboard = [
            [InlineKeyboardButton("1️⃣ Yes, let's start!", callback_data='start_now')],
            [InlineKeyboardButton("2️⃣ Tell me more about the offers.", callback_data='tell_more')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Welcome to bulgefx 🚀\n\n"
            "Start your trading journey with us and enjoy a deposit bonus, free daily trading signals, "
            "exclusive educational content, and access to our smart trading bot for passive income.\n\n"
            "Would you like to create your account now?\n\n"
            "💡 You can click the buttons above or simply type:\n"
            "• Type '1' or 'yes' to get started\n"
            "• Type '2' or 'more' to learn about our offers",
            reply_markup=reply_markup
        )
        logger.info(f"Start command executed for user {update.effective_user.id}")
        return START
    except TelegramError as e:
        logger.error(f"Error in start handler: {e}")
        return START

# Using a callback query handler is more robust for buttons
async def handle_start_callback(update: Update, context) -> int:
    """Handles the callback queries from inline buttons."""
    try:
        query = update.callback_query
        await query.answer()  # Acknowledge the button press

        if query.data == 'start_now':
            await query.edit_message_text(
                "Awesome! Click the link below to create your account and claim your deposit bonus:\n\n"
                "👉 Create Your Account Now: https://member.bulgefx.com/client/register/6898c2449fdf2\n\n"
                "💬 Join our Telegram community: https://t.me/bulgefxgroup\n\n"
                "If you have any questions, just type /help"
            )
            logger.info(f"User {query.from_user.id} clicked 'start_now'")
            return ConversationHandler.END

        elif query.data == 'tell_more':
            await query.edit_message_text(
                "Here's what you get when you join:\n\n"
                "💰 Deposit Bonus: Get up to 20% bonus on your first deposit.\n"
                "📈 Free Trading Signals: Daily tips from expert traders.\n"
                "🎓 Education: Tutorials, webinars, and e-books.\n"
                "🤖 Trading Bot Access: Automate your trades and generate passive income.\n\n"
                "Ready to create your account? Reply Yes to begin."
            )
            logger.info(f"User {query.from_user.id} clicked 'tell_more'")
            return TELL_MORE
            
    except TelegramError as e:
        logger.error(f"Error in callback handler: {e}")
        return START

# Handler for text input in START state
async def handle_start_text(update: Update, context) -> int:
    """Handles text input in the START state."""
    try:
        user_text = update.message.text.lower().strip()
        
        # Handle option 1 variations
        if user_text in ['1', 'yes', 'yep', 'yeah', 'start', 'lets start', "let's start"]:
            await update.message.reply_text(
                "Awesome! Click the link below to create your account and claim your deposit bonus:\n\n"
                "👉 Create Your Account Now: https://member.bulgefx.com/client/register/6898c2449fdf2\n\n"
                "💬 Join our Telegram community: https://t.me/bulgefxgroup\n\n"
                "If you have any questions, just type /help"
            )
            logger.info(f"User {update.effective_user.id} chose option 1 via text")
            return ConversationHandler.END
            
        # Handle option 2 variations
        elif user_text in ['2', 'more', 'tell me more', 'info', 'information', 'offers']:
            await update.message.reply_text(
                "Here's what you get when you join:\n\n"
                "💰 Deposit Bonus: Get up to 20% bonus on your first deposit.\n"
                "📈 Free Trading Signals: Daily tips from expert traders.\n"
                "🎓 Education: Tutorials, webinars, and e-books.\n"
                "🤖 Trading Bot Access: Automate your trades and generate passive income.\n\n"
                "Ready to create your account? Reply Yes to begin."
            )
            logger.info(f"User {update.effective_user.id} chose option 2 via text")
            return TELL_MORE
        else:
            await update.message.reply_text(
                "Please choose an option:\n"
                "• Type '1' or 'yes' to get started\n"
                "• Type '2' or 'more' to learn about our offers\n"
                "• Or use the buttons above"
            )
            return START
    except TelegramError as e:
        logger.error(f"Error in start text handler: {e}")
        return START

# Handler for 'Yes' after "Tell me more..."
async def handle_yes_response(update: Update, context) -> int:
    """Handles the user typing 'Yes' or variations."""
    try:
        user_text = update.message.text.lower().strip()
        
        # Accept various forms of 'yes'
        if user_text in ['yes', 'yep', 'yeah', 'y', 'sure', 'ok', 'okay', 'begin']:
            await update.message.reply_text(
                "Awesome! Click the link below to create your account and claim your deposit bonus:\n\n"
                "👉 Create Your Account Now: https://member.bulgefx.com/client/register/6898c2449fdf2\n\n"
                "💬 Join our Telegram community: https://t.me/bulgefxgroup\n\n"
                "If you have any questions, just type /help"
            )
            logger.info(f"User {update.effective_user.id} confirmed interest")
            return ConversationHandler.END
        else:
            await update.message.reply_text(
                "Please reply with 'Yes' (or 'yep', 'yeah', 'sure') to create your account, or type /help for assistance."
            )
            return TELL_MORE
    except TelegramError as e:
        logger.error(f"Error in yes response handler: {e}")
        return ConversationHandler.END

async def help_command(update: Update, context) -> None:
    """Sends a help message."""
    try:
        help_text = (
            "🤖 BulgeFX Trading Bot Help\n\n"
            "Available commands:\n"
            "/start - Begin your trading journey\n"
            "/help - Show this help message\n\n"
            "About BulgeFX:\n"
            "We offer professional trading services including deposit bonuses, "
            "daily trading signals, educational content, and automated trading solutions.\n\n"
            "🔗 Quick Links:\n"
            "👉 Sign Up: https://member.bulgefx.com/client/register/6898c2449fdf2\n"
            "💬 Telegram Group: https://t.me/bulgefxgroup\n\n"
            "For specific questions about trading or our services, please contact us through our website."
        )
        await update.message.reply_text(help_text)
        logger.info(f"Help command executed for user {update.effective_user.id}")
    except TelegramError as e:
        logger.error(f"Error in help command: {e}")

async def error_handler(update: Update, context) -> None:
    """Handle errors caused by Updates."""
    logger.error(f"Update {update} caused error {context.error}")
    
    # Notify user of error if possible
    if update and update.effective_message:
        try:
            await update.effective_message.reply_text(
                "Sorry, an error occurred. Please try again or contact support at https://bulgefx.com/"
            )
        except TelegramError:
            pass

def main() -> None:
    """Start the bot."""
    # Get token from environment variable
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not found!")
        logger.error("Please set your bot token in environment variables or create a .env file")
        raise ValueError("Bot token is required to start the bot")
    
    try:
        application = Application.builder().token(token).build()
        
        # Add error handler
        application.add_error_handler(error_handler)

        # Create the conversation handler
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
            states={
                START: [
                    CallbackQueryHandler(handle_start_callback),
                    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_start_text)
                ],
                TELL_MORE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_yes_response)],
            },
            fallbacks=[
                CommandHandler("help", help_command),
                CommandHandler("start", start)  # Allow /start to restart conversation
            ],
        )

        application.add_handler(conv_handler)
        application.add_handler(CommandHandler("help", help_command))

        logger.info("BulgeFX Bot started successfully")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    main()