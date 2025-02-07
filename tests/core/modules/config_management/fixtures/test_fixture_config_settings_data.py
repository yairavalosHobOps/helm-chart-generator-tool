# -*- coding: utf-8 -*-


# fixtures
from tests.core.modules.config_management.fixtures import fixture_config_settings_data


def test_fixture_config_settings_data_call(fixture_config_settings_data):
    """
    test_fixture_config_settings_data_call
    @param fixture_config_settings_data: fixture_config_settings_data
    @type fixture_config_settings_data: dict
    """

    number_of_settings = len(fixture_config_settings_data)

    assert number_of_settings == 3
