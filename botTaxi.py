from telethon import TelegramClient, events
from telethon.tl.types import User, Chat, Channel

api_id = 22731419
api_hash = '2e2a9ce500a5bd08bae56f6ac2cc4890'

client = TelegramClient('taxi_session', api_id, api_hash)

# Filtrlash uchun kalit so'zlar ro'yxati (kichik-katta harf farqi yo'q)
keywords = [
    'odam bor', 'rishtondan toshkentga odam bor', 'toshkentdan rishtonga odam bor',
    'odam bor 1', 'rishtonga odam bor', 'toshkentga odam bor',
    'pochta bor', 'rishtonga pochta bor', 'rishtondan pochta bor',
    'toshkentga pochta bor', 'toshkentdan pochta bor',
    'ketadi', 'ketishadi', 'ketishi kerak', 'ketishi', 'ayol kishi ketadi'
]

# Maqsadli kanal yoki guruh username (xabarlar shu yerga yuboriladi)
target_chat = '@rozimuhammadTaxi'

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    try:
        # Shaxsiy chatlarni o'tkazib yuborish
        if event.is_private:
            return

        # Xabar matnini kichik harfga o'tkazib olish
        text = event.raw_text.lower()
        if not text:
            return

        # Kalit so'zlardan hech biri topilmasa, o'tkazib yuborish
        if not any(keyword in text for keyword in keywords):
            return

        # Chat (guruh yoki kanal) ma'lumotlarini olish
        chat = await event.get_chat()

        # Manba nomi va linkini tayyorlash
        if hasattr(chat, 'username') and chat.username:
            chat_link = f"https://t.me/{chat.username}/{event.message.id}"
            chat_name = chat.title or chat.username
            source_line = f"{chat_name} ({chat_link})"
        else:
            chat_name = chat.title or "Noma’lum guruh/kanal"
            source_line = f"{chat_name} (Link yo‘q, yopiq guruh)"

        # Xabarni tayyorlash (oddiy, aniq va chiroyli)
        message_to_send = (
            f"🚖 <b>Xabar topildi!</b>\n\n"
            f"📄 <b>Matn:</b>\n{text}\n\n"
            f"📍 <b>Qayerdan:</b>\n{source_line}\n\n"
            f"🤝 <i>Hamkorlik va do‘stlik yo‘lidamiz. Siz bilan birgamiz!</i>"
        )

        # Maqsadli kanalgga xabar yuborish
        await client.send_message(target_chat, message_to_send, parse_mode='html')

        print("✅ Xabar yuborildi:", text[:50])

    except Exception as e:
        print("❌ Xatolik:", e)

print("🚕 Taxi bot ishga tushdi...")

client.start()
client.run_until_disconnected()
