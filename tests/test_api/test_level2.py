from time import time

from pylob import Level2


def test_init():
    lob = Level2("empty")

    assert lob.name == "empty"
    assert lob.asks == []
    assert lob.bids == []


def test_init_with_snapshot():
    lob = Level2(
        "list_of_tuples",
        bids=[(10, 20), (8, 50), (7, 1)],
        asks=[(11, 5), (15, 9)]
    )

    assert lob.name == "list_of_tuples"
    assert lob.asks == [(11, 5), (15, 9)]
    assert lob.bids == [(10, 20), (8, 50), (7, 1)]


def test_snapshot_after_init():
    lob = Level2("snapshot_after_init")

    lob.set_snapshot(
        bids=[(10, 20), (8, 50), (7, 1)],
        asks=[(11, 5), (15, 9)]
    )

    assert lob.name == "snapshot_after_init"
    assert lob.asks == [(11, 5), (15, 9)]
    assert lob.bids == [(10, 20), (8, 50), (7, 1)]


def test_basic_order_book():
    o = Level2("basic")

    assert len(o._asks) == 0
    assert len(o._bids) == 0
    assert o.get_asks() == []
    assert o.get_bids() == []
    assert o.last_time == 0
    assert o.ask_vol_at(100) == 0
    assert o.bid_vol_at(100) == 0
    assert o.best_ask == ()
    assert o.best_bid == ()
    assert o.snapshot == {"asks": [], "bids": []}
    assert o.frame(1) == {"asks": [(0, 0)], "bids": [(0, 0)]}
    assert o.frame(5) == {
        "asks": [
            (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
        ],
        "bids": [
            (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
        ]
    }
    assert o.frame(10) == {"asks": [
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),

    ], "bids": [
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]}

    snapshot = {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
            (40, 60),
        ],
        "timestamp":
            9059205645767
    }
    o.set_snapshot(
        snapshot["bids"],
        snapshot["asks"],
        snapshot["timestamp"],
    )

    assert len(o._asks) == 3
    assert len(o._bids) == 4
    assert o.get_asks() == [
        (100, 20),
        (120, 30),
        (150, 40),
    ]
    assert o.get_bids() == [
        (90, 60),
        (80, 16),
        (60, 20),
        (40, 60),
    ]
    assert o.last_time == 9059205645767
    assert o.ask_vol_at(120) == 30
    assert o.bid_vol_at(60) == 20
    assert o.best_ask == (100, 20)
    assert o.best_bid == (90, 60)
    assert o.snapshot == {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
            (40, 60),
        ],
    }
    assert o.frame(1) == {
        "asks": [(100, 20)],
        "bids": [(90, 60)]
    }
    assert o.frame(5) == {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
            (0, 0),
            (0, 0),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
            (40, 60),
            (0, 0),
        ]
    }
    assert o.frame(10) == {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
            (40, 60),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
            (0, 0),
        ]
    }


def test_update_empty_lob():
    o = Level2("empty_lob")

    assert len(o._asks) == 0
    assert len(o._bids) == 0
    assert o.last_time == 0

    now = time()

    o.update("ask", 10.1, 3.1, now)

    assert len(o._asks) == 1
    assert o.best_ask == (10.1, 3.1)
    assert o.timestamp == now
    assert o.frame(3) == {
        "asks": [
            (10.1, 3.1),
            (0, 0),
            (0, 0),

        ],
        "bids": [
            (0, 0),
            (0, 0),
            (0, 0),
        ]
    }

    o.update("bid", 9.95, 100, now + 100)
    assert len(o._bids) == 1
    assert o.best_bid == (9.95, 100.0)
    assert o.timestamp == now + 100
    assert o.frame(3) == {
        "asks": [
            (10.1, 3.1),
            (0, 0),
            (0, 0),

        ],
        "bids": [
            (9.95, 100.0),
            (0, 0),
            (0, 0),
        ]
    }


def test_update_non_empty_lob():
    o = Level2("non_empty_lob")

    snapshot = {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
            (40, 60),
        ],
        "timestamp":
            9059205645767
    }
    o.set_snapshot(
        snapshot["bids"],
        snapshot["asks"],
        snapshot["timestamp"],
    )

    assert len(o._asks) == 3
    assert len(o._bids) == 4
    assert o.last_time == 9059205645767
    assert o.frame(3) == {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
        ]
    }

    now = time()
    o.update("ask", 110, 20, now + 100)
    o.update("bid", 90, 100, now + 100)
    assert o.best_ask == (100, 20)
    assert o.best_bid == (90, 100)
    assert o.timestamp == now + 100
    assert o.frame(3) == {
        "asks": [
            (100, 20),
            (110, 20),
            (120, 30),
        ],
        "bids": [
            (90, 100),
            (80, 16),
            (60, 20),
        ]
    }


def test_update_with_zero_size():
    o = Level2("lob")

    snapshot = {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
            (40, 60),
        ],
        "timestamp":
            9059205645767
    }
    o.set_snapshot(
        snapshot["bids"],
        snapshot["asks"],
        snapshot["timestamp"],
    )

    assert len(o._asks) == 3
    assert len(o._bids) == 4
    assert o.last_time == 9059205645767
    assert o.frame(3) == {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
        ]
    }

    now = time()
    o.update("ask", 100, 0, now)
    assert o.last_time == now
    assert o.best_ask == (120, 30)
    assert o.best_bid == (90, 60)
    assert o.frame(3) == {
        "asks": [
            (120, 30),
            (150, 40),
            (0, 0),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
        ]
    }

    now = time()
    o.update("bid", 80, 0, now)
    assert o.last_time == now
    assert o.best_ask == (120, 30)
    assert o.best_bid == (90, 60)
    assert o.frame(3) == {
        "asks": [
            (120, 30),
            (150, 40),
            (0, 0),
        ],
        "bids": [
            (90, 60),
            (60, 20),
            (40, 60),
        ]
    }


def test_delete_level():
    o = Level2("lob")

    snapshot = {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
            (40, 60),
        ],
        "timestamp":
            9059205645767
    }
    o.set_snapshot(
        snapshot["bids"],
        snapshot["asks"],
        snapshot["timestamp"],
    )

    assert len(o._asks) == 3
    assert len(o._bids) == 4
    assert o.last_time == 9059205645767
    assert o.frame(3) == {
        "asks": [
            (100, 20),
            (120, 30),
            (150, 40),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
        ]
    }

    now = time()
    o.delete_level("ask", 100, now)
    assert o.last_time == now
    assert o.best_ask == (120, 30)
    assert o.best_bid == (90, 60)
    assert o.frame(3) == {
        "asks": [
            (120, 30),
            (150, 40),
            (0, 0),
        ],
        "bids": [
            (90, 60),
            (80, 16),
            (60, 20),
        ]
    }

    now = time()
    o.delete_level("bid", 80, now)
    assert o.last_time == now
    assert o.best_ask == (120, 30)
    assert o.best_bid == (90, 60)
    assert o.frame(3) == {
        "asks": [
            (120, 30),
            (150, 40),
            (0, 0),
        ],
        "bids": [
            (90, 60),
            (60, 20),
            (40, 60),
        ]
    }
