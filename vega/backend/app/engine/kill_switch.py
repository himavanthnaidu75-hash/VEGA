import os
import signal
import asyncio
from loguru import logger
from .orchestrator import TradingOrchestrator

class KillSwitch:
    def __init__(self, orchestrator: TradingOrchestrator):
        self.orchestrator = orchestrator

    async def execute(self):
        logger.critical("!!! KILL SWITCH ACTIVATED !!!")

        # 1. Set System Status
        self.orchestrator.is_running = False

        # 2. Square off all positions
        try:
            await self.orchestrator.square_off_all()
        except Exception as e:
            logger.error(f"Error during square off: {e}")

        # 3. Cancel all pending orders
        # (Already handled within square_off_all usually, but can be explicit)

        # 4. Log final P&L
        logger.info("Final system shutdown sequence initiated.")

        # 5. Process Shutdown
        # We use a small delay to allow logs to be written
        await asyncio.sleep(2)
        os.kill(os.getpid(), signal.SIGTERM)

def setup_terminal_shortcut(kill_switch: KillSwitch):
    # This would typically be in a separate thread listening for keystrokes
    pass
