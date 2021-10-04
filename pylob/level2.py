from pylob.statistics import Statistics
from pylob.output import L2Output


class Level2(Statistics, L2Output):
    def __init__(self, name, *, bids=[], asks=[]) -> None:
        self.name = name
        self._bids = {}
        self._asks = {}
        self.best_bid = ()
        self.best_ask = ()
        self.tick_size = 1

        self.set_snapshot(bids, asks)

    def set_tick_size(self, tick_size) -> None:
        self.tick_size = tick_size

    def set_snapshot(self, bids, asks) -> None:
        for b in bids:
            price, size = b
            self._bids[price] = size
        for a in asks:
            price, size = a
            self._asks[price] = size

        if len(self._bids) > 0:
            best_bid_price = max(list(self._bids.keys()))
            self.best_bid = (best_bid_price, self._bids[best_bid_price])
        if len(self._asks) > 0:
            best_ask_price = min(list(self._asks.keys()))
            self.best_ask = (best_ask_price, self._asks[best_ask_price])
