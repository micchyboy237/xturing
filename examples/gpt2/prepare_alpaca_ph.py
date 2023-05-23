import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llama.preparing_your_dataset import preprocess_alpaca_json_data
from openai_dataset.generate import generate_from_seed
from openai_dataset.generate_ph import convert_to_tagalog

file_name = "alpaca_gpt4_data_ph"
folder_path = "examples/llama/"
dataset_path = os.path.join(os.path.dirname(__file__), "../llama/", file_name + ".json")
preprocess_alpaca_json_data(dataset_path, folder_path + file_name)
