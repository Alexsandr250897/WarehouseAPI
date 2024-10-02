Task: Developing an API for warehouse management
Task description:
It is necessary to develop a small REST API using FastAPI for warehouse processes management. The API should allow managing products, stocks and orders.
Main requirements:
1. Creating the database structure:
○ Use SQLAlchemy (2 versions) to interact with the
database.
○ Design tables for the following entities:
■ Product: id, name, description, price, quantity in stock.
■ Order: id, creation date, status (e.g. "in process", "shipped", "delivered").
■ OrderItem: id, order id, product id, quantity of product in the order.
2. Implementing the REST API:
○ Endpoints for products:
■ Creating a product (POST /products).
■ Getting a list of products (GET /products).
■ Getting information about a product by id (GET /products/{id}).
■ Updating information about a product (PUT /products/{id}).
■ Deleting a product (DELETE /products/{id}).
○ Endpoints for orders:
■ Creating an order (POST /orders).
■ Getting a list of orders (GET /orders).
■ Getting information about an order by id (GET /orders/{id}).
■ Updating the order status (PATCH /orders/{id}/status).
3. Business logic:
○ When creating an order, check for sufficient quantities of
the product in stock.
○ Update the quantity of the product in stock when creating an order
(reducing the available quantity).
○ If there is insufficient quantity of the product, return an error with
the corresponding message.
4. Documentation:
○ Use the built-in FastAPI documentation (Swagger/OpenAPI). Additional requirements:
1. Testing:
○ Write some tests using pytest to test the
main API functions.
2. Docker:
○ Create a Dockerfile and docker-compose file to run the project
along with a database (e.g. PostgreSQL).