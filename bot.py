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
START, COMPANY_INFO, ONBOARDING_INFO, OFFICE_INFO, WORK_INFO, FINANCE_INFO, PROJECT_INFO, EXTRA_INFO, FEEDBACK, REGULATIONS_INFO = range(10)

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
        
        reply_keyboard = [['Рабочее время', 'Отпуска и больничные'], ['Как подать заявку', 'Всё сразу']]
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
            "✅ День 1: знакомство с командой, установка всех инструментов, первая встреча с ментором и корректировка плана адаптации."
        )
        
        # Запрос на получение напоминаний
        reply_keyboard = [['Да'], ['Нет']]
        update.message.reply_text(
            "Хочешь получать напоминания о ключевых событиях?",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
        )
        
        return FEEDBACK  # Переход к обработке обратной связи

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
    reply_keyboard = [['Рабочее время', 'Отпуска и больничные'], ['Как подать заявку', 'Пропустить'], ['Назад']]
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

def finish_onboarding(update: Update, context: CallbackContext) -> int:
    """Завершение адаптационного процесса."""
    update.message.reply_text(
        "Спасибо за прохождение адаптационного процесса! Надеемся, эта информация "
        "была полезной для тебя."
    )
    
    # Запрос обратной связи
    reply_keyboard = [['Да'], ['Нет']]
    update.message.reply_text(
        "Хочешь оставить обратную связь о боте?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, resize_keyboard=True
        ),
    )
    
    return FEEDBACK

def handle_feedback(update: Update, context: CallbackContext) -> int:
    """Обработка обратной связи."""
    choice = update.message.text
    
    if choice == 'Да':
        update.message.reply_text(
            "Пожалуйста, напиши свои впечатления о боте и предложения по улучшению:"
        )
        return FEEDBACK
    else:  # 'Нет'
        update.message.reply_text(
            "Хорошо! Если у тебя возникнут вопросы в будущем, не стесняйся "
            "обращаться к своему руководителю или в HR-отдел."
        )
        
        # Завершение диалога
        update.message.reply_text(
            "Желаем успехов в работе! Если захочешь снова пообщаться с ботом, "
            "просто напиши /start",
            reply_markup=ReplyKeyboardMarkup([['Перезапустить бота']], 
                                             one_time_keyboard=True,
                                             resize_keyboard=True)
        )
        
        return ConversationHandler.END

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
            REGULATIONS_INFO: [MessageHandler(Filters.regex('^(Рабочее время|Отпуска и больничные|Как подать заявку|Пропустить|Назад)$'), handle_regulations_info)],
            ONBOARDING_INFO: [MessageHandler(Filters.regex('^(Офис|Работа|Финансы|Проекты|Доп.информация|Назад)$'), handle_onboarding_info)],
            OFFICE_INFO: [MessageHandler(Filters.regex('^(Рабочее место|Доступы|Корпоративные мероприятия|Назад)$'), handle_office_info)],
            WORK_INFO: [MessageHandler(Filters.regex('^(График работы|Больничный|Отпуск|Назад)$'), handle_work_info)],
            FINANCE_INFO: [MessageHandler(Filters.regex('^(Зарплата|Авансы|Премии|Назад)$'), handle_finance_info)],
            PROJECT_INFO: [MessageHandler(Filters.regex('^(Текущие проекты|Будущие разработки|Назад)$'), handle_project_info)],
            EXTRA_INFO: [MessageHandler(Filters.regex('^(Обучение|Карьерный рост|Бонусы|Корпоративная культура|Назад)$'), handle_extra_info)],
            FEEDBACK: [MessageHandler(Filters.regex('^(Да|Нет)$'), handle_feedback), 
                      MessageHandler(Filters.text & ~Filters.command, finish_onboarding)],
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