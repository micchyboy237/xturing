from xturing.models.base import BaseModel
from xturing.ui.playground import Playground

model_path = "./gpt2_weights"

print(f'Launch the playground')
Playground(model_path).launch()