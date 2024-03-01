from flask import Blueprint, render_template, request 
from database.cliente import CLIENTES


cliente_route = Blueprint('cliente', __name__)

"""
    - /cliente/ (Get) - listar os clientes
    - /cliente/ (Post) - inserir cliente no servidor
    - /cliente/new (Get) - rederizar o formulario para criar um cliente 
    - /cliente/<id> (Get) - obter os dados de um cliente 
    - /cliente/<id>/edit (Get) - renderizar um formulario para editar um cliente
    - /cliente/<id>/update (PUT) - atualizar os dados do cliente 
    - /cliente/<id>/delete (Delete) - Deleta

"""

@cliente_route.route('/')
def lista_cliente():
  return render_template('lista_cliente.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
 
 
  data = request.json
  
  novo_usuario = {
    "id": len(CLIENTES) + 1, 
    "nome": data['nome'],
    "email": data['email'],
  }
  
  CLIENTES.append(novo_usuario)
  return render_template('item_cliente.html', cliente=novo_usuario )


@cliente_route.route('/new')
def form_cliente():
  return render_template( 'form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
  return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
  
  cliente = None
  for c in CLIENTES:
    if c['id'] == cliente_id:
      cliente = cliente_id
  
  return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
  pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
  global CLIENTES
  CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id]
  
  return {'deleted': 'ok'}
  