from system.core.model import Model
import re


class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def show_all(self):
      get = "SELECT id, name, description, price FROM products"
      return self.db.query_db(get)

    def show(self, id):
      get = "SELECT id, name, description, price FROM products WHERE id={}".format(id)
      return self.db.query_db(get)

    def update(self, params):
      CURRENCY_REGEX = re.compile(r'^\d*.?\d{0,2}$')
      if not CURRENCY_REGEX.match(params['price']):
        params['error'] ='Please enter the new price with dollars and cents without a $ sign.'
        params['price'] = 'DD.CC'
        return
      else:
        update = "UPDATE products SET name = %s, description = %s, price = %s, updated_at = NOW() WHERE id=%s"
        data = (params['name'], params['description'], params['price'], params['id'])
        self.db.query_db(update, data)
      return

    def add(self, params):
      CURRENCY_REGEX = re.compile(r'^\d*.?\d{0,2}$')
      if not CURRENCY_REGEX.match(params['price']):
        params['error'] ='Please enter the price with dollars and cents without a $ sign.'
        params['price'] = 'DD.CC'
        return
      else:
        insert = "INSERT INTO products(name, description, price, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
        data = (params['name'], params['description'], params['price'])
        self.db.query_db(insert, data)
      return

    def destroy(self, id):
      bye = "DELETE FROM products WHERE id = {}".format(id)
      self.db.query_db(bye)
      return

