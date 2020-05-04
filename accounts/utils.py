from random import choice


def create_token(tamanho=10):
    caracters = '0123456789abcdefghijlmnopqrstuwvxz'
    token = ''
    for char in range(0, tamanho):
        token += choice(caracters)

    return token