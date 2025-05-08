# bot2.py

import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Состояния диалога
START, NEW_FEATURE = range(2)

def start(update: Update, context: CallbackContext) -> int:
    """Начало диалога и отправка приветственного сообщения."""
    user = update.effective_user
    update.message.reply_text(
        f"Привет, {user.first_name}! Я новый бот, готов помочь тебе!"
    )
    
    reply_keyboard = [['Начать']]
    update.message.reply_text(
        "Нажми 'Начать', чтобы продолжить.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    
    return START

def new_feature(update: Update, context: CallbackContext) -> int:
    """Обработка новой функции бота."""
    update.message.reply_text("Это новая функция бота!")
    # Здесь можно добавить логику для новой функции

    return ConversationHandler.END

def main() -> None:
    """Запуск нового бота."""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("Токен бота не найден в переменных окружения")
        return
    
    updater = Updater(token)
    dispatcher = updater.dispatcher
    
    # Создание обработчика диалога
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            START: [MessageHandler(Filters.regex('^Начать$'), new_feature)],
        },
        fallbacks=[CommandHandler('start', start)],
    )
    
    # Добавление обработчика диалога
    dispatcher.add_handler(conv_handler)
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()