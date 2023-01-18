from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from entries import entries

def find_index_by_id(id):
    for index, entry in enumerate(entries):
        if entry['id'] == id:
            return index

def generate_next_id():
    ids = []
    for entry in entries:
        ids.append(entry['id'])
    new_id = 0
    while True:
        if new_id not in ids:
            return new_id
        else:
            new_id += 1

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', entries=entries, user_image='static/logo.png')

@app.route('/add', methods=['POST'])
def add():
    form = request.form
    title = form.get('name')
    description = form.get('role')
    seniority = form.get('seniority')
    entries.append({
        'id': generate_next_id(),
        'name': title,
        'role': description,
        'seniority': seniority
    })
    return redirect('/')

@app.route('/update/<int:id>')
def updateRoute(id):
    entry = entries[find_index_by_id(id)]
    if entry:
        return render_template('update.html', entry=entry, user_image='../static/logo.png')


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    entry = entries[find_index_by_id(id)]
    if entry:
        form = request.form
        title = form.get('name')
        description = form.get('role')
        seniority = form.get('seniority')
        entries[find_index_by_id(id)] = {
            'id': id,
            'name': title,
            'role': description,
            'seniority': seniority
        }
    return redirect('/')



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entries.pop(find_index_by_id(id))
        return redirect('/')
    return None

app.run()