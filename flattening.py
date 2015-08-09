def flattenF(arr, result):    
    """ Flattens an arbitrary nested array returning it in result.
    Assumes that an array is passed in arr var (no validation performed)
    """
    for a in arr:
        if isinstance(a, list):
            flattenF(a, result)
        else:
            result.append(a)
            
def flatten(arr):
    """ Wrapper for calling flattenF and also a doctest envelope.
    >>> flatten([1,2,3])
    [1, 2, 3]
    >>> flatten([1,2,3,[4,5,[6,7]]])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten([1])
    [1]
    >>> flatten([])
    []
    >>> flatten([[1,2,[3]],4])
    [1, 2, 3, 4]
    """
    result = []
    flattenF(arr, result)
    return result
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()
