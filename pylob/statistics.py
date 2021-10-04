class Statistics:

    @property
    def abs_spread(self):
        return self.best_ask[0] - self.best_bid[0]
