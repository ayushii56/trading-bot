from flask import Flask, render_template, request
from bot.orders import OrderService
from bot.validators import validate_order_inputs, ValidationError

app = Flask(__name__)
service = OrderService()


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            data = validate_order_inputs(
                request.form["symbol"],
                request.form["side"],
                request.form["type"],
                request.form["quantity"],
                request.form.get("price"),
                request.form.get("stop-price"),
            )

            result = service.place_order(data)

        except ValidationError as e:
            error = str(e)
        except Exception as e:
            error = str(e)


    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
