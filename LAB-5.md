# LAB 5 - File Inclusion (LFI) y Command Injection

## Objetivo
Demostrar lectura de archivos sensibles y ejecución de comandos remotos por falta de validación de entrada.

## Herramientas
- DVWA Low Security
- Kali Linux

## Parte 1: LFI
*Payload:* ?page=/etc/passwd
*Resultado:* El servidor mostró el contenido de /etc/passwd con usuarios del sistema (root, www-data, etc.)
*Impacto:* Un atacante puede leer archivos críticos del sistema, credenciales, código fuente.

*Evidencia:* lfi_etc_passwd.png - Muestra root:x:0:0...

## Parte 2: Command Injection
*Payload:* 127.0.0.1; whoami
*Resultado:* Además del ping, se ejecutó whoami y devolvió www-data
*Impacto:* Remote Code Execution (RCE) - El atacante ejecuta cualquier comando como usuario del servidor.

*Evidencia:* command_injection_www-data.png

## Mitigación
- LFI: Lista blanca de archivos permitidos, deshabilitar allow_url_include, sanitizar ../
- Command Injection: Validar entrada con regex (solo IPs), usar APIs seguras, no usar exec() con input de usuario.

## Autor
Sam Esparza - 2026<img width="810" height="1080" alt="hack62026" src="https://github.com/user-attachments/assets/a17804d4-3ead-4840-ae48-cea4e28e48a1" />
<img width="1912" height="1137" alt="hack 5 2026" src="https://github.com/user-attachments/assets/b0f4fd94-a798-4e56-8a24-a5784d9a32d7" />
