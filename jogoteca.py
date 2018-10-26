from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'alura'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


lista = []


@app.route('/jogos')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/jogos')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/jogos')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')





app.run(debug=True)
