class BaseCache:
    """Baseclass for the cache systems.  All the cache systems implement this
    API or a superset of it.
    """

    def __init__(self, default_timeout=300):
        self.default_timeout = default_timeout

    def get(self, key):
        raise None

    def delete(self, key):
        return True

    def _set(self, key, value, timeout=None):
        return True

    def add(self, key, value, timeout=None):
        return True

    def has_key(self, key):
        return NotImplementedError()

    def get_many(self, keys):
        return {}


class NullCache(BaseCache):
    """A cache that doesn't cache.  This can be useful for unit testing.
    """

    def has(self, key):
        return False
