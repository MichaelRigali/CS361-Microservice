# Import framework followed by necessary modules
from flask import Flask, jsonify, request

# Creates an instance of the application
app = Flask(__name__)

# Recipe example data, it's a list of dictionaries containing dummy recipe data
# Each dictionary represents a recipe with a name and a list of ingredients
recipes = [
    {"name": "Pasta Carbonara", "ingredients": ["pasta", "eggs", "bacon", "cheese"]},
    {"name": "Caprese Salad", "ingredients": ["tomatoes", "mozzarella", "basil", "olive oil"]}
]

# An endpoint defined by HTTP method 'GET'. 
# This is the endpoint used to retrieve valid recipes based on the ingredients
# provided as query parameters. 
@app.route('/get-recipes', methods=['GET'])
def get_valid_recipes():
    # Extract ingredients from the request query parameters
    ingredients = request.args.getlist('ingredients')
    
    if ingredients:
        # Filter recipes based on the provided ingredients
        matching_recipes = [recipe for recipe in recipes if all(ingredient in recipe['ingredients'] for ingredient in ingredients)]
        # Return the valid recipes in the response body as JSON
        return jsonify(matching_recipes)
    else:
        # If no ingredients are provided, return this error message
        return jsonify({"error": "No ingredients provided"}), 400

# Another endpoint defined with the HTTP method 'POST'. 
# This endpoint is used to send valid recipes
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
    app.run(debug=True)
