#!/bin/bash
FECHA=$(date +%F)
HORA=$(date +%H-%M)
IP=${1:-"127.0.0.1"}
BASE_DIR="$HOME/mis-primeros-scripts/reportes/$FECHA"
REPORTE="$BASE_DIR/reporte-$HORA.md"
mkdir -p "$BASE_DIR/evidencias"
echo "# Reporte Diario - $FECHA $HORA - Target: $IP" > "$REPORTE"
echo "## Inventario" >> "$REPORTE"
hostnamectl | head -5 >> "$REPORTE"
echo "" >> "$REPORTE"
echo "## Puertos Locales" >> "$REPORTE"
ss -tulnp | head -20 >> "$REPORTE"
echo "" >> "$REPORTE"
echo "## Evidencia nmap" >> "$REPORTE"
nmap -F -T4 --open "$IP" -oN "$BASE_DIR/evidencias/nmap-$HORA.txt" 2>&1 | tail -20 >> "$REPORTE"
echo "" >> "$REPORTE"
echo "[+] Reporte creado en: $REPORTE"
echo "[+] nmap guardado en: $BASE_DIR/evidencias/nmap-$HORA.txt"
# Captura rapida ICMP
ping -c 4 "$IP" > "$BASE_DIR/evidencias/ping-$HORA.txt" 2>&1 &
# auto git
cd "$HOME/mis-primeros-scripts"
git add "reportes/$FECHA" 2>/dev/null
git commit -m "auto reporte $FECHA $HORA - $IP" 2>/dev/null
git push origin main 2>/dev/null

