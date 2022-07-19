import logging
import os

path=os.path.basename('display_info.log')
#def my_logger(orig_func):
#    logging.basicConfig(path=os.path.basename(display_info.log),
 #                       format='[%(asctime)s] [%(levelname)s] => %(message)s',
 #                       datefmt='%Y-%m-%d %H:%M:%S',
 #                       level=logging.NOTSET)

 #   def wrapper(*args, **kwargs):
 #       logging.info(f'Числа : {args} и аргументы: {kwargs}')
 #       return orig_func(*args, **kwargs)

#   return wrapper


@my_logger
def display_info(a, b):
    print((a + b) / 10 * a)
    return display_info

display_info(1, -6)


def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwars):
            # здесь код до вызовы функции
            result = foo(*args, **kwars)
            # здесь код после вызовы функции
            return result

        return new_foo

    return decor


@parametrized_decor(parameter=path)
def foo():
    pass
