# AI Research Assistant

This is a Flask web application that uses the Metaphor API and GPT to help users find reputable papers on a given topic, generate APA citations for those papers, and summarize the main ideas of those papers.

## Installation

To install the app, follow these steps:

- Clone the repository to your local machine.
- Install the necessary dependencies by running `pip install -r requirements.txt`.
- Set the environment variables `OPENAI_API_KEY` and `METAPHOR_API_KEY` to your OpenAI and Metaphor API keys, respectively.
- Enter into venv if needed.
- Start the development server by running `python -m flask --app app run`.

To use the app, follow these steps:

- Open your web browser and navigate to where the service is hosted locally 
- Enter a search query in the search bar and click the "Search" button.
- View the search results, which include the title, date, authors, URL, APA citation, and summary of each paper.
- Click on any of the links to view more information about the paper.
- Press the find a similar button to find similar papers to the one you are currently viewing.
- Press the new search button to enter a new query.

## Demo

A Link to a demo of the app can be found [here](https://www.loom.com/share/ee39a637f7bb4f3baa12f69f5a12af1f?sid=cebfd55f-e64d-473f-a571-e9a0fcfa0280)

## Additional Features

- Add a more button to the results page to append and search for more results.
- Utilize Metaphor to find similar function to get similar papers instead of searching with the paper's name.
