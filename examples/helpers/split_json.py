import json

def split_json_file(input_file, output_prefix, limit):
    with open(input_file, 'r') as file:
        data = json.load(file)

    num_files = len(data) // limit + 1
    for i in range(num_files):
        start_index = i * limit
        end_index = (i + 1) * limit
        file_data = data[start_index:end_index]

        output_file = f'{output_prefix}_{i}.json'
        with open(output_file, 'w') as file:
            json.dump(file_data, file, indent=2)
        
        print(f'Saved {output_file} with {len(file_data)} items.')


input_file = 'examples/llama/alpaca_gpt4_data.json'
output_prefix = 'examples/openai_dataset/data/split'
limit = 5

split_json_file(input_file, output_prefix, limit)