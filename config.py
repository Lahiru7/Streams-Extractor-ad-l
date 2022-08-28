#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5361152021:AAGI3di5NlIf1wbb4fcOD3ptBpD9eCdxl8A")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "15816329"))
    API_HASH = os.environ.get("API_HASH", "e57f831ef1d71f707ce63d2f4db35abc")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1178035103 1671626669 1472904517 1495867737 1840565374 1361764484 1837756549 1495867737 1619444244 1875917672 1619444244 1356300848 1837756549").split())
    
