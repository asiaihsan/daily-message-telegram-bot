import asyncio
import schedule
import time
import random
from datetime import datetime, date
from telegram import Bot

BOT_TOKEN = "8609211032:AAENihPItIEctbsDXTj8cAV0bXSzUt7LhtE"
CHAT_ID   = "-1001515629570"

RAMADAN_START = date(2026, 2, 18)
RAMADAN_END   = date(2026, 3, 19)

DUAS = [
    "﴿ إِنَّ الَّذِينَ يَتْلُونَ كِتَابَ اللَّهِ وَأَقَامُوا الصَّلَاةَ وَأَنفَقُوا مِمَّا رَزَقْنَاهُمْ سِرًّا وَعَلَانِيَةً يَرْجُونَ تِجَارَةً لَّن تَبُورَ ﴾\n_سورة فاطر: ٢٩_",
    "﴿ وَنُنَزِّلُ مِنَ الْقُرْآنِ مَا هُوَ شِفَاءٌ وَرَحْمَةٌ لِّلْمُؤْمِنِينَ ﴾\n_سورة الإسراء: ٨٢_",
    "﴿ إِنَّ هَـٰذَا الْقُرْآنَ يَهْدِي لِلَّتِي هِيَ أَقْوَمُ ﴾\n_سورة الإسراء: ٩_",
    "اللّهمّ اجعلنا من أهل القرآن الذين هم أهلك وخاصّتك 🤲",
    "اللّهمّ تقبّل منّا صيامنا وقيامنا وتلاوتنا في هذا الشهر الكريم 🤲",
    "﴿ شَهْرُ رَمَضَانَ الَّذِي أُنزِلَ فِيهِ الْقُرْآنُ هُدًى لِّلنَّاسِ ﴾\n_سورة البقرة: ١٨٥_",
    "اللّهمّ اجعل القرآن ربيع قلوبنا ونور صدورنا 🤲",
]

def get_ramadan_day():
    today = date.today()
    if RAMADAN_START <= today <= RAMADAN_END:
        return (today - RAMADAN_START).days + 1
    return None

def build_message():
    now = datetime.now()
    day_name = now.strftime("%A")
    date_str = now.strftime("%d - %B - %Y")
    ramadan_day = get_ramadan_day()

    lines = [
        f"📅 *{date_str}*",
        f"🗓️ *{day_name}*",
    ]
    if ramadan_day:
        lines.append(f"🌙 *Day {ramadan_day} of Ramadan 1447*")

    lines += [
        "",
        "Aween",
        "",
        "Asia",
        "",
        "Aziz",
        "",
        "Awez",
        "",
        "Amez",
        "",
        "Aysha",
        "",
        "Bahra",
        "",
        "Payam",
        "",
        "Gashbeen",
        "",
        "Skalla",
        "",
        "Sana",
        "",
        "─────────────────────────────",
        random.choice(DUAS),
    ]
    return "\n".join(lines)

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=build_message(), parse_mode="Markdown")
    print(f"✅ Sent at {datetime.now()}")

def job():
    asyncio.run(send_message())

schedule.every().day.at("08:00").do(job)

print("🤖 Bot running... Press Ctrl+C to stop.")
job()
while True:
    schedule.run_pending()
    time.sleep(30)