import React from 'react';
import { taskApi } from '../api/taskApi';
import { STATUSES } from '../utils/constants';

const TaskList = ({ tasks, onRefresh }) => {
    const updateStatus = async (id, newStatus) => {
        try {
            await taskApi.update(id, { status: newStatus });
            onRefresh();
        } catch (err) {
            alert(err.response?.data?.error || 'Update failed');
        }
    };

    const deleteTask = async (id) => {
        if (window.confirm("Delete task?")) {
            await taskApi.delete(id);
            onRefresh();
        }
    };

    return (
        <div>
            {tasks.map(task => (
                <div key={task.id} className={`task-item priority-${task.priority}`}>
                    <div>
                        <div style={{fontWeight: 'bold'}}>{task.title}</div>
                        <div style={{fontSize: '12px', color: '#888'}}>{task.priority.toUpperCase()}</div>
                    </div>
                    <div style={{display: 'flex', gap: '5px'}}>
                        <select value={task.status} onChange={(e) => updateStatus(task.id, e.target.value)}>
                            {STATUSES.map(s => <option key={s} value={s}>{s}</option>)}
                        </select>
                        <button className="delete-btn" onClick={() => deleteTask(task.id)}>Delete</button>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default TaskList;