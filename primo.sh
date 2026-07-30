#!/bin/bash

es_primo() {
    n=$1
    if [ $n -lt 2 ]; then
        return 1
    fi
    for ((i=2; i<n; i++)); do
        if [ $((n % i)) -eq 0 ]; then
            return 1
        fi
    done
    return 0
}

echo "=== Verificar número primo ==="
read -p "Escribe un número: " numero

if es_primo $numero; then
    echo "$numero ES primo"
else
    echo "$numero NO es primo"
fi

