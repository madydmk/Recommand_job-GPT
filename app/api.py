import openai
from flask import Flask, request, jsonify
import time
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# openai.api_key = "sk-proj-fkCiwX1Z6dm4lPQBcVObT3BlbkFJnaofdCNfCcDKfHwQ1NRv"
client = openai.OpenAI(
    api_key = os.environ.get("API_KEY"),
)
def send_request(user_responses):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Utilise le modèle GPT-3.5-turbo ou GPT-4-turbo
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": create_prompt(user_responses)}
            ],
            max_tokens=150,
            temperature=0.7
        )
        result = response.choices[0].message
        print(response.model_fields)
        return result.content.strip()
    # except openai.error.RateLimitError:
    #     time.sleep(5)  # Attendre avant de réessayer
    #     return get_it_job_recommendations(user_responses)
    except openai.OpenAIError as e:  # Note: Modification de l'importation de l'erreur
        return str(e)

def create_prompt(responses):
    prompt = f"""
    Based on the following responses, recommend three IT jobs. Return me a list of tuples (job, description) that can be stocked in a list without your usual text before:
    Name: {responses.get('name')}
    Age: {responses.get('age')}
    Education Level: {responses.get('education_level')}
    Personality: {responses.get('personality')}
    Programming Languages: {', '.join(responses.get('programming_languages', []))}
    Databases: {', '.join(responses.get('databases', []))}
    Web Technologies: {', '.join(responses.get('web_technologies', []))}
    Work Environment Preference: {responses.get('work_environment_preference')}
    Project Type Preference: {responses.get('project_type_preference')}
    Leadership Preference: {responses.get('leadership_preference')}
    """
    return prompt.strip()

app = Flask(__name__)

@app.route('/recommend_jobs', methods=['POST'])
def search():
    data = request.json
    recommendations = send_request(data)
    return jsonify(recommendations)
if __name__ == '__main__':
    app.run()
