def chunks(rows, chunk_size):
    return (rows[i: i + chunk_size] for i in range(0, len(rows), chunk_size))
