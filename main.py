from flask import Flask, render_template

app = Flask(__name__) # padrao para criar aplicação com flask

#route ==> meusitecompython.com.br
#função ==> O que você quer exibir na página
#template

@app.route('/') # padrao para cada página criada no site

def homepag():
	return render_template('homepage.html')

@app.route("/contatos")
def contatos():
	return render_template('contatos.html')

#criar paginas de forma dinamica
#1- dentro do link ,colocar a variavel entre <>
# 2- colocar com o mesmo nome ele sendo variavel
# 3 - dentro do render template colocar a variavel = a variavel, repete o mesmo nome.
#4- voce pode usar a variavel dentro do html, colocando ela dentro de duas chaves.
@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
	return render_template('usuarios.html', nome_usuario=nome_usuario)

#colocar o site no ar

if __name__ == "__main__":
	app.run(debug=True)

#fazer deploy do site  no servidor do Heroku