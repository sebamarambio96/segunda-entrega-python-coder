from segunda_entrega.tienda import *
from primera_entrega.login import *

papitas = Productos('Donde Pepito', 'Papas fritas', 20000)
papel = Productos('Donde Pepito', 'Papel Higienico', 15000)
chorizo = Productos('Donde Pepito', 'Chorizo', 7000)


cliente1 = Clientes('Donde Pepito', '19274535-7',
                    [papitas, papel, chorizo], True)

""" print(cliente1) """
""" print(cliente1.calcular_total()) """
print(cliente1.detalle_de_compra())