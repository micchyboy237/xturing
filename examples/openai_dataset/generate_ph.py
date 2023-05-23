import openai
import json
import os

from dotenv import dotenv_values
env_vars = dotenv_values('.env')
api_key = env_vars['OPENAI_API_KEY']

print(f'OPENAI_API_KEY: {api_key}')

def convert_to_tagalog(input_dir, output_dir):
    # Set OpenAI API key
    openai.api_key = api_key

    # Retrieve file names in the input directory
    file_names = [file for file in os.listdir(input_dir) if file.endswith('.jsonl')]

    for file_name in file_names:
        input_file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)

        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                item = json.loads(line)

                # Specify the model and parameters for translation
                response = openai.Completion.create(
                    engine='text-davinci-003',
                    prompt=item['text'],
                    max_tokens=100,
                    temperature=0.8,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                    stop=None,
                    n=1,
                    log_level='info'
                )

                translated_text = response.choices[0].text.strip()

                # Create a new item with the translated text
                translated_item = {
                    'text': translated_text,
                    'original_text': item['text'],
                    'metadata': item['metadata']  # Include any relevant metadata from the original item
                }

                # Write the translated item to the output file
                output_file.write(json.dumps(translated_item) + '\n')

        print(f"Conversion completed for {file_name}.")

