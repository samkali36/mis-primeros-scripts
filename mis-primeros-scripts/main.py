from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import sqlite3

app = FastAPI(
    title="API Mi Gas La De Pesquería",
    description="Sistema de pedidos, clientes y atención automatizada",
    version="1.1.0"
)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
PRECIOS = {
    "5kg": 110.0,
    "10kg": 220.0,
    "20kg": 440.0,
    "30kg": 660.0,
"45kg": 990.0,
}

# Crear base de datos al iniciar
def iniciar_db():
    conn = sqlite3.connect("negocio.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT UNIQUE NOT NULL,
        direccion TEXT
    )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        tipo_gas TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        total REAL NOT NULL,
        estado TEXT DEFAULT 'pendiente',
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )''')
    conn.commit()
    conn.close()

iniciar_db()

# Modelos de datos
class PedidoCalculo(BaseModel):
    tipo_gas: str
    cantidad: int
    descuento: float = 0.0

class DatosCliente(BaseModel):
    nombre: str
    telefono: str
    direccion: str

class DatosPedido(BaseModel):
    telefono_cliente: str
    tipo_gas: str
    cantidad: int
    descuento: float = 0.0

# --- ENDPOINTS ---
@app.get("/estado")
def raiz():
    return {"empresa":"Mi Gas La De Pesquería","estado":"Activo ✅","fecha":datetime.now().strftime("%d/%m/%Y %H:%M")}

@app.get("/precios")
def lista_precios():
    return PRECIOS

@app.post("/calcular")
def calcular_pedido(datos: PedidoCalculo):
    if datos.tipo_gas not in PRECIOS:
        raise HTTPException(400, "Tipo de gas no disponible")
    if datos.cantidad <= 0:
        raise HTTPException(400, "Cantidad inválida")
    subtotal = PRECIOS[datos.tipo_gas] * datos.cantidad
    total = subtotal * (1 - datos.descuento/100)
    return {
        "tipo": datos.tipo_gas, "cantidad": datos.cantidad,
        "subtotal": round(subtotal,2), "descuento": f"{datos.descuento}%",
        "total": round(total,2)
    }

@app.post("/clientes/nuevo")
def agregar_cliente(cliente: DatosCliente):
    try:
        conn = sqlite3.connect("negocio.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO clientes VALUES (NULL,?,?,?)",
                    (cliente.nombre, cliente.telefono, cliente.direccion))
        conn.commit()
        return {"ok":True,"mensaje":"Cliente registrado"}
    except sqlite3.IntegrityError:
        raise HTTPException(400,"Teléfono ya existe")
    finally: conn.close()

@app.get("/clientes/lista")
def ver_clientes():
    conn = sqlite3.connect("negocio.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    res = [{"id":r[0],"nombre":r[1],"telefono":r[2],"direccion":r[3]} for r in cur.fetchall()]
    conn.close()
    return {"clientes":res}

@app.post("/pedidos/nuevo")
def registrar_pedido(ped: DatosPedido):
    conn = sqlite3.connect("negocio.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM clientes WHERE telefono = ?", (ped.telefono_cliente,))
    cli = cur.fetchone()
    if not cli:
        raise HTTPException(404,"Cliente no registrado")
    if ped.tipo_gas not in PRECIOS or ped.cantidad <=0:
        raise HTTPException(400,"Datos de pedido inválidos")
    total = PRECIOS[ped.tipo_gas] * ped.cantidad * (1 - ped.descuento/100)
    cur.execute('''INSERT INTO pedidos VALUES (NULL,?,?,?,?,'pendiente',CURRENT_TIMESTAMP)''',
                (cli[0], ped.tipo_gas, ped.cantidad, round(total,2)))
    conn.commit()
    conn.close()
    return {"ok":True,"mensaje":"Pedido registrado ✅","total":round(total,2)}

@app.get("/pedidos/lista")
def ver_pedidos():
    try:
        conn = sqlite3.connect("negocio.db")
        cur = conn.cursor()
        cur.execute("""
            SELECT p.id, c.nombre, c.telefono, p.tipo_gas, p.cantidad, p.total, p.estado, p.fecha
            FROM pedidos p
            LEFT JOIN clientes c ON p.cliente_id = c.id
            ORDER BY p.fecha DESC
        """)
        pedidos = []
        for fila in cur.fetchall():
            pedidos.append({
                "id": fila[0],
                "nombre_cliente": fila[1] if fila[1] else "Sin cliente",
                "telefono": fila[2] if fila[2] else "Sin teléfono",
                "tipo_gas": fila[3],
                "cantidad": fila[4],
                "total": fila[5],
                "estado": fila[6],
                "fecha": fila[7]
            })
        conn.close()
        return {"pedidos": pedidos}
    except Exception as e:
        return {"error": str(e)}
