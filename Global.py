_database = None

_internet_connection: bool = False

_text_error: str = ''


def text_error(): return _text_error


def internet() -> bool: return _internet_connection
