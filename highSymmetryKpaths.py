from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.core import Structure
from pymatgen.symmetry.bandstructure import HighSymmKpath


def hs_kpath_gen(working_dir: str = './'):
    structure = Structure.from_file(working_dir+'POSCAR')
    kpath = HighSymmKpath(structure)
    kpts = Kpoints.automatic_linemode(divisions=40, ibz=kpath)
    kpts.write_file(working_dir+'KPOINTS')


if __name__ == '__main__':
    hs_kpath_gen()