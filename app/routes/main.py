from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return jsonify({"mensagen":"Bienvenido"})


@main_bp.route('/products')
def get_products():
    return jsonify({"mensagen":"Pagina de produtos"})


@main_bp.route('/login', methods=['POST'])
def login():
    return jsonify({"mensagen":"Esta es la pagina de login"})