// src/context/AuthContext.tsx - Updated
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import axiosInstance from '../api/axios';

interface AuthContextType {
  isAuthenticated: boolean;
  loading: boolean;
  user: any | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);
  const [user, setUser] = useState<any | null>(null);

  useEffect(() => {
    // Check if user is already logged in
    const checkAuthStatus = async () => {
      const token = localStorage.getItem('accessToken');
      
      if (token) {
        try {
          // Verify token
          await axiosInstance.post('/employee/api/token/verify/', {
            token
          });
          
          // Get user data if you have an endpoint for it
          // const userResponse = await axiosInstance.get('/api/me/');
          // setUser(userResponse.data);
          
          setIsAuthenticated(true);
        } catch (error) {
          // Token verification failed, handled by axios interceptor
        }
      }
      
      setLoading(false);
    };
    
    checkAuthStatus();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      // Using axios without interceptors for login to avoid circular dependencies
      const response = await axiosInstance.post('/employee/api/token/', {
        email,
        password
      });
      
      localStorage.setItem('accessToken', response.data.access);
      localStorage.setItem('refreshToken', response.data.refresh);
      
      setIsAuthenticated(true);
      
      // Fetch user data if you have an endpoint
      // const userResponse = await axiosInstance.get('/api/me/');
      // setUser(userResponse.data);
      
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  const logout = () => {
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    setIsAuthenticated(false);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};