from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db

    def index(self):
        items = self.models['Product'].get_all_items()
        return self.load_view('index.html', items = items)


    def show_new(self):
        return self.load_view('new_product.html')

    def add_new(self):
        self.models['Product'].add_item(request.form)
        return redirect('/')

    def show_product(self, id):
        item = self.models['Product'].get_one_item(id)
        return self.load_view('item.html', item = item)

    def show_edit(self, id):
        item = self.models['Product'].get_one_item(id)
        return self.load_view('edit.html', item = item)

    def update_items(self):
        self.models['Product'].update_item(request.form)
        return redirect('/')

    def delete(self):
        self.models['Product'].delete_item(request.form)
        return redirect('/')