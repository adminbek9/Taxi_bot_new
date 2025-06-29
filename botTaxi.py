from telethon.sync import TelegramClient, events

# Telegram API ma'lumotlaringiz
api_id = 22731419
api_hash = '2e2a9ce500a5bd08bae56f6ac2cc4890'

# Telegram sessiya nomi
client = TelegramClient('taxi_session', api_id, api_hash)

# Faqat "odam bor" yoki "odam kerak" mazmunidagi kalit so‘zlar
keywords = [
    'odam bor',
    'Rishtondan toshkentga odam bor',
    'Toshkentdan Rishtonga odam bor',
    'Odam bor 1',
    'Rishtonga odam bor',
    'Toshkentga odam bor',
    'pochta bor',
    'rishtonga pochta bor',
    'Rishtondan pochta bor',
    'Toshkentga pochta bor',
    'Toshkentdan pochta bor',
    'ketadi',
    'ketishadi',
    'ketishi kerak',
    'ketishi',
    'ayol kishi ketadi'
]

# Xabarlarni yuboriladigan kanal yoki guruh username'i
target_chat = '@rozimuhammadTaxi'  # To‘g‘ridan-to‘g‘ri username, link emas

# Faqat guruh va kanallardan xabarlarni tekshirish (shaxsiy chat emas)
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    try:
        if not (await event.get_chat()).megagroup and not (await event.get_chat()).broadcast:
            return  # Shaxsiy chat bo‘lsa, e'tibor bermaymiz

        text = event.message.message.lower()
        print("🔍 Tekshirilyapti:", text)

        for keyword in keywords:
            if keyword in text:
                await client.send_message(target_chat, f"🚖 E'lon topildi:\n\n{text}")
                print("✅ Topildi va yuborildi:", text)
                break
    except Exception as e:
        print("❌ Xatolik:", e)

print("🚕 Taxi bot ishga tushdi, faqat guruh va kanallardagi xabarlarni tekshiryapti...")
client.start()
client.run_until_disconnected()
