# import requests

# url = 'http://127.0.0.1:5000/recommend_jobs'
# my_data = {
#     "age": "25",
#     "education_level": "Bachelor",
#     "programming_languages": ["Python", "Java"],
#     "databases": ["SQL", "MongoDB"],
#     "web_technologies": ["HTML/CSS", "React"],
#     "work_environment_preference": "Startup",
#     "project_type_preference": "Web Development",
#     "leadership_preference": "Lead teams"
# }

# response = requests.post(url, json=my_data)
# print(response.json())
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key = os.environ.get("API_KEY"),
)

models = client.models.list()
for model in models['data']:
    print(model['id'])
