import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def errorPage(blockTitle, errorMessage, imageSource):
    return render_template("error.html", title = (blockTitle), info = (errorMessage), file = (imageSource))


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

os.environ["API_KEY"] = "he9x6f8hGn86YmAeL910C5z33XyHMVb7MlUSTzzm"
 
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")
 
def lookup(symbol):
    try:
        # api_key = os.environ.get("API_KEY")
        symbol_encoded = urllib.parse.quote_plus(symbol)
        url = f"https://api.stockdata.org/v1/data/quote?symbols={symbol_encoded}&api_token=he9x6f8hGn86YmAeL91QC5z33XyHMVb7MlUSTzzm"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
 
    try:
        data = response.json()
        quote = data["data"][0]
        return {
            "name": quote["name"],
            "symbol": quote["ticker"],
            "price": float(quote["price"]),
            "day_high": float(quote["day_high"]),
            "day_low": float(quote["day_low"]),
            "day_open": float(quote["day_open"]),
            "previous_close_price": float(quote["previous_close_price"]),
            "day_change": float(quote["day_change"]),
            "volume": quote["volume"],
            "currency": quote["currency"],
            "last_trade_time": quote["last_trade_time"]
        }
        # return 
    except (KeyError, TypeError, ValueError, IndexError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
