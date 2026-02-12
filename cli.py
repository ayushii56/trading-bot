import argparse
import logging

from bot.logging_config import setup_logging
from bot.validators import validate_order_inputs, ValidationError
from bot.orders import OrderService


def confirm_order(order_data):
    print("\n=== ORDER PREVIEW ===")

    for k, v in order_data.items():
        if v is not None:
            print(f"{k}: {v}")

    while True:
        confirm = input("\nConfirm order? (y/n): ").strip().lower()

        if confirm in ("y", "yes"):
            return True
        elif confirm in ("n", "no"):
            return False

        print("Please enter y or n.")


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")
    parser.add_argument("--stop-price")

    args = parser.parse_args()

    try:
        order_data = validate_order_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
            args.stop_price,
        )

        # ⭐ Interactive confirmation
        if not confirm_order(order_data):
            print("\n❌ Order cancelled by user.")
            return

        service = OrderService()
        result = service.place_order(order_data)

        print("\n=== ORDER RESPONSE ===")
        for k, v in result.items():
            print(f"{k}: {v}")

        print("\n✅ Order completed successfully")

    except ValidationError as e:
        logger.error(str(e))
        print(f"\n❌ Validation error: {e}")

    except Exception:
        logger.exception("Unexpected failure")
        print("\n❌ Order failed — check logs")


# ⭐ REQUIRED execution trigger
if __name__ == "__main__":
    main()
