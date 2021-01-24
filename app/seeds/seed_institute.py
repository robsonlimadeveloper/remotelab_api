"""This module refer institute seed"""

def seeds(model) -> list:
    """This function refer generate institute seeds"""
    institutes = [
        model(id=1, name="RemoteLab Team", description="RemoteLab", code="99.999.999/9999-99",\
             email="remotelab@remotelab.com", phone="(83) 9999-9999", total_hours=100, is_active=True),
        model(id=2, name="Instituto Federal da Paraíba", description="Universidade", code="99.999.999/9999-99",\
             email="ifpb@ifpb.com", phone="(83) 9999-9999", total_hours=100, is_active=True),
        model(id=3, name="Centro Educacional Anna Mazzucchi", description="Escola de ensino fundamental e médio.", code="99.999.999/9999-99",\
             email="ceam@ceam.com", phone="(83) 9999-9999", total_hours=100, is_active=True)
    ]
    return institutes
