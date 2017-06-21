#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:47:00 2017

@author: markhorvath
"""

import datetime, psycopg2, bleach

DBNAME = "news"

def get_top_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('select author from articles;')
    return c.fetchall()
    db.close()
    
    
get_top_articles()
