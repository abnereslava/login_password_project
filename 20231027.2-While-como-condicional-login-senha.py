login = input("Escolha seu login: ")
print("Login criado com êxito.\n")
senha = input("Escolha sua senha: ")
print("Senha criada com êxito.\n")
inputedlogin = "qqrcoisa"
inputedsenha = "qqrcoisa2"

print("Voltando à tela inicial. \n ... \nVocê está na tela inicial. \n")

while inputedlogin != login or inputedsenha != senha:
    inputedlogin = input("Insira seu login: ")
    inputedsenha = input("Insira sua senha: ")
    
    if inputedlogin != login or inputedsenha != senha:
      print("Login ou senha incorreta. Tente de novo!\n")
    
print("Você está logado.")
print(f"Bem-vindo {login}!")