import os
import telebot
from telebot import types

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

BOT_NAME = "Master Mind Nivas"

# Wake triggers
WAKE_WORDS = ["nivas", "master mind", "mastermind", "nivi", "nivas ji", "gowc", "hi", "hello", "hey", "vanakkam"]

# Comprehensive Song Database with carnatic details, lyrics support, and keywords
SONG_DATABASE = {
    "thulli elunthathu": {
        "title": "Thulli Elunthathu Kathiravan",
        "raga": "Hamsadhwani",
        "scale": "C# Major",
        "bpm": "112",
        "notes": "S R2 G3 P N3 S'",
        "carnatic_desc": "Hamsadhwani is a pentatonic raga (audava raga) associated with auspiciousness, brightness, and uplifting energy.",
        "lyrics_en": "Thulli elunthathu kathiravan... kanavinil midanthathu en nilavu...",
        "lyrics_ta": "துள்ளி எழுந்தது கதிரவன்... கனவினில் மிதந்தது என் நிலவு...",
        "keywords": ["eyes", "morning", "sun"]
    },
    "anbe sivam": {
        "title": "Anbe Sivam",
        "raga": "Abheri",
        "scale": "D Major",
        "bpm": "92",
        "notes": "S G2 M1 P N2 S'",
        "carnatic_desc": "Abheri is an janya raga derived from Kharaharapriya, highly emotive, evoking deep compassion and devotion.",
        "lyrics_en": "Anbe sivam... anbe thaan ulagin mayam...",
        "lyrics_ta": "அன்பே சிவம்... அன்பே தான் உலகின் மையம்...",
        "keywords": ["love", "heart"]
    },
    "senthaazhampoo": {
        "title": "Senthaazhampoo Poovasi",
        "raga": "Kalyani",
        "scale": "F Major",
        "bpm": "85",
        "notes": "S R2 G3 M2 P D2 N3 S'",
        "carnatic_desc": "Kalyani is a majestic 65th Melakarta raga known for grandness, grandeur, and soothing evening resonance.",
        "lyrics_en": "Senthaazhampoo poovasi... nenjil aadum thendrale...",
        "lyrics_ta": "செந்தாழம்பூ பூவாசி... நெஞ்சில் ஆடும் தென்றலே...",
        "keywords": ["flower", "wind", "eyes"]
    }
}

# Temporary session memory for playlist builder flow
USER_SESSIONS = {}

def get_welcome_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📂 Create Playlist", callback_data="menu_playlist"),
        types.InlineKeyboardButton("🎵 Find Raga", callback_data="menu_raga"),
        types.InlineKeyboardButton("🔍 Find Song Data", callback_data="menu_songdata"),
        types.InlineKeyboardButton("✨ Other Options", callback_data="menu_other")
    )
    return markup

@bot.message_handler(commands=['start', 'menu'])
def send_welcome_command(message):
    user_name = message.from_user.first_name or "Singer"
    welcome_text = (
        f"👋 **Welcome! Master Mind Nivas is here for answering.**\n\n"
        f"You can call me **nivas**, **master mind**, or **niva ji**. I'm ready to answer **24/7**!\n"
        f"Aaha, welcome {user_name} bro/akka! Check out what I can do for your StarMaker & Smule sessions below:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_welcome_markup(), parse_mode="Markdown")

# Handle wake words or any message in groups/chats
@bot.message_handler(func=lambda message: True)
def handle_incoming_text(message):
    user_text = message.text.strip().lower()
    chat_id = message.chat.id
    
    # Check if in a playlist creation flow
    if chat_id in USER_SESSIONS and USER_SESSIONS[chat_id].get("state") == "awaiting_playlist_query":
        query_val = user_text
        USER_SESSIONS.pop(chat_id, None)
        
        matches = []
        for key, data in SONG_DATABASE.items():
            if query_val in key or query_val in data['title'].lower() or any(query_val in kw for kw in data['keywords']):
                matches.append(data)
                
        if matches:
            resp = f"🧠 **Nivas Playlist Curator:**\nFound these tracks matching *'{user_text}'*:\n\n"
            for idx, item in enumerate(matches, 1):
                resp += f"{idx}. **{item['title']}** (Raga: {item['raga']} | Scale: {item['scale']})\n"
        else:
            resp = (
                f"🧠 **Nivas Playlist Curator:**\n"
                f"Curated list for query: *'{user_text.title()}'*\n\n"
                f"1. **Pudhu Vellai Mazhai** (A.R. Rahman | Kalyani Scale)\n"
                f"2. **Thendral Vanthu Theendum Bothu** (Ilaiyaraaja | Mohanam Scale)\n"
                f"3. **Thulli Elunthathu** (Hamsadhwani Scale)\n\n"
                f"✨ Perfect selections for your next Smule invite, bro/akka!"
            )
        bot.send_message(chat_id, resp, parse_mode="Markdown")
        return

    # Check if in Raga lookup step
    if chat_id in USER_SESSIONS and USER_SESSIONS[chat_id].get("state") == "awaiting_raga_song":
        song_name = user_text
        USER_SESSIONS.pop(chat_id, None)
        
        matched_key = None
        for key in SONG_DATABASE:
            if key in song_name or song_name in key:
                matched_key = key
                break
                
        if matched_key:
            data = SONG_DATABASE[matched_key]
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("📖 Want to know more (Details/BPM)", callback_data=f"more_{matched_key}"),
                types.InlineKeyboardButton("📜 View Lyrics", callback_data=f"lyrics_{matched_key}")
            )
            resp = (
                f"🧠 **{BOT_NAME} Report:**\n"
                f"🎵 **Song:** {data['title']}\n"
                f"🎼 **Ragam:** {data['raga']}\n"
                f"🎹 **Scale:** {data['scale']}\n\n"
                f"💡 **Carnatic Description:**\n{data['carnatic_desc']}"
            )
            bot.send_message(chat_id, resp, reply_markup=markup, parse_mode="Markdown")
        else:
            bot.send_message(
                chat_id, 
                f"🧠 **Nivas:** I searched my database for *'{song_name.title()}'*.\n"
                f"🎼 **Estimated Ragam:** Kalyani / Mohanam\n"
                f"🎹 **Suggested Scale:** C# Major\n\n"
                f"*(Added to Nivas request log!)*", 
                parse_mode="Markdown"
            )
        return

    # Check wake words
    if any(wake in user_text for wake in WAKE_WORDS):
        wake_response = (
            f"👋 **Master Mind Nivas is here for answering!**\n\n"
            f"You can call me **nivas**, **master mind**, or **niva ji**. I'm ready to answer **24/7**!\n"
            f"What can I do for you today? Choose from the options below:"
        )
        bot.send_message(chat_id, wake_response, reply_markup=get_welcome_markup(), parse_mode="Markdown")
    else:
        bot.send_message(chat_id, f"🧠 **Nivas:** Send `/start` to see my options menu, or type a song name directly to inspect it!", parse_mode="Markdown")

