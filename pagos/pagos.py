import stripe
from tienda.models import pedidosARealizar
stripe.api_key = 'sk_test_51NmvPOL6EpuUZLgWxfSk5KC3FTyjyFZu68kTq8MDBrMbRwDbLjmkYhyLl6Dzm8zusjaJ4gtciKmV8VX3d9EQBCLk00HEKpZqQL'
def create_checkput_session(key, value):
    for keyIdBBDD in pedidosARealizar.items():
        print(keyIdBBDD)
        if keyIdBBDD==key:
            productoCompra = stripe.Price.retrieve(pedidosARealizar[keyIdBBDD])
            print(productoCompra.id)
            # idcompra= productoCompra.prices
    try:
        pass
        stripe.checkout.Session.create(
            line_items= [
                {
                'price': 'price_1NpAktL6EpuUZLgWhO5lflbM',
                'quantity': 1,
                },

            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/' ,
            cancel_url='http://127.0.0.1:8000/' ,
        )
        print('Sesion creada')
    except Exception as e:
        print(e)