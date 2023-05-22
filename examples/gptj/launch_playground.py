from xturing.models.base import BaseModel
from xturing.ui.playground import Playground

# Loads the model
# print(f'Loads the model')
# model = BaseModel.load("./.lr_find_f9a794bd-1b96-45d4-8b6a-66e2ab5e16e0.ckpt")

# Model path
model_path = "./gptj_weights"

# Save the model
# print(f'Save the model')
# model.save(model_path)

print(f'Launch the playground')
Playground(model_path).launch()