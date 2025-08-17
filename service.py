import bentoml
import torch
import numpy as np
import cloudpickle

# torch.serialization.add_safe_globals([cloudpickle._make_skeleton_class])
# torch.serialization.add_safe_globals([cloudpickle.cloudpickle._make_skeleton_class])
# torch.serialization.safe_globals([type])
# torch.serialization.safe_globals([cloudpickle.cloudpickle._make_skeleton_class])
@bentoml.service(
	resources={"cpu": "2"},
	traffic={"timeout": 10},
)
class cifarclassifier:
    bento_model = bentoml.models.BentoModel("cifar10_onnx:latest")
    
    def __init__(self):
        # self.model = bentoml.pytorch.load_model(self.bento_model)
        self.model = bentoml.onnx.load_model(self.bento_model)
        
    @bentoml.api
    def predict(self, input: np.ndarray):
        preds = self.model.predict(input)
        return preds