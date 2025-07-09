from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_NAME = 'ghar_notebook.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Expenses
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL
    )''')
    # Shopping
    c.execute('''CREATE TABLE IF NOT EXISTS shopping (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        quantity TEXT,
        purchased INTEGER DEFAULT 0
    )''')
    # Medicines
    c.execute('''CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        quantity TEXT,
        expiry TEXT
    )''')
    # Income
    c.execute('''CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        source TEXT,
        amount REAL
    )''')
    # Loans
    c.execute('''CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        person TEXT,
        amount REAL,
        type TEXT,
        due_date TEXT
    )''')
    # Notes
    c.execute('''CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        created_at TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return 'Ghar Notebook API is running.'

# --- Expenses Endpoints ---
@app.route('/api/expenses', methods=['GET', 'POST'])
def expenses():
    if request.method == 'POST':
        data = request.json
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)',
                  (data['date'], data['category'], data['description'], data['amount']))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    else:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM expenses ORDER BY date DESC')
        rows = c.fetchall()
        conn.close()
        expenses = [
            {'id': row[0], 'date': row[1], 'category': row[2], 'description': row[3], 'amount': row[4]}
            for row in rows
        ]
        return jsonify(expenses)

# --- Expenses DELETE ---
@app.route('/api/expenses/<int:item_id>', methods=['DELETE'])
def delete_expense(item_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM expenses WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})

# --- Shopping Endpoints ---
@app.route('/api/shopping', methods=['GET', 'POST'])
def shopping():
    if request.method == 'POST':
        data = request.json
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO shopping (item, quantity, purchased) VALUES (?, ?, ?)',
                  (data['item'], data['quantity'], int(data.get('purchased', 0))))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    else:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM shopping')
        rows = c.fetchall()
        conn.close()
        shopping = [
            {'id': row[0], 'item': row[1], 'quantity': row[2], 'purchased': bool(row[3])}
            for row in rows
        ]
        return jsonify(shopping)

# --- Shopping DELETE ---
@app.route('/api/shopping/<int:item_id>', methods=['DELETE'])
def delete_shopping(item_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM shopping WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})

# --- Medicines Endpoints ---
@app.route('/api/medicines', methods=['GET', 'POST'])
def medicines():
    if request.method == 'POST':
        data = request.json
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO medicines (name, quantity, expiry) VALUES (?, ?, ?)',
                  (data['name'], data['quantity'], data['expiry']))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    else:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM medicines')
        rows = c.fetchall()
        conn.close()
        medicines = [
            {'id': row[0], 'name': row[1], 'quantity': row[2], 'expiry': row[3]}
            for row in rows
        ]
        return jsonify(medicines)

# --- Medicines DELETE ---
@app.route('/api/medicines/<int:item_id>', methods=['DELETE'])
def delete_medicine(item_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM medicines WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})

# --- Income Endpoints ---
@app.route('/api/income', methods=['GET', 'POST'])
def income():
    if request.method == 'POST':
        data = request.json
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO income (date, source, amount) VALUES (?, ?, ?)',
                  (data['date'], data['source'], data['amount']))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    else:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM income ORDER BY date DESC')
        rows = c.fetchall()
        conn.close()
        income = [
            {'id': row[0], 'date': row[1], 'source': row[2], 'amount': row[3]}
            for row in rows
        ]
        return jsonify(income)

# --- Income DELETE ---
@app.route('/api/income/<int:item_id>', methods=['DELETE'])
def delete_income(item_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM income WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})

# --- Loans Endpoints ---
@app.route('/api/loans', methods=['GET', 'POST'])
def loans():
    if request.method == 'POST':
        data = request.json
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO loans (date, person, amount, type, due_date) VALUES (?, ?, ?, ?, ?)',
                  (data['date'], data['person'], data['amount'], data['type'], data.get('due_date')))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    else:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM loans ORDER BY date DESC')
        rows = c.fetchall()
        conn.close()
        loans = [
            {'id': row[0], 'date': row[1], 'person': row[2], 'amount': row[3], 'type': row[4], 'due_date': row[5]}
            for row in rows
        ]
        return jsonify(loans)

# --- Loans DELETE ---
@app.route('/api/loans/<int:item_id>', methods=['DELETE'])
def delete_loan(item_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM loans WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})

# --- Notes Endpoints ---
@app.route('/api/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        data = request.json
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO notes (content, created_at) VALUES (?, ?)',
                  (data['content'], data['created_at']))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    else:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM notes ORDER BY created_at DESC')
        rows = c.fetchall()
        conn.close()
        notes = [
            {'id': row[0], 'content': row[1], 'created_at': row[2]}
            for row in rows
        ]
        return jsonify(notes)

# --- Notes DELETE ---
@app.route('/api/notes/<int:item_id>', methods=['DELETE'])
def delete_note(item_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM notes WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    app.run(debug=True) 