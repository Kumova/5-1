import logging
import os

path = os.path.basename('display_info.log')


def log(func):
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler("%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.info("Вызов функции: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Результат: %s" %result)
        return func
    return wrap_log

def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwargs):
            result = foo(*args, **kwargs)
            with open(parameter, 'w') as f:
                f.write(str(result))
            return result
            foo()
            result = foo(new_foo)
            return result

        return new_foo
    return decor


@parametrized_decor(parameter=path)
@log
def foo(a):
    return a * 2

if __name__ == "__main__":
    value = foo(10)

