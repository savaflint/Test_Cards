from telebot import TeleBot, types
from faker import Faker

bot = TeleBot(token='токен', parse_mode='html')

faker = Faker()

card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)
# второй ряд кнопок
card_type_keybaord.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет! Я умею генерировать номер тестовой банковской карты\nВыбери тип карты:',
        reply_markup=card_type_keybaord,
    )


@bot.message_handler()
def message_handler(message: types.Message):
    
    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'
    elif message.text == 'Maestro':
        card_type = 'maestro'
    elif message.text == 'JCB':
        card_type = 'jcb'
    else:
        # если текст не совпал ни с одной из кнопок 
        # выводим ошибку
        bot.send_message(
            chat_id=message.chat.id,
            text='Не понимаю тебя :(',
        )
        return

    
    # card_type может принимать одно из зачений ['maestro', 'mastercard', 'visa13', 'visa16', 'visa19',
    # 'amex', 'discover', 'diners', 'jcb15', 'jcb16']
    card_number = faker.credit_card_number(card_type)
    
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Тестовая карта {card_type}:\n<code>{card_number}</code>'
    )

def main():
    
    bot.infinity_polling()


if __name__ == '__main__':
    main()
