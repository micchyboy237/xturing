import os

from xturing.datasets import InstructionDataset
from xturing.model_apis.openai import Davinci

from dotenv import dotenv_values
env_vars = dotenv_values('.env')
api_key = env_vars['OPENAI_API_KEY']

seeds_file_name ="seed_tasks.jsonl"
output_path = "examples/llama/alpaca_gpt4_data_ph"
folder_path = "examples/llama/"
dataset_path = os.path.join(os.path.dirname(__file__), seeds_file_name)

def generate_from_seed(save_to_disk_path:str = output_path):
    engine = Davinci(api_key)
    instruction_dataset = InstructionDataset.generate_dataset(engine=engine, path=dataset_path)

    instruction_dataset.save(str(save_to_disk_path))