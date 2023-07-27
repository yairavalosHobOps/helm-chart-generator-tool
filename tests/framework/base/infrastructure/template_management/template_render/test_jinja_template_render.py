# -*- coding: utf-8 -*-


# Infrastructure
from framework.base.infrastructure.file_management.file_doubles import FileFaker
from framework.base.infrastructure.file_management.file_handler import FileHandler
from framework.base.infrastructure.path_management.path_doubles import PathFaker
from framework.base.infrastructure.template_management.template_loader import JinjaTemplateLoaderFaker

# Domain
from framework.base.domain.file_management.file_constants.file_type_values import file_type_values
from framework.base.domain.path_management.path_constants.path_type_values import path_types_values


def test_jinja_template_render():
    """
    test_jinja_template_render
    """

    expected_render = """
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: deployment-test
    spec:
      selector:
        matchLabels:
          app: nginx-test
      replicas: 4
      template:
        metadata:
          labels:
            app: nginx-test
        spec:
          containers:
          - name: nginx-container
            image: nginx:latest
            env:
            - name: FOO_VARIABLE1
              value: 123
            - name: FOO_VARIABLE2
              value: $(FOO_VARIABLE1)
    """

    template_content = """
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: {{deployment_name}}
    spec:
      selector:
        matchLabels:
          app: {{app_name}}
      replicas: {{replica_number}}
      template:
        metadata:
          labels:
            app: {{app_name}}
        spec:
          containers:
          - name: {{container_name}}
            image: {{image_name}}:{{image_tag}}
            env:
            - name: {{env_name_1}}
              value: {{env_value_1}}
            - name: {{env_secret_name_2}}
              value: $({{env_secret_value_2}})
    """

    template_file = FileFaker(
        file_name="fake_template_file",
        file_type_suffix=file_type_values.yaml,
        initial_content=template_content,
    )

    template_file.open()

    template_dir_path = PathFaker(
        target_path="/user/folder1/template_folder",
        target_path_type=path_types_values.directory,
    )

    file_handler = FileHandler(file_obj=template_file)

    template_loader = JinjaTemplateLoaderFaker(template_dir_path=template_dir_path, file_handler=file_handler)
    template_jinja = template_loader.get_template(template_name="template_file")

    data_to_render = {
        "deployment_name": "deployment-test",
        "app_name": "nginx-test",
        "replica_number": "4",
        "container_name": "nginx-container",
        "image_name": "nginx",
        "image_tag": "latest",
        "env_name_1": "FOO_VARIABLE1",
        "env_value_1": "123",
        "env_secret_name_2": "FOO_VARIABLE2",
        "env_secret_value_2": "FOO_VARIABLE1",
    }

    content_rendered = template_jinja.render(data_to_render=data_to_render)

    assert template_loader
    assert template_jinja
    assert content_rendered == expected_render