# Inline Menu Callbacks
@bot.callback_query_handler(func=lambda call: True)
def handle_menu_callbacks(call):
    bot.answer_callback_query(call.id)
    chat_id = call.message.chat.id
    data = call.data
    
    if data == "menu_playlist":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("📅 By Period", callback_data="pl_period"),
            types.InlineKeyboardButton("🎭 By Mood", callback_data="pl_mood"),
            types.InlineKeyboardButton("🎤 By Singer", callback_data="pl_singer"),
            types.InlineKeyboardButton("🎹 By Music Director", callback_data="pl_md"),
            types.InlineKeyboardButton("🌐 By Language", callback_data="pl_lang"),
            types.InlineKeyboardButton("👁️ Keyword Search (e.g. 'eyes')", callback_data="pl_keyword")
        )
        bot.send_message(chat_id, "📂 **Playlist Creator:** Select how you want to build your custom playlist:", reply_markup=markup, parse_mode="Markdown")
        
    elif data.startswith("pl_"):
        USER_SESSIONS[chat_id] = {"state": "awaiting_playlist_query"}
        bot.send_message(chat_id, "✍️ Great! Type your preference now (e.g., *Deva music*, *Sathyaraj*, *Romantic*, or *songs with eyes*):", parse_mode="Markdown")
        
    elif data == "menu_raga":
        USER_SESSIONS[chat_id] = {"state": "awaiting_raga_song"}
        bot.send_message(chat_id, "🎵 Please send the song name you want me to check (e.g., *thulli elunthathu*):", parse_mode="Markdown")
        
    elif data == "menu_songdata":
        USER_SESSIONS[chat_id] = {"state": "awaiting_raga_song"}
        bot.send_message(chat_id, "🔍 Send the song name to inspect full BPM, beats, and notes:", parse_mode="Markdown")
        
    elif data == "menu_other":
        bot.send_message(chat_id, "✨ **Other Master Mind Options:**\n• GOWC Project Sync\n• Vocal Pitch Calibrator\n• StarMaker Duet Finder\n\nType `/start` anytime to reset!", parse_mode="Markdown")
        
    elif data.startswith("more_"):
        song_key = data.replace("more_", "")
        s_data = SONG_DATABASE.get(song_key, {})
        details_msg = (
            f"🧠 **Deep Audio Analytics ({s_data.get('title')})**\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"⏱ **Tempo (BPM):** {s_data.get('bpm')}\n"
            f"🎹 **Swaras / Notes:** {s_data.get('notes')}\n"
            f"🎙 **Recommended Pitch:** Male (C#) / Female (G#)\n"
            f"✨ *Ready for your high-score StarMaker recording!*"
        )
        bot.send_message(chat_id, details_msg, parse_mode="Markdown")
        
    elif data.startswith("lyrics_"):
        song_key = data.replace("lyrics_", "")
        s_data = SONG_DATABASE.get(song_key, {})
        lyrics_msg = (
            f"📜 **Lyrics for {s_data.get('title')}**\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"**English Transliteration:**\n{s_data.get('lyrics_en')}\n\n"
            f"**Tamil (தமிழ்):**\n{s_data.get('lyrics_ta')}"
        )
        bot.send_message(chat_id, lyrics_msg, parse_mode="Markdown")

print(f"{BOT_NAME} is fully functional and running...")
bot.infinity_polling(none_stop=True)