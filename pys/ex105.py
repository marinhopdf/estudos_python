def notas(*args, sit=False):
    """
    ESSE PROGRAMA É BARATINAL
    :param args:
    :param sit:
    :return:
    """
    notas = list(args)
    media = sum(notas)/len(notas)
    boletim = {'Quantidade de notas': len(notas),
                'Maior nota': max(notas),
                'Menor nota': min(notas),
                'Média': media,
               }
    if sit:
        boletim.update({'Situação': 'aprovado' if media >= 7 else 'reprovado'})
    print(boletim)

notas(5,8,8,)
help(notas)