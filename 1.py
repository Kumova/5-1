import logging


def my_logger(orig_func):
    logging.basicConfig(filename=f'{orig_func.__name__}.log', format='[%(asctime)s] [%(levelname)s] => %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.NOTSET)

    def wrapper(*args, **kwargs):
        logging.info(f'Числа : {args} и аргументы: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(a, b):
    print((a + b) / 10 * a)
    return display_info


display_info(1, -6)