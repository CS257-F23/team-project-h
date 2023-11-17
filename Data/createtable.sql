drop table if exists allstockdata;
create table allstockdata (
    company varchar(10),
    date date,
    close float,
    primary key (company, date)
)