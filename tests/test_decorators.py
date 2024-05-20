from src.decorators import log


def test_log_console(capsys):
    @log()
    def example_function(x, y):
        return x + y

    result = example_function(5, 100)
    captured = capsys.readouterr()

    assert captured.out == "example_function ok\n"
    assert result == 105


def test_log_console_bad(capsys):
    @log()
    def my_function_not_file_with_error(x, y):
        return x / y

    my_function_not_file_with_error(3, 0)
    captured = capsys.readouterr()

    assert captured.out == "my_function_not_file_with_error error: division by zero. Inputs: (3, 0), {}\n"


def test_log_file_with_mistakes():
    @log(filename="mylog.txt")
    def my_error_function(x, y):
        return x / y

    with open("mylog.txt", "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "my_error_function error: division by zero. Inputs: (5, 0), {}\n"
