#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor: José Reinaldo
# Descrição: Atividade para a disciplina de Introduçãoa Programação.

from random import randint
import os

def banner():
    print("""
            ██ ███████ ██████  ███████ ████████ 
            ██ ██      ██   ██ ██         ██    
            ██ █████   ██████  █████      ██    
            ██ ██      ██   ██ ██         ██    
            ██ ██      ██████  ███████    ██    
    """)

def novo(n1, n2):
    lista = []
    while (len(lista) < 6):
        valor = randint(n1, n2)
        if (contido(valor, lista) == False):
            lista.append(valor)
    return lista

def contido(n, lista):
    if n in lista:
        return True
    else:
        return False

def verificar(l1, l2):
    count = 0
    for i in range(len(l1)):
        if (contido(l1[i], l2) == True):
            count += 1
    return count

def inserir(n, lista):
    if (contido(n, lista) == False):
        lista.append(n)

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')