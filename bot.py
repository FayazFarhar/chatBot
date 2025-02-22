import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Load environment variables
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

async def start(update: Update, context: CallbackContext) -> None:
    """Sends a welcome message with an inline dropdown menu"""
    keyboard = [
        [InlineKeyboardButton("🔥 HSC 2026 All Courses", callback_data="hsc_2026")],
        [InlineKeyboardButton("🔥 HSC 2025 All Courses", callback_data="hsc_2025")],
        [InlineKeyboardButton("❤️ Admission All Courses", callback_data="admission")],
        [InlineKeyboardButton("🔥 Support", callback_data="support")],
        [InlineKeyboardButton("🔥 Our Channel", url="https://t.me/yourchannelusername")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Welcome to the Premium Subscription Bot! Choose an option:", reply_markup=reply_markup)

async def button_handler(update: Update, context: CallbackContext) -> None:
    """Handles button clicks from the inline keyboard"""
    query = update.callback_query
    await query.answer()

    if query.data == "hsc_2026":
        await query.message.reply_text("Here are the HSC 2026 courses...")
    elif query.data == "hsc_2025":
        await query.message.reply_text("Here are the HSC 2025 courses...")
    elif query.data == "admission":
        await query.message.reply_text("Here are the Admission courses...")
    elif query.data == "support":
        await query.message.reply_text("For support, contact @your_support_username.")

async def post(update: Update, context: CallbackContext) -> None:
    """Command to post a message in the channel"""
    if context.args:
        message = " ".join(context.args)
        await context.bot.send_message(chat_id=CHANNEL_ID, text=message)
        await update.message.reply_text("Message posted successfully!")
    else:
        await update.message.reply_text("Usage: /post <message>")

def main():
    """Main function to start the bot"""
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("post", post))
    app.add_handler(CallbackQueryHandler(button_handler))  # Handles inline button clicks

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()