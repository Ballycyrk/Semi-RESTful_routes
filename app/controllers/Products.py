from system.core.controller import *

class Products(Controller):
  def __init__(self, action):
    super(Products, self).__init__(action)

  def index(self):
    return self.load_view('index.html')

  def new(self):
    return self.load_view('new.html')

  def create(self):
    params = {}
    pass

  def show(self, id):
    # call db for product by id
    return self.load_view('show.html', id = id)

  def edit(self):
    #call db load form values with current variables
    return self.load_view('edit.html')

  def update(self, id):
    #insert query from form via edit.html
    pass

  def destroy(self, id):
    #delete from db
    pass

