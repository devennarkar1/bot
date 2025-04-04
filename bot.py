from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
import asyncio
import nest_asyncio  # This is the solution to the event loop issue

TOKEN = "7617448736:AAE3E7Dcx_YRtOci2Dqoy3aT8qnr6XAInH8"  # Replace with your bot's token
SECOND_MESSAGE = "This is the second message set by me!"  # Change this to your second message

# This function will send the first and second messages
async def start(update: Update, context: CallbackContext):
    # Create an inline keyboard with a Start button
    keyboard = [
        [InlineKeyboardButton("Start", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the first message with the start button
    await update.message.reply_text("Hi! Welcome to the bot! Click the start button to interact.", reply_markup=reply_markup)

# This function will handle the callback when the button is clicked
async def button_click(update: Update, context: CallbackContext):
    # Send the second message after 6 seconds
    await asyncio.sleep(6)  # Wait for 6 seconds
    await update.callback_query.answer()  # Acknowledge the callback
    await update.callback_query.message.reply_text(SECOND_MESSAGE)

async def main():
    # Create the Application and pass the bot token
    app = Application.builder().token(TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    # Add callback query handler to handle button clicks
    app.add_handler(CallbackQueryHandler(button_click, pattern='start'))

    # Start the polling
    await app.run_polling()  # Start the polling to listen for updates

# This part will be executed when the script is run
if __name__ == "__main__":
    nest_asyncio.apply()  # Apply nest_asyncio to allow nested event loops
    asyncio.run(main())  # Properly run the async main function
