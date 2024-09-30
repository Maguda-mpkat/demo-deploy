from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (acts as our "database")
data_store = []

# Helper function to find an item by ID
def find_item(item_id):
    return next((item for item in data_store if item['id'] == item_id), None)

# Read (GET) - Fetch all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store), 200

# Read (GET) - Fetch a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = find_item(item_id)
    if item:
        return jsonify(item), 200
    return jsonify({'message': 'Item not found'}), 404

# Create (POST) - Add a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item['id'] = len(data_store) + 1
    data_store.append(new_item)
    return jsonify(new_item), 201

# Update (PUT) - Update an existing item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = find_item(item_id)
    if item:
        updated_data = request.json
        item.update(updated_data)
        return jsonify(item), 200
    return jsonify({'message': 'Item not found'}), 404

# Delete (DELETE) - Remove an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = find_item(item_id)
    if item:
        data_store.remove(item)
        return jsonify({'message': 'Item deleted'}), 200
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
