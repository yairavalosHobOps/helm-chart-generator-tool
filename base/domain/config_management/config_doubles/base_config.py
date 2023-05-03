# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseConfig(Protocol):
    """
    BaseConfig
    """

    @abstractmethod
    def read(self):
        """
        read
        @return: config_data
        @rtype: dict
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")

    @abstractmethod
    def read_file(self):
        """
        read_file
        @return: config_data
        @rtype: dict
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
