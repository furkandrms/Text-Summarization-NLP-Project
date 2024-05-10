from textSummarize.pipeline.StageOneDataIngestion import DataIngestionTrainPipeline
from textSummarize.pipeline.StageTwoDataValidation import DataValidationTrainPipeline
from textSummarize.pipeline.StageThreeDataTransformation import DataTransformationTrainPipeline
from textSummarize.pipeline.StageFourModelTrainer import ModelTrainerTrainPipeline
from textSummarize.logging import logger 

STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x ========= x ")

except Exception as e: 
    logger.exception(e)
    raise e  



STAGE_NAME = "Data Validation Stage"

try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x ========= x ")

except Exception as e: 
    logger.exception(e)
    raise e  



STAGE_NAME = "Data Transformation Stage"

try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x ========= x ")

except Exception as e: 
    logger.exception(e)
    raise e  



STAGE_NAME = "Data Trainer Stage"

try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerTrainPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n x ========= x ")

except Exception as e: 
    logger.exception(e)
    raise e  





