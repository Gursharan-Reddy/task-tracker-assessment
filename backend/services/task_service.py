from models.task import Task
from extensions import db

class TaskService:
    @staticmethod
    def get_all_tasks(status_filter=None, priority_filter=None):
        query = db.select(Task)
        if status_filter:
            query = query.filter_by(status=status_filter)
        if priority_filter:
            query = query.filter_by(priority=priority_filter)
        return db.session.execute(query).scalars().all()

    @staticmethod
    def create_task(data):
        new_task = Task(**data)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def update_task(task_id, data):
        task = db.session.get(Task, task_id)
        if not task:
            return None
        
        if task.status == 'archived' and data.get('status') and data.get('status') != 'archived':
            raise ValueError("Archived tasks must be restored before changing status.")

        for key, value in data.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        db.session.commit()
        return task

    @staticmethod
    def delete_task(task_id):
        task = db.session.get(Task, task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        return False