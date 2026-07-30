#!/bin/bash
echo "=== Revisando números del 1 al 10 ==="

for num in 1 2 3 4 5 6 7 8 9 10
do
    if [ $((num % 2)) -eq 0 ]; then
        echo "$num es PAR"
    else
        echo "$num es IMPAR"
    fi
done

