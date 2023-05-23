from generate import generate_from_seed

def prepare():
    # seeds_file_path = 'examples/openai_dataset/data'  # Directory containing the JSONL input files
    output_path = 'examples/openai_dataset/data_ph'  # Directory where translated JSONL files will be saved

    generate_from_seed(output_path)

if __name__ == '__main__':
    prepare()