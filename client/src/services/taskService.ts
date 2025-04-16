// src/services/taskService.ts
import axiosInstance from '../api/axios';

export interface Task {
  id: number;
  title: string;
  description: string;
  priority: string;
  status: string;
  project: number;
  assigned_to: number;
  created_at: string;
  redline: string; // Due date
  final_time: string;
  estimated_time: number;
  assigned_to_details?: any; // Will contain employee details
}

export interface CreateTaskDto {
  title: string;
  description: string;
  priority: string;
  status: string;
  project: number;
  assigned_to: number;
  redline?: string; // Optional due date
  estimated_time?: number;
}

// Get all tasks
export const getTasks = async (): Promise<Task[]> => {
  const response = await axiosInstance.get('/projects/api/tasks/');
  return response.data;
};

// Get tasks assigned to current user
export const getMyTasks = async (): Promise<Task[]> => {
  const response = await axiosInstance.get('/projects/api/tasks/my_tasks/');
  return response.data;
};

// Get a single task by ID
export const getTaskById = async (id: number): Promise<Task> => {
  const response = await axiosInstance.get(`/projects/api/tasks/${id}/`);
  return response.data;
};

// Create a new task
export const createTask = async (taskData: CreateTaskDto): Promise<Task> => {
  const response = await axiosInstance.post('/projects/api/tasks/', taskData);
  return response.data;
};

// Update an existing task
export const updateTask = async (id: number, taskData: Partial<CreateTaskDto>): Promise<Task> => {
  const response = await axiosInstance.put(`/projects/api/tasks/${id}/`, taskData);
  return response.data;
};

// Delete a task
export const deleteTask = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/projects/api/tasks/${id}/`);
};