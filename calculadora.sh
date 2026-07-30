#!/bin/bash
echo "=== Calculadora simple ==="
read -p "Escribe el primer número: " num1
read -p "Escribe el segundo número: " num2

suma=$((num1 + num2))
resta=$((num1 - num2))
multiplicacion=$((num1 * num2))

echo "Suma: $suma"
echo "Resta: $resta"
echo "Multiplicación: $multiplicacion"

