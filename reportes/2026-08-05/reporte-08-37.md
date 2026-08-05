# Reporte Diario - 2026-08-05 08-37 - Target: 127.0.0.1
## Inventario
 Static hostname: ICV-IDSAM
       Icon name: computer-container
         Chassis: container 📦
      Machine ID: 6da0a50d55634aad86608a90087ef75e
         Boot ID: 21de61d382864b0ca3b3da50f6d8b88f

## Puertos locales
Netid State  Recv-Q Send-Q  Local Address:Port  Peer Address:PortProcess
udp   UNCONN 0      0      10.255.255.254:53         0.0.0.0:*   
udp   UNCONN 0      0           127.0.0.1:323        0.0.0.0:*   
udp   UNCONN 0      0               [::1]:323           [::]:*   
tcp   LISTEN 0      4096        127.0.0.1:41019      0.0.0.0:*   
tcp   LISTEN 0      1000   10.255.255.254:53         0.0.0.0:*   
## Hallazgos
- [OK] Localhost responde
- [INFO] Aprendi a crear scripts y guardar evidencia con nmap -oN
## Hallazgos
- [OK] localhost 127.0.0.1 responde - 1 host up
- [INFO] Puertos locales revisados con ss -tulnp
- [LEARN] Aprendi a usar mkdir -p, cat >, chmod +x y guardar evidencia con -oN

## Siguiente paso
- Escanear mi red local con nmap -sn 192.168.1.0/24
