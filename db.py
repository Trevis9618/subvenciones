import os
import psycopg
from contextlib import contextmanager

DATABASE_URL = os.environ["DATABASE_URL"]

@contextmanager
def get_conn():
    """Context manager to obtain a Postgres connection."""
    with psycopg.connect(DATABASE_URL) as conn:
        yield conn
