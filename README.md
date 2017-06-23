create view views as select path, count(*) as views from log where status = '200 OK' and path != '/' group by path order by views DESC;

create view titleview as select author, views from articles join views on views.path like '%' || articles.slug;

create view logview as select date(time), count(log.time), sum(case when log.status = '404 NOT FOUND' then 1 else 0 end) Errors from log group by date;

create view geterrors as select date, round(((errors * 100.0) / count), 2) as percent from logview;
