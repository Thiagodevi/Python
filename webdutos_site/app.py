from flask import Flask, render_template

app = Flask(__name__)

funcionarios = {
    "dani": {
        "nome": "Dani",
        "cargo": "Líder N1",
        "descricao": "Responsável pela liderança da equipe de suporte N1."
    },
    "yasel": {
        "nome": "Yasel",
        "cargo": "Suporte N1",
        "descricao": "Atendimento e suporte técnico aos clientes."
    },
    "thiago": {
        "nome": "Thiago",
        "cargo": "Suporte N1",
        "descricao": "Especialista em resolução de chamados."
    },
    "murilo": {
        "nome": "Murilo",
        "cargo": "Suporte N1",
        "descricao": "Atendimento técnico e suporte remoto."
    },
    "ana": {
        "nome": "Ana",
        "cargo": "Suporte N1",
        "descricao": "Suporte ao cliente e análise de incidentes."
    }
}

@app.route("/")
def home():
    return render_template("index.html", funcionarios=funcionarios)

@app.route("/perfil/<nome>")
def perfil(nome):
    funcionario = funcionarios.get(nome)
    if funcionario:
        return render_template("perfil.html", funcionario=funcionario)
    else:
        return "<h1>Funcionário não encontrado</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)