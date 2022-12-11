import telepot
import openai

# Masukkan token API Telegram dan API key OpenAI
telegram_api_token = "5975529457:AAHmluqmBTxcINyR7PCKNICr0nLt0Y4XOUE"
openai_api_key = "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"

# Inisialisasi ChatGPT
openai.api_key = openai_api_key

# Inisialisasi bot Telegram
bot = telepot.Bot(telegram_api_token)


# Fungsi untuk mengirim pesan ke ChatGPT dan menerima jawaban
def chat_with_gpt(message):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=message,
    max_tokens=4000,
    n=1,
    temperature=0.5,
  )
  return response["choices"][0]["text"]


# Fungsi callback untuk menangkap pesan yang dikirim ke bot Telegram
def handle_message(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if content_type == "text":
    message = msg["text"]
    response = chat_with_gpt(message)
    if message == '/start':
      bot.sendMessage(chat_id, 'Selamat datang, anda bisa bertanya apa saja.')
    if message != '/start':
      bot.sendMessage(chat_id, response)
      
# Mulai menangkap pesan dari Telegram
bot.message_loop(handle_message)
print("Bot telah siap untuk digunakan!")
while True:
  pass
