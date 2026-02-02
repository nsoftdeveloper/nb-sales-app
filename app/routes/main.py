from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from app.models.user import LoginPayload
from app import db
from bson import ObjectId
from app.models.product import *

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def index():
    return jsonify({"mensagen":"Seja bemvindo"})


@main_bp.route('/login', methods=['POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPayload(**raw_data)

    except ValidationError as e:
           return jsonify({"error":e.errors()}), 400
    
    except Exception as e:
           jsonify({"error":"Erro com a execução da app"}), 500

    if user_data.username == 'admin' and user_data.password == '123':
        return jsonify({"mensagen":"Inicio da sessão com sucesso"})
    else:
        return jsonify({"mensagen":"Credenciais não válidas"})
         
@main_bp.route('/products')
def get_products():
    products_cursor = db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True) for product in products_cursor]
    return jsonify(products_list)


@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({"mensagen":"Essa é a página de produto"})


@main_bp.route('/product/<string:product_id>')
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({"mensagen":f"Erro ao transformar o {product_id} em ObjectID: {e}"})
    
    product = db.products.find_one({'_id': oid})
    if product:
        product_model = ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        return jsonify(product_model)
    else:
        return jsonify({"error":f"Produto {product_id} não encontrado"})

# RF-05: O sistema deve permitir a atualizacao de um unico producto e producto existente
@main_bp.route('/product/<int:product_id>',methods=['PUT'])
def update_product_by_id(product_id, ):
    return jsonify({"mensagen":"Esta es la pagina de actualización de producto por id"})

# RF-06: O sistema deve permitir a delecao de um unico producto e producto existente
@main_bp.route('/product/<int:product_id>',methods=['DELETE'])
def delete_product_by_id(product_id, ):
    return jsonify({"mensagen":"Esta es la pagina de delete producto por id"})

# RF-07: O sistema deve permitir a importacao de vendas atraves de um arquivo
@main_bp.route('/sales/upload', methods=['POST'])
def upload_sales():
    return jsonify({"mensagen":"Esta es la pagina de upload de productos"})
