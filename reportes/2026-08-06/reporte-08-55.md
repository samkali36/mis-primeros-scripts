# Reporte Diario - 2026-08-06 08-55 - Target: 8.8.8.8
## Inventario
 Static hostname: ICV-IDSAM
       Icon name: computer-container
         Chassis: container 📦
      Machine ID: 6da0a50d55634aad86608a90087ef75e
         Boot ID: 22803049c6d749f7b8f994a694ce49ec

## Puertos Locales
Netid State  Recv-Q Send-Q  Local Address:Port  Peer Address:PortProcess
udp   UNCONN 0      0      10.255.255.254:53         0.0.0.0:*   
udp   UNCONN 0      0           127.0.0.1:323        0.0.0.0:*   
udp   UNCONN 0      0             0.0.0.0:5353       0.0.0.0:*   
udp   UNCONN 0      0               [::1]:323           [::]:*   
udp   UNCONN 0      0                [::]:5353          [::]:*   
tcp   LISTEN 0      1000   10.255.255.254:53         0.0.0.0:*   
tcp   LISTEN 0      4096        127.0.0.1:33041      0.0.0.0:*   

## Evidencia nmap
Starting Nmap 7.99 ( https://nmap.org ) at 2026-08-06 08:55 -0600
Nmap scan report for dns.google (8.8.8.8)
Host is up (0.031s latency).
Not shown: 95 filtered tcp ports (no-response), 1 closed tcp port (reset)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE
53/tcp   open  domain
443/tcp  open  https
2000/tcp open  cisco-sccp
5060/tcp open  sip

Nmap done: 1 IP address (1 host up) scanned in 2.28 seconds

