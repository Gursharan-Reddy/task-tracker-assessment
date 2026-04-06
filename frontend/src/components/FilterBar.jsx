import React from 'react';
import { PRIORITIES, STATUSES } from '../utils/constants';

const FilterBar = ({ filters, onFilterChange }) => {
    const handleSelect = (e) => {
        onFilterChange(e.target.name, e.target.value);
    };

    return (
        <div style={{ display: 'flex', gap: '15px', marginBottom: '20px' }}>
            <select name="status" value={filters.status} onChange={handleSelect}>
                <option value="">All Statuses</option>
                {STATUSES.map(s => <option key={s} value={s}>{s}</option>)}
            </select>
            <select name="priority" value={filters.priority} onChange={handleSelect}>
                <option value="">All Priorities</option>
                {PRIORITIES.map(p => <option key={p} value={p}>{p}</option>)}
            </select>
        </div>
    );
};

export default FilterBar;