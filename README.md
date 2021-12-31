# Ambertools-OpenMM-MD
Please come back later until H++ server is up, since this repository relies on it to prepare the initial protein structure, this could be caused by network problem, outage or a website maintenance is in progress. If you could correctly prepare a starting protein PDB, you can still use all the content of the ipynb file, except protein processing at the beginning.
![image](https://user-images.githubusercontent.com/75652473/147806759-19602773-23d7-4afe-a4fc-ee6170c5b761.png)

This repository try to introduce molecular dynamics of protein-ligand complex to more people, especially those beginners, with all open-sourced resouces.
Ambertools (https://ambermd.org/AmberTools.php), H++ web server (http://biophysics.cs.vt.edu/), openmm (https://openmm.org/), and py3Dmol (https://github.com/avirshup/py3dmol), as well as open babel (https://github.com/openbabel/openbabel) are the main components of this protocal. The force field used is Amber (https://ambermd.org/AmberModels.php) for protein and GAFF (http://ambermd.org/antechamber/gaff.html) for small molecule.

This is designed only for learning purpose, anyone with commercial purpose might need to check out by themself if they need a commercial license in relation to some certain package, even these are all "open source".
 

# Usage
It is assumed you already got anaconda installed on your Linux/Mac computer, visit https://docs.anaconda.com/# to get one if not installed.
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
Select the first code cell, then click play button above, all the codes inside first block will be executed. Run all the cells in a sequencial manner.
![image](https://user-images.githubusercontent.com/75652473/146891584-fc35c91a-262e-4edb-834e-aa253ca7c236.png)
You are supposed to provide a PDB code, i.e, change 7L10 to your choice. When you run pdbfixer, pay attention to your browser, a new window should open, go there to
sanitise your protein by deleteling all waters, all hetero, keep only protein. After having finishing pdbfixer and save you clean protein, click the square botton next to play botton to stop the code cell, otherwise you will not allowed to move to next cell. （It is possible to simulate a doced pdb file, but not discussed here）
![image](https://user-images.githubusercontent.com/75652473/146885334-f549740d-8c72-46d4-8a52-e2c4d0dbd9d1.png)
Another cell need your modification is the ligand ID, it can be found from PDB bank, it is a three-letter code, change XEY to the new code, change 7L10.pdb to new pdb as well.
![image](https://user-images.githubusercontent.com/75652473/146888441-6c6bdd0b-69af-4431-a5b6-4346b4ceb566.png)
The rest cells can be run without interfere, until the very last one, similar to prvious pdbfixer step, a new windown will open in your browser, the last section of this whole process will be finished there. For the default 7L10 example, simulation speed is about 7.6 nano second per day, on Macpro 2020 (M1). 
![image](https://user-images.githubusercontent.com/75652473/146885748-2aeefba8-9a9a-401a-992b-e17590bf8f1d.png)

# Result Analysis

A very handy online tool could be https://usegalaxy.org.au/, it is essentially a web server based on Bio3D http://thegrantlab.org/bio3d/.

You can upload the complex.pdb and trajectory.dcd to get an RMSD image, which could tell you if the simulation has reach equilbrium or not. In this case, the simulation is not, due to very short time.

![image](https://user-images.githubusercontent.com/75652473/147025989-c66b3789-ea81-4f6f-aa27-402cc8aa4ce0.png)

For People who can read Chinese, I recommend you read my blog on 中文分析链接 https://zhuanlan.zhihu.com/p/448829436 which shows a local Mac way of analyzing the MD output with Bio3D in R language.

# Troubleshooting

If you have problem opening jupyter notebook from your "Amber-OpenMM-MD" environment, this might happen when you have run the workflow multiple times,try 
```
conda remove jupyter
```
```
sudo apt install jupyter
```
```
jupyter notebook Ambertools-OpenMM-MD.ipynb
```
