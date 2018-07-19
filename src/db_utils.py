from urllib.parse import urlparse

import psycopg2
from psycopg2.extras import RealDictConnection


def connection(con_url):
    result = urlparse(con_url)
    return psycopg2.connect(
        host=result.hostname,
        port=result.port,
        dbname=result.path[1:],
        user=result.username,
        password=result.password,
        connection_factory=RealDictConnection
    )


def execute(sql, curs):
    curs.execute(sql)
    return {} if not curs.description else curs.fetchall()
