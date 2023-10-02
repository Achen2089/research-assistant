# AI Research Assistant

This is a Flask web application that uses the Metaphor API and GPT to help users find reputable papers on a given topic, generate APA citations for those papers, and summarize the main ideas of those papers.

## Installation

To install the app, follow these steps:

- Clone the repository to your local machine.
- Install the necessary dependencies by running pip install -r requirements.txt.
- Set the environment variables OPENAI_API_KEY and METAPHOR_API_KEY to your OpenAI and Metaphor API keys, respectively.
- Enter into venv if needed.
- Start the development server by running python app.py.

To use the app, follow these steps:

- Open your web browser and navigate to where the servel is hosted locally 
- Enter a search query in the search bar and click the "Search" button.
- View the search results, which include the title, date, authors, URL, APA citation, and summary of each paper.
- Click on any of the links to view more information about the paper.
- Press the find similar button to find similar papers to the one you are currently viewing.
- Press the new search button to enter a new query.

## Demo

A Link to a demo of the app can be found [here](https://
## Additional Features

- Add a more button to the results page to append and search for more results.
- Utilize Metaphor's find similar function to get similar papers instead of searching with thew paper's name.