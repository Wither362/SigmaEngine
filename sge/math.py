'''
	Extra math module for doing extra mathematical thingies.
'''

from math import trunc

def truncate(num, decimals):
    '''
		Truncates `num` with the number of `decimals` specified.
    '''
    m = 10 ** decimals
    return trunc(num * m) / m
