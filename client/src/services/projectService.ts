// src/services/projectService.ts
import axiosInstance from '../api/axios';

export interface Project {
  id: number;
  name: string;
  description: string;
  client: string;
  is_active: boolean;
  created_at: string;
  // Add other fields as needed
}

export const getProjects = async (): Promise<Project[]> => {
  const response = await axiosInstance.get('/projects/api/projects/');
  return response.data;
};

export const getProjectById = async (id: number): Promise<Project> => {
  const response = await axiosInstance.get(`/projects/api/projects/${id}/`);
  return response.data;
};

export const getProjectTasks = async (id: number): Promise<any[]> => {
  const response = await axiosInstance.get(`/projects/api/projects/${id}/tasks/`);
  return response.data;
};

export const createProject = async (projectData: Partial<Project>): Promise<Project> => {
  const response = await axiosInstance.post('/projects/api/projects/', projectData);
  return response.data;
};

export const updateProject = async (id: number, projectData: Partial<Project>): Promise<Project> => {
  const response = await axiosInstance.put(`/projects/api/projects/${id}/`, projectData);
  return response.data;
};

export const deleteProject = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/projects/api/projects/${id}/`);
};