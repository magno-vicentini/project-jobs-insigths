from src.counter import count_ocurrences


def test_counter():
    number_of_python_string = count_ocurrences('src/jobs.csv', 'python')
    
    assert number_of_python_string == 1639

    number_of_javascript_string = count_ocurrences('src/jobs.csv', 'javascript')

    assert number_of_javascript_string == 122
