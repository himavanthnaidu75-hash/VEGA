from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from loguru import logger
from .orchestrator import TradingOrchestrator
from ..services.telegram_service import TelegramService
import asyncio
import datetime
import pytz

class VegaScheduler:
    def __init__(self, orchestrator: TradingOrchestrator):
        self.orchestrator = orchestrator
        self.scheduler = AsyncIOScheduler(timezone=pytz.timezone('Asia/Kolkata'))
        self.selected_mode = "equities" # Default

    def start(self):
        # 08:45 IST — Startup
        self.scheduler.add_job(self.startup_check, CronTrigger(hour=8, minute=45))
        # 09:00 IST — Pre-market intent prompt
        self.scheduler.add_job(self.pre_market_session, CronTrigger(hour=9, minute=0))
        # 09:15 IST — Market open: begin scanning
        self.scheduler.add_job(self.orchestrator.start_scanning, CronTrigger(hour=9, minute=15))
        # 15:00 IST — Stop entries
        self.scheduler.add_job(self.stop_new_entries, CronTrigger(hour=15, minute=0))
        # 15:15 IST — Square off
        self.scheduler.add_job(self.orchestrator.square_off_all, CronTrigger(hour=15, minute=15))

        self.scheduler.start()
        logger.info("Vega Scheduler fully configured and started.")

    async def startup_check(self):
        logger.info("System startup. Connecting to broker...")
        self.orchestrator.broker.connect()

    async def pre_market_session(self):
        prompt = (
            "Good morning. What would you like to trade today?\n"
            "1. NSE Equities (default)\n"
            "2. Nifty / BankNifty Options (F&O)\n"
            "3. Futures\n"
            "4. Let VEGA decide\n"
            "Reply with choice number. Auto-selecting Option 1 in 10 minutes."
        )
        await TelegramService.send_message(prompt)
        logger.info("Pre-market session started. Waiting 10 minutes for user intent...")
        # In a real system, we'd listen for an async response.
        # Here we simulate the 10min wait or auto-fallback.
        await asyncio.sleep(600)
        logger.info(f"Session mode finalized: {self.selected_mode}")

    async def stop_new_entries(self):
        self.orchestrator.is_running = False
        logger.info("New trade entries disabled.")
