"""This module refer user seed"""

def seeds(model) -> list:
    """This function refer generate user seeds"""
    users = [
        model(id=1, name="Administrador", username="admin", password="1234", email="admin@admin.com",\
             phone="(83) 99999-9999", is_active=True, date_of_birth="2017-06-15", total_hours=10),
        model(id=2, name="Crismaikon Lins", username="crismaikon.lins", password="1234", email="crismaikon@remotelab.com",\
             phone="(83) 99999-9999", is_active=True, date_of_birth="2017-06-15", total_hours=10),
        model(id=3, name="Robson Soares", username="robson.soares", password="1234", email="robsonlimadeveloper@gmail.com",\
             phone="(83) 99999-9999", is_active=True, date_of_birth="1989-04-20", total_hours=10),
        model(id=4, name="Francisco Fechine", username="francisco.fechine", password="1234", email="fechine@remotelab.com",\
             phone="(83) 99999-9999", is_active=True, date_of_birth="2017-06-15", total_hours=10)
        
    ]
    return users
