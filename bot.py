import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7617448736:AAE3E7Dcx_YRtOci2Dqoy3aT8qnr6XAInH8"  # Replace with your bot's token
SECOND_MESSAGE = "This is the second message set by me!"  # Change this to your second message

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hi")  # First message
    await asyncio.sleep(6)  # Wait for 6 seconds
    await update.message.reply_text(SECOND_MESSAGE)  # Second message

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    await app.run_polling()  # Start the polling to listen for updates

if __name__ == "__main__":
    asyncio.run(main())  # Run the main function
