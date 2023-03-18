import pymysql


def connect_mysql(host,port,user,password,db):
    connection = pymysql.connect(host=host,
                                 port=port,
                                 user=user,
                                 password=password,
                                 db=db)
    return connection

def create_cursor(conn):
    cursor = conn.cursor()
    return cursor





def crete_data(conn,cursor,sql):
    sql = sql
    cursor.execute(sql)
    conn.commit()



def query(cursor,sql):
    sql = sql
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows


def delte_data(conn,cursor,sql):
    sql = sql
    cursor.execute(sql)
    conn.commit()


def updata(conn,cursor,sql):
    sql = sql
    cursor.execute(sql)
    conn.commit()

def close(conn,cursor):
    cursor.close()
    conn.close()





if __name__ == '__main__':
    # Connect to the database
    conn=connect_mysql(host="8.130.34.50",port=3306,user="root",password="my-secret-pw",db="travel_web")

    # Create a cursor object
    cursor = create_cursor(conn)






