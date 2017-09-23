import pandas as pd
import numpy as np
from typing import List, NamedTuple

from .numeric import range_groups
from primitive_interfaces.base import PrimitiveBase

Inputs = pd.DataFrame
Outputs = np.ndarray
Params = dict
CallMetadata = dict

class AggregateByNumericRange(PrimitiveBase[Inputs, Outputs, Params]): 
    __author__ = 'distil'
    __metadata__ = {
        "id": "67a642bc-9e36-3154-b21e-0b74744a8900",
        "name": "aggregator.aggregation.numeric.numeric_range_aggregation",
        "common_name": "NumericRangeAggregation",
        "description": "Determine the best bins for value counts and perform the aggregation",
        "languages": [
            "python3.6"
        ],
        "library": "aggregation",
        "version": "0.1.0",
        "source_code": "https://github.com/NewKnowledge/aggregator/blob/master/aggregator/__init__.py#L29",
        "is_class": True,
        "interface_type": "data_cleaning",
        "algorithm_type": [                                                         
            "aggregation"                                              
        ],
        "task_type": [
            "data cleaning"                                              
        ],
        "output_type": [
            "features"
        ], 
        "team": "distil",
        "schema_version": 1.0,
        "build": [
            {
                "type": "pip",
                "package": "aggregator"
            }
        ],
        "compute_resources": {
            "sample_size": [
                1000.0, 
                10.0
            ],
            "sample_unit": [
                "MB"
            ],
            "num_nodes": [
                1
            ],
            "cores_per_node": [
                1
            ],
            "gpus_per_node": [
                0
            ],
            "mem_per_node": [
                1.0
            ],
            "disk_per_node": [
                1.0
            ],
            "mem_per_gpu": [
                0.0
            ],
            "expected_running_time": [
                5.0
            ]
        }
    }


    def __init__(self):
        pass

    def get_params(self) -> Params:
        return {}

    def set_params(self, params: Params) -> None:
        self.params = params

    def get_call_metadata(self) -> CallMetadata: 
        return {}

    def fit(self) -> None:
        pass

    def produce(self, inputs: Inputs, values: List[str] = []) -> Outputs:
        return range_groups(inputs, values)