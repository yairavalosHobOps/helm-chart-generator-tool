# -*- coding: utf-8 -*-


# Infrastructure
from base.infrastructure.file_management.file_handler import FakeFile
from base.infrastructure.path_management.path_validator import PathFormatValidator

# Domain
from base.domain.file_management.file_constants import file_type_values
from base.domain.path_management.path_constants import path_types_values
from base.domain.path_management.path_handler import BasePath


class FakePath(BasePath):
    """
    FakePath
    """

    def __init__(self, target_path: str = None, target_path_type: str = None, fake_file: FakeFile = None):
        """
        FakePath
        """

        if not isinstance(target_path, (str, type(None))):
            raise ValueError(f"Error target_path: {target_path} is not str type")

        if not isinstance(target_path_type, (str, type(None))):
            raise ValueError(f"Error target_path_type: {target_path_type} is not str type")

        if not isinstance(fake_file, (FakeFile, type(None))):
            raise ValueError(f"Error fake_file: {fake_file} is not str type")

        valid_target_path = "/"

        if target_path is not None:
            valid_target_path = PathFormatValidator.validate_path_format(target_path=target_path)

        self.__fake_stored_path = dict()
        self.__fake_target_path = valid_target_path
        self.__fake_target_path_type = target_path_type or path_types_values.directory
        self.__fake_file = fake_file or FakeFile(file_name="fake_file_default", file_type_suffix=file_type_values.text)

    def exists(self):
        """
        exists
        @return: exists
        @rtype: bool
        """

        if self.__fake_stored_path.get(self.__fake_target_path):
            return True

        return False

    def is_dir(self):
        """
        is_dir
        @return: is_dir
        @rtype: bool
        """

        if self.__fake_target_path_type == path_types_values.directory:
            return True

        return False

    def is_file(self):
        """
        is_file
        @return: is_file
        @rtype: bool
        """

        if self.__fake_target_path_type == path_types_values.file:
            return True

        return False

    def joinpath(self, relative_path: str):
        """
        joinpath
        @param relative_path: relative_path
        @type relative_path: str
        @return: None
        @rtype: None
        """

        path_split = relative_path.split(".")
        valid_file_types = [value for key, value in file_type_values.__dict__.items()]
        self.__fake_target_path_type = path_types_values.file if f".{path_split[1]}" in valid_file_types else path_types_values.directory

        self.__fake_target_path = f"{self.__fake_target_path}/{relative_path}"

        return self.__fake_target_path

    def mkdir(self, parents: bool = None, exist_ok: bool = None):
        """
        mkdir
        @param parents: parents
        @type parents: bool
        @param exist_ok: exist_ok
        @type exist_ok: bool
        @return: None
        @rtype: None
        """

        if not self.exists():

            self.__fake_stored_path[self.__fake_target_path] = "dir"

    def touch(self, exist_ok: bool = None):
        """
        touch
        @param exist_ok: exist_ok
        @type exist_ok: bool
        @return: None
        @rtype: None
        """

        if self.__fake_target_path_type == path_types_values.file:

            self.__fake_stored_path[self.__fake_target_path] = self.__fake_file

    @property
    def suffix(self):
        """
        suffix
        @return: None
        @rtype: None
        """

        return self.__fake_file.suffix

