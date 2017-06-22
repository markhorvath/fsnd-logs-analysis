#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:47:00 2017

@author: markhorvath
"""

import psycopg2

DBNAME = "news"

def get_top_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articles.title, views.views from articles join views on views.path like '%' || articles.slug limit 3;")
    results = c.fetchall()
    print('\n' + 'The top 3 most viewed articles are:')
    for (title, views) in results:
        print('"' + title + '" - ' + str(views))
    db.close()
    
def get_top_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name, sum(views) from authors, titleview where authors.id = titleview.author group by authors.name order by sum DESC;")
    results =  c.fetchall()
    print('\n' + 'The most popular authors of all time are:')
    for (name, sum) in results:
        print(name + ' - ' + str(sum) + ' views')
    db.close()
    
def get_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select time::timestamp::date, count(log.time) as num from log where status != '200 OK' group by time::timestamp::date limit 10;")
    results = c.fetchall()
    print(results)
    db.close()
    
get_top_articles()
get_top_authors()