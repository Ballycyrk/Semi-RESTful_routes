from system.core.controller import *

class Products(Controller):
  def __init__(self, action):
    super(Products, self).__init__(action)
    self.load_model('Product')

  def index(self):
    products = self.models['Product'].show_all()
    return self.load_view('index.html', products = products)

  def new(self):
    return self.load_view('new.html')

  def create(self):
    params = {
    'name'        : request.form['name'],
    'description' : request.form['description'],
    'price'       : request.form['price']}
    self.models['Product'].add(params)
    try:
      params['error']
      flash(params['error'])
      return self.load_view('edit.html', product = params)
    except:
      return redirect('/')

  def show(self, id):
    product = self.models['Product'].show(id)
    return self.load_view('show.html', product = product[0])

  def edit(self, id):
    session['id'] = id
    product = self.models['Product'].show(id)
    return self.load_view('edit.html', product = product[0])

  def update(self, id):
    #insert query from form via edit.html
    params = {
    'id'          : id,
    'name'        : request.form['name'],
    'description' : request.form['description'],
    'price'       : request.form['price']}
    self.models['Product'].update(params)
    try:
      params['error']
      flash(params['error'])
      return self.load_view('edit.html', product = params)
    except:
      return redirect('/')

  def destroy(self, id):
    #delete from d
    pass

