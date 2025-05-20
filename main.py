from PIL import Image
from io import BytesIO
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Replace with your own Telegram Bot token
TOKEN = ""

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Send me an image and I will convert it to PDF.")

def convert_image_to_pdf(image_file: BytesIO) -> BytesIO:
    image = Image.open(image_file)
    pdf_output = BytesIO()
    image.save(pdf_output, "PDF", resolution=100.0)
    pdf_output.seek(0)
    return pdf_output

async def handle_image(update: Update, context: CallbackContext):
    file = await update.message.photo[-1].get_file() 
    image_bytes = await file.download_as_bytearray() 

    pdf_file = convert_image_to_pdf(BytesIO(image_bytes))

    await update.message.reply_document(document=pdf_file, filename="converted_image.pdf")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO | filters.Document.IMAGE, handle_image))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
