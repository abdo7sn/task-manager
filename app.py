from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# قائمة لحفظ المهام
tasks = []

# الصفحة الرئيسية التي تعرض المهام
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# إضافة مهمة جديدة
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    due_date = request.form.get('due_date')
    if task_content and due_date:
        tasks.append({"content": task_content, "due_date": due_date})
    return redirect(url_for('index'))

# تعديل مهمة
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        updated_task = request.form.get('task')
        due_date = request.form.get('due_date')
        tasks[task_id] = {"content": updated_task, "due_date": due_date}
        return redirect(url_for('index'))
    return render_template('edit.html', task=tasks[task_id])

# حذف مهمة
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
