// src/types/index.ts

export interface Project {
    id: number;
    name: string;
    description: string;
    client: string;
    is_active: boolean;
    created_at: string;
    // Add other project fields as needed
  }
  
  export interface Task {
    id: number;
    title: string;
    description: string;
    priority: string;
    status: string;
    project: number;
    assigned_to: number;
    created_at: string;
    redline?: string; // Due date
    final_time?: string;
    estimated_time?: number;
    time_spent?: number; // Add this property
  }
  
  export interface Employee {
    id: number;
    first_name: string;
    last_name: string;
    email: string;
    role: string;
    // Add other employee fields as needed
  }