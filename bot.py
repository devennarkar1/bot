from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio
import nest_asyncio  # This is the solution to the event loop issue

TOKEN = "7617448736:AAE3E7Dcx_YRtOci2Dqoy3aT8qnr6XAInH8"  # Replace with your bot's token
SECOND_MESSAGE = "🎯 Done? Here’s your link: https://t.me/+z0oxXjImMvg1NmNl . Enjoy! 😎"  # Change this to your second message

# This function will send the first and second messages
async def start(update: Update, context: CallbackContext):
    # Send the first message
    await update.message.reply_text("🚨 Want the link? Its easy! Just watch the video below for 90 seconds ⏱️ and make sure to hit that subscribe button 🔔. https://youtu.be/oeenz5JTaoo 😎 After that Link is visible")
    # Wait for 4 seconds
    await asyncio.sleep(85)  
    
    # Send the second message after 4 seconds
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
    nest_asyncio.apply()  # Apply nest_asyncio to allow nested event loops
    asyncio.run(main())  # Properly run the async main function
