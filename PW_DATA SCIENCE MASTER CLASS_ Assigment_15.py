#!/usr/bin/env python
# coding: utf-8

# # Assignment _16-02-2023
# 

# ## 1. What is Database ? Different between SQL and NoSQL databases.
# 
# ### Ans:-
#     
#         A database is an organized collection of data that can be easily accessed, managed, and updated. It can store
#         information about people, products, transactions, or any other type of data that needs to be managed by an 
#         can be added and modified without requiring a predefined schema.Databases are designed to provide a reliable and
#         efficient way to store and retrieve data. They can be used to support various applications such as web applications,   
#         enterprise resource planning (ERP) systems, customer relationship management (CRM) systems, and many others.
#  
#                           SQL                                                            NoSQL
#         1. SQL databases are based on the relational data model,         1.NoSQL databases, on the other hand,use different 
#            which means that data is stored in tables with predefined       data models, such as document-based, key-Value or
#            columns and relationships between them.                         or graph-based, and can be more flexible in 
#                                                                            handling unstructured data.  
#         2. SQL databases have a predefined schema, which defines the     2.NoSQL databases are schema-less,meaning that data 
#            structure of the database and the typesof data that can be      can be added and modified without requiring a  
#            stored in each column.                                          predefined schema.
#         3. SQL databases are typically vertically scalable               3.NoSQL databases are designed to be horizontally
#            which means that you can increasethe performance                scalable, which means that you can add more 
#            of the database by upgrading the hardware (e.g. adding          servers to increase performance and capacity.
#            more memory or CPU). 
#         4. SQL databases use SQL (Structured Query Language)             3.NoSQL databases use different query languages, 
#            to interact with the database and retrieve data.                depending on the type of database.For example,
#                                                                            MongoDB (a document-based NoSQL database) 
#                                                                            uses a query language called MongoDB Query
#                                                                            Language (MQL).
#         5. SQL databases are generally ACID compliant,                   4.NoSQL databases may or may not be ACID compliant 
#            meaning that they provide consistency,                          depending on the database type and the specific 
#            isolation, durability, and atomicity in transactions.           implementation.
#                                
#                                Overall, the choice between SQL and NoSQL databases depends on the specific needs of the 
#            application or project. SQL databases are often a good fit for applications with structured data and strict 
#            requirements for data consistency, while NoSQL databases are better suited for applications with unstructured
#            data and a need for scalability and flexibility.

# # 2. What is DDL ? Explain why CREATE,DROP,ALTER and TRUNCATE are used with example.
# 
# ### Ans:-
#     DDL stands for Data Definition Language, which is a set of SQL (Structured Query Language) commands used to define and 
#     manage the structure of a database. DDL commands are used to create, modify, and delete database objects such as tables,
#     indexes, views, and constraints.
#     
#                                     CREATE, DROP, ALTER, and TRUNCATE are all SQL Data Definition Language (DDL) commands 
#     used to create, modify, and delete database objects. Here's an explanation of each command with examples:
#     
#     1. CREATE :-
#                 The CREATE command is used to create a new database object, such as a table, index, view, or procedure.
#        Here's an example of how to create a new table named "users" with columns for "id", "name", and "email":
#        
#                    CREAT_TABLE users(
#                    id INT PRIMARY KEY
#                    name VARCHAR2(255) NOT NULL
#                    email VARCHAR2(255) NOT NULL
#                    );
#     2. DROP :-
#               The DROP command is used to delete an existing database object, such as a table, index, view, or procedure. 
#        Here's an example of how to drop a table named "users":
#               
#                   DROP TABLE users;
#                   
#                This command will delete the "users" table from the database and all its associated data.   
#                   
#     3. ALTER :-
#               The ALTER command is used to modify the structure of an existing database object, such as adding, renaming
#        or dropping columns in a table. Here's an example of how to add a new column named "phone" to the "users" table:
#        
#                 ALTER TABLE users ADD phone VARCHAR (20);
#              This command will add a new column named "phone" to the "users" table.
#                 
#     4. TRUNCATE :-
#                 The TRUNCATE command is used to delete all the data in a table, while keeping the table structure intact. 
#        Here's an example of how to truncate the "users" table:
#                
#                TRUNCATE TABLE  users;
#                
#                This command will delete all the data in the "users" table, but the table structure and column definitions 
#        will remain intact.
# 

