# Logs Analysis Project for Udacity FSND
#### A project using PostgreSQL and Python to query a database for a hypothetical newspaper website.  Program outputs the most popular articles and authors according to the number of views they receive, as well as any dates where more than 1% of HTTP requests led to errors.  IMPORTANT: Program requires vagrant and virtual machine which can be found here: https://github.com/markhorvath/FSND-Virtual-Machine/tree/master/vagrant and the required database "newsdata.sql" here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip.  Unzip the "newsdata.sql" file and place in your vagrant directory.

## TO THE REVIEWER
#### Assuming you've already got vagrant up and entered "vagrant ssh", cd to the /vagrant folder and enter the following commands

1. psql news  (this will access the "news" database found in newsdata.sql)

2. create view views as select path, count(*) as views from log where status = '200 OK' and path != '/' group by path order by views DESC;

3. create view titleview as select author, views from articles join views on views.path like '%' || articles.slug;

4. create view logview as select date(time), count(log.time), sum(case when log.status = '404 NOT FOUND' then 1 else 0 end) Errors from log group by date;

5. create view geterrors as select date, round(((errors * 100.0) / count), 2) as percent from logview;

#### After these are created, you should be able to simply run "python logs-analysis.py" and it should output the expected data.
