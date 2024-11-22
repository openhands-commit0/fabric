from decorator import decorator

@decorator
def opens(f, self, *args, **kwargs):
    """
    Decorator that ensures a connection is opened before calling the function.
    """
    if not self.is_connected:
        self.open()
    return f(self, *args, **kwargs)