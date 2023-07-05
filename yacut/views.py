import random
import string

from ..settings import ID_LENGTH


def get_unique_short_id():
    char_set = string.ascii_lowercase + string.ascii_lowercase + string.digits
    short_id = ''.join(random.choices(char_set, k=ID_LENGTH))
    return short_id
