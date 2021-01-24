"""This module refer experiment seed"""

def seeds(model) -> list:
    """This function refer generate user seeds"""
    experiment = [
        model(id=1, title="Experimento Teste", description="Experimento de teste usando Arduino UNO",\
            url_socket_server="http://45.233.12.76:5010/", url_stream_server="http://45.233.12.76:8000/stream.mjpeg",\
                 is_active=True)
        
    ]
    return experiment
