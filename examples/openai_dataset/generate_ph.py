import openai

from dotenv import dotenv_values
env_vars = dotenv_values('.env')
api_key = env_vars['OPENAI_API_KEY']

print(f'OPENAI_API_KEY: {api_key}')

def convert_to_tagalog(english_text):
    # Set OpenAI API key
    openai.api_key = api_key
    
    # English to Tagalog translation prompt
    prompt = 'Convert to Tagalog\n\n{}'.format(english_text)

    print(f'prompt: {prompt}')
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You will convert all prompts from English to Tagalog after the line \"Convert to Tagalog.\""},
                {"role": "user", "content": prompt}
            ]
        )
    
    print(f'RESPONSE:\n{response}')
    
    tagalog_translation = response.choices[0].message.content

    print(f'TAGALOG TRANSLATION:\n{tagalog_translation}')

    return tagalog_translation
