from app import add



def test_add_success():

    assert add(2, 3) == 5


def test_subtract_success():

    from app import subtract

    assert subtract(5, 1) == 3