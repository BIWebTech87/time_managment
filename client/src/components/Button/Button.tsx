import React from 'react';
import './Button.css';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> { 
    variant?: 'primary' | 'secondary' | 'outline';
    size?: 'small' | 'medium' | 'large';
    isLoading?: boolean;
}

const Button: React.FC<ButtonProps> = ({ 
    children,
    variant = 'primary',
    size = 'medium',
    isLoading = false,
    ...props 
}) => {
    
    const classes = [
    'button',
    `button--${variant}`, 
    `button--${size}`,
    isLoading ? 'button--loading' : ''
].filter(Boolean).join(' ');

return (
    <button className={classes} disabled={isLoading || props.disabled} {...props}>
{isLoading ? <span className="button__loader" /> : children} 
    </button>
 ); 
};


export default Button;