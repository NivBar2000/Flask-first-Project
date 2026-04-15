from flask import jsonify,Blueprint,current_app
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity

error_bp = Blueprint("errors",__name__)

@error_bp.errorhandler(NotFound)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 404

@error_bp.errorhandler(BadRequest)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 400
    
@error_bp.errorhandler(UnprocessableEntity)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 422