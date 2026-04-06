from flask import Blueprint, request, jsonify
from services.task_service import TaskService
from schemas.task_schema import task_schema, tasks_schema
from marshmallow import ValidationError

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    status = request.args.get('status')
    priority = request.args.get('priority')
    tasks = TaskService.get_all_tasks(status, priority)
    return jsonify(tasks_schema.dump(tasks)), 200

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = task_schema.load(request.json)
        new_task = TaskService.create_task(data)
        return jsonify(task_schema.dump(new_task)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    try:
        data = request.json
        updated_task = TaskService.update_task(id, data)
        
        # Explicitly handle the 'Not Found' case to satisfy the test
        if not updated_task:
            return jsonify({"error": "Task not found"}), 404
            
        return jsonify(task_schema.dump(updated_task)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        return jsonify({"error": "Internal server error"}), 500

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        success = TaskService.delete_task(id)
        
        # Return 404 if the task didn't exist for deletion
        if not success:
            return jsonify({"error": "Task not found"}), 404
            
        return '', 204
    except Exception:
        return jsonify({"error": "Internal server error"}), 500