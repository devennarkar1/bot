import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

TOKEN = "7617448736:AAE3E7Dcx_YRtOci2Dqoy3aT8qnr6XAInH8"  # Replace with your bot's token
SECOND_MESSAGE = "This is the second message set by me!"  # Change this to your second message

# This function sends the first message and adds the start button.
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Start", callback_data="start_button")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Please press the 'Start' button to continue.", reply_markup=reply_markup)

# This function handles the button press and sends the first and second messages with a 6-second delay.
async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()  # Acknowledge the button press
    
    # First message
    await query.edit_message_text("Hi")  # Edit the message to "Hi"
    
    # Wait for 6 seconds before sending the second message
    await asyncio.sleep(6)
    
    # Second message
    await query.edit_message_text(SECOND_MESSAGE)  # Edit the message to the second one

async def main():
    app = Application.builder().token(TOKEN).build()
    
    # Adding handlers for the /start command and button press
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler, pattern="start_button"))
    
    print("Bot is running...")
    await app.run_polling()  # Start the polling to listen for updates

if __name__ == "__main__":
    asyncio.run(main())  # Run the main function
