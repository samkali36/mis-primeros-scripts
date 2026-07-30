#!/bin/bash
echo "=== MENÚ PRINCIPAL ==="
echo "1) Saludo"
echo "2) Calculadora (suma)"
echo "3) Par o impar"
echo "4) Salir"
read -p "Elige una opción: " opcion

case $opcion in
    1)
        echo "Hola, $USER. Hoy es $(date)"
        ;;
    2)
        read -p "Primer número: " a
        read -p "Segundo número: " b
        echo "Resultado: $((a + b))"
        ;;
    3)
        read -p "Escribe un número: " n
        if [ $((n % 2)) -eq 0 ]; then
            echo "$n es PAR"
        else
            echo "$n es IMPAR"
        fi
        ;;
    4)
        echo "¡Hasta luego!"
        ;;
    *)
        echo "Opción no válida"
        ;;
esac

