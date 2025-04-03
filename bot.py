import telebot
import os
import re
import random
import time
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

OWNER = 
API_ID = os.getenv("API_ID", "20484128")
API_HASH = os.getenv("API_HASH", "22d633560d88a98c871c4e7b13ff4261")
TOKEN = os.getenv("BOT_TOKEN", "7285637327:AAFvLMRhCVS3vDwGZkWcxeqrJJSVazDA_NY")

bot = telebot.TeleBot(TOKEN)


# Function to extract URLs from text
def extract_links(content):
    # Captures descriptions (any text) and URLs (HTTP/HTTPS links)
    pattern = re.compile(r'(.+?)\s*[-:]\s*(https?://\S+)')
    return pattern.findall(content)

# Function to convert TXT to HTML with extracted links
def txt_to_html(txt_path, html_path):
    file_name = os.path.basename(txt_path).replace('.txt', '')

    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()

    links = extract_links(content)

    if not links:
        return None  # No valid links found

    link_rows = "".join([
        f"<tr><td>{name}</td><td><a href='{url}' target='_blank'>🔗 𝐕𝐢𝐞𝐰 𝐍𝐨𝐰</a></td></tr>" 
        for name, url in links
    ])
    
    html_content = f"""
    <!doctype html>
<html>
<head>
    <link rel='preconnect' href='https://fonts.googleapis.com'>
    <link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>
    <link href='https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap' rel='stylesheet'>
    <meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=5' name='viewport'>
    <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
    <title>{file_name}</title>
    <style>
        body {{ margin: 0; font-family: 'Poppins', sans-serif; text-align: center; }}
        table {{ word-break: break-word; border-collapse: collapse; width: 100%; margin-top: 10px; }}
        summary {{ font-weight: 600; text-align: center; padding: 14px; background-color: #0f0120; color: #ffffff; font-size: 18px; list-style: none; border-radius: 50px; margin: 3px; cursor: pointer; }}
        td {{ font-size: 13px; padding: 13px; width: 50%; }}
        a {{ text-decoration: none; color: #007bff; font-weight: bold; }}
        h1 {{ color: rgb(248, 123, 6); text-align: center; font-size: 25px; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        .header {{ display: flex; justify-content: center; gap: 20px; padding: 10px; background-color: #f8f9fa; }}
        .header img {{ width: 20px; margin-right: 5px; }}
        .header a {{ display: flex; align-items: center; }}
        .footer {{ text-align: center; margin-top: 20px; }}
        .footer-text {{ font-size: 15px; font-weight: bold; background: linear-gradient(to right, #f5f37a, #f1c480); padding: 10px; }}
    </style>
</head>
<body>

    <div style="text-align: center; margin: 20px 0;">
        <img src="https://envs.sh/tOz.jpg" height="150" alt="Image Above Summary">
    </div>

    <details>
        <summary>CLICK TO OPEN</summary>
        
        <div class="header">
            <a href='https://t.me/AJ_STYLE_EDITS' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg' alt='Telegram Channel'>
                Telegram Channel
            </a>
            <a href='https://telegram.me/AJ_TECH_WORLD' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg' alt='Telegram Main Channel'>
                Telegram Main
            </a>
            <a href='https://t.me/AJ_PYTHON_15' target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg' alt='Telegram Username'>
                Telegram Username
            </a>
        </div>

        <div style="text-align: center; margin: 20px 0;">
            <img src="https://envs.sh/tdy.jpg" height="150" alt="ΛJ Tech World">
        </div>

        <h1>ΛJ 𝐓𝐄𝐂𝐇 𝐖𝐎𝐑𝐋𝐃</h1>

        <details>
            <summary>{file_name}</summary>
            <table>
                <tr><th>Title</th><th>Link</th></tr>
                {link_rows}
            </table>
            <h3>THANK YOU</h3>
            <h4>Contact with us on 
                <a href='http://telegram.me/itz_AJPYTHON_BOT'>ΛJ OFFICIAL BOT</a> in TELEGRAM.
            </h4>
        </details>
    </details>

    <div class='footer'>
        <div class='footer-text'>
            Developed By: ＡＪ_ＰＹＴＨＯＮ ㊝
        </div>
    </div>

</body>
</html>
"""
    
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

# Function to create inline keyboard
def start_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("📢 𝕺𝖋𝖋𝖎𝖈𝖎𝖆𝖑 𝕮𝖍𝖆𝖓𝖓𝖊𝖑", url="https://t.me/AJ_TECH_WORLD"),
        InlineKeyboardButton("👨‍💻 𝕺𝖜𝖓𝖊𝖗", url="https://t.me/AJ_PYTHON_15")
    )
    keyboard.row(
        InlineKeyboardButton("📸 𝕱𝖔𝖑𝖑𝖔𝖜 𝕸𝖊", url="https://www.instagram.com/obito_shots?igsh=czBkNzM5bXp6M3I2")
    )
    return keyboard

