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
START, COMPANY_INFO, ONBOARDING_INFO, OFFICE_INFO, WORK_INFO, FINANCE_INFO, PROJECT_INFO, EXTRA_INFO, FEEDBACK, REGULATIONS_INFO, TOOLS_SETUP, CHANNELS_INFO = range(12)

def start(update: Update, context: CallbackContext) -> int:
    """Начало диалога и отправка первого сообщения."""
    user = update.effective_user
    
    # Приветственное сообщение
    update.message.reply_text(
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
            "Расскажу немного о Height Line. Мы передовое агентство \n"
            "performance-маркетинга, основанное с целью помогать брендам и \n"
            "предприятиям в России и за ее пределами достигать максимальной \n"
            "эффективности их онлайн-рекламных кампаний."
        )
        
        # Предложение выбрать информацию о компании
        reply_keyboard = [['История', 'Клиенты'], ['Команда', 'Пропустить']]
        update.message.reply_text(
            "Хочешь узнать:\n"
            "1. Историю компании\n"
            "2. Кто наши клиенты\n"
            "3. Команду\n"
            "4. Пропустить",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        
        return COMPANY_INFO
    
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
        # Добавление кнопки "Назад"
        reply_keyboard = [['Назад']]
        update.message.reply_text(
            "Если хотите вернуться, нажмите 'Назад'.",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        )
        return COMPANY_INFO
    
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
        # Добавление кнопки "Назад"
        reply_keyboard = [['Назад']]
        update.message.reply_text(
            "Если хотите вернуться, нажмите 'Назад'.",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        )
        return COMPANY_INFO
    
    elif choice == 'Команда':
        update.message.reply_text(
            "Наша команда — это профессионалы в области digital-маркетинга: "
            "PPC-специалисты, таргетологи, аналитики, дизайнеры и разработчики. "
            "Вместе мы создаем эффективные маркетинговые решения."
        )
        # Добавление кнопки "Назад"
        reply_keyboard = [['Назад']]
        update.message.reply_text(
            "Если хотите вернуться, нажмите 'Назад'.",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        )
        return COMPANY_INFO
    
    elif choice == 'Назад':
        # Возврат к выбору информации о компании
        reply_keyboard = [['История', 'Клиенты'], ['Команда', 'Пропустить']]
        update.message.reply_text(
            "Хочешь узнать:\n"
            "1. Историю компании\n"
            "2. Кто наши клиенты\n"
            "3. Команду\n"
            "4. Пропустить",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return COMPANY_INFO
    
    elif choice == 'Пропустить':
        update.message.reply_text(
            "Регламенты и процессы\n"
            "\n"

            "Здесь — важная информация про работу в Height Line.\n"
            "О чём расскажем?"
        )
        
        reply_keyboard = [['Рабочее время', 'Отпуска и больничные'], ['Как подать заявку', 'Пропустить']]
        update.message.reply_text(
            "Выберите интересующий вас раздел:",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        )
        
        return REGULATIONS_INFO

def handle_regulations_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора информации о регламентах."""
    choice = update.message.text
    
    if choice == 'Рабочее время':
        update.message.reply_text(
            "Обычно мы работаем с 10:00 до 19:00, но график гибкий. Главное — быть на связи и соблюдать дедлайны."
        )
    
    elif choice == 'Отпуска и больничные':
        update.message.reply_text(
            "У каждого сотрудника есть ежегодный оплачиваемый отпуск на срок 4 недели или 20 рабочих дней. "
            "Одна часть отпуска не может быть меньше двух недель, а оставшееся время можно делить – по неделям и по дням. "
            "Оплачиваются отпускные исходя из среднего дневного заработка за последние полгода."
        )
    
    elif choice == 'Как подать заявку':
        update.message.reply_text(
            "Если вдруг тебе потребуется дополнительное оборудование, канцелярские принадлежности и т. д. - "
            "обращайся к нашему офис-менеджеру Екатерине.\n"
            "Telegram для связи: {телеграм офис менеджера}\n"
            "Вот твой персональный план на первые 2 недели:\n"
            "✅ День 1: знакомство с командой, установка всех инструментов, первая встреча с ментором и корректировка плана адаптации."
        )
    
    elif choice == 'Пропустить':
        # Переход к блоку "Онбординг-план"
        update.message.reply_text(
            "Шаг 4. Онбординг-план\n"
            "Если вдруг тебе потребуется дополнительное оборудование, канцелярские принадлежности и т. д. - "
            "обращайся к нашему офис-менеджеру Екатерине.\n"
            "Telegram для связи: {телеграм офис менеджера}\n"
            "Вот твой персональный план на первые 2 недели:\n"
            "✅\n"
            "📅 День 1:\n"
            "1) Знакомство с командой\n"
            "2) Установка всех инструментов\n"
            "3) Первая встреча с ментором и корректировка плана адаптации\n"
            "📅 День 2\n"
            "📅 День 3\n"
            "…"
        )
        
        # Запрос на получение напоминаний
        reply_keyboard = [['Да'], ['Нет']]
        update.message.reply_text(
            "Хочешь получать напоминания о ключевых событиях?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        )
        
        return FEEDBACK  # Переход к обработке обратной связи

    # После показа информации предлагаем вернуться к выбору темы
    reply_keyboard = [['Рабочее время', 'Отпуска и больничные'], ['Как подать заявку', 'Пропустить']]
    update.message.reply_text(
        "Что еще тебя интересует по регламентам?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return REGULATIONS_INFO

def handle_onboarding_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора информации об адаптации."""
    choice = update.message.text
    
    if choice == 'Офис':
        # Переход к информации об офисе
        reply_keyboard = [['Рабочее место', 'Доступы'], ['Корпоративные мероприятия'], ['Назад']]
        update.message.reply_text(
            "Что именно тебя интересует по офису:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return OFFICE_INFO
    
    elif choice == 'Работа':
        # Переход к информации о работе
        reply_keyboard = [['График работы', 'Больничный'], ['Отпуск'], ['Назад']]
        update.message.reply_text(
            "Что именно тебя интересует по работе:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return WORK_INFO
    
    elif choice == 'Финансы':
        # Переход к финансовой информации
        reply_keyboard = [['Зарплата', 'Авансы'], ['Премии'], ['Назад']]
        update.message.reply_text(
            "Что именно тебя интересует по финансам:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return FINANCE_INFO
    
    elif choice == 'Проекты':
        # Переход к информации о проектах
        reply_keyboard = [['Текущие проекты', 'Будущие разработки'], ['Назад']]
        update.message.reply_text(
            "Что именно тебя интересует по проектам:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return PROJECT_INFO
    
    elif choice == 'Доп.информация':
        # Переход к дополнительной информации
        reply_keyboard = [['Обучение', 'Карьерный рост'], ['Бонусы', 'Корпоративная культура'], ['Назад']]
        update.message.reply_text(
            "Какая дополнительная информация тебя интересует:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return EXTRA_INFO
    
    else:
        # Возврат к основному меню
        reply_keyboard = [['История', 'Клиенты'], ['Команда', 'Пропустить']]
        update.message.reply_text(
            "Вернемся к информации о компании. Что тебя интересует?",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return COMPANY_INFO

def handle_office_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора информации об офисе."""
    choice = update.message.text
    
    if choice == 'Рабочее место':
        update.message.reply_text(
            "Рабочее место будет подготовлено к твоему приходу. У нас современный офис "
            "с удобными рабочими станциями, оснащенными всем необходимым."
        )
    elif choice == 'Доступы':
        update.message.reply_text(
            "В первый рабочий день ты получишь все необходимые доступы: "
            "корпоративную почту, доступ к внутренним системам и инструментам."
        )
    elif choice == 'Корпоративные мероприятия':
        update.message.reply_text(
            "Мы регулярно проводим корпоративные мероприятия: "
            "тимбилдинги, профессиональные встречи, праздничные события. "
            "Следи за анонсами в корпоративном чате."
        )
    elif choice == 'Назад':
        # Возврат к выбору информации о компании
        reply_keyboard = [['История', 'Клиенты'], ['Команда', 'Пропустить']]
        update.message.reply_text(
            "Хочешь узнать:\n"
            "1. Историю компании\n"
            "2. Кто наши клиенты\n"
            "3. Команду\n"
            "4. Пропустить",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return COMPANY_INFO
    
    # После показа информации предлагаем вернуться к выбору темы
    reply_keyboard = [['Рабочее место', 'Доступы'], ['Корпоративные мероприятия'], ['Назад']]
    update.message.reply_text(
        "Что еще тебя интересует по офису?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return OFFICE_INFO

def handle_work_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора информации о работе."""
    choice = update.message.text
    
    if choice == 'График работы':
        update.message.reply_text(
            "Мы работаем по гибкому графику с 9:00 до 18:00 с понедельника по пятницу. "
            "У нас есть возможность удаленной работы по согласованию с руководителем."
        )
    elif choice == 'Больничный':
        update.message.reply_text(
            "В случае болезни сообщи своему руководителю. После выздоровления "
            "предоставь больничный лист в отдел кадров."
        )
    elif choice == 'Отпуск':
        update.message.reply_text(
            "Отпуск составляет 28 календарных дней в году. Для оформления отпуска "
            "необходимо подать заявление минимум за 2 недели до планируемой даты."
        )
    elif choice == 'Назад':
        # Возврат к выбору информации об адаптации
        reply_keyboard = [['Офис', 'Работа'], ['Финансы', 'Проекты'], ['Доп.информация']]
        update.message.reply_text(
            "О чем ты хочешь узнать:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return ONBOARDING_INFO
    
    # После показа информации предлагаем вернуться к выбору темы
    reply_keyboard = [['График работы', 'Больничный'], ['Отпуск'], ['Назад']]
    update.message.reply_text(
        "Что еще тебя интересует по работе?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return WORK_INFO

def handle_finance_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора финансовой информации."""
    choice = update.message.text
    
    if choice == 'Зарплата':
        update.message.reply_text(
            "Зарплата выплачивается два раза в месяц: аванс 20-го числа и основная часть "
            "5-го числа следующего месяца. Перечисление производится на банковскую карту."
        )
    elif choice == 'Авансы':
        update.message.reply_text(
            "В компании предусмотрена возможность получения внеочередного аванса. "
            "Для этого необходимо обратиться к руководителю с соответствующим запросом."
        )
    elif choice == 'Премии':
        update.message.reply_text(
            "Система премирования основана на результатах работы и достижении KPI. "
            "Премии выплачиваются ежеквартально после подведения итогов работы."
        )
    elif choice == 'Назад':
        # Возврат к выбору информации об адаптации
        reply_keyboard = [['Офис', 'Работа'], ['Финансы', 'Проекты'], ['Доп.информация']]
        update.message.reply_text(
            "О чем ты хочешь узнать:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return ONBOARDING_INFO
    
    # После показа информации предлагаем вернуться к выбору темы
    reply_keyboard = [['Зарплата', 'Авансы'], ['Премии'], ['Назад']]
    update.message.reply_text(
        "Что еще тебя интересует по финансам?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return FINANCE_INFO

def handle_project_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора информации о проектах."""
    choice = update.message.text
    
    if choice == 'Текущие проекты':
        update.message.reply_text(
            "В настоящее время агентство ведет несколько крупных проектов в сфере "
            "e-commerce, ритейла и финансового сектора. Подробная информация доступна "
            "во внутренней системе проектов."
        )
    elif choice == 'Будущие разработки':
        update.message.reply_text(
            "Мы постоянно развиваемся и осваиваем новые направления. В ближайших планах "
            "расширение спектра услуг и выход на новые рынки."
        )
    elif choice == 'Назад':
        # Возврат к выбору информации об адаптации
        reply_keyboard = [['Офис', 'Работа'], ['Финансы', 'Проекты'], ['Доп.информация']]
        update.message.reply_text(
            "О чем ты хочешь узнать:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return ONBOARDING_INFO
    
    # После показа информации предлагаем вернуться к выбору темы
    reply_keyboard = [['Текущие проекты', 'Будущие разработки'], ['Назад']]
    update.message.reply_text(
        "Что еще тебя интересует по проектам?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return PROJECT_INFO

def handle_extra_info(update: Update, context: CallbackContext) -> int:
    """Обработка выбора дополнительной информации."""
    choice = update.message.text
    
    if choice == 'Обучение':
        update.message.reply_text(
            "Компания поддерживает профессиональное развитие сотрудников. У нас есть "
            "программа обучения, включающая внутренние тренинги, мастер-классы и "
            "возможность посещения профессиональных конференций."
        )
    elif choice == 'Карьерный рост':
        update.message.reply_text(
            "Мы поощряем карьерный рост наших сотрудников. Продвижение основано на "
            "результатах работы, приобретении новых навыков и вкладе в развитие компании."
        )
    elif choice == 'Бонусы':
        update.message.reply_text(
            "Помимо основной зарплаты, у нас действует система бонусов и льгот: "
            "медицинская страховка, компенсация спортзала, корпоративные скидки у "
            "партнеров и многое другое."
        )
    elif choice == 'Корпоративная культура':
        update.message.reply_text(
            "Наша корпоративная культура основана на уважении, открытости и взаимопомощи. "
            "Мы ценим инициативность, креативность и стремление к постоянному "
            "совершенствованию."
        )
    elif choice == 'Назад':
        # Возврат к выбору информации об адаптации
        reply_keyboard = [['Офис', 'Работа'], ['Финансы', 'Проекты'], ['Доп.информация']]
        update.message.reply_text(
            "О чем ты хочешь узнать:",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True, resize_keyboard=True
            ),
        )
        return ONBOARDING_INFO
    
    # После показа информации предлагаем вернуться к выбору темы
    reply_keyboard = [['Обучение', 'Карьерный рост'], ['Бонусы', 'Корпоративная культура'], ['Назад']]
    update.message.reply_text(
        "Какая еще дополнительная информация тебя интересует?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    return EXTRA_INFO

def handle_feedback(update: Update, context: CallbackContext) -> int:
    """Обработка обратной связи."""
    choice = update.message.text
    
    if choice == 'Да':
        update.message.reply_text(
            "Коммуникации в команде\n"
            "У нас ценится открытость и инициатива.\n"
            "В папке Telegram HL2b:\n"
            "#daily — делимся планами на день\n"
            "#random — свободные темы\n"
            "#project — каналы по проектам\n"
            "Хочешь список всех каналов с описанием?"
        )
        
        # Кнопки для выбора
        reply_keyboard = [['Да', 'Нет']]
        update.message.reply_text(
            "Выберите вариант:",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        )
        
        return CHANNELS_INFO  # Переход к следующему шагу, например, к обработке информации о каналах

    else:  # 'Нет'
        update.message.reply_text(
            "Хорошо, двигаемся дальше!",
            reply_markup=ReplyKeyboardMarkup([['Далее']], 
                                             one_time_keyboard=True,
                                             resize_keyboard=True)
        )
        
        return ConversationHandler.END  # Завершение диалога, если выбрано "Нет"

def handle_channels_info(update: Update, context: CallbackContext) -> int:
    """Обработка ответа на вопрос о списке каналов."""
    choice = update.message.text
    
    if choice == 'Да':
        update.message.reply_text(
            "Вот список наших каналов:\n"
            "Канал 1 - https://t.me/channel1\n"
            "Канал 2 - https://t.me/channel2\n"
            "Канал 3 - https://t.me/channel3",
            reply_markup=ReplyKeyboardMarkup([['Далее']], 
                                          one_time_keyboard=True,
                                          resize_keyboard=True)
        )
    else:  # 'Нет'
        update.message.reply_text(
            "Хорошо, двигаемся дальше!",
            reply_markup=ReplyKeyboardMarkup([['Далее']], 
                                          one_time_keyboard=True,
                                          resize_keyboard=True)
        )
    
    return ConversationHandler.END  # Завершение диалога

def handle_tools_setup(update: Update, context: CallbackContext) -> int:
    """Обработка выбора настройки инструментов."""
    choice = update.message.text
    
    if choice == 'Да, Нужна':
        # Инструкции по инструментам
        update.message.reply_text(
            "Инструкция по Telegram\n"
            "Для входа в рабочие чаты перейди по ссылке [ссылка], чтобы добавить папку HL2B на свой аккаунт.\n"
            "❗ВАЖНО❗\n"
            "Зайди на свой рабочий Telegram аккаунт. Если у тебя еще нет рабочего аккаунта, обратись за помощью к [имя/контакт].\n\n"
            
            "Инструкция по Notion\n"
            "Чтобы войти в базу знаний, перейди по ссылке: [ссылка].\n"
            "Здесь ты найдешь всю актуальную информацию.\n\n"
            
            "Инструкция по Google Drive\n"
            "Чтобы перейти к рабочим файлам, перейди по ссылке [ссылка].\n\n"
            
            "Инструкция по Bitrix24\n"
            "Чтобы войти в Bitrix24, напиши Сергею, чтобы он выдал тебе рабочую почту для входа в аккаунт.\n"
            "Telegram Сергея: {ссылка на тг Сергея}."
        )
    
    else:  # 'Нет, уже настроил'
        update.message.reply_text(
            "Отлично! Нажми 'Далее', чтобы продолжить."
        )
    
    # Завершение диалога
    update.message.reply_text(
        "Коммуникации в команде\n"
        "У нас ценится открытость и инициатива.\n"
        "В папке Telegram HL2b:\n"
        "#daily — делимся планами на день\n"
        "#random — свободные темы\n"
        "#project — каналы по проектам\n"
        "Хочешь список всех каналов с описанием?",
        reply_markup=ReplyKeyboardMarkup([['Да', 'Нет']], 
                                         one_time_keyboard=True,
                                         resize_keyboard=True)
    )
    
    return CHANNELS_INFO  # Переход к обработке информации о каналах

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
            COMPANY_INFO: [MessageHandler(Filters.regex('^(История|Клиенты|Команда|Пропустить|Назад)$'), handle_company_info)],
            REGULATIONS_INFO: [MessageHandler(Filters.regex('^(Рабочее время|Отпуска и больничные|Как подать заявку|Пропустить)$'), handle_regulations_info)],
            FEEDBACK: [MessageHandler(Filters.regex('^(Да|Нет)$'), handle_feedback)],
            TOOLS_SETUP: [MessageHandler(Filters.regex('^(Да, Нужна|Нет, уже настроил)$'), handle_tools_setup)],
            CHANNELS_INFO: [MessageHandler(Filters.regex('^(Да|Нет)$'), handle_channels_info)],
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