import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Состояния диалога
START, COMPANY_INFO, ONBOARDING_INFO, OFFICE_INFO, WORK_INFO, FINANCE_INFO, PROJECT_INFO, EXTRA_INFO, FEEDBACK, REGULATIONS_INFO, TOOLS_INFO, TOOLS_SETUP, CHANNELS_INFO, FEEDBACK_SUPPORT, CULTURE_INFO, GAMIFICATION, CULTURE_LIFE, LINKS_INFO = range(18)

def start(update: Update, context: CallbackContext) -> int:
    """Начало диалога и отправка первого сообщения."""
    user = update.effective_user
    
    # Приветственное сообщение
    update.message.reply_text(
        "Шаг 1. Приветствие и знакомство с ботом: \n"
        f"Привет, {user.first_name}! \n"
        f"Добро пожаловать в команду Height Line — агентство, \n"
        f"где рождаются креативные кампании и большие бренды.\n"
        f"Я твой адаптационный бот и помогу тебе освоиться в новом месте"
    )
    
    # Предложение начать знакомство
    reply_keyboard = [['Да, поехали'], ['Хочу позже']]
    update.message.reply_text(
        "Хочешь начать знакомство?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    
    return START

def handle_start_choice(update: Update, context: CallbackContext) -> int:
    """Обработка выбора пользователя на начальном этапе."""
    choice = update.message.text
    
    if choice == 'Да, поехали':
        # Переход к информации о компании
        update.message.reply_text(
            "Шаг 2. О компании 'Height Line': \n"
            "Расскажу немного о Height Line. Мы передовое агентство \n"
            "performance-маркетинга, основанное с целью помогать брендам и \n"
            "предприятиям в России и за ее пределами достигать максимальной \n"
            "эффективности их онлайн-рекламных кампаний."
        )
        
        # Предложение выбрать информацию о компании
        reply_keyboard = [['История', 'Клиенты'], ['Команда', 'Далее']]
        update.message.reply_text(
            "Хочешь узнать:\n"
            "1. Историю компании\n"
            "2. Кто наши клиенты\n"
            "3. Команду\n"
            "4. Далее",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        
        return COMPANY_INFO  # Переход к состоянию выбора информации о компании
    
    else:  # 'Хочу позже'
        update.message.reply_text(
            "Хорошо, возвращайся, как будешь готов!",
            reply_markup=ReplyKeyboardMarkup([['Перезапустить бота']], 
                                             one_time_keyboard=True,
                                             resize_keyboard=True)
        )
        
        return ConversationHandler.END

def handle_company_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора информации о компании."""
    choice = update.message.text
    
    if choice == 'История':
        update.message.reply_text(
            "Начав свою деятельность более десяти лет назад, Height Line за 2023 год "
            "проявило себя как агентство, способное привносить инновации в индустрию "
            "и обеспечивать клиентам превосходные результаты.\n\n"
            "Агентство Height Line было основано в 2012 году. Идея возникла, когда "
            "основатели осознали: имеющееся предложение на рынке услуг маркетинга не "
            "покрывает растущий спрос на специализированные услуги в области "
            "настройки, ведения и анализа рекламы. Они увидели возможность "
            "предоставить качественные услуги рекламы в таких областях, как "
            "таргетированная и контекстная для e-commerce, недвижимость, ритейл, "
            "медицина и т.д. В современном мире цифрового маркетинга изменения "
            "происходят с беспрецедентной скоростью. Новые платформы, технологии и "
            "тренды появляются постоянно, и компании, которые не могут или не хотят "
            "адаптироваться, рискуют оказаться позади конкурентов. Сегодня агентство "
            "специализируется на глубокой сквозной аналитике от рекламы до продаж, "
            "что является performance-маркетингом. В Height Line есть готовые решения по "
            "эффективной рекламе и сквозной аналитике."
        )
    
    elif choice == 'Клиенты':
        update.message.reply_text(
            "В портфолио агентства входят крупные бренды и компании, работающие в "
            "различных отраслях рынка как в России так и заграницей, что подтверждает "
            "гибкость и универсальность предлагаемых решений.\n\n"
            "В своей работе Height Line уделяет особое внимание постоянному обучению и "
            "развитию, что позволяет агентству не только следовать актуальным трендам "
            "в маркетинге, но и предвосхищать потребности клиентов, предлагая "
            "инновационные стратегии, которые отражаются на их бизнесе наилучшим "
            "образом. Каждый проект в агентстве — это сочетание креатива, данных и "
            "технологий, направленное на достижение конкретных бизнес-целей клиента."
        )
    
    elif choice == 'Команда':
        update.message.reply_text(
            "Наша команда — это профессионалы в области digital-маркетинга: "
            "PPC-специалисты, таргетологи, аналитики, дизайнеры и разработчики. "
            "Вместе мы создаем эффективные маркетинговые решения."
        )
    
    elif choice == 'Далее':
        update.message.reply_text(
            "Шаг 3. Регламенты и процессы\n"
            "\n"
            "Здесь — важная информация про работу в Height Line.\n"
            "О чём расскажем?"
        )
        
        reply_keyboard = [['Рабочее время', 'Отпуска и больничные'], ['Как подать заявку', 'Далее']]
        update.message.reply_text(
            "Выберите интересующий вас раздел:",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        )
        
        return REGULATIONS_INFO  # Переход к состоянию REGULATIONS_INFO

    # Возврат к выбору информации о компании
    reply_keyboard = [['История', 'Клиенты'], ['Команда', 'Далее']]
    update.message.reply_text(
        "Хочешь узнать:\n"
        "1. Историю компании\n"
        "2. Кто наши клиенты\n"
        "3. Команду\n"
        "4. Далее",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    
    return COMPANY_INFO  # Переход к состоянию выбора информации о компании

def handle_regulations_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора информации о регламентах и процессах."""
    choice = update.message.text
    
    if choice == 'Рабочее время':
        update.message.reply_text(
            "Рабочее время в Height Line: \n"
            "Стандартное рабочее время с 9:00 до 18:00, с понедельника по пятницу."
        )
        
    elif choice == 'Отпуска и больничные':
        update.message.reply_text(
            "Отпуска и больничные: \n"
            "Сотрудники имеют право на 28 дней оплачиваемого отпуска в год. "
            "Больничные оплачиваются в соответствии с законодательством."
        )
        
    elif choice == 'Как подать заявку':
        update.message.reply_text(
            "Чтобы подать заявку на отпуск или больничный, необходимо заполнить форму "
            "внутренней документации и отправить её вашему руководителю."
        )
        
    elif choice == 'Далее':
        # Переход на шаг 4
        return handle_onboarding_plan(update, context)  # Переход к функции обработки онбординга
    
    # После обработки выбора, возвращаем пользователя к выбору
    reply_keyboard = [['Рабочее время', 'Отпуска и больничные'], ['Как подать заявку', 'Далее']]
    update.message.reply_text(
        "Выберите интересующий вас раздел:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    
    return REGULATIONS_INFO  # Возврат к состоянию REGULATIONS_INFO

def handle_onboarding_plan(update: Update, context: CallbackContext) -> int:
    """Обработка информации о плане онбординга."""
    update.message.reply_text(
        "Шаг 4. Онбординг план: \n"
        "Здесь будет информация о процессе онбординга, включая важные даты, "
        "мероприятия и ресурсы, которые помогут вам адаптироваться в компании."
    )
    
    # Добавление кнопок "Да" и "Нет"
    reply_keyboard = [['Да', 'Нет']]
    update.message.reply_text(
        "Хотите узнать больше о процессе онбординга?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    
    return ONBOARDING_INFO  # Переход к состоянию ONBOARDING_INFO

def handle_onboarding_response(update: Update, context: CallbackContext) -> int:
    """Обработка ответа на вопрос о процессе онбординга."""
    choice = update.message.text
    
    if choice == 'Да':
        update.message.reply_text(
            "Отлично! Мы предоставим вам всю необходимую информацию о процессе онбординга."
        )
        # Переход к шагу 5
        return handle_step_five(update, context)
    else:  # 'Нет'
        update.message.reply_text(
            "Хорошо, если у вас возникнут вопросы, не стесняйтесь спрашивать!"
        )
        # Переход к шагу 5
        return handle_step_five(update, context)

def handle_step_five(update: Update, context: CallbackContext) -> int:
    """Обработка шага 5.  Инструменты и доступы."""
    update.message.reply_text(
        "Шаг 5. Инструменты и доступы: \n"
        "Здесь будет информация о процессе онбординга, включая важные даты, "
        "мероприятия и ресурсы, которые помогут вам адаптироваться в компании."
    )
    
    # Здесь можно добавить кнопки или другую логику для шага 5
    reply_keyboard = [['Да', 'Нет']]
    update.message.reply_text(
        "Вы можете завершить процесс онбординга.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    
    return TOOLS_INFO  # Переход к состоянию обработки ответа на вопрос о доступах

def handle_tools_response(update: Update, context: CallbackContext) -> int:
    """Обработка ответа на вопрос о процессе онбординга."""
    choice = update.message.text
    
    if choice == 'Да':
        update.message.reply_text(
            "Отлично! Вот инструкции по процессу онбординга:\n"
            "- Инструкция 1: [ссылка](http://example.com)\n"
            "- Инструкция 2: [ссылка](http://example.com)\n"
            "- Инструкция 3: [ссылка](http://example.com)"
        )
    
    # Переход к шагу 6
    return handle_step_six(update, context)  # Переход к шагу 6

def handle_step_six(update: Update, context: CallbackContext) -> int:
    """Обработка шага 6. Коммуникации в команде."""
    update.message.reply_text(
        "Шаг 6. Коммуникации в команде: \n"
        "Здесь будет информация о том, как эффективно общаться с вашей командой, "
        "включая используемые инструменты и лучшие практики."
    )
    
    # Добавление кнопок "Да" и "Нет"
    reply_keyboard = [['Да', 'Нет']]
    update.message.reply_text(
        "Хотите получить ссылки на полезные ресурсы?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    )
    
    return LINKS_INFO  # Переход к состоянию обработки ответа на вопрос о ссылках

def handle_links_response(update: Update, context: CallbackContext) -> int:
    """Обработка ответа на вопрос о ссылках."""
    choice = update.message.text
    
    if choice == 'Да':
        update.message.reply_text(
            "Вот несколько полезных ссылок:\n"
            "- Ссылка 1: [пример](http://example.com)\n"
            "- Ссылка 2: [пример](http://example.com)\n"
            "- Ссылка 3: [пример](http://example.com)\n"
        )
        # Переход к шагу 7
        return handle_step_seven(update, context)  # Переход к шагу 7
    else:  # 'Нет'
        update.message.reply_text(
            "Хорошо, переходим к следующему шагу."
        )
    
    # Переход к шагу 7
    return handle_step_seven(update, context)  # Переход к шагу 7

def handle_step_seven(update: Update, context: CallbackContext) -> int:
    """Обработка шага 7."""
    update.message.reply_text(
        "Шаг 7. Завершение онбординга: \n"
        "Здесь будет информация о том, как завершить процесс онбординга и что делать дальше."
    )
    
    return ConversationHandler.END  # Завершение диалога

def restart(update: Update, context: CallbackContext) -> int:
    """Перезапуск бота."""
    return start(update, context)

def main() -> None:
    """Запуск бота."""
    # Создание Updater и передача ему токена бота
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("Токен бота не найден в переменных окружения")
        return
    
    updater = Updater(token)
    
    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher
    
    # Создание обработчика диалога
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            START: [MessageHandler(Filters.regex('^(Да, поехали|Хочу позже)$'), handle_start_choice)],
            COMPANY_INFO: [MessageHandler(Filters.regex('^(История|Клиенты|Команда|Далее)$'), handle_company_info)],
            REGULATIONS_INFO: [MessageHandler(Filters.regex('^(Рабочее время|Отпуска и больничные|Как подать заявку|Далее)$'), handle_regulations_info)],
            ONBOARDING_INFO: [MessageHandler(Filters.regex('^(Да|Нет)$'), handle_onboarding_response)],  # Новое состояние для обработки ответа
            TOOLS_INFO: [MessageHandler(Filters.regex('^(Да|Нет)$'),handle_tools_response )],  # Обработка ответа на вопрос о ссылках
            LINKS_INFO: [MessageHandler(Filters.regex('^.*$'),handle_links_response )],  # Обработка шага 7
        },
        fallbacks=[CommandHandler('start', start)],
    )
    
    # Добавление обработчика диалога
    dispatcher.add_handler(conv_handler)
    
    # Обработчик для перезапуска бота
    dispatcher.add_handler(MessageHandler(Filters.regex('^Перезапустить бота$'), restart))
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main() 