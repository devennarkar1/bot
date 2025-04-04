from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

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
    
    # Send the second message after 6 seconds
    await asyncio.sleep(6)  # Wait for 6 seconds
    await update.message.reply_text(SECOND_MESSAGE)

async def main():
    # Create the Application and pass the bot token
    app = Application.builder().token(TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    # Start the polling
    await app.run_polling()  # Start the polling to listen for updates

# This part will be executed when the script is run
if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()  # Fixes the issue with already running event loop
    asyncio.run(main())  # Properly run the async main function
