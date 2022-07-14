import logging


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]


def my_logger(orig_func):
    logging.basicConfig(filename=f'{orig_func.__name__}.log', format='[%(asctime)s] [%(levelname)s] => %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.NOTSET)

    def wrapper(*args, **kwargs):
        logging.info(f'Числа : {args} и аргументы: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def gen(*args, **kwargs):
	for i in (i for lst in nested_list for i in lst):
		yield i

gen(9,0,0,9,9,8, 'yes',1, 3, 4, 5, 6.6,6, 8)
gen(9,0,0,9,9,8,1, 3, 4, 5, 6.6,6, 8)
gen(9,0,0, 8)
gen(9,0,0,9,9,8, 'yes',1, 3, 4, 5, 6.6,6, 8)
gen(9,0,0,98)
print(my_logger(gen))

for item in gen():
	print(item)

