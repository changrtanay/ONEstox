# one-stox

## Overview
ONEstox is a comprehensive software solution designed for managing products, purchases, sales, and databases within an inventory system. This application uses a MySQL database and provides an interactive interface using Python's `tkinter` for managing product details, placing orders, tracking sales, and performing database setup.

## Features

### Product Management
- **Add New Product**: Add new products with unique product codes, names, prices, quantities, and categories.
- **View Products**: View a list of all products or search by product code or category.
- **Update Product**: Modify product details, including product code, name, price, quantity, and category.
- **Delete Product**: Delete a product from the system using its product code.

### Purchase Management
- **Add New Order**: Add new orders with details such as product code, quantity, total cost, and supplier information.
- **View Orders**: View a list of all orders or search by order ID, product code, or supplier.
- **Update Order**: Update order details, including product code, order quantity, cost, and supplier.
- **Delete Order**: Delete orders by order ID.

### Sales Management
- **Sale Products**: Sell products by specifying the product code, quantity, and sales price.
- **View Sales**: View sales records by sale ID, product code, or category.

### Database Management
- **Setup Database**: Automatically create the necessary database and tables for managing products, orders, and sales.
- **View Database**: View the tables present in the connected database.

## Requirements

- Python 3.x
- MySQL
- `mysql-connector-python` library
- `tkinter` library for GUI
- A MySQL server running on localhost

## Installation

1. Install Python from the [official website](https://www.python.org/downloads/).
2. Install MySQL server from the [official website](https://dev.mysql.com/downloads/).
3. Install the necessary Python libraries:
   ```bash
   pip install mysql-connector-python
   ```
4. Clone or download the `ONEstox` source code.
5. Run the script:
   ```bash
   python onestox.py
   ```

## Usage

1. **Main Menu**:
   - Choose a number from the main menu to proceed to the corresponding section (Product Management, Purchase Management, Sales Management, or Database Setup).
   
2. **Product Management**:
   - Add new products, view products by code or category, update product details, or delete a product.

3. **Purchase Management**:
   - Add, view, update, or delete orders from suppliers for products.

4. **Sales Management**:
   - Manage sales of products, view sales records, and update or delete sales transactions.

5. **Database Setup**:
   - Set up the database and create required tables (`products`, `orders`, `sales`).

## Database Structure

The system uses the following tables:

1. **products**: Stores information about products (e.g., product code, name, price, quantity, category).
2. **orders**: Stores information about orders (e.g., order ID, product code, quantity, cost, supplier).
3. **sales**: Stores information about sales (e.g., sale ID, product code, quantity sold, total amount, category).

### Table Definitions
```sql
CREATE TABLE IF NOT EXISTS products (
    pcode INT(4) PRIMARY KEY,
    pname CHAR(30) NOT NULL,
    pprice FLOAT(8, 2),
    pqty INT(4),
    pcat CHAR(30)
);

CREATE TABLE IF NOT EXISTS orders (
    oid INT(4) PRIMARY KEY,
    odate DATETIME,
    pcode INT(4) REFERENCES products(pcode),
    cost FLOAT(8, 2),
    oqty INT(4),
    supp CHAR(50),
    pcat CHAR(30)
);

CREATE TABLE IF NOT EXISTS sales (
    sid INT(4) PRIMARY KEY,
    sdate DATETIME,
    pcode INT(4) REFERENCES products(pcode),
    sprice FLOAT(8, 2),
    sqty INT(4),
    total DOUBLE(8, 2),
    pcat CHAR(30)
);
```

## Customization

- Modify the `mysql.connector.connect()` function parameters to match your MySQL server configuration (host, username, password, and database).
- Customize the GUI by changing the `tkinter` window configurations, labels, and layout.

## Contributing

If you wish to contribute to the development of this project:
1. Fork the repository.
2. Create a new branch.
3. Make changes and commit them.
4. Open a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- The system uses MySQL for database management.
- `tkinter` was used for creating the graphical user interface.
