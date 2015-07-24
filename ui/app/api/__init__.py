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

#
# traces
# services
# annotations
# dependencies

# pin
from . import pin
