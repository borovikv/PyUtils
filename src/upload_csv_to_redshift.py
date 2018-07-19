import csv

from db_utils import execute_with_connection
from src.collection_utils import chunks
from src.db_utils import execute
from src.execution_utils import log


@log
def upload(file_csv, table, con_url, chunk_size):
    execute_with_connection(con_url, lambda curs: upload_csv(file_csv, table, chunk_size, curs))


def upload_csv(file_csv, table, chunk_size, curs):
    rows = read_csv(file_csv)
    for i, chunk in enumerate(chunks(rows, chunk_size)):
        print(f'chunk {i}')
        insert_rows(chunk, curs, table)


def read_csv(file_csv):
    with open(file_csv) as fin:
        return list(csv.DictReader(fin))


@log
def insert_rows(chunk, curs, table):
    sql = insert_sql(chunk, table)
    execute(sql, curs)
    curs.connection.commit()


def insert_sql(chunk, table):
    columns = chunk[0].keys()
    values = ', '.join(insert_values(row, columns) for row in chunk)
    columns = ', '.join(columns)
    return f'insert into {table} ({columns}) VALUES {values}'


def insert_values(row, columns):
    values = ', '.join(val(row, c) for c in columns)
    return f'({values})'


def val(row, column):
    value = escape(row[column])
    return f"'{value}'"


def escape(value):
    return value.replace("'", "''").replace('\\', '\\\\')
