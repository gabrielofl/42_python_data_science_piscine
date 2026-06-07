def ft_filter(function, iterable):
    """ft_filter(function or None, iterable)
        Return a list with items of iterable for which function(item)
        is true. If function is None, return the items that are true.
        Implementation of filter function."""
    if function is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]
