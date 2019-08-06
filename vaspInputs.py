from pymatgen.ext.matproj import MPRester
from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import IStructure
from pymatgen.io.vasp.sets import MPRelaxSet
from pymatgen.io.vasp.inputs import Incar, Poscar, Potcar, Kpoints, VaspInput

import numpy as np
import json
import os


APIkey = 'Cc0MLFoRBsT4lQ8J'  # update the key when necessary
mpr = MPRester(APIkey)
# os.system('pmg config --add PMG_VASP_PSP_DIR G:/pseudo-potential/')
# os.system('pmg config --add PMG_DEFAULT_FUNCTIONAL PW91')


class VaspInputs:

    def __init__(self, mp_id):

        self.mp_id = str(mp_id)
        self.structure = mpr.get_structure_by_material_id(self.mp_id)
        self.relaxed_structure = MPRelaxSet(self.structure)
        self.relaxed_structure.potcar_functional = 'PW91'  # Vasp functional set as potpaw_GGA

    def get_incar(self):
        return

    def get_poscar(self):
        return

    def get_kpoints(self):
        return

    def get_potcar_map(self):
        return

    def write_input(self):
        self.relaxed_structure.write_input('.')


if __name__ == '__main__':
    VaspInputs('mp-1').write_input()
