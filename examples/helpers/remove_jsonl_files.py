import os

def remove_jsonl_files(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Iterate over each file in the directory
    for file in files:
        # Check if the file has the .jsonl extension
        if file.endswith('.jsonl'):
            # Construct the file path
            file_path = os.path.join(directory, file)

            # Remove the file
            os.remove(file_path)

            print(f"Removed file: {file_path}")

    print("Removal completed for all .jsonl files.")

jsonl_path = os.path.abspath('examples/openai_dataset/data_ph')
# Usage example
remove_jsonl_files(jsonl_path)
