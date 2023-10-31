drop table if exists stockdata;
create table stockdata (
    company varchar(10),
    date varchar(20),
    close float,
    primary key (company, date)
)