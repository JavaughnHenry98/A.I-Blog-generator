
## AI Blog ##


# Enabling deepseek AI with our api key 

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

#core Function

def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model = 'deepseek-chat',
        messages=[
        {"role": "user", "content": 'Write a paragraph about the following topic.' + paragraph_topic},
        ],
        max_tokens = 1000,
        temperature = 0.7
         
    )

    retrieve_blog = response.choices[0].message.content

    return retrieve_blog

print(generate_blog('Why Toronto is so expensive.'))

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for yes, anything else for no. ')
    if (answer == 'Y'):
        paragraph_topic = input('What should this paragraph talk about?')
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False