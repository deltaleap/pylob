# test api in common between Level2 and Level3
from pylob import Level2


def test_level2_repr(capsys):
    book = Level2('test')
    print(book)
    captured = capsys.readouterr()
    assert captured.out == "L2[test]\n"
