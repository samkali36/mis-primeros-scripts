# Laboratorio 4: File Upload Bypass - DVWA

*Nivel:* Low
*URL:* /vulnerabilities/upload/

### Vulnerabilidad
DVWA no valida extensión. Permite subir archivos .php

### Procedimiento
1. Crear archivo de prueba test.php con un echo de prueba
2. Subir por el formulario de DVWA
3. El servidor lo guarda en /hackable/uploads/
4. Al abrir la URL del archivo, se ejecuta en el servidor

### Evidencia
(espacio para tus 2 fotos del upload)

### Mitigación
Validar por lista blanca jpg/png, validar MIME, renombrar archivo, guardar fuera de web root.
