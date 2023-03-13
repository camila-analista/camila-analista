qnt_rodas=int(input("Quantas rodas tem o veículo? "))
peso=float(input("Qual o Peso Bruto do veículo(kg)? "))
qnt_pessoas=int(input("Quantas pessoas cabe no veículo? "))

if qnt_rodas>=4 and qnt_pessoas>8 and peso>6000:
    print("Categoria D")
elif peso>3500 and peso<6000:
    print("Categoria C")
elif qnt_rodas==4 and qnt_pessoas<8 and peso<3500:
    print("Categoria B")
elif qnt_rodas<3:
    print("Categoria A")

   
