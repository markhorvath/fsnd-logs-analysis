create view views as select path, count(*) as views from log where status = '200 OK' and path != '/' group by path order by views DESC;

create view titleview as select author, views from articles join views on views.path like '%' || articles.slug;
