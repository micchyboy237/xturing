import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llama.preparing_your_dataset import preprocess_alpaca_json_data

file_name = "alpaca_gpt4_data"
folder_path = "examples/llama/"
dataset_path = os.path.join(os.path.dirname(__file__), "../llama/", file_name + ".json")
preprocess_alpaca_json_data(dataset_path, folder_path + file_name)
