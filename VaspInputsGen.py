from pymatgen.ext.matproj import MPRester
from pymatgen.io.vasp.sets import MPRelaxSet

import os


APIkey = 'Cc0MLFoRBsT4lQ8J'  # update the key when necessary
mpr = MPRester(APIkey)
os.system('pmg config --add PMG_VASP_PSP_DIR G:/pseudo-potential/POT_GGA_PAW_PW91/')
os.system('pmg config --add PMG_DEFAULT_FUNCTIONAL PW91')

structure = mpr.get_structure_by_material_id('mp-1')
relaxed_structure = MPRelaxSet(structure)
relaxed_structure.potcar_functional ='PW91'
relaxed_structure.write_input('.')


