// src/services/authService.ts
import axios from 'axios';

const API_URL = 'http://localhost:8000/employee';

export const login = async (email: string, password: string) => {
  const response = await axios.post(`${API_URL}/api/token/`, { email, password });
  return response.data;
};

export const refreshToken = async (refresh: string) => {
  const response = await axios.post(`${API_URL}/api/token/refresh/`, { refresh });
  return response.data;
};

export const verifyToken = async (token: string) => {
  const response = await axios.post(`${API_URL}/api/token/verify/`, { token });
  return response.data;
};