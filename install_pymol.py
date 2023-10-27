from IPython.utils import io
import tqdm.notebook
import os
class install_pymol:
    def install_Pymol_source(self):
        total = 100
        with tqdm.notebook.tqdm(total=total) as pbar:
            with io.capture_output() as captured:
        
                !pip install -q condacolab
                import condacolab
                condacolab.install()
                pbar.update(10)
        
                import sys
                sys.path.append('/usr/local/lib/python3.7/site-packages/')
                pbar.update(20)
        
                # Install PyMOL
                %shell mamba install pymol-open-source --yes
        
                pbar.update(100)
