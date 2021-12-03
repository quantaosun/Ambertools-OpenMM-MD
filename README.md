# Ambertools-OpenMM-MD
The author of this repository try to introduce molecular dynamics of protein-ligand complex to more people, especially those beginners, with all open-sourced resouces.
Ambertools (https://ambermd.org/AmberTools.php), H++ web server (http://biophysics.cs.vt.edu/), openmm (https://openmm.org/), and py3Dmol (https://github.com/avirshup/py3dmol), as well as open babel (https://github.com/openbabel/openbabel) are the main components contained in this protocal. The force file package used is Amber (https://ambermd.org/AmberModels.php) for protein and GAFF (http://ambermd.org/antechamber/gaff.html) for small molecule.

This is designed only for learning purpose, anyone with commercial purpose might need to check out by themself if they need a commercial license in relation to some certain package, even these are all "open source".
 

# Usage
It is assumed you already got anaconda installed on your linux computer, visit https://docs.anaconda.com/# to get one if not installed.
```
git clone https://github.com/quantaosun/Ambertools-OpenMM-MD.git
```
```
cd Ambertools-OpenMM-MD
```
Create a new Conda environment named "Ambertools-OpenMM-MD "
```
conda create -n Ambertools-OpenMM-MD python=3.7
```
Activate the new environment 
```
conda activate Ambertools-OpenMM-MD
```
In the new environment, install jupyter notebook
```
conda install jupyter
```
Start jupyter notebook and run the "Amber-OpenMM-MD.ipynb"
```
jupyter notebook Ambertools-OpenMM-MD.ipynb
```
# If you have problem opening jupyter notebook in your "Amber-OpenMM-MD" environment, try 
```
conda remove jupyter
```
```
sudo apt install jupyter
```
```
jupyter notebook
```
# Note, when you excute openmm-setup, your web browser will be automaticlly open, and you shoud do some work there outside of the notebook itself.
