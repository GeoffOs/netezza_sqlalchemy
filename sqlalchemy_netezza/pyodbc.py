# access/pyodbc.py
# Copyright (C) 2005-2012 the SQLAlchemy authors and contributors <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from .base import NetezzaExecutionContext, NetezzaODBC
from sqlalchemy.connectors.pyodbc import PyODBCConnector
from sqlalchemy import types as sqltypes, util


class NetezzaExecutionContext_pyodbc(NetezzaExecutionContext):
    pass

class NetezzaODBC_pyodbc(PyODBCConnector, NetezzaODBC):

    #execution_ctx_cls = AccessExecutionContext_pyodbc

    pyodbc_driver_name = 'Netezza ODBC'

    colspecs = util.update_copy(
        NetezzaODBC.colspecs
    )