#with abre e fecha automaticamente
#para criar um arquivo colocar o with open( "NOME DO ARQUIVO".TXT, A,encoding="UTF-8") as arq.
# (a) Continua escrevendo sem tirar oque ja estava, o (w) Escreve em cima 
#arquivos com acento dao problema, para resolver colocar: enconding(UTF8)
#(r) pega o conteudo do arquivo
#para o (r) funcionar e ncessario criar uma variavel
#para ler a variavel, precisa colocar VARIAVEL=arq.read()
try:
    with open("tested.txt","r",encoding="UTF-8") as arq:
        cont=arq.read()
        print(cont)
except FileNotFoundError:
    print("NAO TEM NADA")
