from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # length Zufalls-Bytes erzeugen
    tb: bytes = token_bytes(length)
    # Diese Bytes in einem Bit-String konvertieren und zurückgeben
    return int.from_byte(tb, "big")