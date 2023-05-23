import json
import os

def convert_jsonl_files_to_json(jsonl_directory, json_directory):
    # Get a list of all JSONL files in the directory
    jsonl_files = [file for file in os.listdir(jsonl_directory) if file.endswith('.jsonl')]

    # Iterate over each JSONL file
    for jsonl_file in jsonl_files:
        # Construct the input and output file paths
        jsonl_file_path = os.path.join(jsonl_directory, jsonl_file)
        json_file_path = os.path.join(json_directory, jsonl_file.replace('.jsonl', '.json'))

        # Open the JSONL file for reading
        with open(jsonl_file_path, 'r') as file:
            # Read all lines from the JSONL file
            lines = file.readlines()

        # Create an empty list to store the JSON objects
        json_objects = []

        # Iterate over each line in the JSONL file
        for line in lines:
            # Load the JSON object from the line
            json_obj = json.loads(line)
            # Append the JSON object to the list
            json_objects.append(json_obj)

        # Open the JSON file for writing
        with open(json_file_path, 'w') as file:
            # Write the JSON objects as a single JSON array
            json.dump(json_objects, file)

        print(f"Converted {len(json_objects)} JSONL objects to JSON file: {json_file_path}")

    print("Conversion completed for all JSONL files.")

input_jsonl_path = os.path.abspath('examples/openai_dataset/data_ph')
output_json_path = os.path.abspath('examples/openai_dataset/data_ph')

convert_jsonl_files_to_json(input_jsonl_path, output_json_path)
