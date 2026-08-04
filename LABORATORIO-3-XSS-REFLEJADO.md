# Laboratorio 3: XSS Reflejado (Cross Site Scripting)

*Plataforma:* DVWA - Damn Vulnerable Web App  
*URL:* http://localhost:8080/vulnerabilities/xss_r/  
*Nivel:* Low

### Vulnerabilidad
Reflected XSS - El servidor refleja sin sanitizar el parámetro name.

### Payloads probados
```html
<script>alert('XSS by Sam')</script>
<img width="810" height="1080" alt="kali 2" src="https://github.com/user-attachments/assets/9f8e91b4-dbb6-4335-a2f2-2767ea55827f" />
<img width="810" height="1080" alt="kali" src="https://github.com/user-attachments/assets/da089559-bd7a-4936-8642-ee5e4ddbb04e" />
