#!/bin/bash
FECHA=$(date +%F)
HORA=$(date +%H-%M)
IP=${1:-"127.0.0.1"}
BASE_DIR="$HOME/mis-primeros-scripts/reportes/$FECHA"
REPORTE="$BASE_DIR/reporte-$HORA.md"
mkdir -p "$BASE_DIR/evidencias"

echo "# Reporte Diario - $FECHA $HORA - Target: $IP" > "$REPORTE"
echo "## Puertos" >> "$REPORTE"
nmap -F -T4 --open "$IP" -oN "$BASE_DIR/evidencias/nmap-$HORA.txt" 2>&1 | tail -20 >> "$REPORTE"

echo "## Captura" >> "$REPORTE"
# Captura con sudo para que SI cree el pcapng
sudo timeout 8 tshark -i any -f "host $IP" -w "$BASE_DIR/evidencias/captura-$HORA.pcapng" 2>/dev/null &
sleep 1
ping -c 4 "$IP" > "$BASE_DIR/evidencias/ping-$HORA.txt" 2>&1
wait
# si tshark falló, creamos un pcap con tcpdump como respaldo
if [ ! -s "$BASE_DIR/evidencias/captura-$HORA.pcapng" ]; then
  sudo timeout 8 tcpdump -i any host "$IP" -w "$BASE_DIR/evidencias/captura-$HORA.pcapng" 2>/dev/null &
  sleep 1
  ping -c 4 "$IP" >> "$BASE_DIR/evidencias/ping-$HORA.txt" 2>&1
  wait
fi

ls -lh "$BASE_DIR/evidencias/" >> "$REPORTE"
echo "[+] Reporte $HORA listo"

cd "$HOME/mis-primeros-scripts"
sudo chown -R samuel:samuel "reportes/$FECHA"
git add "reportes/$FECHA" 2>/dev/null
git commit -m "auto $FECHA $HORA - $IP con pcap" 2>/dev/null
git push origin main 2>/dev/null
