from xturing.models.base import BaseModel
from xturing.ui.playground import Playground

# Load the model
# print(f'Load the model')
# model = BaseModel.load("./gpt2_weights")

# Model path
model_path = "./gpt2_weights"

print(f'Launch the playground')
Playground(model_path).launch()