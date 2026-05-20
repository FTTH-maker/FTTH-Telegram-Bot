from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from flask import Flask
from threading import Thread

# ============================================
# BOT TOKEN
# ============================================

TOKEN = "8781557191:AAEgCd5ajY60qbfl149Z6Ktl67QKNY2zzSU"

# ============================================
# FLASK KEEP-ALIVE SERVER
# ============================================

app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "✅ FTTH Bot is Running!"

def run_web():
    app_web.run(
        host="0.0.0.0",
        port=8080,
        debug=False,
        use_reloader=False
    )

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# ============================================
# LANGUAGE STORAGE
# ============================================

user_language = {}

# ============================================
# START COMMAND
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["🇬🇧 English", "🇪🇹 አማርኛ"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 Welcome / እንኳን ደህና መጡ\n\n"
        "Please choose language / ቋንቋ ይምረጡ",
        reply_markup=reply_markup
    )

# ============================================
# ENGLISH MENU
# ============================================

async def show_english_menu(update):

    keyboard = [
        ["🌐 Internet Not Working"],
        ["🚨 LOS Red Light"],
        ["🐢 Slow Internet"],
        ["📄 Package Information"],
        ["🌍 Change Language"],
        ["📞 Talk to Agent"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    message = (
        "━━━━━━━━━━━━━━━━━━\n"
        "📡 SAFARICOM BET-WIFI SUPPORT\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Welcome 👋\n\n"
        "Please choose a service below."
    )

    await update.message.reply_text(
        message,
        reply_markup=reply_markup
    )

# ============================================
# AMHARIC MENU
# ============================================

async def show_amharic_menu(update):

    keyboard = [
        ["🌐 ኢንተርኔት አይሰራም"],
        ["🚨 LOS ቀይ መብራት"],
        ["🐢 የኢንተርኔት ፍጥነት ዝቅተኛ"],
        ["📄 የጥቅል መረጃ"],
        ["🌍 ቋንቋ ለመቀየር"],
        ["📞 ኤጀንት ለማግኘት"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    message = (
        "━━━━━━━━━━━━━━━━━━\n"
        "📡 የሳፋሪኮም ቤት-ዋይፋይ ድጋፍ\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "እንኳን ደህና መጡ 👋\n\n"
        "እባክዎ ከታች አማራጭ ይምረጡ።"
    )

    await update.message.reply_text(
        message,
        reply_markup=reply_markup
    )

# ============================================
# HANDLE MESSAGES
# ============================================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.message.from_user.id

    # ========================================
    # LANGUAGE SELECTION
    # ========================================

    if text == "🇬🇧 English":
        user_language[user_id] = "english"
        await show_english_menu(update)
        return

    elif text == "🇪🇹 አማርኛ":
        user_language[user_id] = "amharic"
        await show_amharic_menu(update)
        return

    # ========================================
    # CHANGE LANGUAGE
    # ========================================

    elif "Change Language" in text or "ቋንቋ" in text:
        await start(update, context)
        return

    # ========================================
    # INTERNET ISSUE
    # ========================================

    elif text == "🌐 Internet Not Working":

        reply = (
            "🔧 Please follow these steps:\n\n"
            "1. Check power cable\n"
            "2. Restart router\n"
            "3. Wait 1 minute\n"
            "4. Check LOS light\n\n"
            "If issue continues, contact support."
        )

    elif text == "🌐 ኢንተርኔት አይሰራም":

        reply = (
            "🔧 እባክዎ የሚከተሉትን ይፈትሹ:\n\n"
            "1. የኃይል ገመድ\n"
            "2. Router ዳግም ያስጀምሩ\n"
            "3. 1 ደቂቃ ይጠብቁ\n"
            "4. LOS መብራት ይፈትሹ"
        )

    # ========================================
    # LOS ISSUE
    # ========================================

    elif text == "🚨 LOS Red Light":

        reply = (
            "🚨 LOS red light means fiber signal issue.\n\n"
            "• Check fiber cable\n"
            "• Restart router\n"
            "• Wait 2 minutes"
        )

    elif text == "🚨 LOS ቀይ መብራት":

        reply = (
            "🚨 LOS ቀይ መብራት የፋይበር ችግር ነው።\n\n"
            "• Fiber cable ይፈትሹ\n"
            "• Router ዳግም ያስጀምሩ"
        )

    # ========================================
    # SLOW INTERNET
    # ========================================

    elif text == "🐢 Slow Internet":

        reply = (
            "🐢 For slow internet:\n\n"
            "• Restart router\n"
            "• Disconnect unused devices\n"
            "• Move closer to WiFi"
        )

    elif text == "🐢 የኢንተርኔት ፍጥነት ዝቅተኛ":

        reply = (
            "🐢 የኢንተርኔት ፍጥነት ችግር:\n\n"
            "• Router ዳግም ያስጀምሩ\n"
            "• ያልተጠቀሙ መሳሪያዎች ያጥፉ"
        )

    # ========================================
    # PACKAGE INFO
    # ========================================

    elif text == "📄 Package Information":

        reply = (
            "📦 Available Packages\n\n"
            "🔹 10 Mbps — 1599 ETB\n"
            "🔹 20 Mbps — 2899 ETB\n"
            "🔹 Device Price — 3000 ETB"
        )

    elif text == "📄 የጥቅል መረጃ":

        reply = (
            "📦 ያሉ ፓኬጆች\n\n"
            "🔹 10 Mbps — 1599 ETB\n"
            "🔹 20 Mbps — 2899 ETB\n"
            "🔹 Device — 3000 ETB"
        )

    # ========================================
    # TALK TO AGENT
    # ========================================

    elif text == "📞 Talk to Agent" or text == "📞 ኤጀንት ለማግኘት":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📞 Join Support Group",
                    url="https://t.me/BetWiFiSupport"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "👇 Click below to contact support",
            reply_markup=reply_markup
        )

        return

    # ========================================
    # UNKNOWN MESSAGE
    # ========================================

    else:
        reply = "⚠ Please choose an option from the menu."

    await update.message.reply_text(reply)

# ============================================
# MAIN APPLICATION
# ============================================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
)

keep_alive()

print("✅ Flask server started")
print("✅ FTTH Support Bot Running...")

app.run_polling()