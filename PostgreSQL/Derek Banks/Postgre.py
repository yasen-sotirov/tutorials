"PGADMIN"   # Най-добрият курс!!
    # https://www.youtube.com/watch?v=85pG_pDkITY&ab_channel=DerekBanas
    # https://github.com/derekbanas/postgresql-tutorial/blob/main/PostgreSQL%20Tutorial.txt


"СВЪРЗВАНЕ С ПИТОН"     # https://www.youtube.com/watch?v=miEFm1CyjfM&ab_channel=NeuralNine
import psycopg2
conn = psycopg2.connect(host='localhost',
                        dbname='sales_db_2',
                        user='postgres',
                        password='Tur6ia',
                        port=5432)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person(
    id SERIAL PRIMARY KEY,
    name VARCHAR(256),
    age INT,
    gander CHAR);
""")

cur.execute("""INSERT INTO person (name, age, gander) VALUES
('Mike', '44', 'M'),
('John', '25', 'M'),
('Bob', '18', 'M'),
('Lisa', '33', 'F'); 
""")

cur.execute("""SELECT * FROM person WHERE age > 20;""")

for row in cur.fetchall():
    print(row)



# затваряне на връзката
conn.commit()
cur.close()
conn.close()

'''


ФУНКЦИИ SQL
    CREATE OR REPLACE FUNCTION fn_get_last_order()
    RETURNS sales_order as 
    $body$
        SELECT *
        FROM sales_order
        ORDER BY time_order_taken DESC
        LIMIT 1;
    $body$
    LANGUAGE SQL
    
    SELECT fn_get_last_order();		    връща на един ред

    SELECT (fn_get_last_order()).*;		връща в табличен вид



ФУНКЦИИ PL/PG
    CREATE OR REPLACE FUNCTION fn_get_product_price(product_name varchar)
    RETURNS numeric AS 
    $body$
    BEGIN
        RETURN item.price
        FROM item
        NATURAL JOIN product
        WHERE product.name = product_name;
    END
    $body$
    LANGUAGE plpgsql

SELECT fn_get_product_price('Grandview')


AUTOINCREMENT SERIAL KEY
     id SERIAL PRIMARY KEY


CHARACTER TYPES
    TRUE - 1, t, y, yes, on
    FALSE - 0, f, n, no, off
    
    DATA TIME
    1 D 1 H 1 M 1 S:: INTERVAL -> 01:01:01:01

    current_timestamp - дава часа на създаване на записа


SELF JOIN
    https://www.youtube.com/watch?v=Wi3Q_aNLZsY&list=PL0hSJrxggIQrz5OKtnaFuPiyMDTXUF5J1&index=24&ab_channel=AnalyticsExcellence
    SELECT tableA.col, tableB.col
    FROM employee AS tableA
    JOIN employee AS tableB ON
    tableA.some_col = tableB.other_col
        

ДЕБЪГВАНЕ НА ФУНКЦИИ
    https://www.youtube.com/watch?v=wYyUjmnsbT4&list=PLownlFUq_rL6iJF0hiSXKT0cnIAtBgHoX&index=2&ab_channel=EDB
    
    
    

'''