import os
import gc

from xturing.models.base import BaseModel

model_path = "./gpt2_weights"

if os.path.exists(model_path):
    # Load the model
    print(f'Load existing weights')
    model = BaseModel.load(model_path)
else:
    # Initialize the model
    print(f'Initialize the model')
    model = BaseModel.create("gpt2_lora")

    # Save the model
    print(f'Save the model')
    model.save(model_path)

    # Garbage collection
    print(f'Model garbage collection')
    del model
    gc.collect()
