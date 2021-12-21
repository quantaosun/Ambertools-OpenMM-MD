# Ambertools-OpenMM-MD
This repository try to introduce molecular dynamics of protein-ligand complex to more people, especially those beginners, with all open-sourced resouces.
Ambertools (https://ambermd.org/AmberTools.php), H++ web server (http://biophysics.cs.vt.edu/), openmm (https://openmm.org/), and py3Dmol (https://github.com/avirshup/py3dmol), as well as open babel (https://github.com/openbabel/openbabel) are the main components contained in this protocal. The force field used is Amber (https://ambermd.org/AmberModels.php) for protein and GAFF (http://ambermd.org/antechamber/gaff.html) for small molecule.

This is designed only for learning purpose, anyone with commercial purpose might need to check out by themself if they need a commercial license in relation to some certain package, even these are all "open source".
 

# Usage
It is assumed you already got anaconda installed on your linux computer, visit https://docs.anaconda.com/# to get one if not installed.
```
git clone https://github.com/quantaosun/Ambertools-OpenMM-MD.git
```
```
cd Ambertools-OpenMM-MD
```
Create a new Conda environment named "Ambertools-OpenMM-MD " (noly run this for the 1st time)
```
conda create -n Ambertools-OpenMM-MD python=3.7 
```
Activate the new environment 
```
conda activate Ambertools-OpenMM-MD
```
In the new environment, install jupyter notebook (only run this for the 1st time)
```
conda install jupyter
```
Start jupyter notebook and run the "Amber-OpenMM-MD.ipynb"
```
jupyter notebook Ambertools-OpenMM-MD.ipynb
```
Select the first code cell, then click "run" button above, all the codes inside first block will be executed, run all the cells one by one until simulation finish.
![image](https://user-images.githubusercontent.com/75652473/146884751-256a5668-4de9-4818-9631-29c3984d41a2.png)

If you have problem opening jupyter notebook from your "Amber-OpenMM-MD" environment, try 
```
conda remove jupyter
```
```
sudo apt install jupyter
```
```
jupyter notebook Ambertools-OpenMM-MD.ipynb
```
