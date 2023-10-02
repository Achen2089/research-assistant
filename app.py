import os
import openai
from flask import Flask, render_template, request

from metaphor_python import Metaphor

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize the SDK 
metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))

# Generate summary
def generate_summary(content):
    summary_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": f"Summarize the main ideas of the following text in three separate concise sentences: {content}"}
        ],
        max_tokens=300)
    summary = summary_completion['choices'][0]['message']['content']
    return summary

# Generate APA citation
def generate_citation(result, content):
    citation_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": f"Provide an APA citation for the following text: {result.title}, {result.published_date}, {result.author}, {result.url},{content}"}
        ],
        max_tokens=60)
    citation = citation_completion['choices'][0]['message']['content'].strip()
    return citation

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        # Fetch results from Metaphor API using its SDK.
        response = metaphor.search(
            "Most Reputable Papers about" + query,
            num_results= 6,
            use_autoprompt=True,
        )

        content_results = response.get_contents()
        for i in range(len(response.results)):
            result = response.results[i]
            content = content_results.contents[i]
            

            results.append({
                'title': result.title,
                'date': result.published_date,
                'authors': result.author,
                'url': result.url,
                'citation': generate_citation(result, content),
                'summary': generate_summary(content),
            })

        return render_template('results.html', query=query, results=results)
    elif request.method == 'GET' and request.args.get('query'):
        query = request.args.get('query') 
        # Fetch results from Metaphor API using its SDK.
        response = metaphor.search(
            "Most Reputable Papers about" + query,
            num_results= 6,
            use_autoprompt=True,
        )

        content_results = response.get_contents()
        for i in range(len(response.results)):
            result = response.results[i]
            content = content_results.contents[i]
            
            results.append({
                'title': result.title,
                'date': result.published_date,
                'authors': result.author,
                'url': result.url,
                'citation': generate_citation(result, content),
                'summary': generate_summary(content),
            })

        return render_template('results.html', query=query, results=results)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)