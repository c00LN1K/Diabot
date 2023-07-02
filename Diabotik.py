import telebot
from telebot import types
from time import sleep

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

a = 0     #Длительность диабета
w = 0     #Вес
h = 0     #Рост
ideal = 0 #Идеальный вес
day = 0   #Суточная доза инсулина
basal = 0 #Доза базального инсулина


button_1 = types.KeyboardButton(text="Что такое диабет?")
button_2 = types.KeyboardButton(text="Виды диабетов")
button_3 = types.KeyboardButton(text="Симптомы сахарного диабета")
button_4 = types.KeyboardButton(text="Группа риска")
button_5 = types.KeyboardButton(text="Диагностика диабета")
button_6 = types.KeyboardButton(text="Причины сахарного диабета")
button_7 = types.KeyboardButton(text="Профилактика сахарного диабета")
button_8 = types.KeyboardButton(text="Лекарственные средства для диабетиков")
button_9 = types.KeyboardButton(text="Калькулятор инсулина")
button_10 = types.KeyboardButton(text="Показать всё")
buttons=[button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9,button_10]

@bot.message_handler(commands=['start'])
def start_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(text="Начать")
    keyboard.add(button)
    bot.send_message(message.chat.id, '👋Здравствуйте! Это диаботик)',
                     reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Если вы хотите побольше узнать про диабет, нажмите кнопку "Начать"!',
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Начать')
def begin_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, "Выберите один из интересующих пунктов:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Что такое диабет?')
def what_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if button_1 in buttons:
        buttons.remove(button_1)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id,
                     "Диабет – это общее название группы хронических эндокринных заболеваний. \nВсе недуги этой группы имеют общий симптом – полиурию (повышенное образование мочи). Но только сахарный диабет связан с повышением концентрации глюкозы в крови.",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Виды диабетов')
def types_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Центральный несахарный")
    button_2 = types.KeyboardButton(text="Нефрогенный несахарный")
    button_3 = types.KeyboardButton(text="Сахарный диабет")
    button_4 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, "Выберите интересующих диабет или вернитесь назад", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Центральный несахарный')
def center_nosug_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_2 = types.KeyboardButton(text="Нефрогенный несахарный")
    button_3 = types.KeyboardButton(text="Сахарный диабет")
    button_4 = types.KeyboardButton(text="Назад")
    keyboard.add(button_2, button_3, button_4)
    bot.send_message(message.chat.id, "▶ Центральный несахарный", reply_markup=keyboard)
    bot.send_message(message.chat.id,
                     "Вызван недостатком или сопротивляемостью организма к вазопрессину – пептидному гормону гипоталамуса, ответственному за сохранение в теле жидкости.",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Нефрогенный несахарный')
def nefro_nosug_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_2 = types.KeyboardButton(text="Центральный несахарный")
    button_3 = types.KeyboardButton(text="Сахарный диабет")
    button_4 = types.KeyboardButton(text="Назад")
    keyboard.add(button_3, button_2, button_4)
    bot.send_message(message.chat.id, "▶ Нефрогенный несахарный", reply_markup=keyboard)
    bot.send_message(message.chat.id,
                     "Характеризуется утратой способности к концентрированию мочи. Наследственный вызван генетическими мутациями, приобретенный – почечными заболеваниями или патологиями в мозге.",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Сахарный диабет')
def sugar_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_2 = types.KeyboardButton(text="Центральный несахарный")
    button_3 = types.KeyboardButton(text="Нефрогенный несахарный")
    button_1 = types.KeyboardButton(text="Типы сахарного диабета")
    button_4 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, "▶ Сахарный диабет", reply_markup=keyboard)
    bot.send_message(message.chat.id,
                     "Он является наиболее распространенным. Сахарный диабет – эндокринное заболевание, вызванное нарушением метаболических процессов в организме. Его главный симптом – гипергликемия (высокий сахар в крови), обусловленная инсулиновой недостаточностью.",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Типы сахарного диабета')
def types_sug_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_2 = types.KeyboardButton(text="Центральный несахарный")
    button_3 = types.KeyboardButton(text="Нефрогенный несахарный")
    button_1 = types.KeyboardButton(text="Сахарный диабет")
    button_4 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id,
                     "В зависимости от причины, по которой нарушается транспортировка глюкозы, выделяют следующие типы сахарного диабета:")
    bot.send_message(message.chat.id,
                     "• СД первого типа. \nОн вызван дефицитом инсулина. Поджелудочная железа не справляется, поэтому больному необходимо принимать препараты, содержащие этот гормон.\n\n"
                     "• СД второго типа. \nЕго причина – инсулинорезистентность. Самого гормона в организме достаточно, но клетки к нему нечувствительны, поэтому транспортировка глюкозы не происходит.\n\n"
                     "• Гестационный диабет. \nРазвивается во время беременности в отсутствие сахарного диабета и угрожает здоровью матери и ребенка.\n\n",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Назад')
def types_handler(message):
    if button_2 in buttons:
        buttons.remove(button_2)
    begin_handler(message)


@bot.message_handler(func=lambda message: message.text == 'Симптомы сахарного диабета')
def symp_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if button_3 in buttons:
        buttons.remove(button_3)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id,
                     "Сахарному диабету присущи частые приступы голода, постоянное ощущение жажды и учащенное мочеиспускание. Все это – признаки гипергликемии. Это значит, что в крови больного много сахара. Его нельзя ограничивать в жидкости во избежание обезвоживания.",
                     reply_markup=None)
    bot.send_message(message.chat.id, "Также сахарный диабет сопровождается такими симптомами:\n"
                                      "• Ухудшение зрения;\n"
                                      "• Онемение конечностей;\n"
                                      "• Повышенная утомляемость;\n"
                                      "• Усиленное потоотделение;\n"
                                      "• Мышечная слабость;\n"
                                      "• Долгое заживление ран;\n"
                                      "• Кожный зуд.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Группа риска')
def group_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if button_4 in buttons:
        buttons.remove(button_4)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id,
                     "Пациенты с избыточной массой тела или синдромом поликистозных яичников имеют более высокие шансы заболеть диабетом. Также в группу риска попадают люди:\n"
                     "• Старше 45 лет;\n"
                     "• Имеющие родителей-диабетиков;\n"
                     "• Страдающие артериальной гипертензией;\n"
                     "• Ведущие малоподвижный образ жизни;\n"
                     "• Лишенные в детстве грудного вскармливания;\n"
                     "• Употребляющие в пищу много простых углеводов и жиров;\n"
                     "• Курящие."
                     , reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Диагностика диабета')
def diag_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,
                     "Результаты анализа крови на глюкозу, превышающие норму, позволяют заподозрить СД. Но для уточнения диагноза эндокринолог назначит также:",
                     reply_markup=None)
    if button_5 in buttons:
        buttons.remove(button_5)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, "• Анализ на глюкозу натощак;\n"
                                      "• Пероральный глюкозотолерантный тест;\n"
                                      "• Биохимический анализ крови;\n"
                                      "• Анализ на гликированный гемоглобин;\n"
                                      "• Анализ на холестерин (общий, липопротеидов высокой плотности и низкой плотности);\n"
                                      "• Определение индекса инсулинорезистентности.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Причины сахарного диабета')
def reasons_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if button_6 in buttons:
        buttons.remove(button_6)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id,
                     "Сахарным диабетом можно заболеть в любом возрасте. Люди, у чьих родственников когда-либо был диагностирован недостаток инсулина, входят в группу риска. На сегодняшний день выявлены следующие причины диабета:\n"
                     "• Генетическая предрасположенность;\n"
                     "• Перманентная терапия хронических заболеваний;\n"
                     "• Несбалансированный рацион, вызывающий ожирение, усугубленный малоподвижным образом жизни;\n"
                     "• Хронические эмоциональные и физические стрессы.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Профилактика сахарного диабета')
def profil_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if button_7 in buttons:
        buttons.remove(button_7)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id,
                     "Основные принципы:\n"
                     "• Придерживаться диетического питания с ограничением жирных продуктов животного происхождения, жареной, жирной и острой пищи, алкогольных напитков;\n"
                     "• Контролировать вес тела, при избытке обязательно снижать до нормы;\n"
                     "• Заниматься лечебной гимнастикой, ходьбой, плаванием, бегом;\n"
                     "• Исключить стрессовый фактор;\n"
                     "• Отказаться от вредных привычек.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Лекарственные средства для диабетиков')
def medicines_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if button_8 in buttons:
        buttons.remove(button_8)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id,
                     "Врач прописывает прием лекарственных средств после первых негативных результатов исследования. Если заболевание прогрессирует, больному назначаются дополнительные медикаменты. Если концентрация глюкозы остается на прежнем уровне, терапевтическая схема не изменяется.")
    bot.send_message(message.chat.id,
                     "Таблетированные сахароснижающие препараты можно разделить на несколько групп в зависимости от принципа их действия:\n"
                     "• Улучшающие чувствительность к инсулину;\n"
                     "• Повышающие секрецию собственного инсулина поджелудочной железой;\n"
                     "• Замедляющие всасывание углеводов в кишечнике.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Перечень основных препаратов')
def medic_handler(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Лекарственные средства для диабетиков")
    button_2 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1, button_2)
    bot.send_message(message.chat.id,
                     "Список рекомендованных лекарственных средств выглядит так:\n"
                     "• Форсига;\n"
                     "• Янувия;\n"
                     "• Янумет;\n"
                     "• Амарил;\n"
                     "• Винидия;\n"
                     "• Галвус;\n"
                     "• Глибомет;\n"
                     "• Глиформин;\n"
                     "• Манинил;\n"
                     "• Новонорм;\n"
                     "• Сиофор;\n"
                     "• Диалек.", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Показать всё')
def clear_handler(message):
    buttons.clear()
    buttons.extend([button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9,button_10])
    begin_handler(message)

@bot.message_handler(func=lambda message: message.text == 'Калькулятор инсулина')
def calc_handler(message):
    button_1 = types.KeyboardButton(text="Начать")
    button_2 = types.KeyboardButton(text="Назад")
    bot.send_message(message.chat.id, "Вас приветствует калькулятор инсулина. Давайте рассчитаем дозу инсулина.",
                     reply_markup=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(button_1, button_2))
    bot.register_next_step_handler(message, cont)


def cont(message):
    k = types.ReplyKeyboardRemove()
    if (message.text == "Начать"):
        bot.send_message(message.chat.id, "1. Укажите, пожалуйста, ваш вес в кг", reply_markup=k)
        bot.register_next_step_handler(message, weight)
    elif (message.text == "Назад"):
        begin_handler(message)
    else:
        bot.send_message(message.chat.id, "Ой, произошла ошибка. Убедитесь в корректности ввода", reply_markup=None)
        bot.register_next_step_handler(message, cont)


def weight(message):
    if ((message.text).isdigit() and 0 < int(message.text) < 400):  # проверить на строчку
        bot.send_message(message.chat.id, "2. Укажите, пожалуйста, ваш рост в см", reply_markup=None)
        global w
        w = int(message.text)
        bot.register_next_step_handler(message, height)
    else:
        bot.send_message(message.chat.id, "Похоже вы ошиблись при вводе. Попробуйте еще раз.", reply_markup=None)
        bot.register_next_step_handler(message, weight)


def height(message):
    if ((message.text).isdigit() and 0 < int(message.text) < 300):  # проверить на строчку
        bot.send_message(message.chat.id, "3. Укажите, пожалуйста, длительность сахарного диабета (в годах)",
                         reply_markup=None)
        global h
        h = int(message.text)
        bot.register_next_step_handler(message, age)
    else:
        bot.send_message(message.chat.id, "Похоже вы ошиблись при вводе. Попробуйте еще раз.", reply_markup=None)
        bot.register_next_step_handler(message, height)


def age(message):
    if ((message.text).isdigit() and 0 < int(message.text) < 150):  # проверить на строчку
        a = int(message.text)
        global h, w
        imt = w / ((h / 100) ** 2)
        imt = round(imt, 2)
        bot.send_message(message.chat.id, f'Отлично! Ваш индекса массы тела (ИМТ): {imt}', reply_markup=None)
        if (19 <= imt <= 25):
            ideal = round(((h / 100) ** 2) * 19, 2)
        else:
            ideal = w

        if (a < 5):
            day = round((ideal * 0.5), 2)
        elif (5 <= a < 10):
            day = round((ideal * 0.7), 2)
        else:
            day = round((ideal * 0.9), 2)
        basal = round((day * 0.4), 2)

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton("Ещё раз")
        button_2 = types.KeyboardButton("Назад")
        keyboard.add(button_1, button_2)
        bot.send_message(message.chat.id, f'Суточная доза инсулина (СДИ): {day}', reply_markup=keyboard)
        bot.send_message(message.chat.id, f'Доза базального инсулина: {basal}', reply_markup=keyboard)

    else:
        bot.send_message(message.chat.id, "Похоже вы ошиблись при вводе. Попробуйте еще раз.", reply_markup=None)
        bot.register_next_step_handler(message, age)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if (message.text == "Ещё раз"):
        calc_handler(message)
    else:
        bot.send_message(message.chat.id, "Ой, произошла ошибка. Убедитесь в корректности ввода")


# Запускаем бота
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as _ex:
        print(_ex)
        sleep(15)
