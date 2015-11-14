from system.core.router import routes

routes['default_controller']            = 'Products'
routes['/Products']                     = 'Products#index'
routes['GET']['/Products/new']          = 'Products#new'
routes['POST']['/Products/create']      = 'Products#create'
routes['POST']['/Products/update/<id>'] = 'Products#update'
routes['GET']['/Products/show/<id>']    = 'Products#show'
routes['GET']['/Products/edit/<id>']    = 'Products#edit'
routes['GET']['/Products/destroy/<id>']  = 'Products#destroy'
