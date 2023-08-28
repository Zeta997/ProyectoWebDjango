
class Carro:
    def __init__(self, request):
        self.request= request
        self.session= request.session
        carro = self.session.get('carro')
        if not carro:
            carro=self.session['carro']=dict()
        else:
            self.carro= carro
    
    def agregarProducto(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id]= {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad':1,
                'imagen':producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value['cantidad'] +=1
                    break
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session['carro']= self.carro
        self.session.modified=True
    

    def eliminarProducto(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def quitarProducto(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id):
                    if value['cantidad']<1:
                        self.eliminarProducto(producto)
                        break
                    else:
                        value['cantidad'] -=1
                        break
        self.guardar_carro()
    
    def limpiarCarro(self):
        self.session['carro']=dict()
        self.session.modified=True