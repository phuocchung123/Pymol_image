from pymol import cmd
import os
import glob
from IPython.utils import io
import tqdm.notebook
import os
class create_image:
    def __init__(self):
        self.type_image=int(input('Please input to choose type of molecular to take photos:\n 0: \t 2D;\n 1: \t 3D_cube;\n 2: \t 3D_tetrahedron'))
        self.ligand_dir=str(input('Please input the path of location to take pdb files or sdf files'))
        self.png_dir=str(input('Please input the path of location to save image'))

    def png_mol_2D(self):
        cmd.delete('all')
        command = "load "+self.ligand_dir+"/"+a+".sdf"
        cmd.do(command)
        cmd.do("set stick_ball, on;")
        cmd.do("set stick_radius=0.25;")
        cmd.do("set stick_ball_ratio, 1.6;")
        cmd.center(a)
        cmd.zoom(a,1)
        cmd.do("set depth_cue, 0;")
        cmd.do("set bg_rgb,[1,1,1];")
        cmd.do("set ray_shadows,0;")
        cmd.do("set valence, 1;")
        cmd.do("set valence_mode, 1;")
        cmd.do("set valence_size, 0.2;")
        cmd.do("color green, (name C*)")
        cmd.do("color atomic, (not elem C)")
        cmd.do("color purple, (elem I)")
        cmd.do("color orange, (elem Br)")
        cmd.do("color cyan, (elem Cl)")
        cmd.do("color deepsalmon, (elem F)")
        command = self.png_dir+"/"+i+".png"
        cmd.png(command, width=300, height=300, dpi=600)
        cmd.rotate("x","90")
        cmd.zoom(a,1)

    def png_mol_3D_cube(self,a):
        cmd.delete('all')
        command = "load "+self.ligand_dir+"/"+a+".pdb"
        cmd.do(command)
        cmd.do("set stick_ball, on;")
        # cmd.do("set stick_radius=0.12;")
        cmd.do("set stick_ball_ratio, 4;")
        cmd.hide("sticks", a)
        cmd.show("lines", a)
        cmd.do("set sphere_scale, 0.2, (all);")
        cmd.do("show spheres;")
        cmd.do("set line_width, 2;")
        cmd.center(a)
        cmd.zoom(a,2)
        cmd.do("set depth_cue, 0;")
        cmd.do("set bg_rgb,[1,1,1];")
        cmd.do("set ray_shadows,0;")
        cmd.do("set valence, 1;")
        cmd.do("set valence_mode, 1;")
        cmd.do("set valence_size, 0.2;")
        cmd.do("color green, (name C*)")
        cmd.do("color atomic, (not elem C)")
        cmd.do("color purple, (elem I)")
        cmd.do("color orange, (elem Br)")
        cmd.do("color cyan, (elem Cl)")
        cmd.do("color deepsalmon, (elem F)")
        command = self.png_dir+"/"+i+"_1.png"
        cmd.png(command, width=300, height=300, dpi=600)
        cmd.rotate("x","90")
        cmd.zoom(a,2)
        command = self.png_dir+"/"+i+"_2.png"
        cmd.png(command, width=300, height=300, dpi=600)
        cmd.rotate("x","90")
        cmd.zoom(a,2)
        command = self.png_dir+"/"+i+"_3.png"
        cmd.png(command, width=300, height=300, dpi=600)
        cmd.rotate("x","90")
        cmd.zoom(a,2)
        command = self.png_dir+"/"+i+"_4.png"
        cmd.png(command, width=300, height=300, dpi=600)
        cmd.rotate("x","90")
        cmd.rotate("y","90")
        cmd.zoom(a,2)
        command = self.png_dir+"/"+i+"_5.png"
        cmd.png(command, width=300, height=300, dpi=600)
        cmd.rotate("y","180")
        cmd.zoom(a,2)
        command = self.png_dir+"/"+i+"_6.png"
        cmd.png(command, width=300, height=300, dpi=600)
        cmd.rotate("y","90")
        cmd.delete(a)



    def png_mol_3D_tetra(self):
        cmd.delete('all')
        command = "load " + self.ligand_dir + "/" + a + ".pdb"
        cmd.do(command)
        cmd.do("set stick_ball, on;")
        # cmd.do("set stick_radius=0.12;")
        cmd.do("set stick_ball_ratio, 4;")
        cmd.hide("sticks", a)
        cmd.show("lines", a)
        cmd.do("set sphere_scale, 0.2, (all);")
        cmd.do("show spheres;")
        cmd.do("set line_width, 2;")
        cmd.center(a)
        cmd.zoom(a, 2)
        cmd.do("set depth_cue, 0;")
        cmd.do("set bg_rgb,[1,1,1];")
        cmd.do("set ray_shadows, 0;")
        cmd.do("set valence, 1;")
        cmd.do("set valence_mode, 1;")
        cmd.do("set valence_size, 0.2;")
        cmd.do("color green, (name C*)")
        cmd.do("color atomic, (not elem C)")
        cmd.do("color purple, (elem I)")
        cmd.do("color orange, (elem Br)")
        cmd.do("color cyan, (elem Cl)")
        cmd.do("color deepsalmon, (elem F)")

        # Capture the four sides of a tetrahedron
        cmd.rotate("x", "0")  # Reset rotation along x-axis
        cmd.rotate("y", "0")  # Reset rotation along y-axis
        cmd.rotate("z", "0")  # Reset rotation along z-axis

        cmd.rotate("x", "0")
        cmd.rotate("y", "0")
        cmd.rotate("z", "0")
        cmd.zoom(a, 2)
        command = self.png_dir + "/" + a + "_1.png"
        cmd.png(command, width=300, height=300, dpi=600)

        cmd.rotate("x", "120")
        cmd.rotate("y", "0")
        cmd.rotate("z", "0")
        cmd.zoom(a, 2)
        command = self.png_dir + "/" + a + "_2.png"
        cmd.png(command, width=300, height=300, dpi=600)

        cmd.rotate("x", "120")
        cmd.rotate("y", "0")
        cmd.rotate("z", "0")
        cmd.zoom(a, 2)
        command = self.png_dir + "/" + a + "_3.png"
        cmd.png(command, width=300, height=300, dpi=600)

        cmd.rotate("x", "120")
        cmd.rotate("y", "120")
        cmd.rotate("z", "0")
        cmd.zoom(a, 2)
        command = self.png_dir + "/" + a + "_4.png"
        cmd.png(command, width=300, height=300, dpi=600)

        cmd.delete(a)

    def fit(self):

      if self.type_image==0:
        ligand_name = []
        for i in sorted(glob.glob("/content/drive/MyDrive/Dataset_ALK 2.0/ALK mới/Regression/2d_sdf/data_test/*.sdf")):
          ligand_name.append(i[len(self.ligand_dir)+1:-4])

        for i in ligand_name:
            self.png_mol_2D(i)


      elif self.type_image==1 or self.type_image==2:
        ligand_name=[]
        for i in sorted(glob.glob("/content/drive/MyDrive/Dataset_ALK 2.0/ALK mới/Regression/3d_pdb/data_valid/*.pdb")):
            ligand_name.append(i[len(self.ligand_dir)+1:-4])

        if self.type_image==1:
          for i in ligand_name:
            self.png_mol_3D_cube(i)
        else:
          for i in ligand_name:
            self.png_mol_3D_tetra(i)

      else:
          print('Check again! Dont have option you need')
