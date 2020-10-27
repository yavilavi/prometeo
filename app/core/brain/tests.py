from config.wsgi import *
from core.brain.models import *

positions = ['Agente', 'Supervisor', 'Formador', 'ACCM']
Lobs = ['BGI ARGENTINA', 'BGI CHILE', 'BGI COLOMBIA', ]

for i in range(0, len(positions)):
    try:
        position = Position()
        position.position_name = positions[i]
        position.save()
    except Exception as e:
        print(e)

for i in range(0, len(Lobs)):
    try:
        lob = Lob()
        lob.lob_name = Lobs[i]
        lob.save()
    except Exception as e:
        print(e)
