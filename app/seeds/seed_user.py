"""This module refer user seed"""

def seeds(model) -> list:
    """This function refer generate user seeds"""
    users = [
        model(id=1, name="Administrador", username="admin", password="1234", email="admin@admin.com"),
        model(id=2, name="Robson Soares", username="robson.soares", password="1234", email="robsonlimadeveloper@gmail.com"),
        model(id=3, name="Ronilson", username="ronilson.lima", password="1234", email="ronilson.lima@hotmail.com")
    ]
    return users
