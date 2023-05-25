from xturing.models.base import BaseModel
from xturing.ui.playground import Playground

model_path = "./saved_model"

print(f'Launch the playground')
Playground(model_path).launch()