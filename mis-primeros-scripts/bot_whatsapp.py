import requests

API_URL = "https://mi-gas-la-de-pesqueria.onrender.com"

def procesar_pedido(telefono, tipo_gas, cantidad, descuento=0):
    respuesta = requests.post(f"{API_URL}/calcular", json={
        "tipo_gas": tipo_gas,
        "cantidad": cantidad,
        "descuento": descuento
    })
    if respuesta.status_code != 200:
        return f"❌ Error: {respuesta.json().get('detail')}"
    
    datos = respuesta.json()

    guardado = requests.post(f"{API_URL}/pedidos/nuevo", json={
        "telefono_cliente": telefono,
        "tipo_gas": tipo_gas,
        "cantidad": cantidad,
        "descuento": descuento
    }).json()

    return f"""
✅ *Mi Gas La De Pesquería* — Pedido Confirmado
────────────────────────────────────
📦 Producto: {cantidad} × {tipo_gas}
💰 Subtotal: ${datos['subtotal']} MXN
🏷️ Descuento: {datos['descuento']}
💵 Total a pagar: *${datos['total']} MXN*
────────────────────────────────────
📝 Estado: {guardado.get('mensaje', 'Pendiente')}
📞 Te contactaremos para coordinar entrega.
¡Gracias por tu preferencia!
"""

# Línea corregida (doble guion bajo en cada lado)
if __name__ == "__main__":
    resultado = procesar_pedido("8117980922", "20kg", 2, 5)
    print("\n" + resultado + "\n")

