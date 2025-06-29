from telethon.sync import TelegramClient, events

# Telegram API ma'lumotlaringiz
api_id = 22731419
api_hash = '2e2a9ce500a5bd08bae56f6ac2cc4890'

# Session nomi
client = TelegramClient('taxi_session', api_id, api_hash)

# Faqat odam bor so'ziga oid kalitlar
keywords = [
    'odam bor',
    '2 ta odam bor',
    '3 ta odam bor',
    '4 ta odam bor',
    '5 ta odam bor',
    '6 ta odam bor',
    '7 ta odam bor',
    '8 ta odam bor',
    '9 ta odam bor',
    '10 ta odam bor',
    'necha odam bor',
    'nechtadir odam bor',
    'odam boru',
    'odam bor.',
    'odam bor!',
    'odam bor?',
    'Rishtondan odam bor',
    'Toshkentdan odam bor',
    'Rishtondan Toshkentga odam bor',
    'Toshkentdan Rishtonga odam bor',
    'Toshkentga odam bor',
    'Rishtonga odam bor',
]

# Xabarlarni forward qilinadigan joy (TO‘G‘RI formatda)
target_chat = 'https://t.me/rozimuhammadTaxi'

# Xabarlarni hamma joydan kuzatish
@client.on(events.NewMessage(chats=None))
async def handler(event):
    try:
        text = event.message.message.lower()
        print("🔍 Tekshirilyapti:", text)  # Har bir xabarni ko‘rsatish uchun
        for keyword in keywords:
            if keyword in text:
                await client.send_message(target_chat, f"🚖 E'lon topildi:\n\n{text}")
                print("✅ Topildi va yuborildi:", text)
                break
    except Exception as e:
        print("❌ Xatolik:", e)

print("🚕 Taxi bot ishga tushdi, barcha guruhdagi xabarlarni tekshiryapti...")
client.start()
client.run_until_disconnected()
