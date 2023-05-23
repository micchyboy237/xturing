from generate_ph import convert_to_tagalog

def prepare():
    # Example usage
    input_dir = 'examples/openai_dataset/data'  # Directory containing the JSONL input files
    output_dir = 'examples/openai_dataset/data_ph'  # Directory where translated JSONL files will be saved

    convert_to_tagalog(input_dir, output_dir)

if __name__ == '__main__':
    prepare()