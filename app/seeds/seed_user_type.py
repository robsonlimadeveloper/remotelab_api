"""This module refer user_type seed"""

def seeds(model) -> list:
    """This function refer generate user_type seeds"""
    user_types = [
        model(id=1, name="Administrador", is_active=1),
        model(id=2, name="Professor", is_active=1),
        model(id=3, name="Estudante", is_active=1),
        model(id=4, name="Gestor", is_active=1),
        model(id=5, name="Monitor", is_active=1)
    ]
    return user_types
