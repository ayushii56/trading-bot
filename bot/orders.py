import logging

from bot.client import BinanceFuturesClient
from bot.validators import ValidationError


logger = logging.getLogger(__name__)


class OrderService:
    """
    Handles order construction and execution logic.
    """

    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(self, order_data: dict):
        try:
            logger.info(f"Preparing order: {order_data}")

            payload = {
                "symbol": order_data["symbol"],
                "side": order_data["side"],
                "quantity": order_data["quantity"],
            }

            order_type = order_data["type"]

            # MARKET order
            if order_type == "MARKET":
                payload["type"] = "MARKET"

            # LIMIT order
            elif order_type == "LIMIT":
                payload.update({
                    "type": "LIMIT",
                    "price": order_data["price"],
                    "timeInForce": "GTC",
                })

            # STOP-LIMIT order
            elif order_type == "STOP_LIMIT":
                payload.update({
                    "type": "STOP",
                    "price": order_data["price"],
                    "stopPrice": order_data["stopPrice"],
                    "timeInForce": "GTC",
                })

            response = self.client.place_order(**payload)

            formatted = self._format_response(response)

            logger.info("Order executed successfully")

            return formatted

        except ValidationError as e:
            logger.error(f"Validation failed: {e}")
            raise

        except Exception:
            logger.exception("Order execution failed")
            raise
        
    def _format_response(self, response):

# Format Binance response for both regular and conditional orders.

    # Conditional (STOP_LIMIT) order response
      if "algoId" in response:
        return {
            "orderType": "STOP_LIMIT",
            "algoId": response.get("algoId"),
            "status": response.get("algoStatus"),
            "triggerPrice": response.get("triggerPrice"),
            "price": response.get("price"),
            "symbol": response.get("symbol"),
        }
      return {
        "orderType": "STANDARD",
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice": response.get("avgPrice"),
        "symbol": response.get("symbol"),
    }

