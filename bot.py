import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

TOKEN = "7617448736:AAE3E7Dcx_YRtOci2Dqoy3aT8qnr6XAInH8"  # Replace with your bot's token
SECOND_MESSAGE = "This is the second message set by me!"  # Change this to your second message

# Function to send the start button when a user starts the bot
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Start", callback_data="start_button")]  # Button with callback_data "start_button"
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send message with start button
    await update.message.reply_text("Click the button to start!", reply_markup=reply_markup)

# Function to handle the button press (user clicks the "Start" button)
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()  # Answer the callback to remove the loading state on the button

    # Send the first message
    await query.message.reply_text("Hi")

    # Wait for 6 seconds before sending the second message
    await asyncio.sleep(6)

    # Send the second message after the delay
    await query.message.reply_text(SECOND_MESSAGE)

async def main():
    app = Application.builder().token(TOKEN).build()

    # Add handlers for /start and button callback
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button, pattern="start_button"))

    print("Bot is running...")
    await app.run_polling()  # Start polling to listen for updates

if __name__ == "__main__":
    asyncio.run(main())  # Run the main function
