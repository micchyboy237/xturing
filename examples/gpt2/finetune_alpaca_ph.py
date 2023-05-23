import gc

from xturing.datasets.instruction_dataset import InstructionDataset
from xturing.models.base import BaseModel

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def finetune():
    instruction_dataset = InstructionDataset("../llama/alpaca_gpt4_data_ph")
    model_path = "./gpt2_weights"

    # Load the model
    print(f'Load the model')
    model = BaseModel.load(model_path)

    # Finetuned the model
    print(f'Finetune the model')
    model.finetune(dataset=instruction_dataset)

    # Save the model
    print(f'Save the model')
    model.save(model_path)

    # Garbage collection
    print(f'Model garbage collection')
    del model
    gc.collect()

if __name__ == '__main__':
    finetune()
