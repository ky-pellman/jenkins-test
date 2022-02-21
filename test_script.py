#!/usr/bin/env python

#import postgres module
import psycopg2
#import sys library to interact with shell
import sys

def main(customer_id):
    """

    :param: customer_id is passed as a str via jenkins (shell)
    The main(function) will determine if the argument is a number.
    It will then either return an exception or call connnect() with a sanitized and converted int.
    """
    if customer_id.isnumeric():
        connect(int(customer_id.strip()))
    else:
        print("please provide a valid number")

def connect(customer_id):
    """

    :param: customer_id is passed as a sanitized int
    + Connect to the database using fixed credentials
    + Execute the sql statement
    + Commit the changes to the database
    """
    #establishes a connection instance to the database
    try:
        conn = psycopg2.connect(dbname = 'kyle', user = 'postgres')
    except psycopg2.Error as err:
        raise err.pgerror
    
    #establishes a cursor instance that enables execution of commands
    cur = conn.cursor()

    #query to use
    sql1 = "UPDATE customer SET status = 'Approved' WHERE customer_id = %s;"

    #exeutes query
    try:
        cur.execute(sql1, (customer_id,))
    except psycopg2.Error as err:
        raise err.pgerror

    #commit the changes to the database for persistence
    conn.commit()

    #close the cursor instance
    cur.close()

    #close the connection instance
    conn.close()

#initializes the script
if __name__ == "__main__":
    main(sys.argv[1])
