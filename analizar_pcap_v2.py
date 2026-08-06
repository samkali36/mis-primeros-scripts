import os
from pathlib import Path
for pcap in Path("reportes").rglob("*.pcapng"):
    size = pcap.stat().st_size
    # tshark con -q para no fallar sin sudo
    import subprocess
    result = subprocess.run(f"capinfos {pcap} 2>/dev/null | grep 'Number of packets'", shell=True, capture_output=True, text=True)
    print(f"📦 {pcap.name}: {size} bytes -> {result.stdout.strip()}")
    # Muestra los ICMP
    subprocess.run(f"tshark -r {pcap} -Y icmp 2>/dev/null | head -5", shell=True)
