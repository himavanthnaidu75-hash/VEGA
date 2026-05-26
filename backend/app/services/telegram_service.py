import asyncio
from telegram import Bot

class TelegramNotifier:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.bot = Bot(token=self.token) if token else None

    async def send_alert(self, message):
        if self.bot and self.chat_id:
            try:
                await self.bot.send_message(chat_id=self.chat_id, text=f"🚨 VEGA ALERT: {message}")
            except Exception as e:
                print(f"Telegram failed: {e}")
