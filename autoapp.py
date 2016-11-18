# -*- coding: utf-8 -*-
"""Create an application instance."""
import os

from flask.helpers import get_debug_flag

from myflaskapp.app import create_app
from myflaskapp.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

# port = int(os.environ.get('PORT', 5000))
# app.run(host='0.0.0.0', port=port)
