#Faça um programa que converta da notação de 24 horas para a notação de 12 horas.\
#Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois\
#inteiros, sendo eles horas e minutos. Deve haver pelo menos duas funções: uma para\
#fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor\
#‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um\
#parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário\
#repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def hrs24_to_hrs12(horas, min):
    if horas > 23 or min > 59:
        print("valor invalido de hrs e min")

    else:
        if horas < 12:
            return horas, min, "A"
        else:
            n_hrs = horas-12
            return n_hrs, min, "P"
op = "s"
while op == "s":
    hrs = int(input("Informe as hrs: "))
    min = int(input("Informe os min: "))
    result = hrs24_to_hrs12(hrs, min)
    print(result)
    if result is not None:
        print(f"A hr {hrs}:{min} ficaram {result[0]}:{result[1]} {result[2]}M")
    op = input("s para continuar ")