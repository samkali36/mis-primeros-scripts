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
<img width="810" height="1080" alt="hack3" src="https://github.com/user-attachments/assets/a7c2a9c0-e42a-415f-ae22-c9695e7fb6fa" />
<img width="810" height="1080" alt="hack1" src="https://github.com/user-attachments/assets/9f0df009-e850-4e08-aaac-226026b33ed5" />


<img width="810" height="1080" alt="hack2" src="https://github.com/user-attachments/assets/72693a53-8321-4bde-9b63-79afb3cc6493" />

