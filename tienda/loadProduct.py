from models import Producto
import stripe

def LoadProduct():
    producto = Producto.objects.all()

    for item in producto:
        item_product=stripe.Product.create(
            name=f'{item.nombre}',
            desciption = f'{item.categoria}'
        )
        stripe.Price.create(
            unit_amount= float(item.precio),
            currency = 'eur',
            product = item_product['id']
        )


if __name__=='__main__':
    LoadProduct()