from pylob import Level2


def test_init():
    lob = Level2("empty")

    assert lob.name == "empty"
    assert lob.asks == []
    assert lob.bids == []


def test_init_with_snapshot():
    lob = Level2("list_of_tuples",
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
