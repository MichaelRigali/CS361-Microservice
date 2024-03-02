# microservice.py

# Import necessary modules
from flask import Flask, jsonify, request

# Create an instance of the Flask application
app = Flask(__name__)

# Recipe example data, it's a list of dictionaries containing dummy recipe data
# Each dictionary represents a recipe with a name and a list of ingredients
recipes = [
    {"name": "Pasta Carbonara", "ingredients": ["pasta", "eggs", "bacon", "cheese"]},
    {"name": "Caprese Salad", "ingredients": ["tomatoes", "mozzarella", "basil", "olive oil"]}
]

# Define the route for the endpoint to send recipes
@app.route('/send-recipes', methods=['POST'])
def send_valid_recipes():
    data = request.json
    # Extract the ingredients from the received data
    received_ingredients = data.get('ingredients', [])
    
    if received_ingredients:
        # Filter recipes based on the received ingredients
        matched_recipe = next((recipe for recipe in recipes if set(recipe['ingredients']) == set(received_ingredients)), None)
        if matched_recipe:
            # Return only the name of the matched recipe
            return jsonify({"name": matched_recipe['name']})
        else:
            return jsonify({"message": "No matching recipe found"}), 404
    else:
        return jsonify({"error": "No ingredients provided"}), 400

# Runs the application
if __name__ == '__main__':
    # Run the Flask application on Heroku
    # The host needs to be set to '0.0.0.0' for Heroku deployment
    app.run(debug=True, host='0.0.0.0')
