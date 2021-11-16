"""
from trades import Trades


def test_trades():
    trades = Trades("test_pair")

    # timestamp, price, size, direction
    # direction = 0 -> buy
    # direction = 1 -> sell

    test_trades = [
        [1633388771199, 321.3, 19.4, 1],
        [1633388772299, 343.4, 24.0, 1],
        [1633388773399, 500.1, 44.2, 1],
        [1633388773545, 495.1, 1.2, 0],
        [1633388791209, 421.1, 90.9, 0],
        [1633388800000, 386.0, 55.5, 0],
    ]

    for n, t in enumerate(test_trades):
        trades.add(*t)
        trades.len == n + 1
"""
