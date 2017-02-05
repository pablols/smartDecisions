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


api_key = 'c55e4cc78fed9752274056a24a5bbbf7'
user_auth_token = 'aa7121a7a8cc263c91752c949055901e599890f463a592cb05d878fca47262e7'

organisation = 'smartdecisions1' #'588d095968a1972b407f2d5c'
board_id = '588d0bb61aae1a8635b2bd5d'
list_id = ''
card_id = ''
checklist_id = ''
member_id = ''

def getBoards():
    try:
        client=Client(api_key, user_auth_token)
        org=Organisation(client, organisation)
        for board in org.get_boards():
            print 'Proyecto: ', board.name
            print 'Esclavos: '
            for esclavo in board.get_members():
                print '          -', esclavo.name
            print '  '
    except:
        print 'error, plsss revisa tus inputs flojo qliao'

def getCards(board_id=None):
    if board_id:
        try:
            client=Client(api_key, user_auth_token)
            board=trolly.board.Board(client,board_id)
            print 'Tareas y sus responsbles'
            for card in board.get_cards():
                print 'Tarae: ', card.name
                print 'Esclavos :'
                for esclavo in card.get_members():
                    print '       -',esclavo.name
                print '¿Tarea Terminada? ', card.get_card_information()['dueComplete']
                print '              '
        except:
            print 'error, plsss revisa tus inputs flojo qliao'
    else:
        print 'ingresa un board_id'
        
print ' ------------ Proyectos ------------'          
getBoards()
print ''
print ' ------------ Tareas del Proyecto Tierra ------------'
getCards(board_id)
