#!/bin/bash
echo "=== Par o Impar ==="
read -p "Escribe un número: " num

if [ $((num % 2)) -eq 0 ]; then
    echo "$num es PAR"
else
    echo "$num es IMPAR"
fi

