from pymatgen.ext.matproj import MPRester

from pymatgen.io.vasp.sets import MPRelaxSet
from pymatgen.io.vasp.inputs import Incar, Poscar, Potcar, Kpoints, VaspInput
from pymatgen.symmetry.bandstructure import HighSymmKpath


APIkey = 'Cc0MLFoRBsT4lQ8J'  # update the key when necessary
mpr = MPRester(APIkey)

# TODO:
# Every time when changing running environment, need uncomment the following two lines
# os.system('pmg config --add PMG_VASP_PSP_DIR G:/pseudo-potential/')
# os.system('pmg config --add PMG_DEFAULT_FUNCTIONAL PW91')


class VaspInputs:

    def __init__(self, mp_id, incar_settings: dict):

        self.mp_id = str(mp_id)

        self.structure = mpr.get_structure_by_material_id(self.mp_id)
        self.primitive_structure = self.structure.get_primitive_structure()

        self.kpath = HighSymmKpath(self.primitive_structure)
        # self.new_kpoints = self.add_kpoints(self.kpath)

        self.add_kpoints(self.kpath)  # Add inverse kpoints intp kpath.__dict__['kpoints ']
        self.relaxed_structure = MPRelaxSet(self.structure,
                                            user_incar_settings=incar_settings)
        self.relaxed_structure.potcar_functional = 'PW91'  # Vasp functional set as potpaw_GGA

    @staticmethod
    def get_incar(working_dir: str, incar_config: dict):
        file_name = working_dir+'INCAR'
        Incar(incar_config).write_file(file_name)

    def get_poscar(self):
        pass

    def get_kpoints(self):
        pass

    def get_potcar_map(self):
        pass

    # def add_kpoints(self, kpath):
    #     # Add inverse of high symmetry kpoints
    #
    #     kpoints_dict = OrderedDict(kpath.__dict__['_kpath']['kpoints'])
    #     new_kpoints_list = []
    #
    #     for k, v in kpoints_dict.items():
    #         new_kpoints_list.append(v)
    #         new_kpoints_list.append(v*(-1))
    #
    #     return new_kpoints_list

    def add_kpoints(self, kpath):
        kpoints_dict = kpath.__dict__['_kpath']['kpoints']
        kpath_list = kpath.__dict__['_kpath']['path']

        print(kpath.__dict__)

        total_kpath = len(kpath_list)

        for i in range(total_kpath):
            tmp_list = []
            for c in kpath_list[i]:
                tmp_list.append(c)

            for c in tmp_list:
                c_inv = c+'_inv'
                kpath_list[i].append(c_inv)
                kpoints_dict[c_inv] = kpoints_dict[c]*(-1)

        print(kpath_list)
        print(kpoints_dict)
        pass

    def write_inputs(self):
        save_dir = 'VaspInputsDir/'+self.mp_id+'/'
        self.relaxed_structure.write_input(save_dir, make_dir_if_not_present=True)  # save_dir: mp_id

    # def write_kpoints(self):
    #     save_dir = 'VaspInputsDir/'+self.mp_id+'/'
    #     file_name = save_dir+'KPOINTS'
    #
    #     if os.path.isfile(file_name):
    #         os.remove(file_name)
    #
    #     with open(file_name, 'w') as f:
    #         print('KPOINTS', file=f)
    #         print(1, file=f)
    #         print('Reciprocal', file=f)
    #         for coord in self.new_kpoints:
    #             for index, i in enumerate(coord):
    #                 if index != 2:
    #                     print(i, file=f, end=' ')
    #                 else:
    #                     print(i, file=f)

    def write_hs_kpoints(self):
        save_dir = 'VaspInputsDir/' + self.mp_id + '/'
        kpts = Kpoints.automatic_linemode(divisions=1, ibz=self.kpath)
        kpts.write_file(save_dir + 'KPOINTS')


if __name__ == '__main__':
    inputs = VaspInputs('mp-4701', incar_settings={'ISIF': 2, 'ISYM': -1, 'ISEMEAR': 0, 'IBRION': -1,
                                                     'NSW': 0, 'NELM': 200, 'ISPIN': -1, 'LSORBIT': '.TRUE.'})
    inputs.write_inputs()
    inputs.write_hs_kpoints()
