from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

# Criar tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "done": False
    }
    tasks.append(task)
    return jsonify(task), 201

# Listar tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Marcar como concluída
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)