import React, { useState, useEffect, useCallback } from 'react';
import { taskApi } from '../api/taskApi';
import TaskForm from '../components/TaskForm';
import TaskList from '../components/TaskList';
import FilterBar from '../components/FilterBar';

const Dashboard = () => {
    const [tasks, setTasks] = useState([]);
    const [filters, setFilters] = useState({ status: '', priority: '' });

    const fetchTasks = useCallback(async () => {
        try {
            const response = await taskApi.getAll(filters);
            setTasks(response.data);
        } catch (err) {
            console.error(err);
        }
    }, [filters]);

    useEffect(() => {
        fetchTasks();
    }, [fetchTasks]);

    return (
        <div className="container">
            <h1>Task Tracker</h1>
            <div className="card">
                <TaskForm onRefresh={fetchTasks} />
            </div>
            <FilterBar filters={filters} onFilterChange={(n, v) => setFilters(prev => ({ ...prev, [n]: v }))} />
            <TaskList tasks={tasks} onRefresh={fetchTasks} />
        </div>
    );
};

export default Dashboard;