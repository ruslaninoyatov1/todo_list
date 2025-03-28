from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    today_date = datetime.now().strftime('%d-%m-%Y')

    # 24 soatdan eski bo‘lgan vazifalarni o‘chirish
    global tasks
    now = datetime.now()
    tasks = [task for task in tasks if task["deadline"] > now - timedelta(days=1)]

    return render_template('index.html', tasks=tasks, today_date=today_date)

@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['task_name']
    deadline = request.form['deadline']
    tasks.append({
        "id": len(tasks) + 1,
        "name": name,
        "deadline": datetime.strptime(deadline, '%Y-%m-%dT%H:%M'),
        "status": "❌"
    })
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "✅"
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        new_name = request.form['task_name']
        new_deadline = request.form['deadline']
        for task in tasks:
            if task["id"] == task_id:
                task["name"] = new_name
                task["deadline"] = datetime.strptime(new_deadline, '%Y-%m-%dT%H:%M')
                break
        return redirect(url_for('index'))
    
    task_to_edit = next((task for task in tasks if task["id"] == task_id), None)
    return render_template('edit.html', task=task_to_edit)

if __name__ == '__main__':
    app.run(debug=True)
