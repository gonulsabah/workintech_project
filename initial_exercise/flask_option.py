# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    env = os.getenv(key = 'FLASK_ENV', default="empty")
    return f"ENV {env}"


if __name__ == "__main__":
    print(start())