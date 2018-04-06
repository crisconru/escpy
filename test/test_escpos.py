from src import escpos

esc = escpos.ESCPOS()
# ESC @ (ASCII)   | 1B 40 (HEX)   | 27 40 (DEC)
initialization = b'\x1b@'
# ESC d n (ASCII) | 1B 64 n (HEX) | 27 100 n (DEC) -> n is an int 0-255 (n=3)
three_feed_lines = b'\x1bd\x03'


def test_ascii_initialization():
    # ESC @
    assert esc.ascii_command('ESC', '@') == initialization


def test_ascii_three_feed_lines():
    # ESC d 3
    assert esc.ascii_command('ESC', 'd', 3) == three_feed_lines


def test_hex_initialization():
    # 1B 40
    assert esc.hex_command('1B', '40') == initialization


def test_hex_three_feed_lines():
    # 1B 64 n
    assert esc.hex_command('1B', '64', '03') == three_feed_lines


def test_dec_initialization():
    # 27 64
    assert esc.dec_command(27, 64) == initialization


def test_dec_three_feed_lines():
    # 27 100 3
    assert esc.dec_command(27, 100, 3) == three_feed_lines


def test_string():
    # Lorem ipsum
    e = 'Lorem ipsum'.encode('utf-8')
    assert esc.string_to_escpos('Lorem ipsum') == e
