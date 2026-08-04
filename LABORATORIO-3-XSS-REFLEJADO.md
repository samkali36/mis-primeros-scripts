# Laboratorio 3: XSS Reflejado (Cross Site Scripting)

*Plataforma:* DVWA - Damn Vulnerable Web App  
*URL:* http://localhost:8080/vulnerabilities/xss_r/  
*Nivel:* Low

### Vulnerabilidad
Reflected XSS - El servidor refleja sin sanitizar el parámetro name.

### Payloads probados
```html
<script>alert('XSS by Sam')</script>
