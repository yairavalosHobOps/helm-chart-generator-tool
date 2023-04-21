# -*- coding: utf-8 -*-


from abc import abstractmethod
from typing import Protocol
from typing import runtime_checkable


@runtime_checkable
class BaseFileWriter(Protocol):
    """
    BaseFileWriter
    """

    @abstractmethod
    def write_file(self):
        """
        write_file
        @return: None
        @rtype: None
        """

        raise NotImplementedError(f"{self.__class__.__name__} Interface Missing Implementation")
