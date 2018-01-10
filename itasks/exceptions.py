
""" Custom Exceptions """


class CouldNotReadStdIOException(Exception):
    """
    Failed to read data from the StdIO
    """
    pass


class UnsupportedOperatingSystemException(Exception):
    """
    The operating system is not supported
    """
    pass
