# 🛡️ SOC Automatizado - De 0 a evidencias forenses

Sistema automatizado en WSL2 que cada dia a las 8am recolecta evidencias de red.

### Flujo automatico (cron)
0 8 * * * daily.sh 8.8.8.8

1. nmap -F -T4 escaneo rapido
2. tshark/tcpdump captura real .pcapng (984 bytes ICMP)
3. Genera reporte.md + .txt + .pcapng
4. git push automatico

### Evidencia real
