# Import necessary modules
from flask import Flask, jsonify, request

# Create an instance of the Flask application
app = Flask(__name__)

# Recipe example data, it's a list of dictionaries containing dummy recipe data
# Each dictionary represents a recipe with a name and a list of ingredients
recipes = [
    {
	"name": "Garlic Fries",
	"ingredients": ["Potato", "Olive Oil", "Garlic"],
	"instructions": "Peel and slice the potato.\nCut the potatoe julienne style.\nSoak fry slices in salted water for 30 minutes.\nDry fries with paper towel, then toss in a bowl with crushed garlic and olive oil.\nBake in oven on 420 for 20 minutes."
},

{
	"name": "Hamburger",
	"ingredients": ["Ground Beef", "Garlic", "Hamburger Buns"],
	"instructions": "Knead the ground beef into a 8 2 inch balls, then flatten into patties.\nAdd salt and garlic powder, then cook on skillet until brown.\nPlace on bun and add condiments as desired."
},

{
	"name": "Meatballs",
	"ingredients": ["Ground Beef", "Bread Crumbs", "Garlic", "Olive Oil", "Cream", "Egg"],
	"instructions": "Mix ground beef, bread crumbs, garlic, salt, eggs, and cream together in a bowl.\nKnead gently and form into 2 inch balls.\nLightly coat meatballs in olive oil and bake them in the oven for 30 minutes at 350 degrees."
},

{
	"name": "Pasta Carbonara",
	"ingredients": ["Spaghetti", "Bacon", "Parmesan", "Egg", "Garlic"],
	"instructions": "Simmer bacon on skillet.\nRemove when crispy, and save the frond.\nSaute garlic until golden, then add to a bowl with the bacon fat, eggs, parmesan, and pepper.\nCook noodles until al dente, reserving some pasta water.\nAdd pasta water to mixture, then coat noodles."
},

{
	"name": "Paratha",
	"ingredients": ["Potato", "Atta", "Cumin", "Green Chili Pepper", "Chaat Masala", "Onion"],
	"instructions": "Peel and boil potatoes in salted water.\nMeanwhile, finely dice the peppers and onions.\nMash the potatoes and combine with the onions, peppers, cumin, and chaat masala.\nKnead the dough until done, then let rest for 15 minutes.\nRoll out dough and stuff with potato mixture.\nRoll again until flat, and cook on griddle onr tawa for 3 minutes each side."
},

{
	"name": "Rajma Chawal",
	"ingredients": ["Red Beans", "Garlic", "Ginger", "Tomato", "Cream", "Rice"],
	"instructions": "Soak red beans overnight.\nFinely chop garlic and ginger.\nToast the garlic-ginger paste lightly in a deep-sided skillet until fragrant.\nAdd tomatoes and reduce.\nPressure cook beans and add to sauce.\nFinally, lightly top with cream to serve with rice."
}
]

# Define the route for the endpoint to send recipes
@app.route('/send-recipes', methods=['POST'])
def send_valid_recipes():
    data = request.json
    # Extract the ingredients from the received data
    received_ingredients = data.get('ingredients', [])
    
    if received_ingredients:
        # Filter recipes based on the received ingredients
        matched_recipe = next((recipe for recipe in recipes if all(ingredient in recipe['ingredients'] for ingredient in received_ingredients)), None)
        if matched_recipe:
            # Return the name and instructions of the matched recipe in JSON format
            response_data = {"name": matched_recipe['name'], "instructions": matched_recipe['instructions']}
            return jsonify(response_data)
        else:
            return jsonify({"message": "No matching recipe found"}), 404
    else:
        return jsonify({"error": "No ingredients provided"}), 400


# Runs the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
