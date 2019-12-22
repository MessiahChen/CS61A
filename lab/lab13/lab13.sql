.read data.sql

-- QUESTIONS --



-------------------------------------------------------------------------
------------------------ Give Interest- ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
update accounts set amount = amount*1.02;


create table give_interest_result as select * from accounts; -- just for tests

-------------------------------------------------------------------------
------------------------ Split Accounts ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
create table temp as
  select name||"'s Checking account" as name, amount*0.5 as amount from accounts UNION
  select name||"'s Savings account"          , amount*0.5           from accounts;
delete from accounts;
insert into accounts select * from temp;



create table split_account_results as select * from accounts; -- just for tests

-------------------------------------------------------------------------
-------------------------------- Whoops ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
drop table accounts;


CREATE TABLE average_prices AS
  SELECT category as category, AVG(MSRP) as average_price from products GROUP By category;

CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) from inventory GROUP By item;

CREATE TABLE shopping_list AS
  SELECT name,store from products as p, lowest_prices as l
  where p.name = l.item
  group by category having min(MSRP/rating);

CREATE TABLE total_bandwidth AS
  SELECT sum(distinct s.mbs) from stores as s, shopping_list as sl
  where s.store = sl.store;
