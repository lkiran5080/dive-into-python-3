SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    """Convert a file size to human-readable form.

    Args:
        size (int): file size in bytes
        a_kilobyte_is_1024_bytes (bool, optional): if True, use multiples of 1024
                                                   if False, use multiples of 1000
                                                    Defaults to True.
    Returns:
    string
    """
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    # if execution comes out of the above loop
    raise ValueError('number too large')


if __name__ == '__main__':
    print(approximate_size(10000000000))
    print(approximate_size(10000000000, False))
    print(approximate_size(100000000000000))
    print(approximate_size(100000000000000, False))
    # print(approximate_size(1000000000000000000000000000000000000, False)) #Value too large
