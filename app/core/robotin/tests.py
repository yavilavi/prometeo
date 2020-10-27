from config.wsgi import *

from core.robotin.models import *

#listar
query = Position.objects.all();
#
# Insertar

p = Position()
p.position_name = 'Supervisor'
p.save()

# #editar

e = Position.objects.get(id=2)

print(e.position_name)


