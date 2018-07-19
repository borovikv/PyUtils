import collection_utils as u


def test_chunk():
    collection = list(range(10))
    result = u.chunks(collection, 3)
    assert [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]] == list(result)
