from models import Cuenta_Ahorro

def create_cuenta(cuenta: Cuenta_Ahorro):
    # Lógica para crear una cuenta de ahorro
    return {"mensaje": "Cuenta creada exitosamente", "cuenta": cuenta}