import json
import os
import sys

from generate_ph import convert_to_tagalog

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from helpers.convert_jsonl_to_json import convert_jsonl_files_to_json

def prepare(input_file_path, output_file_path):
    print(f"Preparing file: {input_file_path}")

    # Load the data from json file
    with open(input_file_path, 'r') as file:
        data = json.load(file)

    # Translate all attributes for each item
    for item in data:
        for key in item:
            english_text = item[key]
            print(f"KEY:" + key)
            tagalog_translation = convert_to_tagalog(english_text) if english_text else ""
            item[key] = tagalog_translation

        line = json.dumps(item)
        
        # Append each translated line to a new file in JSONL format
        with open(output_file_path, 'a') as file:
            file.write(line + '\n')

def append_line_to_file(file_path, line):
    # Open the file in read mode to read its existing content
    with open(file_path, 'r') as file:
        content = file.read()

    # Open the file in append mode to append the new line
    with open(file_path, 'a') as file:
        # Write the existing content
        file.write(content)

        # Append the new line
        file.write(line + '\n')
        
def process_files():
    data_dir = 'examples/openai_dataset/data-to-process'  # Directory containing the JSONL data files
    output_dir = 'examples/openai_dataset/data_ph'  # Directory where translated JSONL files will be saved
    
    # Retrieve all file names with .json extension
    file_names = [
        file for file in os.listdir(data_dir) 
        if file.startswith("split_") and file.endswith(".json")
    ]

    sorted_file_names = sorted(file_names)

    for file_name in sorted_file_names:
        data_file_path = os.path.join(data_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name + 'l')

        prepare(data_file_path, output_file_path)

if __name__ == '__main__':
    process_files()

    input_jsonl_path = os.path.abspath('examples/openai_dataset/data_ph')
    output_json_path = os.path.abspath('examples/openai_dataset/data_ph')

    convert_jsonl_files_to_json(input_jsonl_path, output_json_path)

print("DONE")