# ## 3. What is DML? Explain INSERT,UPDATE, and DELETE with an Example.
# 
# ### Ans:-
# 
#         DML stands for Data Manipulation Language, which is a set of SQL commands used to manipulate data stored in a 
#         database. DML commands are used to insert, update, and delete data from database tables. Here's an explanation
#         of each command with examples:
# 
#         1. INSERT :-
#                 The INSERT command is used to add new rows of data to a database table. Here's an example of how to insert 
#            a new record into a table named "customers":
#            
#    INSERT INTO customers(name,email,phone) Values('Manas Ranjan Pandey','pandey.manasranjan@gmail.com','9826470741')
#            
#            This command will insert a new record into the "customers" table with the specified values 
#            for the "name", "email", and "phone" columns.
#            
#         2. UPDATE :-
#                 The UPDATE command is used to modify existing data in a database table. Here's an example of how to update a 
#            record in a table named "customers" where the "id" column equals 1:
#            
#            UPDATE customers
#            SET email = 'pandey_manasranjan@yahoo.com'
#            WHERE id = 1;
#            
#         3. DELETE :-
#                 The DELETE command is used to remove one or more records from a database table. Here's an example of how to
#            delete a record from a table named "customers" where the "id" column equals 2:
#            
#            DELETE FROM customers
#            WHERE id =2;
#            
#                                            Overall, DML commands are essential for manipulating data stored in a database, 
#            and are commonly used in applications that require frequent interaction with a database. 
#                
#                 

# ## 4. What is DQL ? Explain SELECT with an example.
# 
# ### Ans:-
# 
#         DQL stands for Data Query Language, which is a set of SQL commands used to retrieve data from a database. 
#         DQL commands are used to perform queries on database tables to retrieve specific data based on certain conditions.
#         Here's an explanation of one of the most commonly used DQL commands:
#         
#         
#         1. SELECT :-
#                 The SELECT command is used to retrieve data from one or more tables in a database. 
#        Here's an example of how to use the SELECT command to retrieve all columns and rows from a table named "customers":
#        
#                SELECT * from customers;
#                       [This command will retrieve all the data in the "customers" table, including all columns and rows.]
#                
#                You can also specify which columns you want to retrieve by listing them after the SELECT keyword, separated
#        by commas. For example, if you only want to retrieve the "name" and "email" columns from the "customers" table, 
#        you would use the following command:
#        
#                SELECT name,email FROM customers;
#                
#                SELECT * FROM customers
#                WHERE name = 'manas'
#                
#                Overall, the SELECT command is an essential tool for retrieving data from a database, and is commonly 
#         used in applications that require frequent access to database data. By using this command, developers and database
#         administrators can retrieve specific data based on a wide range of criteria, allowing them to build more powerful
#         and efficient applications.
#         
#         
# 

# ## 5. Explain Primary key and Foreign key.
# 
# ### Ans:-
# 
#         In a relational database, a primary key and a foreign key are two important concepts used to establish relationships
#         between tables.
#         
#         
#         1.Primary Key:-
#                   A primary key is a column or a set of columns in a table that uniquely identifies each row in that table.
#           The primary key is used to enforce data integrity and ensure that each row in the table is unique. The primary key
#           must be unique, not null, and immutable.
#           
#           For example, in a table named "customers", the primary key may be the "customer_id" column. This ensures that each
#           customer in the table is uniquely identified by their customer ID, and that no two customers have the same ID.
#         
#       2.Foreign Key:-
#                 A foreign key is a column or a set of columns in a table that references the primary key of another table. 
#          The foreign key establishes a link between two tables, allowing data to be related across tables.
#          
#          For example, in a table named "orders", there may be a foreign key column named "customer_id" that references the 
#          primary key column "customer_id" in the "customers" table. This links the orders in the "orders" table to the 
#         customers in the "customers" table, allowing us to retrieve information about orders and their associated customers.
#          
#          
#           
#           
# 

# ## 6. Write a Python code to connect mySQL to python . Explain the cursor()and execute()method.
# 
# ### Ans:-

# ## 7.Give the order of execution of SQL clauses in a SQL query.
# 
# ### Ans:-
# 
#         The order of execution of clauses in a SQL query typically follows the following sequence:
# 
#         1.FROM clause: This clause specifies the tables from which the data will be retrieved.
#         2.WHERE clause: This clause filters the data based on specified conditions.
#         3.GROUP BY clause: This clause groups the data based on specified columns.
#         4.HAVING clause: This clause filters the grouped data based on specified conditions.
#         5.SELECT clause: This clause specifies the columns to be retrieved.
#         6.ORDER BY clause: This clause sorts the result set based on specified columns.
#         7.LIMIT/OFFSET clause: This clause limits the number of rows returned by the query and specifies the starting row
#         to return when using OFFSET.
#                                     It is important to note that not all SQL queries will include all of these clauses and
#         that some clauses, such as WHERE and GROUP BY, may be omitted if they are not necessary for the specific query being
#         executed. Additionally, some SQL dialects may vary slightly in the exact order of execution of clauses, but the
#         general sequence outlined above is common to most SQL implementations.
# 
# 
