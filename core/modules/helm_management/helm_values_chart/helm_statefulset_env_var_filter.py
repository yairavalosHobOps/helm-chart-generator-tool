# -*- coding: utf-8 -*-


import re
from copy import deepcopy

# Domain
from core.modules.data_management import BaseDataHandler


class HelmStatefulSetEnvVarsFilter(BaseDataHandler):
    """
    HelmStatefulSetEnvVarsFilter
    """

    DEFAULT_ENV_VAR_PATTERN = r'\$\(.*?\)'

    def __init__(self, config_data: str = None):
        """
        HelmStatefulsetEnvVarsFilter constructor
        @param config_data: config_data
        @type config_data: str
        """

        if not isinstance(config_data, (str, type(None))):
            raise ValueError(f"Error config_data: {config_data} is not str type")

        self.__config_data = config_data or self.DEFAULT_ENV_VAR_PATTERN

    def process(self, conf: dict):
        """
        process
        @param conf: conf
        @type conf: dict
        @return: conf
        @rtype: dict
        """

        if not isinstance(conf, dict):
            raise ValueError(f"Error conf: {conf} is not dict type")

        statefulset_resources = conf["common-library"].get("StatefulSet")

        if not statefulset_resources:
            return conf

        for component in statefulset_resources:

            component_env_vars: list = statefulset_resources[component].get("env")

            if component_env_vars:
                filtered_env_ars = [item for item in component_env_vars if re.search(self.__config_data, item['value'])]
                statefulset_resources[component]["env"] = filtered_env_ars

        conf["common-library"]["StatefulSet"] = statefulset_resources

        return conf
