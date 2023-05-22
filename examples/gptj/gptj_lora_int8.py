import gc

from xturing.datasets.instruction_dataset import InstructionDataset
from xturing.models import BaseModel

# instruction_dataset = InstructionDataset("../llama/alpaca_data")

# Initializes the model
print(f'Initialize the model')
model = BaseModel.create("gptj_lora_int8")

# Finetuned the model
# model.finetune(dataset=instruction_dataset)

# Save the model
print(f'Save the model')
model.save("./gptj_weights")

# Garbage collection
print(f'Model garbage collection')
del model
gc.collect()

# Load the model
print(f'Load the model')
model = BaseModel.load("./gptj_weights")

# Once the model has been finetuned, you can start doing inferences
print(f'Generate output')
output = model.generate(texts=["Why LLM models are becoming so important?"])
print("Generated output by the model: {}".format(output))
