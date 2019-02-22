"""
    A função principal(main) vai ser responsavel por verificar linha por linha
    do arquivo aberto, onde ele vai separar o user e a hash por dois pontos
    e vai dar um .split(':')[0] para pegar a primeira palavra antes dos dois pontos, e então
    sendo armazenado na variável user.
    Logo após, o cryptPass vai armazenar a senha criptografada, a qual o .split(':')[1] vai pegar a primeira
    frase depois dos dois pontos, e então, retirando os espaços dela com o .strip

    A função testPass vai abrir um dicionário de senhas e fazer a comparação entre elas.
"""

import crypt


def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print("[+] Found Password: "+word+"\n")
            return
    print("[-] Password Not Found.\n")
    return


def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password For: "+user)
            testPass(cryptPass)


if __name__ == "__main__":
    main()