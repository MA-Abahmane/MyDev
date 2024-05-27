create database test;
use test;

create table Products (	
	ProductID varchar(100) primary key,
	ProductName varchar(70),
	CategoryID INT,	
    Price FLOAT
);

create table Categorys (	
	CategoryID INT primary key,
    CategoryName varchar(70),
    `Description` varchar(200)
);

alter table Products 
add constraint productCategorys foreign key(CategoryID) references Categorys(CategoryID);

insert into Categorys values
(1,	'Beverages',	'Soft drinks, coffees, teas, beers, and ales'),
(2,	'Condiments',	'Sweet and savory sauces, relishes, spreads, and seasonings'),
(7,	'Condiments',	'Sweet and savory sauces, relishes, spreads, and seasonings, ...'),
(3,	'Confections',	'Desserts, candies, and sweet breads');

insert into Products values
(1,	'Chais',	1,	18),
(2,	'Chang',	1,	19),
(3,	'Aniseed Syrup',	2,	10),
(5,	'jibi soramint',	2,	10);

SET SQL_SAFE_UPDATES = 0;

update Products
set CategoryID = null
where ProductID = 5;


select * from Products p 
inner join Categorys c on p.CategoryID = c.CategoryID;

select p.ProductID, p.ProductName, c.CategoryID from Products p
left join Categorys c using(CategoryID);

select p.ProductID, p.ProductName, c.CategoryID, c.CategoryName from Products p
cross join Categorys c; 
