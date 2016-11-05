import epr
import os

path = os.path.os.path.dirname(os.path.realpath(__file__))
print('now')

epr.epr_recursive_import(path + '/../../gen')
