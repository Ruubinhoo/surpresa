from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/introducao')
def introducao():
    return render_template('introducao.html')

@app.route('/complexidade')
def complexidade():
    return render_template('complexidade.html')

@app.route('/tempo')
def tempo():
    return render_template('tempo.html')

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

@app.route('/despertar')
def despertar():
    return render_template('despertar.html')

@app.route('/conhecimento')
def conhecimento():
    return render_template('conhecimento.html')

@app.route('/pensamentos')
def pensamentos():
    return render_template('pensamentos.html')

@app.route('/colors')
def colors():
    return render_template('colors.html')

@app.route('/life')
def life():
    return render_template('life.html')

@app.route('/final')
def final():
    return render_template('final.html')

@app.route('/pagina_final', methods=['GET', 'POST'])
def pagina_final():
    if request.method == 'POST':
        senha_digitada = request.form.get('senhaa')
        senha_correta = '1363'  # Substitua pela sua senha correta
        
        if senha_digitada == senha_correta:
            return render_template('pagina_final.html')
        else:
            return redirect(url_for('final'))
    return render_template('pagina_final.html')

if __name__ == '__main__':
    # port = str(os.getenv('PORT'),'8080')
    app.run(host='0.0.0.0', port=8080,debug=True)

    # host='0.0.0.0', port=808
