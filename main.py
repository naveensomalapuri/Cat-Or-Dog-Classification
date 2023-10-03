from Cat_Or_Dog_Classification import logger
from Cat_Or_Dog_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>stage {STAGE_NAME} complete <<<<<\n\nx=====")
except Exception as e:
    logger.exception(e)
    raise e