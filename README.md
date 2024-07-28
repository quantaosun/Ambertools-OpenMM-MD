# Ambertools-OpenMM-MD

This repository tries to introduce the molecular dynamics of the protein-ligand complex to more people, especially beginners, through open-sourced resources.
- Ambertools (https://ambermd.org/AmberTools.php),
-  H++ web server (http://newbiophysics.cs.vt.edu/H++/),
-  Openmm (https://openmm.org/), and py3Dmol (https://github.com/avirshup/py3dmol), as well as
-  Open babel (https://github.com/openbabel/openbabel) are the main component of this protocol.
-  The force field used is Amber (https://ambermd.org/AmberModels.php) for protein and GAFF (http://ambermd.org/antechamber/gaff.html) for small molecules.
 
# How to use
[![My Skills](https://skillicons.dev/icons?i=apple,linux,anaconda&perline=3)](https://skillicons.dev)

It is assumed you already have Anaconda/Miniconda installed on your Linux/Mac computer.
```
git clone https://github.com/quantaosun/Ambertools-OpenMM-MD.git
```
```
cd Ambertools-OpenMM-MD
```
Create a new Conda environment named "Ambertools-OpenMM-MD " (only run this for the 1st time)
```
conda create -n Ambertools-OpenMM-MD python=3.8.8 
```
Activate the new environment. 
```
Conda activate Ambertools-OpenMM-MD
```
In the new environment, install jupyter notebook (only run this for the 1st time)
```
conda install jupyter
```
Start jupyter notebook and run the "Amber-OpenMM-MD.ipynb"
```
jupyter notebook Ambertools-OpenMM-MD.ipynb
```

# Result Analysis

- Simulation quality analysis. It is possible to use VMD to do all related analyses, but to me, it is tedious and lacks beauty. I strongly recommend people use Bio3D in Rstudio. Download and install a package called Rstudio. It provides you with an R computer language environment. In that environment, installing Bio3D and then finishing all the plots is easy.
- Simulated Protein-ligand interaction analysis. You could use this Pymol script. https://github.com/quantaosun/Pymol_Script

# MMGBSA/PBSA free energy calculation and per-residue decomposition

The energy-related section is not included in the notebook since I added this later; I put it here instead. Note that if some of the file names in your simulation have been modified, you also need to modify the names of the files below inside the coding cell.

For new users, it is suggested that GB-based decomposition be tried before PB due to its difficulty and longer time requirement.
The following script takes 3RY2, biotin-bound protein as an example. The simulation was finished by [making-it-rain ](https://github.com/pablo-arantes/making-it-rain/blob/main/Protein_ligand.ipynb) online for free. We can use it the same way here. Changing the input name is fine. Note that the code below does the binding free energy decomposition to all your protein residues, not on your binding pocket residues only, so you might need to extract those residues yourself for analysis.


1. Create a new file called mmpbsa.in, and write inside. ( Copied from making-it-rain, the format is slightly different from that of Amber tutorial)

```
&general 
  endframe=1000,  interval=100, strip_mask=:WAT:Na+:Cl-:Mg+:K+, 
/ 
&gb 
 igb=2, saltcon=0.15, 
/ 

&decomp

 idecomp=1,
/
```
The decomposed data is saved in a file called FINAL_DECOMP_MMPBSA.dat

2. Run ante-MMPBSA.py

But first, let's define Amber's home


```
source /usr/local/amber.sh
```


```
ante-MMPBSA.py  -p SYS_gaff2.prmtop -c com.prmtop -r rec.prmtop -l ligand.prmtop -s :WAT:Na+:Cl-:Mg+:K+ -n :LIG --radii mbondi2 
```

3. Run MMPBSA.py, write the result to a file called FINAL_RESULTS_MMPBSA.dat


```
MMPBSA.py -O -i mmpbsa.in -o FINAL_RESULTS_MMPBSA_decomposition.dat -sp  SYS_gaff2.prmtop -cp com.prmtop -rp rec.prmtop -lp ligand.prmtop -y prot_lig_prod_all.dcd
```

# Known Issues

- H++ webserver troubleshooting: If you consistently encounter problems with missing residues that PDBfixer can not fix, you are suggested to use predicted structures from AlphaFold2 https://alphafold.ebi.ac.uk/ (for example, right) instead of PDB bank version (for example, left). There will be some weird-looking branches, but that is fine to carry on. Please delete any repeated chains if it has multiple chains to increase simulation speed and minimise the chances of having unnecessary errors about multiple chains.
![image](https://user-images.githubusercontent.com/75652473/171746366-5f17177f-b69f-42f4-815c-64b06bd2b074.png)

- Ambertools' "reduce" and open babel sometimes gives the wrong H number. For example, it was accidentally adding an H to a carbonyl group or adding an extra H to an aromatic ring it shouldn't have. An error will be saying, "The electro number is odd." In this case, you should carefully check the chemical structure after adding hydrogen. If "reduce" or Obabel keeps adding the wrong number, please consider using Pymol's "h_add" to add H to small molecules and compare it to the result out of "reduce" or Obabel. The error is currently unclear as to why it happens, but the error always adds more H, not less, to the best of my knowledge.

<img width="766" alt="image" src="https://user-images.githubusercontent.com/75652473/171793595-575c067c-6de3-4f59-ae31-fdfc1021be18.png">
