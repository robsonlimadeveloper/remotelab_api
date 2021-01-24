"""This module refer discipline type seed"""

def seeds(model) -> list:
    """This function refer generate discipline types seeds"""
    discipline_type = [
        model(id=1, name="Física", is_active=True),
        model(id=2, name="Química", is_active=True),
        model(id=3, name="Matemática", is_active=True),
        model(id=4, name="Eletrônica", is_active=True),
        model(id=5, name="Programação", is_active=True), 
    ]
    return discipline_type