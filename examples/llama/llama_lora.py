import gc

from xturing.models import BaseModel

model_path = "./saved_model"

# Initialize the model
print(f'Initialize the model')
model = BaseModel.create("llama_lora")

# Save the model
print(f'Save the model')
model.save(model_path)

# Garbage collection
print(f'Model garbage collection')
del model
gc.collect()
