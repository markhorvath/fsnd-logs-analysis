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
        print('"' + title + '" - ' + str(views) + ' views')
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
    c.execute("select to_char(date, 'fmMonth DD, YYYY') as day, percent from geterrors where percent > 1.0;")
    results = c.fetchall()
    print('\n' + 'Days where more than 1% of requests led to errors:')
    for (day, percent) in results:
        print(str(day) + ' - ' + str(percent) + '% errors')
    db.close()
    
get_top_articles()
get_top_authors()
get_errors()
