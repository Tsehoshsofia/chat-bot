from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

current = 0

questions = ['Какой фон имеют временные дорожные знаки?\n 1.Желтный фон.\n2.Синий фон.\n3.Оранжевый фон',
                 'На каком расстояние водитель должен переключать дальний свет фар на ближний от встречного автомобиля?\n 1. 300 метров.\n 2.150 метров.\n 3.100 метров']
answers = [3, 2]
explanation = ['Установлено ГОСТом\n', 'Принято ГОСТом\n']
async def my_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global questions
    global answers
    global explanation
    global current

    if questions == []:
        await update.message.reply_text('Тест окончен')
    elif update.message.text.isdigit():
        if update.message.text == str(answers[current]):
            questions.remove(questions[current])
            answers.remove(answers[current])
           # explanation.remove(explanation[current])
            await update.message.reply_text('Правильно' + '\n' + explanation[current])
        else:
            await update.message.reply_text('Не правильно' + '\n' + explanation[current])
    else:
        question = random.choice(questions)
        current = questions.index(question)
        await update.message.reply_text(question)



app = ApplicationBuilder().token("6719666823:AAFy_cPoUSSlTOQjW2xLkvuV1oDxKVh0Db8").build()
app.add_handler(MessageHandler(filters.TEXT & ~ filters.COMMAND, my_message_handler))
app.run_polling()
