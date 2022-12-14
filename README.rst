========
cachelib
========


.. image:: https://img.shields.io/pypi/v/cachelib.svg
        :target: https://pypi.python.org/pypi/cachelib

.. image:: https://img.shields.io/travis/yusufadell/cachelib.svg
        :target: https://travis-ci.com/yusufadell/cachelib

.. image:: https://readthedocs.org/projects/cachelib/badge/?version=latest
        :target: https://cachelib.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A collection of cache libraries in the same API interface.


* Free software: Apache Software License 2.0
* Documentation: https://cachelib.readthedocs.io.


Features
--------

- ✅ **BaseCache**  - Base class for all cache implementations
- ✅ **NullCache** - A cache that does nothing
- **SimpleCache** - A simple in-memory cache
- **FileSystemCache** - A cache that stores data on the filesystem
- **MemcachedCache** - A cache that stores data in memcached
- **RedisCache** - A cache that stores data in redis
- **UWSGICache** - A cache that stores data in uwsgi

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
