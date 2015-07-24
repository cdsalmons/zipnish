from flask import Blueprint

api = Blueprint('api', __name__)

#
# end-points to create

# query
from . import query

# services
from . import services

# spans
from . import spans

# annotations
from . import annotations

# dependencies
from . import dependencies

#
# traces
# services
# annotations

# pin
from . import pin
