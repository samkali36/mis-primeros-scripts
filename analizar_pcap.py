import os, subprocess
print("🛡️ SOC Report - Buscando evidencias")
for root, dirs, files in os.walk("reportes"):
    for f in files:
        if f.endswith(".pcapng"):
            path = os.path.join(root, f)
            size = os.path.getsize(path)
            print(f"\n - {path} : {size} bytes")
            subprocess.run(f"tshark -r {path} 2>/dev/null | head -3", shell=True)
            subprocess.run(f"tshark -r {path} 2>/dev/null | wc -l | xargs echo '   Paquetes:'", shell=True)
