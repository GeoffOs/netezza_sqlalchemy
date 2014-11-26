__version__ = '0.1.8'

from sqlalchemy.dialects import registry

#registry.register("netezza", "sqlalchemy_netezza.pyodbc", "NetezzaDialect")
#registry.register("netezza.pyodbc", "sqlalchemy_netezza.pyodbc", "NetezzaDialect")

registry.register("netezza", "netezza_dialect", "NetezzaODBC")
registry.register("netezza.pyodbc", "netezza_dialect", "NetezzaODBC")