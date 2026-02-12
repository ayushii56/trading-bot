import logging
import os

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv


logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


class BinanceFuturesClient:
    """
    Wrapper for Binance Futures Testnet API.
    Handles connection, order placement, and error logging.
    """

    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("Missing Binance API credentials in .env")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Connected to Binance Futures Testnet")

    def place_order(self, **order_params):
        """
        Send order to Binance Futures API.
        """

        try:
            logger.info(f"Sending order request: {order_params}")

            response = self.client.futures_create_order(**order_params)

            logger.info(f"Order response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Request/network error: {str(e)}")
            raise

        except Exception as e:
            logger.exception("Unexpected error placing order")
            raise
