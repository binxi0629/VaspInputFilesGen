from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter


def plot_bs(working_dir: str = './'):
    vaspout = Vasprun(working_dir+"vasprun.xml")
    bandstr = vaspout.get_band_structure(line_mode=True)
    plt = BSPlotter(bandstr).get_plot()
    plt.savefig("band.pdf")


if __name__ == '__main__':
    plot_bs()