#off white #d6d6d6
#grey #373737 #333333 
#blue #0071e3 #2c86fa #3b91ff

import mysql.connector
import tkinter
import datetime

def product_mgmt( ):
    while True:
        print("\n\t\t\t     PRODUCT MANAGEMENT")
        print("\t\t\t  ************************")
        print("\n\t\t 1. Add New Product")
        print("\t\t 2. View Products")
        print("\t\t 3. Update Product")
        print("\t\t 4. Delete Product")
        print("\t\t 5. Back (Main Menu)")
        c=int(input("\n\t\t Enter Your Choice: "))
        if c==1:
            add_product()
        elif c==2:
            view_products()
        elif c==3:
            update_product()
        elif c==4:
            delete_product()
        elif c== 5:
            break
        else:
            print("\n\t\t ERROR: Invalid Input.")
            print("\t\t Enter from the numbers given in the menu only.")
            print("\t\t Please Try Again :/ \n")


def add_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t     ADD NEW PRODUCT")
    print("\t\t\t\t  *********************")
    
    pcode=int(input("\n\t\t\t Enter Product Code: "))
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        name=input("\t\t\t Enter Product Name: ")
        price=float(input("\t\t\t Enter Product Unit Price: "))
        qty=int(input("\t\t\t Enter Product Quantity: "))
        cat=input("\t\t\t Enter Product Category: ")
        print("\n\t\t\t You can always update the product details later.")
        confirm=input("""\n\t\t\t Enter "YES" to confirm the above product details: """)
        if confirm=="YES" or confirm=="yes" or confirm=="Yes":
            val=(pcode,name,price,qty,cat)
            sql="INSERT INTO products(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
            mycursor.execute(sql,val)
            mydb.commit()
            print("\n\t\t\t Product Details Added Successfully.")
        else:
            print("\t\t\t Action Revoked. :/")
    else:
        print("\n\t\t\t ERROR: Product already exists.\n")

def view_products():
    while True:
        print("\n\t\t\t\t     VIEW PRODUCTS")
        print("\t\t\t\t  *******************")
        print("\n\t\t\t 1. View All Products")
        print("\t\t\t 2. View Product By Code")
        print("\t\t\t 3. View Products By Category")
        print("\t\t\t 4. Back (Product Management)")
        c=int(input("\n\t\t\t Enter Your Choice: "))
        if c==1:
            view_all_products()
        elif c==2:
            pcode=int(input("\n\t\t\t Enter Product Code: "))
            view_product_pcode(pcode)            
        elif c==3:
            cat=input("\n\t\t\t Enter Category: ")
            view_product_cat(cat)
        elif c== 4:
            break
        else:
            print("\n\t\t\t ERROR: Invalid Input.")
            print("\t\t\t Enter from the numbers given in the menu only.")
            print("\t\t\t Please Try Again :/ \n")


def view_all_products():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\n\t\t\t\t   ALL PRODUCTS")
    print("\t\t\t        ******************")
    sql="SELECT * from products"
    mycursor.execute(sql)
    print("\n\t\t\t\t PRODUCT DETAILS")
    print("\t","-"*60,sep="")
    print("\t Code        Name        Price      Quantity      Category")
    print("\t","-"*60,sep="")
    for i in mycursor:
        print("\t ", i[0], "\t  ", i[1], "\t", i[2], "\t     ", i[3], "\t ", i[4])
    print("\t","-"*60,"\n",sep="")

