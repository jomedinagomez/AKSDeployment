import os
import logging
import json
import numpy


def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model_path
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    model_path = os.getenv("AZUREML_MODEL_DIR")
    # deserialize the model file back into a sklearn model
    logging.info("Init complete")


def run(raw_data):
    """
    This function is called for every invocation of the endpoint to perform the actual scoring/prediction.
    In the example we extract the data from the json input and call the scikit-learn model's predict()
    method and return the result back
    """
    files = os.listdir(os.getenv("AZUREML_MODEL_DIR"))
    print(files)
    return_files = os.listdir(model_path)
    return return_files
