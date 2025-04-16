// src/components/Dashboard.tsx
import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { getProjects, Project } from '../services/projectService';
import { getMyTasks, Task } from '../services/taskService';

const Dashboard = () => {
  const { logout } = useAuth();
  const [projects, setProjects] = useState<Project[]>([]);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        
        // Fetch projects and current user's tasks in parallel
        const [projectsData, tasksData] = await Promise.all([
          getProjects(),
          getMyTasks()
        ]);
        
        setProjects(projectsData);
        setTasks(tasksData);
        setError(null);
      } catch (err: any) {
        console.error('Error fetching data:', err);
        setError('Failed to load data. Please try again.');
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Time Management Dashboard</h1>
        <button 
          onClick={logout}
          className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
        >
          Logout
        </button>
      </div>
      
      {error && (
        <div className="p-4 mb-6 bg-red-100 text-red-700 rounded">
          {error}
        </div>
      )}
      
      {loading ? (
        <div className="flex justify-center p-8">
          <div className="text-lg">Loading...</div>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* My Tasks */}
          <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-lg font-medium mb-3">My Tasks</h2>
            {tasks.length > 0 ? (
              <ul className="space-y-2">
                {tasks.slice(0, 5).map((task) => (
                  <li key={task.id} className="p-2 border-b">
                    <div className="font-medium">{task.title}</div>
                    <div className="text-sm text-gray-600">
                      Priority: {task.priority}
                    </div>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-gray-600">No tasks assigned to you yet.</p>
            )}
          </div>
          
          {/* Current Projects */}
          <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-lg font-medium mb-3">Current Projects</h2>
            {projects.length > 0 ? (
              <ul className="space-y-2">
                {projects.slice(0, 5).map((project) => (
                  <li key={project.id} className="p-2 border-b">
                    <div className="font-medium">{project.name}</div>
                    <div className="text-sm text-gray-600">
                      Client: {project.client}
                    </div>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-gray-600">No projects available yet.</p>
            )}
          </div>
          
          {/* Time Summary */}
          <div className="p-4 bg-white rounded-lg shadow">
            <h2 className="text-lg font-medium mb-3">Time Summary</h2>
            <p className="text-gray-600">
              {tasks.length} tasks across {projects.length} projects
            </p>
          </div>
        </div>
      )}
    </div>
  );
};

export default Dashboard;