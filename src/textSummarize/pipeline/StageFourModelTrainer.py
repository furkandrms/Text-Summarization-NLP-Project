from textSummarize.config.configuration import ConfigurationManager
from textSummarize.conponents.model_trainer import ModelTrainer
from textSummarize.logging import logger


class ModelTrainerTrainPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()