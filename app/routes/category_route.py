from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from app.models.category import Category

category_bp = Blueprint('category_bp', __name__)


@category_bp.route('/categories')
def get_categories():
    return jsonify({"categories": "Pagina de categorias"})

@category_bp.route('/categories/<int:category_id>')
def get_categories_by_id(category_id):
    return jsonify({"category": f"category id {category_id}"})

@category_bp.route('/categories', methods=['POST'])
def create_category():
    try:
        raw_data = request.get_json()
        category_data = Category(**raw_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": "Error en la aplicación de category"}), 500
    
    return jsonify({"category": f"{category_data.category}"})

@category_bp.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    return jsonify({"categories": f"Atualizando categoria {category_id}"})

@category_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    return jsonify({"categories": f"Apagando categoria {category_id}"})