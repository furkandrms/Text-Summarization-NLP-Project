from textSummarize.config.configuration import ConfigurationManager
from textSummarize.conponents.data_validation import DataValidation_
from textSummarize.logging import logger


class DataValidationTrainPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation_(config=data_validation_config)
        data_validation.validate_all_files_exist()