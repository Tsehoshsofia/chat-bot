from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

start1 = False


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def my_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global start1
    if update.message.text in "start":
        start1 = True
        await update.message.reply_text('Ввелите ваш возраст:')
        global current_handler
        current_handler=whats_age

    elif start1:
        age = update.message.text
        await update.message.reply_text(f'Вам {age} лет')

    elif "пока" in str(update.message.reply_text).lower():
        await update.message.reply_text("Пока")
    else:
        await update.message.reply_text("Я Вас не понимаю")

current_handler = my_message_handler

async def whats_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    age = update.message.text
    global current_handler
    current_handler = my_message_handler
    await update.message.reply_text(f'Вам {age} годов')



app = ApplicationBuilder().token("6719666823:AAFy_cPoUSSlTOQjW2xLkvuV1oDxKVh0Db8").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT & ~ filters.COMMAND, current_handler))
app.run_polling()
