import datetime
from pathlib import Path


def log_with_path(path):
    def log_execution(old_function):
        file_name = f'{str(datetime.date.today()).replace(" ", "_")}' \
                    f'_logs.txt'
        work_path = Path(path)
        work_path.mkdir(parents=True, exist_ok=True)
        file_to_open = work_path / file_name

        def new_function(*args, **kwargs):
            source_fun = old_function(*args, **kwargs)
            time_string = datetime.datetime.today().strftime(
                "%b %d %Y %H:%M:%S")
            res_str = f'{time_string}: {old_function.__name__}; ' \
                      f'args = {args}, kwargs = {kwargs}. ' \
                      f'Output: {old_function(*args, **kwargs)}'
            with open(file_to_open, 'at',
                      encoding='utf-8') as log_file:
                log_file.write(f'{res_str}\n')
            return source_fun

        return new_function

    return log_execution


@log_with_path('logs/my_print_logs')
def my_print(string):
    print(string)


@log_with_path('logs/my_sum_logs')
def my_sum(a, b):
    return a + b


if __name__ == '__main__':
    my_print('This is the test of decorated function')

    my_sum(4, 3)
