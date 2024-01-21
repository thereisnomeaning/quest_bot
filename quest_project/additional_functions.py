import telebot
from telebot import types


def quest_markup(options):
    option1 = options[0]
    option2 = options[1]

    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton(option1)
    button2 = types.KeyboardButton(option2)
    markup.add(button1)
    markup.add(button2)

    return markup


def start_quest_markup(options):
    option1 = options[0]
    option2 = options[1]
    option3 = options[2]

    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton(option1)
    button2 = types.KeyboardButton(option2)
    button3 = types.KeyboardButton(option3)
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)

    return markup


help_text = '''Взаимодействие с ботом происходит засчет кнопок. В зависимости от вашего выбора вам будут представлены различные ветви развития событий. Если захотите начать прохождение квеста заново, введите команду '/start'''
starting_text = '''Добро пожаловать в мир, где лес становится чем-то гораздо более темным и загадочным. Вы окунулись в глубокие тени леса, где каждое дерево кажется хранит в себе зловещую тайну, а каждый шорох – предупреждение о надвигающейся угрозе. Однако, самая страшная опасность скрывается в темных закоулках этого леса – монстр, чей взгляд замерзает кровь в жилах.

Вы должны бережно выбирать свой путь. В глубинах леса ваши решения будут иметь вес, ибо каждый неверный шаг может привести к встрече с тем, чего лучше не видеть.'''