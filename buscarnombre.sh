#!/bin/bash
amigos=("Samuel" "Ana" "Carlos" "Maria" "Luis")

echo "=== Buscar en la lista de amigos ==="
echo "Lista actual: ${amigos[@]}"
read -p "¿Qué nombre quieres buscar? " buscado

encontrado=0
for nombre in "${amigos[@]}"
do
    if [ "${nombre,,}" == "${buscado,,}" ]; then
        encontrado=1
    fi
done

if [ $encontrado -eq 1 ]; then
    echo "$buscado SÍ está en la lista"
else
    echo "$buscado NO está en la lista"
fi

