import pytest
from app import create_app
from extensions import db
from models.task import Task

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_create_task_success(client):
    payload = {"title": "Finish Assessment", "priority": "high", "status": "todo"}
    response = client.post('/api/tasks', json=payload)
    assert response.status_code == 201
    assert response.json['title'] == "Finish Assessment"

def test_create_task_empty_title(client):
    payload = {"title": "", "priority": "high", "status": "todo"}
    response = client.post('/api/tasks', json=payload)
    assert response.status_code == 400

def test_create_task_invalid_priority(client):
    payload = {"title": "Test", "priority": "urgent", "status": "todo"}
    response = client.post('/api/tasks', json=payload)
    assert response.status_code == 400

def test_get_invalid_task_id(client):
    response = client.put('/api/tasks/999', json={"status": "done"})
    assert response.status_code == 404

def test_prevent_archived_transition(client):
    with client.application.app_context():
        t = Task(title="Old Task", status="archived", priority="low")
        db.session.add(t)
        db.session.commit()
        task_id = t.id

    response = client.put(f"/api/tasks/{task_id}", json={"status": "todo"})
    assert response.status_code == 400

def test_filter_tasks_by_status(client):
    with client.application.app_context():
        t1 = Task(title="Task A", status="todo", priority="low")
        t2 = Task(title="Task B", status="done", priority="high")
        db.session.add_all([t1, t2])
        db.session.commit()

    response = client.get('/api/tasks?status=done')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['title'] == "Task B"