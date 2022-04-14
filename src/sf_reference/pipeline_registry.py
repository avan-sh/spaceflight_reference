"""Project pipelines."""
from typing import Dict

from kedro.pipeline import pipeline

from sf_reference.pipelines import data_processing as dp
from sf_reference.pipelines import data_science as ds


def register_pipelines() -> Dict[str, pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    return {
        "__default__": data_processing_pipeline + data_science_pipeline,
        "dp": data_processing_pipeline,
        "ds": data_science_pipeline,
    }
