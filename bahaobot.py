import telebot, random, os
bot = telebot.TeleBot(")

@bot.message_handler(commands = ['start', 'help'])
def echo(message):
    bot.reply_to(message, "WELCOME TO BOT PROTECT YOUR SCRIPT PHP , PLEASE USED COMMAND :\n/enc_php")

def enc(message):
    rd = random.randint(0, 1000)
    file_send = f'{str(rd)}.php'
    try:
        if message.document:
            file_info = bot.get_file(message.document.file_id)
            bot.reply_to(message, 'CURRENTLY PROCESSING FILE...')
            downloaded_file = bot.download_file(file_info.file_path)
            bot.send_message(message.chat.id, 'PROCESS SUCCESS')
            with open(file_send, 'wb') as f:
                f.write(downloaded_file)
            bot.send_message(message.chat.id, 'PLEASE WAIT 5 MINUTE')
            out = 'obf-' + file_send
            os.system(f"php main.php {file_send} {out}")
            with open(out, 'rb') as enc:
                bot.send_document(message.chat.id, enc)
            bot.send_message(message.chat.id, 'SUCCESS, THANK YOU USED OBFUSCATE!')
            os.system("rm -rf {file_send}")
            os.system("rm -rf {out}")
        else:
            bot.reply_to(message, "Invalid File?")
            return
    except Exception as e:
        bot.reply_to(message, str(e))
        
@bot.message_handler(commands = ['enc_php'])
def enc_php(message):
    bot.send_message(message.chat.id, "PLEASE SEND SCRIPT PHP ")
    bot.register_next_step_handler(message, enc)

bot.polling()