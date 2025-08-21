import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const codespaceName = process.env.REACT_APP_CODESPACE_NAME || window.location.hostname.split('-')[0];
const protocol = window.location.protocol;
const port = window.location.port || '8000';
const REACT_APP_CODESPACE_URL = `${protocol}//${codespaceName}-8000.app.github.dev`;
process.env.REACT_APP_CODESPACE_URL = REACT_APP_CODESPACE_URL;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
