# -*- coding: utf-8 -*-

from twython import Twython
from keys import *
import time
import random

twitter = Twython(app_key,app_secret,oauth_token,oauth_secret)

while True:
    palabroide = ''     #palabroide is a made up name for a made up word
    pre = ['pr','tr','cr','cl','pl','tl','br','qui','que','gl','gr','bl','br',
            'll','rr','ch','z','x','c','v','b','n','m','s','d','f','g','h','j',
            'k','l','w','r','t','y','p','ñ']
    vocales = 'aeuio'
    preoVocal = 0
    largo = random.randint(3,10)
    started = False
    cuentaVocales = 0

    for i in xrange(largo):

        if not started:
            #comenzar palabra
            palabroide += pre[random.randint(0,len(pre) - 1)]
            started = True

        elif preoVocal == 1:
            palabroide += pre[random.randint(0,len(pre) - 1)]
            preoVocal = 0

        else:
            #aqui vocales
            
            if cuentaVocales < 1:
                palabroide += vocales[random.randint(0,len(vocales)-1)]
                cuentaVocales += 1
                preoVocal = random.randint(0,1)

            else:
                palabroide += vocales[random.randint(0,len(vocales)-1)]
                preoVocal = 1
                cuentaVocales = 0

    if palabroide[len(palabroide) - 1] in pre:
        palabroide += vocales[random.randint(0,len(vocales)-1)]


    # print palabroide
    twitter.update_status(status = palabroide)

    time.sleep(3600)        #3600 es una hora, 300 son 5 mins