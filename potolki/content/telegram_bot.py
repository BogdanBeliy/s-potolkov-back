import telepot

my_id = [662122625, 862543651, 1305202028]
bot = telepot.Bot(token)


def send_message(text):
    for i in my_id:
        bot.sendMessage(i, text, parse_mode="Markdown")
