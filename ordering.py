import mysql.connector


# def insertProduct(name, proce, imageurl, description):

# def insertProducts(list):

def getProducts():
    connection = mysql.connector.connect(host="localhost", user="root", password="Cihan0156", database="node-app")
    cursor = connection.cursor()

    cursor.execute("Select * From Products Order By name, price")
    #cursor.execute("Select name,price  From Products;")
    try:
        result = cursor.fetchall()
        for product in result:
            print(f'id: {product[0]} name:{product[1]} price:{product[2]}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database baglantisi kapandi.')

    #result = cursor.fetchone()

    #print(f'name: {result[0]} price:{result[1]}')
    #for product in result:
        #print(f'id: {product[0]} name:{product[1]} price:{product[2]}')
    # print(f'name: {product[0]} price:{product[1]}')

    #print(f'name: {result[1]} price:{result[2]}')

'''def getProductById(id):
    connection = mysql.connector.connect(host="localhost", user="root", password="Cihan0156", database="node-app")
    cursor = connection.cursor()
    sql = "Select * From Products Where id=%s"
    params =(id,)
    cursor.execute(sql, params)
    #cursor.execute("Select name,price  From Products;")

    #result = cursor.fetchone()
    result = cursor.fetchone()

    #print(f'name: {result[0]} price:{result[1]}')
    #for product in result:
        #print(f'id: {product[0]} name:{product[1]} price:{product[2]}')
    # print(f'name: {product[0]} price:{product[1]}')

    print(f'name: {result[1]} price:{result[2]}')'''

getProducts()
#getProductById(4)














###