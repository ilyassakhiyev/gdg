from telegram.ext import Updater, CommandHandler
import requests

TELEGRAM_TOKEN = '7846759097:AAGBZCXA1d4TtQ0ppav79rYdmjR8uzpWjcE'

API_URL = 'http://127.0.0.1:8000/news/'

def start(update, context):
    update.message.reply_text('Привет! Напиши /news чтобы получить свежие спортивные новости.')

def news(update, context):
    response = requests.get(API_URL)
    if response.status_code == 200:
        news_list = response.json()
        if news_list:
            for item in news_list[:5]:
                update.message.reply_text(f"{item['title']}\n\n{item['content']}\n")
        else:
            update.message.reply_text('Пока новостей нет.')
    else:
        update.message.reply_text('Не удалось получить новости с сервера.')

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("news", news))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()