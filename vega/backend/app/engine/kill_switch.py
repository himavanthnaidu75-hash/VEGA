import os
import signal
import asyncio
from loguru import logger
from .orchestrator import TradingOrchestrator
from ..services.telegram_service import TelegramService

class KillSwitch:
    def __init__(self, orchestrator: TradingOrchestrator):
        self.orchestrator = orchestrator

    async def execute(self):
        logger.critical("!!! KILL SWITCH ACTIVATED !!!")

        # 1. Broadcast and Notify
        await TelegramService.send_kill_alert()

        # 2. Halt Scanning
        self.orchestrator.is_running = False

        # 3. Explicitly Cancel All Orders
        try:
            logger.info("Cancelling all open orders...")
            self.orchestrator.broker.cancel_all_orders()
        except Exception as e:
            logger.error(f"Error cancelling orders: {e}")

        # 4. Square off all positions
        try:
            logger.info("Squaring off all positions...")
            await self.orchestrator.square_off_all()
        except Exception as e:
            logger.error(f"Error during square off: {e}")

        # 5. Process Shutdown
        logger.critical("System shutdown sequence complete. Terminating process.")
        await asyncio.sleep(2)
        os.kill(os.getpid(), signal.SIGTERM)
