# PokeSeek - Pokémon Search Web App

## Project Overview  
PokeSeek is a web application that allows users to search for Pokémon and view their details using the PokéAPI. The application is built with Flask and fetches data from the API to display key information about the searched Pokémon, including its image, height, weight, type, abilities, base stats, and description.

## How It Works  
The application has a simple user interface where users can enter a Pokémon’s name in a search bar. Upon submitting the search, Flask sends a request to the PokéAPI to fetch the relevant data. If the Pokémon exists, its details are displayed on the page. If the name is incorrect or the Pokémon does not exist, an error message is shown. Additionally, an API endpoint is available that returns Pokémon details in JSON format.

## Project Files  
- `poke.py` - The main Flask application that handles requests and fetches Pokémon data.  
- `templates/poke.html` - The HTML file used for rendering Pokémon details.  
- `static/poke.css` - The CSS file for styling the user interface.  

## Requirements  
- Python 3.x  
- Flask (`pip install flask`)  
- Requests (`pip install requests`)  

## How to Run  
```bash
pip install flask requests  
python poke.py  
# Open browser and go to: http://127.0.0.1:5000/

## Why I Built This  
I built PokeSeek to practice working with APIs, Flask, and web development while creating something fun and interactive. This project helps improve backend skills by handling API requests and responses, managing errors, and integrating a simple frontend with Flask. Additionally, it serves as a great example of how to fetch and display real-time data dynamically.
