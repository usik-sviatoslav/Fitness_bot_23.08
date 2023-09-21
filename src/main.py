from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
import os
from db import engine, SessionLocal
from models import Base, User
from sqlalchemy.orm import Session  # Import Session

from src.csv_file_handler import CSVFileHandler
from src.user_service import UserService

Base.metadata.create_all(bind=engine)

"""
example of a function to create a user

def create_user(username: str, email: str):
    db = SessionLocal()
    db_user = User(username=username, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user
"""


class FitnessBot:

    def __init__(self, token):
        self.app = Application.builder().token(token).build()

        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CallbackQueryHandler(self.handle_type_options, pattern='^type_.*$'))
        self.app.add_handler(CallbackQueryHandler(self.handle_coach_options, pattern='^coach_.*$'))

    async def start(self, update: Update, context: CallbackContext) -> None:
        keyboard = [
            [
                InlineKeyboardButton("Coach", callback_data='type_coach'),
                InlineKeyboardButton("Athlete", callback_data='type_athlete')
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Please choose your type:", reply_markup=reply_markup)

    async def handle_coach_options(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query_data = query.data
        user_type = query_data.split('_')[1]

        await query.edit_message_text(user_type)

    async def handle_type_options(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        query_data = query.data
        user_id = update.callback_query.from_user.id
        user_type = query_data.split('_')[1]
        user_name = update.callback_query.from_user.username
        first_name = update.callback_query.from_user.first_name
        last_name = update.callback_query.from_user.last_name
        user_service = UserService(CSVFileHandler("users.csv"))
        user_service.add_user([user_id, user_name, first_name, last_name, user_type])
        if user_type == 'coach':
            coach_keyboard = [
                [
                    InlineKeyboardButton("Show my athletes", callback_data='coach_show_athletes'),
                    InlineKeyboardButton("Add workout program", callback_data='coach_add_program')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(coach_keyboard)
            await query.edit_message_text("Choose an option:", reply_markup=reply_markup)
        elif user_type == 'athlete':
            await query.edit_message_text("Athlete options go here")
        else:
            await query.edit_message_text("Invalid type. Please choose either 'Coach' or 'Athlete'.")

    def run(self):
        self.app.run_polling()


if __name__ == '__main__':
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    bot = FitnessBot(TOKEN)
    bot.run()
