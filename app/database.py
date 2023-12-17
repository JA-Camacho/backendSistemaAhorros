from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost/ahorros"
database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
metadata.create_all(bind=engine)

clientes = Table(
    "clientes",
    metadata,
    Column("id_cliente", Integer, primary_key=True, index=True),
    Column("nombre", String, index=True),
    Column("correo_electronico", String, index=True),
    Column("password", String, index=True)
)

# Verifica si puedes realizar una consulta simple
async def check_database_connection():
    query = clientes.select().limit(1)
    result = await database.fetch_one(query)
    return result

# Función para insertar un nuevo cliente
async def insert_cliente(nombre, correo, password):
    query = clientes.insert().values(nombre=nombre, correo_electronico=correo, password=password)
    await database.execute(query)

# Función para ejecutar y verificar la conexión a la base de datos
async def run():
    print("Conectando a la base de datos...")
    await database.connect()
    print("Conexión establecida.")

    # Verifica la conexión y realiza una consulta
    result = await check_database_connection()
    print("Resultado de la conexión a la base de datos:", result)

    # Imprime valores específicos de la fila
    if result:
        print("Valores específicos de la fila:")
        print("ID Cliente:", result['id_cliente'])
        print("Nombre:", result['nombre'])
        print("Correo Electrónico:", result['correo_electronico'])
        print("Contraseña:", result['password'])


# Si ejecutas este script, debería imprimir el resultado de la consulta
if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
