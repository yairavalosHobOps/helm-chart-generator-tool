# -*- coding: utf-8 -*-


# Infrastructure
from framework.base.infrastructure.file_management.file_creator import FileWriterCreator
from framework.base.infrastructure.file_management.file_doubles import FileFaker
from framework.base.infrastructure.file_management.file_handler import FileHandler
from framework.base.infrastructure.file_management.file_writer import JsonFileWriter
from framework.base.infrastructure.file_management.file_writer import RawFileWriter
from framework.base.infrastructure.file_management.file_writer import TextFileWriter
from framework.base.infrastructure.file_management.file_writer import YamlFileWriter
from framework.base.infrastructure.path_management.path_doubles import PathFaker
from framework.base.infrastructure.path_management.path_factory import SimplePathCreator

# Domain
from framework.base.domain.file_management.file_constants.file_mode_values import file_mode_values
from framework.base.domain.file_management.file_constants.file_type_values import file_type_values
from framework.base.domain.path_management.path_constants import path_types_values


def test_file_writer_creator_for_json_file_writer_type():
    """
    test_file_writer_creator_for_json_file_writer_type
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.json

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_suffix)
    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)

    fake_file_path = PathFaker(
        target_path=target_file_path,
        target_path_type=path_types_values.file,
        parent_path=fake_folder_path,
        file_obj=fake_file,
    )

    path_creator = SimplePathCreator(root_path=root_path)
    created_fake_path = path_creator.generate_path(path_obj=fake_file_path)

    file_handler = FileHandler(path_obj=created_fake_path, file_obj=fake_file, file_mode=file_mode_values.write)

    file_writer_creator = FileWriterCreator(path_obj=created_fake_path, file_handler=file_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="json")

    assert isinstance(file_writer, JsonFileWriter)


def test_file_writer_creator_for_text_file_writer_type():
    """
    test_file_writer_creator_for_text_file_writer_type
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.text

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_suffix)
    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)

    fake_file_path = PathFaker(
        target_path=target_file_path,
        target_path_type=path_types_values.file,
        parent_path=fake_folder_path,
        file_obj=fake_file,
    )

    path_creator = SimplePathCreator(root_path=root_path)
    created_fake_path = path_creator.generate_path(path_obj=fake_file_path)

    file_handler = FileHandler(path_obj=created_fake_path, file_obj=fake_file, file_mode=file_mode_values.write)

    file_writer_creator = FileWriterCreator(path_obj=created_fake_path, file_handler=file_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="text")

    assert isinstance(file_writer, TextFileWriter)


def test_file_writer_creator_for_yaml_file_writer_type():
    """
    test_file_writer_creator_for_yaml_file_writer_type
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.yaml

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}"

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_suffix)
    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)

    fake_file_path = PathFaker(
        target_path=target_file_path,
        target_path_type=path_types_values.file,
        parent_path=fake_folder_path,
        file_obj=fake_file,
    )

    path_creator = SimplePathCreator(root_path=root_path)
    created_fake_path = path_creator.generate_path(path_obj=fake_file_path)

    file_handler = FileHandler(path_obj=created_fake_path, file_obj=fake_file, file_mode=file_mode_values.write)

    file_writer_creator = FileWriterCreator(path_obj=created_fake_path, file_handler=file_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="yaml")

    assert isinstance(file_writer, YamlFileWriter)


def test_file_writer_creator_for_raw_file_writer_type():
    """
    test_file_writer_creator_for_raw_file_writer_type
    """

    root_path = "/home/user1"
    project_path = "/project1"
    folder_path = "/folder1"

    file_name = "test_file"
    file_type_suffix = file_type_values.raw
    file_raw_custom_suffix = "values.toml"

    target_folder_path = f"{root_path}{project_path}{folder_path}"
    target_file_path = f"{target_folder_path}/{file_name}{file_type_suffix}{file_raw_custom_suffix}"

    fake_file = FileFaker(file_name=file_name, file_type_suffix=file_type_suffix)
    fake_folder_path = PathFaker(target_path=target_folder_path, target_path_type=path_types_values.directory)

    fake_file_path = PathFaker(
        target_path=target_file_path,
        target_path_type=path_types_values.file,
        parent_path=fake_folder_path,
        file_obj=fake_file,
    )

    path_creator = SimplePathCreator(root_path=root_path)
    created_fake_path = path_creator.generate_path(path_obj=fake_file_path)

    file_handler = FileHandler(path_obj=created_fake_path, file_obj=fake_file, file_mode=file_mode_values.write)

    file_writer_creator = FileWriterCreator(path_obj=created_fake_path, file_handler=file_handler)
    file_writer = file_writer_creator.create_file_writer(file_type="raw")

    assert isinstance(file_writer, RawFileWriter)




