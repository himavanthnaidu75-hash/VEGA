import PyPDF2
import os

class SkillService:
    @staticmethod
    def learn_from_pdf(file_path):
        """Extract strategy logic from PDF."""
        text = ""
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text()
            # Simple keyword extraction for now
            # In a real scenario, this would use a local LLM to parse rules
            strategies = []
            if "FVG" in text: strategies.append("Fair Value Gap")
            if "Liquidity" in text: strategies.append("Liquidity Sweeps")
            return {"status": "success", "strategies_found": strategies}
        except Exception as e:
            return {"status": "error", "message": str(e)}

class ObsidianIntegration:
    def __init__(self, api_key, base_url="http://localhost:27123"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def log_trade(self, trade_data):
        """Journal trade to Obsidian vault."""
        date_str = trade_data.get('date', 'today')
        url = f"{self.base_url}/vault/Trading_Journal/VEGA_{date_str}.md"
        content = f"# VEGA Trade Log\n\n- Symbol: {trade_data['symbol']}\n- Side: {trade_data['side']}\n- P&L: {trade_data['pnl']}\n"
        try:
            import requests
            requests.put(url, data=content, headers=self.headers)
            return True
        except:
            return False
