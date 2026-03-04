from flask import Flask, render_template

app = Flask(__name__)

# Descrição do setor
descricao_setor = """
O Suporte Técnico N1 da Webdutos é responsável pelo primeiro atendimento ao cliente,
tratamento de chamados, diagnóstico inicial de incidentes e garantia de SLA.
A equipe atua com foco em agilidade, qualidade e excelência no atendimento.
"""

# Funcionários da equipe
funcionarios = {
    "dani": {
        "nome": "Dani",
        "cargo": "Líder N1",
        "descricao": "Lidera a equipe de suporte, garantindo cumprimento de SLA, organização de demandas e qualidade no atendimento técnico.",
        "foto": "dani.jpg"
    },
    "yasel": {
        "nome": "Yasel",
        "cargo": "Analista de Suporte N1",
        "descricao": "Responsável pelo atendimento inicial ao cliente, registro de chamados e resolução de incidentes de baixa e média complexidade.",
        "foto": "yasel.jpg"
    },
    "thiago": {
        "nome": "Thiago",
        "cargo": "Analista de Suporte N1",
        "descricao": "Especialista em troubleshooting técnico, análise de erros sistêmicos e suporte remoto ao usuário final.",
        "foto": "thiago.jpg"
    },
    "murilo": {
        "nome": "Murilo",
        "cargo": "Analista de Suporte N1",
        "descricao": "Atua no suporte técnico operacional, validação de incidentes e acompanhamento de chamados escalonados.",
        "foto": "murilo.jpg"
    },
    "ana": {
        "nome": "Ana",
        "cargo": "Analista de Suporte N1",
        "descricao": "Responsável pela triagem de solicitações, suporte ao cliente e monitoramento de indicadores de atendimento.",
        "foto": "ana.jpg"
    }
}

# Página inicial
@app.route("/")
def home():
    return render_template("index.html", 
                           funcionarios=funcionarios,
                           descricao_setor=descricao_setor)

# Página de perfil individual
@app.route("/perfil/<nome>")
def perfil(nome):
    funcionario = funcionarios.get(nome)
    if funcionario:
        return render_template("perfil.html", funcionario=funcionario)
    else:
        return "<h1>Funcionário não encontrado</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)