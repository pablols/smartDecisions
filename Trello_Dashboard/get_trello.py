import numpy as np 
import trolly

import unittest
import uuid

from trolly.client import Client
from trolly.organisation import Organisation
from trolly.board import Board
from trolly.list import List
from trolly.card import Card
from trolly.checklist import Checklist
from trolly.member import Member
from trolly import ResourceUnavailable

#Pablo recuerda comentar tus codigos !
#Editado y subido command line por GIT

# la api_key y user_auth_token son obtenidos en Trello y son unicos por usuario, 
# estas son como las contraseñas de la API de trello.
# Ambos valores son ocupados por la libreria para conectarse a la API
api_key = 'c55e4cc78fed9752274056a24a5bbbf7'
user_auth_token = 'aa7121a7a8cc263c91752c949055901e599890f463a592cb05d878fca47262e7'

# definimos la Organisacion a la cual leeremos, en este caso es nuestra organizacion en Trello
organisation = 'smartdecisions1' #'588d095968a1972b407f2d5c'
# El board_id corresppnde al ID de algun proyecto que deseemos revisar
board_id = '588d0bb61aae1a8635b2bd5d'


#Con esta funcion , obtenemos los proyectos y sus responsables, recibe como input la organisation, 
# dejaremos como default nuestra organizacion.
def getBoards(organisation='smartdecisions1'):
    try:
       client=Client(api_key, user_auth_token)
       org=Organisation(client, organisation)
       for board in org.get_boards():
           print 'Proyecto: ', board.name
           print 'Responsables: '
           for responsable in board.get_members():
               print '          -', responsable.name
               print '  '
    except:
        print 'error, plsss revisa tus inputs flojo qliao'
#con esta funcion obtenemos todos los proyectos, sus reponsables y estado de avance. recibe como input el board_id
def getCards(board_id='588d0bb61aae1a8635b2bd5d'):
    try:
        client=Client(api_key, user_auth_token)
        board=trolly.board.Board(client,board_id)
        print 'Tareas y sus responsbles'
        for card in board.get_cards():
            print 'Tarae: ', card.name
            print 'Responsables :'
            for responsable in card.get_members():
                print '       -',responsable.name
            print '¿Tarea Terminada? ', card.get_card_information()['dueComplete']
            print ''
            print ''
    except:
        print 'error, plsss revisa tus inputs flojo qliao'
        
print ' ------------ Proyectos ------------'          
getBoards()
print ''
print ' ------------ Tareas del Proyecto Tierra ------------'
getCards()
