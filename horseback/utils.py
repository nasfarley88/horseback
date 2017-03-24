class ServiceNotFound(Exception):
    """Raised when a horseback service is not found."""


class ServicesDict(dict):
    """Dictionary of services.

    Only differs by raising a ServiceNotFound error instead of KeyError if key
    is not found.

    """

    def __getitem__(self, key: str):
        try:
            return super().__getitem__(key)
        except KeyError:
            raise ServiceNotFound("Service '{}' not found.".format(key))
