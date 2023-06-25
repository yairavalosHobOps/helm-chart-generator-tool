# -*- coding: utf-8 -*-


# Domain
from core.modules.data_management import BaseDataHandler


class DictCleanerDataUtility(BaseDataHandler):
    """
    DictCleanerDataUtility
    """

    def process(self, input_data):
        """
        process
        @param input_data: input_data
        @type input_data: input_data
        @return: input_data
        @rtype: input_data
        """

        if not isinstance(input_data, (dict, list)):
            raise ValueError(f"Error input_data: {input_data} is not dict type nor list type ")

        if type(input_data) is dict:
            return dict((k, self.process(v)) for k, v in input_data.items() if v and self.process(v))

        if type(input_data) is list:
            return [self.process(v) for v in input_data if v and self.process(v)]