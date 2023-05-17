from abc import abstractmethod

from src.util.singleton_meta import SingletonMeta


class ServiceResponse:
    def __init__(self, data, message: str, code: int):
        self.data = data
        self.message = message
        self.code = code


class ServiceHandler(metaclass=SingletonMeta):

    @abstractmethod
    def handle_request(self, *args, **kwargs) -> ServiceResponse:
        pass
