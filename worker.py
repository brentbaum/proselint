"""Heroku web worker."""

from builtins import map

import os
import redis
from rq import Worker, Queue, Connection
import proselint

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

def worker_function(text):
    """Lint the text using a worker dyno."""
    return proselint.tools.lint(text)


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
