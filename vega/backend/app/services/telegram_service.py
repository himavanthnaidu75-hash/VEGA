import httpx
from ..core.config import settings
from loguru import logger

class TelegramService:
    @staticmethod
    async def send_message(message: str):
        if not settings.TELEGRAM_BOT_TOKEN or not settings.TELEGRAM_CHAT_ID:
            logger.warning("Telegram not configured. Skipping message.")
            return

        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        async with httpx.AsyncClient() as client:
            try:
                await client.post(url, json=data)
            except Exception as e:
                logger.error(f"Failed to send Telegram message: {e}")

    @staticmethod
    async def send_kill_alert():
        await TelegramService.send_message("<b>[VEGA 2.0] KILL SWITCH ACTIVATED</b>\nAll positions squared off. System halted.")
