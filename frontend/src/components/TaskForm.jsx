import React, { useState } from 'react';
import { taskApi } from '../api/taskApi';
import { PRIORITIES } from '../utils/constants';

const TaskForm = ({ onRefresh }) => {
    const [title, setTitle] = useState('');
    const [priority, setPriority] = useState('medium');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!title.trim()) {
            setError('Title cannot be empty');
            return;
        }

        try {
            await taskApi.create({ title, priority, status: 'todo' });
            setTitle('');
            setPriority('medium');
            setError('');
            onRefresh();
        } catch (err) {
            setError('Failed to create task');
        }
    };

    return (
        <form onSubmit={handleSubmit} style={{ marginBottom: '25px', padding: '15px', border: '1px solid #ddd' }}>
            <input 
                type="text" 
                value={title} 
                onChange={(e) => setTitle(e.target.value)} 
                placeholder="Task title..."
            />
            <select value={priority} onChange={(e) => setPriority(e.target.value)}>
                {PRIORITIES.map(p => <option key={p} value={p}>{p}</option>)}
            </select>
            <button type="submit">Create Task</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </form>
    );
};

export default TaskForm;