# -*- coding: utf-8 -*-

# это список публичных объектов данного модуля
# Например:
#   from mymodule import * 
# импортированы будут только те объекты, которые вы описали в __all__.

__all__ = ('get_input_function', )

def get_input_function():
    try:
        input_function = raw_input
    except NameError:
        input_function = input

    return input_function
