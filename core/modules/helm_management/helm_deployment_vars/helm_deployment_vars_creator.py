# -*- coding: utf-8 -*-


# Domain
from core.modules.helm_management.helm_values_chart import HelmConfigValuesFilter
from core.modules.helm_management.helm_deployment_vars import HelmDeploymentEnvVarsFilter
from core.modules.helm_management.helm_deployment_vars import HelmDeploymentVarsDataProcessing
from core.modules.utility_services import DictCleanerDataUtility


class HelmDeploymentVarsCreator:
    """
    HelmDeploymentVarsCreator
    """

    def __init__(self, config_data: str = None):
        """
        HelmDeploymentVarsCreator constructor
        """

        if not isinstance(config_data, (str, type(None))):
            raise ValueError(f"Error config_data: {config_data} is not str type")

        self.__config_data = config_data
        self.__remove_empty_from_dict = DictCleanerDataUtility()
        self.__helm_config_values_filter = HelmConfigValuesFilter()
        self.__helm_deployment_env_vars_filter = HelmDeploymentEnvVarsFilter(config_data=self.__config_data)

    def create_vars_data(self, conf: dict):
        """
        create_vars_data
        @param conf: conf 
        @type conf: dict
        @return: conf
        @rtype: dict
        """""

        if not isinstance(conf, dict):
            raise ValueError(f"Error conf: {conf} is not dict type")

        helm_values_pipeline = (
            HelmDeploymentVarsDataProcessing()
            .add_handler(self.__remove_empty_from_dict)
            .add_handler(self.__helm_config_values_filter)
            .add_handler(self.__helm_deployment_env_vars_filter)
        )
        output_data = helm_values_pipeline.execute(input_data=conf)

        return output_data
