drop table if exists allstockdata;
create table allstockdata (
    company varchar(10),
    date varchar(20),
    close float,
    primary key (company, date)
)