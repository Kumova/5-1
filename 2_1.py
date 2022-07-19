import os

path=os.path.basename('display_info.log')

def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwargs):
            2*parameter(*args, **kwargs)
            return foo(*args, **kwargs)
            foo()
            result = foo(new_foo)
            return result

        return new_foo

    return decor


@parametrized_decor(parameter=path)
def foo():
    pass

