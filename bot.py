import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "7617448736:AAE3E7Dcx_YRtOci2Dqoy3aT8qnr6XAInH8"  # Replace with your bot's token
SECOND_MESSAGE = "This is the second message set by me!"  # Change this to your second message

# This function will send the first and second messages
async def start(update: Update, context: CallbackContext):
    # Send the first message
    await update.message.reply_text("Hi! Welcome to the bot! Click the start button to interact.")
    
    # Send the second message after 6 seconds
    await asyncio.sleep(6)  # Wait for 6 seconds
    await update.message.reply_text(SECOND_MESSAGE)

async def main():
    # Create the Application and pass the bot token
    app = Application.builder().token(TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    # Create inline keyboard with the start button
    keyboard = [
        [InlineKeyboardButton("Start", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the start button when the user interacts with the bot
    await app.bot.send_message(chat_id=update.message.chat_id, text="Welcome!", reply_markup=reply_markup)

    # Start the polling
    await app.run_polling()  # Start the polling to listen for updates

# Ensure the main function is awaited correctly
if __name__ == "__main__":
    asyncio.run(main())  # Properly run the async main function
