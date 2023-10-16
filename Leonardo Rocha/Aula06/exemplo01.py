contato = {
    "Nome" : "Leleo", 
    "Telefone" : 123456,
    "Email" : "leo@leo"
}

print (contato["Nome"])

contato["endereço"] = "Rua ao Infinito e Além"

print (contato)

valor = contato["Nome"]

print (valor)

contato['Nome']= "Mário"

print (contato["Nome"])

if 'endereço' in contato:
    print ("Achei")

else:
    print ("Tem não")

    for Nome in contato.items():
        print(contato["Nome"])