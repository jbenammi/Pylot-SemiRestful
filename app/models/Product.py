from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def add_item(self, info):
        query = "INSERT INTO products(name, description, price, created_on, updated_on) VALUES(:name, :description, :price, now(), now())"
        data = {
                'name': info['name'],
                'description': info['description'],
                'price': info['price']
                }
        self.db.query_db(query, data)

    def get_all_items(self):
        query = "SELECT id, name, description, price FROM products"
        return self.db.query_db(query)

    def get_one_item(self, info):
        query = "SELECT id, name, description, price FROM products WHERE id = :id"
        data = {
                'id': info
                }
        return self.db.query_db(query, data)

    def update_item(self, info):
        query = "UPDATE products SET name = :name, description = :description, price = :price, updated_on = now() WHERE id = :id"
        data = {
                'name': info['name'],
                'description': info['description'],
                'price': info['price'],
                'id': info['id']
                }
        self.db.query_db(query, data)

    def delete_item(self, info):
        query = "DELETE FROM products WHERE id = :id"
        data = {
                'id': info['id']
                }
        return self.db.query_db(query, data)