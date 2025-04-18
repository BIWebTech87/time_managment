// src/components/Dashboard.tsx
import { useState, useEffect } from 'react';
import { Project, Task } from '../types';
import { useAuth } from '../context/AuthContext';
import { getProjects } from '../services/projectService';
import { getMyTasks } from '../services/taskService';
import '../styles/Dashboard.css';
import { FiPlus, FiFilter, FiSearch, FiCode, FiEdit, FiEye, 
  FiTrash2, FiInfo, FiMenu, FiX, FiPieChart, FiCheckSquare, 
  FiUsers, FiFolder, FiBriefcase, FiBarChart2 } from 'react-icons/fi';
import { useTranslation } from 'react-i18next';

// Define a type for the recent task display
interface RecentTaskDisplay {
  id: number;
  title: string;
  client: string;
  time: number;
  status: string;
}

const Dashboard = () => {
  const { logout } = useAuth();
  const [projects, setProjects] = useState<Project[]>([]);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [recentTasks, setRecentTasks] = useState<RecentTaskDisplay[]>([]);
  const { t, i18n } = useTranslation();
  
  // Add state for mobile menu
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  
  // Stats summary initialized with zeros
  const [stats, setStats] = useState({
    totalHours: 0,
    activeTasks: 0,
    completedTasks: 0,
    activeProjects: 0
  });

  // Toggle mobile menu
  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };
  
  // Close mobile menu when clicking overlay
  const closeMobileMenu = () => {
    setIsMobileMenuOpen(false);
  };

  const changeLanguage = (lng: string) => {
    i18n.changeLanguage(lng);
  };

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
        
        // Update stats based on actual data (when available)
        if (projectsData.length > 0 || tasksData.length > 0) {
          setStats({
            // Use a safer way to calculate time without relying on specific properties
            totalHours: tasksData.reduce((total, task) => {
              // Use any available time property or fallback to 0
              // Use type assertion to access properties that might not be in the interface
              const taskAny = task as any;
              const timeValue = 
                typeof taskAny.time_spent === 'number' ? taskAny.time_spent :
                typeof taskAny.estimated_time === 'number' ? taskAny.estimated_time :
                typeof taskAny.time === 'number' ? taskAny.time : 0;
              return total + timeValue;
            }, 0),
            
            activeTasks: tasksData.filter(task => {
              const status = String(task.status).toLowerCase();
              return status === 'in_progress' || status === 'active';
            }).length,
            
            completedTasks: tasksData.filter(task => {
              const status = String(task.status).toLowerCase();
              return status === 'completed' || status === 'done';
            }).length,
            
            activeProjects: projectsData.filter(project => {
              // Safely access is_active property
              const projectAny = project as any;
              return Boolean(projectAny.is_active) === true;
            }).length
          });
          
          // Set recent tasks based on actual data
          if (tasksData.length > 0) {
            // Convert backend tasks to RecentTaskDisplay format
            const recentTasksData = tasksData
              .slice(0, 5) // Take up to 5 most recent tasks
              .map(task => {
                const taskAny = task as any;
                return {
                  id: task.id,
                  title: task.title,
                  client: taskAny.project_name || 'Unknown Client',
                  time: taskAny.time_spent || taskAny.estimated_time || 0,
                  status: task.status || 'In Progress'
                };
              });
            
            setRecentTasks(recentTasksData);
          }
        }
        
        setError(null);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('Failed to load data. Please try again.');
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, []);

  return (
    <div className="dashboard-container">
      {/* Header */}
      <header className="dashboard-header">
        <div className="app-title">
          <span className="app-title-icon">🚀</span> WebTech87
        </div>
        <div className="header-actions">
          {/* Language Buttons */}
          <div className="language-buttons">
            <button className="language-button" onClick={() => changeLanguage('en')}>EN</button>
            <button className="language-button" onClick={() => changeLanguage('pt')}>PT</button>
          </div>

          {/* Mobile menu toggle button */}
          <button 
            className="mobile-menu-button" 
            onClick={toggleMobileMenu}
            aria-label="Toggle navigation menu"
          >
            {isMobileMenuOpen ? <FiX /> : <FiMenu />}
          </button>
          
          <button className="logout-button" onClick={logout}>
            {t('logout')}
          </button>
        </div>
      </header>

      {/* Mobile menu overlay */}
      <div 
        className={`sidebar-overlay ${isMobileMenuOpen ? 'show' : ''}`} 
        onClick={closeMobileMenu}
      ></div>

      {/* Main content */}
      <div className="dashboard-content">
        {/* Sidebar - notice the added class for mobile open state */}
        <aside className={`dashboard-sidebar ${isMobileMenuOpen ? 'open' : ''}`}>
          <nav className="sidebar-nav">
          <div className="nav-item active">
  <span className="nav-icon"><FiPieChart /></span> {t('Dashboard')}
</div>
<div className="nav-item">
  <span className="nav-icon"><FiCheckSquare /></span> {t('My Tasks')}
</div>
<div className="nav-item">
  <span className="nav-icon"><FiUsers /></span> {t('My Team')}
</div>
<div className="nav-item">
  <span className="nav-icon"><FiFolder /></span> {t('Projects')}
</div>
<div className="nav-item">
  <span className="nav-icon"><FiBriefcase /></span> {t('Clients')}
</div>
<div className="nav-item">
  <span className="nav-icon"><FiBarChart2 /></span> {t('Reports')}
</div>



          </nav>
        </aside>

        {/* Main panel */}
        <main className="main-panel">
          {error && (
            <div className="error-message">
              {error}
            </div>
          )}

          <div className="panel-header">
            <h1 className="panel-title">{t('Dashboard')}</h1>
            
            <div className="panel-actions">
              <button className="new-task-button">
                <FiPlus className="button-icon" /> {t('newTask')}
              </button>
              
              <button className="filter-button">
                <FiFilter className="button-icon" /> {t('filter')}
              </button>
              
              <div className="search-container">
                <input
                  type="text"
                  placeholder={t('searchTasks')}
                  className="search-input"
                />
                <FiSearch className="search-icon" />
              </div>
            </div>
          </div>

          {loading ? (
            <div className="loading-container">
              <div className="loading-text">{t('loading')}</div>
            </div>
          ) : (
            <>
              {/* Stats Cards */}
              <div className="stats-grid">
                {/* Total Hours */}
                <div className="stat-card">
                  <div className="stat-header">
                    <div>
                      <h3 className="stat-title">{t('totalHours')}</h3>
                      <p className="stat-value">{stats.totalHours}h</p>
                      <p className="stat-subtitle">{t('thisWeek')}</p>
                    </div>
                    <div className="info-icon">
                      <FiInfo />
                    </div>
                  </div>
                </div>

                {/* Active Tasks */}
                <div className="stat-card">
                  <div className="stat-header">
                    <div>
                      <h3 className="stat-title">{t('activeTasks')}</h3>
                      <p className="stat-value">{stats.activeTasks}</p>
                      <p className="stat-subtitle">{t('inProgress')}</p>
                    </div>
                    <div className="list-icon">
                      <FiMenu />
                    </div>
                  </div>
                </div>

                {/* Completed */}
                <div className="stat-card">
                  <div className="stat-header">
                    <div>
                      <h3 className="stat-title">{t('completed')}</h3>
                      <p className="stat-value">{stats.completedTasks}</p>
                      <p className="stat-subtitle">{t('thisMonth')}</p>
                    </div>
                    <div className="info-icon">
                      <FiInfo />
                    </div>
                  </div>
                </div>

                {/* Active Projects */}
                <div className="stat-card">
                  <div className="stat-header">
                    <div>
                      <h3 className="stat-title">{t('activeProjects')}</h3>
                      <p className="stat-value">{stats.activeProjects}</p>
                      <p className="stat-subtitle">{t('currently')}</p>
                    </div>
                    <div className="list-icon">
                      <FiMenu />
                    </div>
                  </div>
                </div>
              </div>

              {/* Recent Tasks */}
              <div className="tasks-card">
                <div className="tasks-header">
                  <h2 className="tasks-title">{t('recentTasks')}</h2>
                </div>

                <div className="tasks-table-container">
                  {recentTasks.length > 0 ? (
                    <table className="tasks-table">
                      <thead>
                        <tr>
                          <th>{t('task')}</th>
                          <th>{t('client')}</th>
                          <th>{t('time')}</th>
                          <th>{t('status')}</th>
                          <th>{t('actions')}</th>
                        </tr>
                      </thead>
                      <tbody>
                        {recentTasks.map((task) => (
                          <tr key={task.id}>
                            <td>
                              <div className="task-name">
                                <span className="task-icon">
                                  {task.title.toLowerCase().includes('frontend') || 
                                   task.title.toLowerCase().includes('development') ? 
                                    <FiCode /> : <FiEdit />}
                                </span>
                                {task.title}
                              </div>
                            </td>
                            <td className="task-client">{task.client}</td>
                            <td className="task-time">{task.time}h</td>
                            <td>
                              <span className={`status-badge ${
                                task.status.toLowerCase().includes('complete') 
                                  ? 'status-completed' 
                                  : 'status-in-progress'
                              }`}>
                                {task.status}
                              </span>
                            </td>
                            <td>
                              <div className="task-actions">
                                <button className="action-button"><FiEye /></button>
                                <button className="action-button"><FiTrash2 /></button>
                              </div>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  ) : (
                    <div className="empty-tasks-message">
                      <p>{t('noRecentTasks')}</p>
                    </div>
                  )}
                </div>
              </div>
            </>
          )}
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
