from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler


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
        user_type = query_data.split('_')[1]

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
    TOKEN = "6339442727:AAEA7V9pgUX4uo80fSR4eG1PCWQwOQJF2aQ"
    bot = FitnessBot(TOKEN)
    bot.run()
