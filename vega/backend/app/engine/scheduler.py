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
        self.intent_received = asyncio.Event()
        self.selected_mode = "equities"

    def start(self):
        # 08:45 IST — Startup
        self.scheduler.add_job(self.startup_check, CronTrigger(hour=8, minute=45))
        # 09:00 IST — Pre-market intent prompt
        self.scheduler.add_job(self.pre_market_session, CronTrigger(hour=9, minute=0))
        # 09:15 IST — Market open: begin scanning
        self.scheduler.add_job(self.orchestrator.start_scanning, CronTrigger(hour=9, minute=15))
        # 09:30 IST — ORB Strategy Activation
        self.scheduler.add_job(self.activate_orb, CronTrigger(hour=9, minute=30))
        # 11:00 IST — ORB Strategy Deactivation
        self.scheduler.add_job(self.deactivate_orb, CronTrigger(hour=11, minute=0))
        # 12:00 IST — Midday recalibration (Hurst exponent)
        self.scheduler.add_job(self.midday_recalibration, CronTrigger(hour=12, minute=0))
        # 15:00 IST — Stop entries
        self.scheduler.add_job(self.stop_new_entries, CronTrigger(hour=15, minute=0))
        # 15:15 IST — Square off
        self.scheduler.add_job(self.orchestrator.square_off_all, CronTrigger(hour=15, minute=15))
        # 15:20 IST — EOD Report
        self.scheduler.add_job(self.generate_eod_report, CronTrigger(hour=15, minute=20))

        self.scheduler.start()
        logger.info("Vega Scheduler fully configured with all daily jobs.")

    async def startup_check(self):
        logger.info("System startup. Connecting to broker...")
        self.orchestrator.broker.connect()

    async def pre_market_session(self):
        prompt = (
            "<b>Good morning. What would you like to trade today?</b>\n"
            "1. NSE Equities (default)\n"
            "2. Nifty / BankNifty Options (F&O)\n"
            "3. Futures\n"
            "4. Let VEGA decide\n"
            "Reply with choice number. Auto-selecting Option 1 in 10 minutes."
        )
        await TelegramService.send_message(prompt)
        logger.info("Pre-market session started. Waiting 10 minutes for user intent...")

        try:
            # Wait for intent_received event with 10-minute timeout
            await asyncio.wait_for(self.intent_received.wait(), timeout=600)
            logger.info(f"User intent received: {self.selected_mode}")
        except asyncio.TimeoutError:
            self.selected_mode = "equities"
            logger.info("No response received. Defaulting to NSE Equities.")

    def set_intent(self, mode: str):
        self.selected_mode = mode
        self.intent_received.set()

    async def activate_orb(self):
        logger.info("Activating ORB strategies.")
        # Logic to enable ORB in strategy engine

    async def deactivate_orb(self):
        logger.info("Deactivating ORB strategies.")

    async def midday_recalibration(self):
        logger.info("Running midday recalibration (Hurst exponent calculation).")
        # Logic to switch strategy sets based on Hurst

    async def stop_new_entries(self):
        self.orchestrator.is_running = False
        logger.info("New trade entries disabled.")

    async def generate_eod_report(self):
        logger.info("Generating EOD performance report.")
        await TelegramService.send_message("<b>EOD Report</b>\nTrading session completed.")