# Start Command
@bot.message_handler(commands=["start"])
def start_command(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    mention = f"[{first_name}](tg://user?id={user_id})"

    random_image_url = random.choice([
        "http://envs.sh/teT.jpg",
        "http://envs.sh/teS.jpg",
        "http://envs.sh/ten.jpg",
        "http://envs.sh/te0.jpg",
        "http://envs.sh/tt9.jpg",
        "http://envs.sh/tdy.jpg"
    ])

    caption = (
        f"**Hello {mention} 👋!**\n"
        f"➠ **Your Telegram ID:** {user_id}\n\n"
        "➠ I am a **Text To HTML Converter Bot** ♥️\n"
        "➠ I can extract and convert links from your **TXT file** into a **readable HTML page**!\n\n"
        "➠ Use **/html** to convert a .txt file to .html\n\n"
        "‡ 𝕮𝖗𝖊𝖆𝖙𝖊𝖉 𝕭𝖞: 𝗔𝗝 𝗣𝗬𝗧𝗛𝗢𝗡 💀 ‡"
    )

    bot.send_photo(
        chat_id=message.chat.id,
        photo=random_image_url,
        caption=caption,
        parse_mode="Markdown",
        reply_markup=start_keyboard()
    )

# /html Command
@bot.message_handler(commands=["html"])
def ask_for_file(message: Message):
    bot.send_message(
        message.chat.id, 
        "📂 **𝐒𝐞𝐧𝐝 𝐘𝐨𝐮𝐫 𝐓𝐗𝐓 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐜𝐨𝐧𝐯𝐞𝐫𝐭 𝐢𝐧𝐭𝐨 𝐇𝐓𝐌𝐋.**", 
        parse_mode="Markdown"
    )

# TXT File Handling
@bot.message_handler(content_types=['document'])
def handle_txt_file(message: Message):
    try:
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        
        original_file_name = message.document.file_name
        if not original_file_name.endswith('.txt'):
            bot.send_message(message.chat.id, "⚠️ Please send a valid .txt file.")
            return

        file_name_without_ext = os.path.splitext(original_file_name)[0].replace(" ", "_")
        txt_path = f"{file_name_without_ext}.txt"
        html_path = f"{file_name_without_ext}.html"

        downloaded_file = bot.download_file(file_info.file_path)
        with open(txt_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        txt_to_html(txt_path, html_path)

        with open(html_path, 'rb') as html_file:
            bot.send_document(
                message.chat.id, html_file, 
                caption=f"✅ 𝚈𝚘𝚞𝚛 𝙷𝚃𝙼𝙻 𝙵𝚒𝚕𝚎 𝚒𝚜 𝚁𝚎𝚊𝚍𝚢❗",
                parse_mode="Markdown"
            )
        
        # Send keyboard separately
        bot.send_message(
            message.chat.id,
            "𝔍𝔬𝔦𝔫 𝔒𝔲𝔯 ℭ𝔥𝔞𝔫𝔫𝔢𝔩𝔰 𝔣𝔬𝔯 𝔘𝔭𝔡𝔞𝔱𝔢𝔰",
            reply_markup=start_keyboard()
        )

        os.remove(txt_path)
        os.remove(html_path)
        
    except Exception as e:
        bot.send_message(message.chat.id, "❌ An error occurred while processing your file.")
        print(f"Error: {e}")

# Run bot polling
if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            print(f"Bot crashed: {e}")
            time.sleep(5)

import os
import html
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Set in Render environment variables
ALLOWED_USER_IDS = []  # Add your user ID if you want to restrict access

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the command /start is issued."""
    await update.message.reply_text(
        '📄 TXT to HTML Converter Bot\n\n'
        'Send me a .txt file and I will convert it to HTML format!'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when the command /help is issued."""
    await update.message.reply_text(
        'Simply send me a .txt file and I will convert it to HTML.\n\n'
        'The HTML file will preserve your original formatting with:\n'
        '- Paragraphs (<p> tags)\n'
        '- Line breaks (<br> tags)\n'
        '- Special characters properly escaped'
    )

def convert_txt_to_html(txt_content):
    """Convert plain text to basic HTML format."""
    # Escape HTML special characters
    escaped_content = html.escape(txt_content)
    
    # Replace line breaks with HTML tags
    html_content = escaped_content.replace('\n\n', '</p><p>')  # Double newline = paragraph
    html_content = html_content.replace('\n', '<br>')          # Single newline = line break
    
    # Wrap in basic HTML structure
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Converted Document</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }}
    </style>
</head>
<body>
    <p>{html_content}</p>
</body>
</html>"""
    
    return full_html

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the document upload and convert it to HTML."""
    # Check if user is allowed (if restrictions are set)
    if ALLOWED_USER_IDS and update.effective_user.id not in ALLOWED_USER_IDS:
        await update.message.reply_text("Sorry, you're not authorized to use this bot.")
        return
    
    document = update.message.document
    
    # Check if it's a .txt file
    if not document.file_name.lower().endswith('.txt'):
        await update.message.reply_text("Please send a .txt file.")
        return
    
    # Download the file
    file = await context.bot.get_file(document.file_id)
    txt_file = await file.download_to_drive()
    
    # Read the file content
    with open(txt_file, 'r', encoding='utf-8') as f:
        txt_content = f.read()
    
    # Convert to HTML
    html_content = convert_txt_to_html(txt_content)
    
    # Create HTML file
    html_filename = os.path.splitext(document.file_name)[0] + '.html'
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Send the HTML file back
    with open(html_filename, 'rb') as f:
        await update.message.reply_document(
            document=InputFile(f, filename=html_filename),
            caption="Here's your HTML file!"
        )
    
    # Clean up temporary files
    os.remove(txt_file)
    os.remove(html_filename)

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    
    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
