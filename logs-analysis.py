#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:47:00 2017

@author: markhorvath
"""
import sys
import psycopg2

DBNAME = "news"

def connect(database_name):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        sys.exit(1)

def get_query_results(query):
    db, c = connect(DBNAME)
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

def get_top_articles():
    results = get_query_results("""select articles.title, views.views
                  from articles
                  join views on views.path like '%' || articles.slug limit 3;
                  """)
    print('\n' + 'The top 3 most viewed articles are:')
    for (title, views) in results:
        print('"' + title + '" - ' + str(views) + ' views')

def get_top_authors():
    results = get_query_results("""select authors.name, sum(views)
                 from authors, titleview
                 where authors.id = titleview.author
                 group by authors.name
                 order by sum DESC;
                 """)
    print('\n' + 'The most popular authors of all time are:')
    for (name, sum) in results:
        print(name + ' - ' + str(sum) + ' views')

def get_top_error_days():
    results = get_query_results("""select to_char(date, 'fmMonth DD, YYYY') as day, percent
                 from geterrors
                 where percent > 1.0;
                 """)
    print('\n' + 'Days where more than 1% of requests led to errors:')
    for (day, percent) in results:
        print(str(day) + ' - ' + str(percent) + '% errors')

if __name__ == '__main__':
    get_top_articles()
    get_top_authors()
    get_top_error_days()
