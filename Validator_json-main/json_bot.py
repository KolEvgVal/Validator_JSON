from telebot import TeleBot, types
import json

bot = TeleBot(token='6950782744:AAEHO3CgPx5J8YVOMWu_2DzZBsVC2Nnxme8', parse_mode='html')


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет! Я умею проверять JSON и форматировать его в красивый текст\nВведи JSON в виде строки:',
    )

@bot.message_handler()
def message_handler(message: types.Message):
    try:
        payload = json.loads(message.text)
    except json.JSONDecodeError as ex:
        bot.send_message(
            chat_id=message.chat.id,
            text=f'При обработке произошла ошибка:\n<code>{str(ex)}</code>'
        )
        return
    
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'JSON:\n<code>{text}</code>'
    )

def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