def view_product_pcode(pcode):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        print("\n\n\t\t\t     PRODUCT WITH CODE - (",pcode,")", sep="")
        print("\t\t          ******************************")
        sql="SELECT * from products WHERE pcode=%s"
        val=(pcode,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t PRODUCT DETAILS")
        print("\t","-"*60,sep="")
        print("\t Code        Name        Price      Quantity      Category")
        print("\t","-"*60,sep="")
        for i in mycursor:
            print("\t ", i[0], "\t  ", i[1], "\t", i[2], "\t     ", i[3], "\t ", i[4])
        print("\t","-"*60,"\n",sep="")

def view_product_cat(cat):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM products WHERE pcat=%s;"
    val=(cat,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        print("\n\n\t\t\t PRODUCTS WITH CATEGORY - (",cat,")", sep="")
        print("\t\t      ****************************************")
        sql="SELECT * from products WHERE pcat=%s"
        val=(cat,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t PRODUCT DETAILS")
        print("\t","-"*60,sep="")
        print("\t Code        Name        Price      Quantity      Category")
        print("\t","-"*60,sep="")
        for i in mycursor:
            print("\t ", i[0], "\t  ", i[1], "\t", i[2], "\t     ", i[3], "\t ", i[4])
        print("\t","-"*60,"\n",sep="")


def update_product():
    while True:
        print("\n\t\t\t\t     UPDATE PRODUCT")
        print("\t\t\t\t  ********************")
        print("\n\t\t\t 1. Update Product Code")
        print("\t\t\t 2. Update Product Name")
        print("\t\t\t 3. Update Product Price")
        print("\t\t\t 4. Update Product Quantity")
        print("\t\t\t 5. Update Product Category")
        print("\t\t\t 6. Back (Product Management)")
        c=int(input("\n\t\t\t Enter Your Choice: "))
        if c==1:
            update_product_pcode()
        elif c==2:
            update_product_name()            
        elif c==3:
            update_product_price()
        elif c== 4:
            update_product_qty()
        elif c== 5:
            update_product_cat()
        elif c== 6:
            break
        else:
            print("\n\t\t\t ERROR: Invalid Input.")
            print("\t\t\t Enter from the numbers given in the menu only.")
            print("\t\t\t Please Try Again :/ \n")


def update_product_pcode():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     UPDATE PRODUCT CODE")
    print("\t\t\t\t\t  *************************")
    pcode=int(input("\n\t\t\t\t Enter Product Code: "))
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        pcode1=int(input("\t\t\t\t Enter NEW Product Code: "))
        confirm=input("""\n\t\t\t\t Enter "YES" to confirm NEW Product Code: """)
        if confirm=="YES" or confirm=="yes" or confirm=="Yes":
            sql="UPDATE products SET pcode=%s WHERE pcode=%s;"
            val=(pcode1,pcode)
            mycursor.execute(sql,val)
            sql="UPDATE orders SET pcode=%s WHERE pcode=%s;"
            val=(pcode1,pcode)
            mycursor.execute(sql,val)
            sql="UPDATE sales SET pcode=%s WHERE pcode=%s;"
            val=(pcode1,pcode)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\n\t\t\t\t Product Code Updated Successfully.\n")
    
    
def update_product_name():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     UPDATE PRODUCT NAME")
    print("\t\t\t\t\t  *************************")
    pcode=int(input("\n\t\t\t\t Enter Product Code: "))
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        name=input("\t\t\t\t Enter NEW Product Name: ")
        sql="UPDATE products SET pname=%s WHERE pcode=%s;"
        val=(name,pcode)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\n\t\t\t\t Product Name Updated Successfully.")
    
def update_product_price():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     UPDATE PRODUCT PRICE")
    print("\t\t\t\t\t  **************************")
    pcode=int(input("\n\t\t\t\t Enter Product Code: "))
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        price=float(input("\t\t\t\t Enter NEW Product Price: "))
        sql="UPDATE products SET pprice=%s WHERE pcode=%s;"
        val=(price,pcode)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\n\t\t\t\t Product Price Updated Successfully.")
    
def update_product_qty():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     UPDATE PRODUCT QUANTITY")
    print("\t\t\t\t\t  *****************************")
    pcode=int(input("\n\t\t\t\t Enter Product Code: "))
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        qty=int(input("\t\t\t\t Enter NEW Product Quantity: "))
        sql="UPDATE products SET pqty=%s WHERE pcode=%s;"
        val=(qty,pcode)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\n\t\t\t\t Product Quantity Updated Successfully.")
    
def update_product_cat():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     UPDATE PRODUCT CATEGORY")
    print("\t\t\t\t\t  *****************************")
    pcode=int(input("\n\t\t\t\t Enter Product Code: "))
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        cat=input("\t\t\t\t Enter NEW Product Category: ")
        sql="UPDATE products SET pcat=%s WHERE pcode=%s;"
        val=(cat,pcode)
        mycursor.execute(sql,val)
        sql="UPDATE orders SET pcat=%s WHERE pcode=%s;"
        val=(cat,pcode)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\n\t\t\t\t Product Category Updated Successfully.")


def delete_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     DELETE PRODUCT")
    print("\t\t\t\t\t  ********************")
    pcode=int(input("\n\t\t\t\t Enter Product Code: "))
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        print("""\n\t\t\t\t Enter "YES" to delete product (""",pcode,"): ", sep="", end="")
        confirm=input()
        if confirm=="YES" or confirm=="yes" or confirm=="Yes":
            sql="DELETE FROM products WHERE pcode = %s;"
            val=(pcode,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\n\t\t\t\t"," Product (",pcode,") Deleted Successfully.", sep="")
        else:
            print("\n\t\t\t\t Action Revoked. ")


def purchase_mgmt( ):
    while True:
        print("\n\t\t\t\t     PURHASE MANAGEMENT")
        print("\t\t\t\t  ************************")
        print("\n\t\t\t 1. Add New Order")
        print("\t\t\t 2. View Orders")
        print("\t\t\t 3. Update Order")
        print("\t\t\t 4. Delete Order")
        print("\t\t\t 5. Back (Main Menu)")
        c=int(input("\n\t\t\t Enter Your Choice: "))
        if c==1:
            add_order()
        elif c==2:
            view_orders()
        elif c==3:
            update_order()
        elif c==4:
            delete_order()
        elif c==5:
            break
        else:
            print("\n\t\t\t ERROR: Invalid Input.")
            print("\t\t\t Enter from the numbers given in the menu only.")
            print("\t\t\t Please Try Again :/ \n")


def add_order():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     ADD ORDER ")
    print("\t\t\t\t\t  ***************")
    pcode=int(input("\n\t\t\t\t Enter Product Code: "))
    search="SELECT count(*) FROM products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Product does not exist.\n")
    else:
        now = datetime.datetime.now()
        oid=now.year+now.month+now.day+now.hour+now.minute+now.second
        qty=int(input("\t\t\t\t Enter Product Quantity: "))
        cost=float(input("\t\t\t\t Enter Total Order Cost: "))
        supp=input("\t\t\t\t Enter Supplier Name: ")
        confirm=input("""\n\t\t\t\t Enter "YES" to confirm the above order details: """)
        if confirm=="YES" or confirm=="yes" or confirm=="Yes":
            sql="INSERT INTO orders(oid,odate,pcode,cost,oqty,supp) values (%s,%s,%s,%s,%s,%s)"
            val=(oid,now,pcode,cost,qty,supp)
            mycursor.execute(sql,val)
            sql="UPDATE orders SET pcat=(SELECT pcat FROM products WHERE orders.pcode=products.pcode) WHERE oid=%s"
            val=(oid,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\n\t\t\t\t Order Details Added Successfully.")
        else:
            print("\n\t\t\t\t Action Revoked. :/")

def view_orders():
    while True:
        print("\n\t\t\t\t\t\t     VIEW ORDERS")
        print("\t\t\t\t\t\t  *****************")
        print("\n\t\t\t\t\t 1. View All Orders")
        print("\t\t\t\t\t 2. View Order By Order ID")
        print("\t\t\t\t\t 3. View Orders By Product Code")
        print("\t\t\t\t\t 4. View Orders By Supplier")
        print("\t\t\t\t\t 5. View Orders By Category")
        print("\t\t\t\t\t 6. Back (Purchase Management)")
        c=int(input("\n\t\t\t\t\t Enter Your Choice: "))
        if c==1:
            view_all_orders()
        elif c==2:
            oid=int(input("\n\t\t\t\t\t Enter Order ID: "))
            view_order_oid(oid)
        elif c==3:
            pcode=int(input("\n\t\t\t\t\t Enter Product Code: "))
            view_order_pcode(pcode)
        elif c==4:
            supplier=input("\n\t\t\t\t\t Enter Supplier Name: ")
            view_order_supp(supplier)
        elif c==5:
            cat=input("\n\t\t\t\t\t Enter Product Category: ")
            view_order_cat(cat)
        elif c== 6:
            break
        else:
            print("\n\t\t\t\t\t ERROR: Invalid Input.")
            print("\t\t\t\t\t Enter from the numbers given in the menu only.")
            print("\t\t\t\t\t Please Try Again :/ \n")


def view_all_orders():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\n\t\t\t\t\t    ALL ORDERS")
    print("\t\t\t\t\t ****************")
    sql="SELECT * from orders"
    mycursor.execute(sql)
    print("\n\t\t\t\t\t   ORDER DETAILS")
    print(" ","-"*90)
    print("   Order ID  Product Code   Total Cost   Quantity   Supplier   Category         Date           ")
    print(" ","-"*90)
    for i in mycursor:
        print("    ",i[0],"        ",i[2],"\t     ",i[3],"\t  ",i[4],"\t   ",i[5],"\t",i[6],"  ",i[1])
    print(" ","-"*90,"\n")

def view_order_oid(oid):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM orders WHERE oid=%s;"
    val=(oid,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t ERROR: Order does not exist.\n")
    else:
        print("\n\n\t\t\t\t     ORDER ID - (",oid,")", sep="")
        print("\t\t\t ************************")
        sql="SELECT * from orders WHERE oid=%s"
        val=(oid,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t\t  ORDER DETAILS")
        print(" ","-"*90)
        print("   Order ID  Product Code   Total Cost   Quantity   Supplier   Category         Date           ")
        print(" ","-"*90)
        for i in mycursor:
            print("    ",i[0],"        ",i[2],"\t     ",i[3],"\t  ",i[4],"\t   ",i[5],"\t",i[6],"  ",i[1])
        print(" ","-"*90,"\n")

def view_order_pcode(pcode):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM orders WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t ERROR: Order(s) does not exist.\n")
    else:
        print("\n\n\t\t\t\t   ORDER CODE - (",pcode,")", sep="")
        print("\t\t\t\t **************************")
        sql="SELECT * from orders WHERE pcode=%s"
        val=(pcode,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t\t  ORDER DETAILS")
        print(" ","-"*90)
        print("   Order ID  Product Code   Total Cost   Quantity   Supplier   Category         Date           ")
        print(" ","-"*90)
        for i in mycursor:
            print("    ",i[0],"        ",i[2],"\t     ",i[3],"\t  ",i[4],"\t   ",i[5],"\t",i[6],"  ",i[1])
        print(" ","-"*90,"\n")

def view_order_supp(supplier):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM orders WHERE supp=%s;"
    val=(supplier,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t ERROR: Order(s) does not exist.\n")
    else:
        print("\n\n\t\t\t\t   ORDER WITH SUPPLIER - (",supplier,")", sep="")
        print("\t\t\t\t *************************************")
        sql="SELECT * from orders WHERE supp=%s"
        val=(supplier,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t\t  ORDER DETAILS")
        print(" ","-"*90)
        print("   Order ID  Product Code   Total Cost   Quantity   Supplier   Category         Date           ")
        print(" ","-"*90)
        for i in mycursor:
            print("    ",i[0],"        ",i[2],"\t     ",i[3],"\t  ",i[4],"\t   ",i[5],"\t",i[6],"  ",i[1])
        print(" ","-"*90,"\n")

def view_order_cat(cat):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM orders WHERE pcat=%s;"
    val=(cat,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t ERROR: Order(s) does not exist.\n")
    else:
        print("\n\n\t\t\t\t   ORDER WITH CATEGORY - (",cat,")", sep="")
        print("\t\t\t\t ************************************")
        sql="SELECT * from orders WHERE pcat=%s"
        val=(cat,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t\t  ORDER DETAILS")
        print(" ","-"*90)
        print("   Order ID  Product Code   Total Cost   Quantity   Supplier   Category         Date           ")
        print(" ","-"*90)
        for i in mycursor:
            print("    ",i[0],"        ",i[2],"\t     ",i[3],"\t  ",i[4],"\t   ",i[5],"\t",i[6],"  ",i[1])
        print(" ","-"*90,"\n")


def update_order():
    while True:
        print("\n\t\t\t\t\t     UPDATE ORDER")
        print("\t\t\t\t\t  ********************")
        print("\n\t\t\t\t 1. Update Product Code")
        print("\t\t\t\t 2. Update Order Total Cost")
        print("\t\t\t\t 3. Update Order Quantity")
        print("\t\t\t\t 4. Update Supplier")
        print("\t\t\t\t 5. Back (Purchase Management)")
        c=int(input("\n\t\t\t\t Enter Your Choice: "))
        if c==1:
            update_order_code()
        elif c==2:
            update_order_cost()            
        elif c==3:
            update_order_qty()
        elif c== 4:
            update_order_supp()
        elif c== 5:
            break
        else:
            print("\n\t\t\t ERROR: Invalid Input.")
            print("\t\t\t Enter from the numbers given in the menu only.")
            print("\t\t\t Please Try Again :/ \n")


def update_order_code():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t\t     UPDATE PRODUCT CODE")
    print("\t\t\t\t\t\t  *************************")
    oid=int(input("\n\t\t\t\t\t Enter Order ID: "))
    search="SELECT count(*) FROM orders WHERE oid=%s;"
    val=(oid,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t\t ERROR: Order does not exist.\n")
    else:
        code=int(input("\t\t\t\t\t Enter NEW Product Code: "))
        confirm=input("""\n\t\t\t\t\t Enter "YES" to confirm NEW Product Code: """)
        if confirm=="YES" or confirm=="yes" or confirm=="Yes":
            sql="UPDATE orders SET pcode=%s WHERE oid=%s;"
            val=(code,oid)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\n\t\t\t\t\t Product Code Updated Successfully.")
    
    
def update_order_cost():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t\t     UPDATE ORDER COST")
    print("\t\t\t\t\t\t  ************************")
    oid=int(input("\n\t\t\t\t\t Enter Order ID: "))
    search="SELECT count(*) FROM orders WHERE oid=%s;"
    val=(oid,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t\t ERROR: Order does not exist.\n")
    else:
        cost=float(input("\t\t\t\t\t Enter NEW Order Cost: "))
        sql="UPDATE orders SET cost=%s WHERE oid=%s;"
        val=(name,oid)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t\t Order Cost Updated Successfully.")
    
def update_order_qty():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t\t     UPDATE ORDER QUANTITY")
    print("\t\t\t\t\t\t  ****************************")
    oid=int(input("\n\t\t\t\t\t Enter Order ID: "))
    search="SELECT count(*) FROM orders WHERE oid=%s;"
    val=(oid,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t\t ERROR: Order does not exist.\n")
    else:
        qty=int(input("\t\t\t\t\t Enter NEW Order Quantity: "))
        sql="UPDATE orders SET oqty=%s WHERE pcode=%s;"
        val=(qty,code)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\n\t\t\t\t\t Order Quantity Updated Successfully.")
    
def update_order_supp():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t\t     UPDATE ORDER SUPPLIER")
    print("\t\t\t\t\t\t  ****************************")
    oid=int(input("\n\t\t\t\t\t Enter Order ID: "))
    search="SELECT count(*) FROM orders WHERE oid=%s;"
    val=(oid,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t\t ERROR: Order does not exist.\n")
    else:
        supp=input("\t\t\t\t\t Enter NEW Order Supplier: ")
        sql="UPDATE orders SET supp=%s WHERE oid=%s;"
        val=(supp,oid)
        mycursor.execute(sql,val)
        mydb.commit()
        print("\n\t\t\t\t\t Order Supplier Updated Successfully.")


def delete_order():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     DELETE ORDER")
    print("\t\t\t\t\t  ******************")
    oid=int(input("\n\t\t\t\t Enter Order ID: "))
    search="SELECT count(*) FROM orders WHERE oid=%s;"
    val=(oid,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t\t\t ERROR: Order does not exist.\n")
    else:
        print("""\n\t\t\t\t Enter "YES" to delete order (""",oid,"): ", sep="", end="")
        confirm=input()
        if confirm=="YES" or confirm=="yes" or confirm=="Yes":
            sql="DELETE FROM orders WHERE oid = %s;"
            val=(oid,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\n\t\t\t\t"," Order (",oid,") Deleted Successfully.\n", sep="")
        else:
            print("\n\t\t\t\t Action Revoked. ")
        

def sales_mgmt( ):
    while True:
        print("\n\t\t\t\t     SALES MANAGEMENT")
        print("\t\t\t\t  **********************")
        print("\n\t\t\t 1. Sale Products")
        print("\t\t\t 2. View Sales")
        print("\t\t\t 3. Back (Main Menu)")
        c=int(input("\n\t\t\t Enter Your Choice: "))
        if c==1:
            sale_product()
        elif c== 2 :
            view_sales()
        elif c== 3 :
            break
        else:
            print("\n\t ERROR: Invalid Input.")
            print("\t Enter from the numbers given in the menu only.")
            print("\t Please Try Again :/ \n")


def sale_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\t\t\t\t\t     SALE PRODUCTS")
    print("\t\t\t\t\t  *******************")
    pcode=input("\n\t\t\t\t Enter Product Code: ")
    sql="SELECT count(*) from products WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(sql,val)
    for x in mycursor:
        count=x[0]
    if count !=0 :
        sql="SELECT * from products WHERE pcode=%s;"
        val=(pcode,)
        mycursor.execute(sql,val)
        for x in mycursor:
            price=int(x[2])
            pqty=int(x[3])
        qty=int(input("\t\t\t\t Enter Quantity: "))
        if qty <= pqty:
            total=qty*price;
            sid=int(count+1)
            print ("\t\t\t\t Please Pay  Rs. ", total)
            sql="INSERT into sales(sid,sdate,pcode,sprice,sqty,total) values(%s,%s,%s,%s,%s,%s)"
            val=(sid,datetime.datetime.now(),pcode,price,qty,total)
            mycursor.execute(sql,val)
            sql="UPDATE sales SET pcat=(SELECT pcat FROM products WHERE sales.pcode=products.pcode) WHERE sid=%s"
            val=(sid,)
            mycursor.execute(sql,val)
            sql="UPDATE products SET pqty=pqty-%s WHERE pcode=%s"
            val=(qty,pcode)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            print("\n\t\t\t\t Please Reduce Product Quantity.")
            print("\t\t\t\t Max Quantity Allowed:", pqty)
    else:
        print("\n\t\t\t\t Error: Product does not exist.")
        

def view_sales():
    while True:
        print("\n\t\t\t\t\t\t     VIEW SALES")
        print("\t\t\t\t\t\t  ****************")
        print("\n\t\t\t\t\t 1. View All Sales")
        print("\t\t\t\t\t 2. View Sale By Sale ID")
        print("\t\t\t\t\t 3. View Sales By Product Code")
        print("\t\t\t\t\t 4. View Sales By Category")
        print("\t\t\t\t\t 5. Back (Sales Management)")
        c=int(input("\n\t\t\t\t\t Enter Your Choice: "))
        if c==1:
            view_all_sales()
        elif c==2:
            sid=int(input("\n\t\t\t\t\t Enter Sales ID: "))
            view_sales_sid(sid)
        elif c==3:
            pcode=int(input("\n\t\t\t\t\t Enter Product Code: "))
            view_sales_pcode(pcode)
        elif c==4:
            cat=input("\n\t\t\t\t\t Enter Product Category: ")
            view_sales_cat(cat)
        elif c==5:
            break
        else:
            print("\n\t\t\t\t\t ERROR: Invalid Input.")
            print("\t\t\t\t\t Enter from the numbers given in the menu only.")
            print("\t\t\t\t\t Please Try Again :/ \n")


def view_all_sales():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    print("\n\n\t\t\t\t\t    ALL SALES")
    print("\t\t\t\t\t ***************")
    sql="SELECT * from sales"
    mycursor.execute(sql)
    print("\n\t\t\t\t\t   SALES DETAILS")
    print("\t","-"*100, sep="")
    print("\t Sales ID          Date          Product Code     Price     Quantity       Total      Category")
    print("\t","-"*100, sep="")
    for x in mycursor:
        print("\t  ",x[0],"\t  ",x[1],"\t     ",x[2],"\t ",x[3],"\t",x[4],"\t  ",x[5],"\t",x[6])
    print("\t","-"*100, sep="")

def view_sales_sid(sid):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM sales WHERE sid=%s;"
    val=(sid,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t ERROR: Sale does not exist.\n")
    else:
        print("\n\n\t\t\t\t     SALE ID - (",sid,")", sep="")
        print("\t\t\t ***********************")
        sql="SELECT * from sales WHERE sid=%s"
        val=(sid,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t\t   SALES DETAILS")
        print("\t","-"*100, sep="")
        print("\t Sales ID          Date          Product Code     Price     Quantity       Total      Category")
        print("\t","-"*100, sep="")
        for x in mycursor:
            print("\t  ",x[0],"\t  ",x[1],"\t     ",x[2],"\t ",x[3],"\t",x[4],"\t  ",x[5],"\t",x[6])
        print("\t","-"*100, sep="")

def view_sales_pcode(pcode):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM sales WHERE pcode=%s;"
    val=(pcode,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t ERROR: Sales(s) does not exist.\n")
    else:
        print("\n\n\t\t\t\t   SALE CODE - (",pcode,")", sep="")
        print("\t\t\t\t **************************")
        sql="SELECT * from sales WHERE pcode=%s"
        val=(pcode,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t\t   SALES DETAILS")
        print("\t","-"*100, sep="")
        print("\t Sales ID          Date          Product Code     Price     Quantity       Total      Category")
        print("\t","-"*100, sep="")
        for x in mycursor:
            print("\t  ",x[0],"\t  ",x[1],"\t     ",x[2],"\t ",x[3],"\t",x[4],"\t  ",x[5],"\t",x[6])
        print("\t","-"*100, sep="")

def view_sales_cat(cat):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")
    mycursor=mydb.cursor()
    search="SELECT count(*) FROM sales WHERE pcat=%s;"
    val=(cat,)
    mycursor.execute(search,val)
    for x in mycursor:
        count=x[0] 
    if count==0:
        print("\n\t\t ERROR: Sale(s) does not exist.\n")
    else:
        print("\n\n\t\t\t\t   SALES WITH CATEGORY - (",cat,")", sep="")
        print("\t\t\t\t ************************************")
        sql="SELECT * from sales WHERE pcat=%s"
        val=(cat,)
        mycursor.execute(sql,val)
        print("\n\t\t\t\t\t   SALES DETAILS")
        print("\t","-"*100, sep="")
        print("\t Sales ID          Date          Product Code     Price     Quantity       Total      Category")
        print("\t","-"*100, sep="")
        for x in mycursor:
            print("\t  ",x[0],"\t  ",x[1],"\t     ",x[2],"\t ",x[3],"\t",x[4],"\t  ",x[5],"\t",x[6])
        print("\t","-"*100, sep="")


def db_mgmt( ):
    while True:
        print("\n\t\t\t\t     DATABASE MANAGEMENT")
        print("\t\t\t\t  *************************")
        print("\n\t\t\t 1. Database Setup")
        print("\t\t\t 2. View Database")
        print("\t\t\t 3. Back (Main Menu)")
        c=int(input("\n\t\t\t Enter Your Choice: "))
        if c==1:
            setup_database()
        elif c==2:
            view_database()
        elif c== 3:
            break
        else:
            print("\n\t ERROR: Invalid Input.")
            print("\t Enter from the numbers given in the menu only.")
            print("\t Please Try Again :/ \n")


def setup_database():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
    mycursor=mydb.cursor()
    print("\n\t\t\t Please wait while we finish setting up the database.")
    
    print("\n\t\t\t Creating DATABASE...")
    sql="CREATE DATABASE if not exists onestox;"
    mycursor.execute(sql)
    print("\t\t\t DATABASE Created Successfully.")

    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234", database="onestox")
    mycursor=mydb.cursor()
    
    print("\n\t\t\t Creating PRODUCTS Table...")
    sql="""CREATE TABLE if not exists products
        (pcode int(4) PRIMARY KEY,
         pname char(30) NOT NULL,
         pprice float(8,2),
         pqty int(4),
         pcat char(30));"""
    mycursor.execute(sql)
    print("\t\t\t PRODUCTS Table Created Successfully.")

    print("\n\t\t\t Creating ORDERS Table...")
    sql="""CREATE TABLE if not exists orders
        (oid int(4) PRIMARY KEY,
         odate datetime,
         pcode char(30) references products(pcode),
         cost float(8,2),
         oqty int(4),
         supp char(50),
         pcat char(30));"""
    mycursor.execute(sql)
    print("\t\t\t ORDER Table Created Successfully.")

    print("\n\t\t\t Creating SALES Table...")
    sql="""CREATE TABLE if not exists sales
        (sid int(4) PRIMARY KEY,
         sdate datetime,
         pcode char(30) references products(pcode),
         sprice float(8,2),
         sqty int(4),
         Total double(8,2),
         pcat char(30));"""
    mycursor.execute(sql)
    print("\t\t\t SALES Table Created Successfully.")
           
    print("\n\t\t\t Database Setup Completed Successfully.\n")


def view_database():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="onestox")   
    mycursor=mydb.cursor()
    print("\n\t\t\t Tables in the Database:-\n")
    sql="show tables;"
    mycursor.execute(sql)
    for i in mycursor:
        print("\t\t\t", i)



root=tkinter.Tk()
root.title("ONEstox")
root.geometry("800x500")

bg=tkinter.PhotoImage(file="bg.png")
header=tkinter.PhotoImage(file="header.png")
tkinter.Label(root, image=bg, borderwidth=0).place(x=0,y=0)
tkinter.Label(root, image=header, borderwidth=0).place(x=0,y=0)

header_prm=tkinter.Label(root, bg="#333333", text="Product Management", foreground="#d6d6d6", activeforeground="#ffffff", borderwidth=0,)
header_prm.place(x=33,y=10)
header_prm.configure(font=("SF Pro Display", 13))

header_pum=tkinter.Label(root, bg="#333333", text="Purchase Management", foreground="#d6d6d6", activeforeground="#ffffff", borderwidth=0)
header_pum.place(x=223,y=10)
header_pum.configure(font=("SF Pro Display", 13))

header_sm=tkinter.Label(root, bg="#333333", text="Sales Management", foreground="#d6d6d6", activeforeground="#ffffff", borderwidth=0)
header_sm.place(x=423,y=10)
header_sm.configure(font=("SF Pro Display", 13))

header_um=tkinter.Label(root, bg="#333333", text="Database Management", foreground="#d6d6d6", activeforeground="#ffffff", borderwidth=0)
header_um.place(x=593,y=10)
header_um.configure(font=("SF Pro Display", 13))

proj=tkinter.Label(root, bg="black", text='''Computer Science (083)
Term 2 Project''', foreground="white", borderwidth=0)
proj.place(x=310,y=60)
proj.configure(font=("SF Pro Display", 15, "bold"))

logo=tkinter.PhotoImage(file="1stox black blue.png")
tkinter.Label(root, image=logo, borderwidth=0).place(x=222,y=110)

memb=tkinter.Label(root, bg="black", text='''Prepared By
Tanay Changoiwala
Divyansh Gupta
Bhavya Sheorayan''', foreground="white", borderwidth=0)
memb.place(x=324,y=255)
memb.configure(font=("SF Pro Display", 15, "bold"))

box=tkinter.PhotoImage(file="box.png")
tkinter.Label(root, image=box, borderwidth=0).place(x=310,y=375)

welc=tkinter.Label(root, bg="#333333", text="Welcome to ONEstox :)", foreground="white", borderwidth=0)
welc.place(x=320,y=385)
welc.configure(font=("SF Pro Display", 14))

proceed=tkinter.Label(root, bg="#333333", text="To proceed,", foreground="white", borderwidth=0)
proceed.place(x=338,y=423)
proceed.configure(font=("Arial", 10, "bold"))

tkinter.Button(root, bg="white", text="Click Here", command=root.destroy,).place(x=420,y=418)

footer=tkinter.PhotoImage(file="footer.png")
tkinter.Label(root, image=footer, borderwidth=0).place(x=0,y=470)

footer_txt=tkinter.Label(root, bg="#3b91ff", text="If you're new here, setup your database first.", foreground="white", borderwidth=0)
footer_txt.place(x=260,y=473)
footer_txt.configure(font=("SF Pro Display", 13))

root.mainloop()


print("\n\n\t\t\t\t  ***************")
print("\t\t\t\t  *   ONEstox   *")
print("\t\t\t\t  *************** \n")
print("\t\tPlease enter a number from the menu to proceed.\n")

while True:
    print("\n\t\t     Main Menu")
    print("\t\t  *************** \n")
    print("\t 1. PRODUCT MANAGEMENT")
    print("\t 2. PURCHASE MANAGEMENT")
    print("\t 3. SALES MANAGEMENT")
    print("\t 4. DATABASE SETUP")
    print("\t 5. EXIT\n")
    n=int(input("\t Enter Your Choice: "))
    if n==1:
        product_mgmt()
    elif n==2:
        purchase_mgmt()
    elif n==3:
        sales_mgmt()
    elif n==4 :
        db_mgmt()
    elif n==5:
        break
    else:
        print("\n\t ERROR: Invalid Input.")
        print("\t Enter from the numbers given in the menu only.")
        print("\t Please Try Again :/")
