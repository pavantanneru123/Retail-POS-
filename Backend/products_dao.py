from sql_connection import getSQLConnection

def getAllProducts():
    cursor = connection.cursor()
    query = "SELECT product_id, product_name, products.uom_id, uom_name, price_per_unit from products inner join uom on products.uom_id=uom.uom_id"
    cursor.execute(query)
    for (product_id, product_name, uom_id, uom_nmae, price_per_unit) in cursor:
        print((product_id, product_name, uom_id, uom_nmae, price_per_unit))
    connection.close()


def insertNewProducts():
    product_name = input("What is the name of the product? ")
    uom_id = int(input("What is the uom_id? "))
    price_per_unit = float(input("What is the price in INR? "))

    cursor = connection.cursor()
    query = "INSERT INTO products (product_name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
    cursor.execute(query, (product_name, uom_id, price_per_unit))
    connection.commit()  # Commit the transaction
    print("Product added successfully.")


def deleteProduct():
    product_id = input("What is the product_id? ")
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id=%s"
    cursor.execute(query, (product_id,))
    connection.commit()
    print("Product deleted successfully.")
    cursor.close()


if __name__== "__main__":
    connection=getSQLConnection()
