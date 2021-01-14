"""Routes module."""
import importlib
import traceback
from types import ModuleType
from flask import jsonify
from app import app
from app.modules import get_named_modules

for named_module in get_named_modules():
    
    try:
        module: ModuleType = importlib.import_module(
            f'.modules.{named_module}.views', package='app')
        app.register_blueprint(getattr(module, 'blueprint'))
    except ModuleNotFoundError as exception:
        print("error")
        pass
    except Exception as exception:
        print(traceback.format_exc())
        pass

@app.route("/api")
def index():
    """api index base"""
    link_serializable = []
    links = app.url_map.iter_rules()
    for link in links:
        link_serializable.append(str(f"{link} {link.methods}"))
        
    return jsonify(Rotas=link_serializable)
