class BaseCache:
    """Baseclass for the cache systems.  All the cache systems implement this
    API or a superset of it.
    """

    def __init__(self, default_timeout=300):
        self.default_timeout = default_timeout

    def _normalize_timeout(self, timeout):
        if timeout is None:
            timeout = self.default_timeout
        return timeout

    def get(self, key):
        raise None

    def get_many(self, keys):
        return [self.get(k) for k in keys]

    def get_dict(self, *keys):
        return dict(zip(keys, self.get_many(*keys)))

    def delete(self, key):
        return True

    def delete_many(self, *keys: str):

        deleted_keys = []
        for key in keys:
            if self.delete(key):
                deleted_keys.append(key)
        return deleted_keys

    def set(self, key, value, timeout=None):
        return True

    def set_many(self, mapping, timeout=None):

        set_keys = []
        for key, value in mapping.items():
            if self.set(key, value, timeout):
                set_keys.append(key)
        return set_keys

    def add(self, key, value, timeout=None):
        return True

    def has(self, key):
        raise NotImplementedError(
            "%s doesn't have an efficient implementation of `has`. That "
            "means it is impossible to check whether a key exists without "
            "fully loading the key's data. Consider using `self.get` "
            "explicitly if you don't care about performance.")

    def clear(self) -> bool:
        return True

    def inc(self, key=0, delta=1):

        value = key + delta
        return value if self.set(key, value) else None

    def dec(self, key=0, delta=1):

        value = key - delta
        return value if self.set(key, value) else None


class NullCache(BaseCache):
    """A cache that doesn't cache.  This can be useful for unit testing.
    """

    def has(self, key):
        return False
