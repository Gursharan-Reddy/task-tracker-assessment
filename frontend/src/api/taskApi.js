import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/api/tasks';

export const taskApi = {
    getAll: (filters) => axios.get(API_BASE_URL, { params: filters }),
    create: (taskData) => axios.post(API_BASE_URL, taskData),
    update: (id, taskData) => axios.put(`${API_BASE_URL}/${id}`, taskData),
    delete: (id) => axios.delete(`${API_BASE_URL}/${id}`)
};