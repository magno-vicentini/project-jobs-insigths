from src.counter import count_ocurrences


def test_counter():
    number_of_py_string = count_ocurrences('src/jobs.csv', 'python')
    assert number_of_py_string == 1639

    number_of_js_string = count_ocurrences('src/jobs.csv', 'javascript')

    assert number_of_js_string == 122
