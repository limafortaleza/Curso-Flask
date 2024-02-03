from flask import Flask, render_template, request
app = Flask(__name__) #dander objects __name__ --> nome do módulo atual

#Nome de rota nao se repete
@app.route("/", methods=["GET", "POST"]) #@ é o decorator--> uma função sobre outra função. o"/" significa a página inicial.
@app.route("/index", methods=["GET", "POST"]) #rota alternativa, caso o usuário digite no navegador o nome do site /index.
def index(): #cria o método index para executar o resultado de exibir a página html.
    if request.method =="POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        peso = int(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        resultado= peso/(altura*altura) #calcula aqui e depois joga dentro da função.
        
        # Função para determinar a categoria do IMC
        def calcular_imc(imc):
            if imc <18.5:
                return "Abaixo do peso: IMC menor que 18,5"
            elif 18.5 <= imc < 24.9:
                return "Peso normal: IMC entre 18,5 e 24,9"
            elif 25 <= imc < 29.9:
                return "Sobrepeso: IMC entre 25 e 29,9"
            else:
                return "Obesidade: IMC 30 ou superior"
        
        resultado_final = calcular_imc(resultado) #o resultado final sendo string, recebendo o r esultado da função 

        #o \\n serve para quebrar a linha no alerta
        return f"""
                <script>
                alert("Nome: {nome}\\nIdade: {idade}\\nPeso: {peso}\\nAltura: {altura}\\nResultado final: {resultado_final}");
                window.location.href = '/';
                </script>
        
        """
    #se for o método GET ele faz isso aqui:
    else:
        return render_template ("index.html") #quando clicar em ok ele recarregaa página principal novamente.

@app.route ("/info")
def info():
    nome = request.args.get("nome","Anonimo") #no caso o anonimo so aparece se não for definido o nome.
    idade = request.args.get("idade","indefinido")

    return f"Nome: {nome}, Idade: {idade}"

@app.route("/info2")
@app.route ("/info2/<string:nome>") #caso so informe o nome.
@app.route ("/info2/<int:idade>") #caso so informe a idade.
@app.route ("/info2/<string:nome>/<int:idade>") #no caso se digitar info2 com o nome e idade ele vai para o return
def info2(nome="Anonimo", idade="indefinida"): #caso so digite na barra do navegador a rota info2 ele vai atribuir anonimo ao nome e indefido para a idade.
    return f"Nome: {nome}, Idade: {idade}"

@app.route("/caracteristica", methods=["POST"])
def caracteristica():
     nome=request.form.get('nome')
     idade=request.form.get('idade')
     return f"nome: {nome}, idade :{idade}"

if __name__ == "__main__": #termo de segurança, evita executar o arquivo principal duas vezes.
    app.run(debug=True) #com o debug transforma o console para ver tudo o que acontecendo.