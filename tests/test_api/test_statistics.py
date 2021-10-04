import pytest

from pylob import Level2

""" require pytest-cases
@pytest.fixture
def thin_level2():
    # Thin level 2 limit order book.
    # Thin book definition: book with absolute bid ask spread less or equal
    # the tick size
    lob = Level2("thin")
    lob.set_tick_size(.1)
    lob.set_snapshot(
        asks=[(100.1, 50), (100.9, 120), (101.2, 150)],
        bids=[(99.9, 35), (99.5, 20), (99.4, 360)]
    )
    return lob


@pytest.fixture
def tick_wide_level2():
    # Tick-wide level 2 limit order book.
    # Tick-wide book definition: book with absolute bid ask spread exactly
    # equal to 2x the tick size
    lob = Level2("tick")
    lob.set_tick_size(.1)
    lob.set_snapshot(
        asks=[(100.0, 50), (100.9, 120), (101.2, 150)],
        bids=[(99.9, 35), (99.5, 20), (99.4, 360)]
    )
    return lob


@pytest.fixture
def thick_level2():
    # Very thick level 2 limit order book.
    # Very thick book definition: book with absolute bid ask spread greater than
    # 2x the thick size
    lob = Level2("thick")
    lob.set_tick_size(.1)
    lob.set_snapshot(
        asks=[(100.5, 50), (100.9, 120), (101.2, 150)],
        bids=[(99.8, 35), (99.5, 20), (99.4, 360)]
    )
    return lob


@pytest.mark.parametrize(
    "lob, expected_spread",
    [
        (thin_level2, abs(100.1 - 99.9)),
        (tick_wide_level2, abs(100.0 - 99.9)),
        (thick_level2, abs(99.8 - 100.5)),
    ]
)
def test_abs_spread(lob, expected_spread):
    print(lob)
    print(dir(lob))
    assert lob.abs_spread == expected_spread
"""

def test_thin_level2():
    """Thin level 2 limit order book.
    Thin book definition: book with absolute bid ask spread less or equal
    the tick size
    """
    lob = Level2("thin")
    lob.set_tick_size(.1)
    lob.set_snapshot(
        asks=[(100.1, 50), (100.9, 120), (101.2, 150)],
        bids=[(99.9, 35), (99.5, 20), (99.4, 360)]
    )
    assert lob.abs_spread == abs(100.1 - 99.9)


def test_tick_wide_level2():
    """Tick-wide level 2 limit order book.
    Tick-wide book definition: book with absolute bid ask spread exactly
    equal to 2x the tick size
    """
    lob = Level2("tick")
    lob.set_tick_size(.1)
    lob.set_snapshot(
        asks=[(100.0, 50), (100.9, 120), (101.2, 150)],
        bids=[(99.9, 35), (99.5, 20), (99.4, 360)]
    )
    assert lob.abs_spread == abs(100.0 - 99.9)


def test_thick_level2():
    """Very thick level 2 limit order book.
    Very thick book definition: book with absolute bid ask spread greater than
    2x the thick size
    """
    lob = Level2("thick")
    lob.set_tick_size(.1)
    lob.set_snapshot(
        asks=[(100.5, 50), (100.9, 120), (101.2, 150)],
        bids=[(99.8, 35), (99.5, 20), (99.4, 360)]
    )
    assert lob.abs_spread == abs(99.8 - 100.5)
