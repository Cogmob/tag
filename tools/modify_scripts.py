import epr
import os

path = os.path.os.path.dirname(os.path.realpath(__file__))

epr.epr_recursive_import(path + '/../.gen')