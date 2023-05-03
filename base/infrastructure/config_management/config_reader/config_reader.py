# -*- coding: utf-8 -*-


import configparser


# Infrastructure
from base.infrastructure.file_management.file_handler import FileHandler


# Domain
from base.domain.config_management.config_doubles import BaseConfig
from base.domain.config_management.config_reader import BaseConfigReader
from base.domain.file_management.file_constants.file_mode_values import file_mode_values
from base.domain.file_management.file_handler import BaseFileHandler
from base.domain.path_management.path_doubles import BasePath


class ConfigReader(BaseConfigReader):
    """
    ConfigReader
    """

    def __init__(self, path_obj: BasePath, file_handler: BaseFileHandler = None, config_obj: BaseConfig = None):
        """
        ConfigReader constructor
        @param path_obj: path_obj
        @type path_obj: BasePath
        @param file_handler: file_handler
        @type file_handler: BaseFileHandler
        @param config_obj: config_obj
        @type config_obj: config_obj
        """

        if not isinstance(path_obj, BasePath):
            raise ValueError(f"Error path_obj: {path_obj} is not an instance of {BasePath}")

        if not isinstance(file_handler, BaseFileHandler):
            raise ValueError(f"Error file_handler: {file_handler} is not an instance of {BaseFileHandler}")

        if not isinstance(config_obj, BaseConfig):
            raise ValueError(f"Error config_obj: {config_obj} is not an instance of {BaseConfig}")

        if not path_obj.exists():
            raise ValueError(f"Error path_obj: {path_obj} doesn't exists in the file system")

        if not path_obj.is_file():
            raise ValueError(f"Error path_obj: {path_obj} is not a file path")

        self.__stored_path = path_obj
        self.__file_handler = file_handler or FileHandler(file_mode=file_mode_values.read, path_obj=path_obj)
        self.__config_parser = config_obj or configparser.RawConfigParser()

    def read_config_file(self):
        """
        read_config_file
        @return: config_data
        @rtype: dict
        """

        with self.__file_handler as file_handler:
            self.__config_parser.read_file(file_handler)

        return self.__config_parser


