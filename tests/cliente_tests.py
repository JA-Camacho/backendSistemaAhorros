# tests/test_cliente_controllers.py

def test_create_cliente():
    """
    Test para la función create_cliente.

    >>> from models.cliente import Cliente
    >>> cliente_data = {"id_cliente": 1, "nombre": "John", "correo_electronico": "john@example.com", "password": "secret"}
    >>> cliente = Cliente(**cliente_data)
    >>> result = create_cliente(cliente)
    >>> "mensaje" in result
    True
    >>> "cliente" in result
    True

    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()