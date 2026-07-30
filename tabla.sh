#!/bin/bash
echo "=== Tabla de multiplicar ==="
read -p "¿De qué número quieres la tabla? " num

for i in 1 2 3 4 5 6 7 8 9 10
do
    resultado=$((num * i))
    echo "$num x $i = $resultado"
done

