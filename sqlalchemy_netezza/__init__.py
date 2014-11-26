__version__ = '0.1'

from sqlalchemy.dialects import registry

registry.register("netezza", "sqlalchemy_netezza.pyodbc", "NetezzaDialect_pyodbc")
registry.register("netezza.pyodbc", "sqlalchemy_netezza.pyodbc", "NetezzaDialect_pyodbc")