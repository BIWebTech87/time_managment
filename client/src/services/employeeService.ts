// src/services/employeeService.ts
import axiosInstance from '../api/axios';

export const getEmployees = async () => {
  const response = await axiosInstance.get('/employees/employees_list/');
  return response.data;
};

export const getEmployeeById = async (id: number) => {
  const response = await axiosInstance.get(`/employees/${id}/`);
  return response.data;
};

export const createEmployee = async (employeeData: any) => {
  const response = await axiosInstance.post('/employees/add_new_employee/', employeeData);
  return response.data;
};

export const updateEmployee = async (id: number, employeeData: any) => {
  const response = await axiosInstance.post(`/employees/${id}/`, employeeData);
  return response.data;
};

export const deleteEmployee = async (id: number, email: string) => {
  const response = await axiosInstance.post(`/employees/${id}/`, {
    action: 'delete',
    email
  });
  return response.data;
};