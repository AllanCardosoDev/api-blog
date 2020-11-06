# Explain that there are about 2 big players when it comes to creating elegant apis in python, one is using django, the other is using flask.
# A Opção de usar o django é na minha visão muito mais complexa para quem está iniciado. Então escolhi ensinar flask por que, além de ser muito mais simples de enter, o flask por sí só é considerada uma micro-framework e por isso ele é extremamente leve, rápido e fácil de aplicar, sem muitas depêndencias.
# Então agora entendendo que iremos usar o Flask para construir nosso api, temos 2 vamos chamar de modos diferentes de criar um api dentro do flask
# As duas opções são FLASK comum e FLASK RESTFUL.
# O flask restuful usa um biblioteca extra e na minha opinião e experiência adicona uma nivel de complexidade que pode dificultar muito para quem está iniciando e não consegui encontrar benefícios significativos que justifcasse ensinar usando ele.
# Então iremos usar o flask comum que é infinitamente mais simples de criar e usar.
# vamos lá
# Para começar nós temos que importar algumas funcionalidades de dentro do módulo flask
# Vamos precisa do flask em si
# o método jsonify para processar os dados no formato json que serão usados em nossas apis
# e o módulo request do flask(não cofunda ele com o módulo requets do python, esse request aqui(que inclusive está no singular) é exclusivo do flask
# oo request aqui é útil porque é através dele que você conseguirá acessar os recursos que são passados para a API
from flask import Flask, jsonify, request

# Para inicializar nossa aplicação web flask, temos que usar a seguinte sintaxe
app = Flask(__name__)
# Não se preocupe muito com isso, essa sintaxe está apenas dizendo que o arquivo atual deve executar e rodar um servidor flask
# Então vamos ao passo a passo sobre como criar apis
# Qual é
'''
1- Definir o objetivo da API:
	ex: Iremos montar uma api de blog, onde eu poderei consultar, edit, criar e excluir postagens em um blog usando somente a api(maybe show them devaprender.com)
2 - Qual será o URL base do api?
	ex: Quando você cria uma aplicação local ela terá um url tipo http://localhost:5000 , porém quando você for subir isso para nuvem, você terá que comprar ou usar um domínio como url base, vamos imaginar um exemplo de devaprender.com/api/
3 - Quais são os endpoints?
	ex: Se seu requisito é de pode consultar, editar, criar e excluir, você terá que disponibilizar os endpoints para essas questões
			> /postagens
4 - Quais recursos será disponibilizado pelo api: informações sobre as postagens
5 - Quais verbos http serão disponibilizados?
	* GET
	* POST
	* PUT
	* DELETE
6 - Quais são os URL completos para cada um?
	http://localhost:5000/postagens
'''
postagens = [
    {
        'título': 'Minha história',
        'autor': 'Jhonatan de Souza'
    },
    {
        'título': 'Como Instalar Python',
        'autor': 'Jhonatan de Souza'
    },
    {
        'título': 'Como Instalar Selenium',
        'autor': 'Jhonatan de Souza'
    }
]


# Rota get padrão
@app.route("/")
def obter_todas_postagens():
    return jsonify(postagens)

# Explain how the routing works
# Você deve especificar para como você espera receber os valores
# E obrigatóriamente você precisa passar o mesmo parâmetro que é passado dentro de route,como parâmetro para a função abaixo ou não irá funcionar.


# Obter recurso com parâmetro
@app.route("/postagens/<int:indice>", methods=['GET'])
def obter_postagem(indice):
    # request contem tudo que está vindo da requisição
    return jsonify(postagens[indice], 200)


# Criar novo recurso
@app.route("/postagens", methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    return jsonify({'id': len(postagens)}, 200)


# Editar recurso existente
@app.route("/postagens/<int:indice>", methods=['PUT'])
def atualizar_postagem(indice):
    test = request.get_json()
    postagens[indice].update(test)
    return jsonify(postagens[indice], 200)


# Excluir um recurso
@app.route('/postagens/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    postagem = postagens[indice]
    del postagens[indice]
    return jsonify(f'Foi excluído a postagem {postagem}', 200)


# test
if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
