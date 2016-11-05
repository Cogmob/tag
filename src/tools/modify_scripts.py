import epr
import os

path = os.path.os.path.dirname(os.path.realpath(__file__))
print('now')

<<<<<<< HEAD
epr.epr_recursive_import(path + '/../../gen')
=======
epr.epr(path + '/../../gen/src')
epr.epr_recursive_import(path + '/../../gen/src')
>>>>>>> 91aeb195db7618d3a190eab50d6657a754984229
