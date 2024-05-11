# Es un palindromo

def isPalindromo(txtEntrada):
    j = len(txtEntrada) - 1
    var = "False"
    for i in txtEntrada:
        if( i == txtEntrada[j] ):
            var = "True"
            return var
        j = j - 1
        
    return var
     

txtEntrada = input()

print(isPalindromo(txtEntrada))