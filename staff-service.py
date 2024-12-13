from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for staff data (this could be replaced with a database)
staff_data = {}

@app.route('/staff', methods=['GET'])
def get_all_staff():
    """Retrieve all staff members"""
    return jsonify(staff_data), 200

@app.route('/staff/<int:staff_id>', methods=['GET'])
def get_staff(staff_id):
    """Retrieve a single staff member by ID"""
    staff = staff_data.get(staff_id)
    if not staff:
        return jsonify({'error': 'Staff member not found'}), 404
    return jsonify(staff), 200

@app.route('/staff', methods=['POST'])
def create_staff():
    """Create a new staff member"""
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'position', 'department', 'email', 'phone')):
        return jsonify({'error': 'Missing required fields'}), 400

    staff_id = len(staff_data) + 1  # Auto-generate staff ID
    staff = {
        'id': staff_id,
        'name': data['name'],
        'position': data['position'],
        'department': data['department'],
        'email': data['email'],
        'phone': data['phone']
    }
    staff_data[staff_id] = staff
    return jsonify(staff), 201

@app.route('/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    """Update an existing staff member"""
    staff = staff_data.get(staff_id)
    if not staff:
        return jsonify({'error': 'Staff member not found'}), 404

    data = request.get_json()
    staff['name'] = data.get('name', staff['name'])
    staff['position'] = data.get('position', staff['position'])
    staff['department'] = data.get('department', staff['department'])
    staff['email'] = data.get('email', staff['email'])
    staff['phone'] = data.get('phone', staff['phone'])
    return jsonify(staff), 200

@app.route('/staff/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    """Delete a staff member"""
    if staff_id not in staff_data:
        return jsonify({'error': 'Staff member not found'}), 404

    del staff_data[staff_id]
    return jsonify({'message': 'Staff member deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
