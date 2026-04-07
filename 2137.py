
while True:
    try:
        livros = []

        n =int(input())

        for i in range(n):
           livro = input()
           livros.append(livro)

        livros.sort()
        for j in range(n):
            print (livros[j])

    except EOFError:
        break