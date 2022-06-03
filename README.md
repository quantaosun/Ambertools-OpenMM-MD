# Ambertools-OpenMM-MD

# Run the simulation with Google's free GPU if you don't have a good local computer to support you finsh you work.
<img width="1015" alt="image" src="https://user-images.githubusercontent.com/75652473/171800298-8b9ca368-cdbc-440e-8a79-87ba10423bf7.png">

# WARNING 

Warning1, H++ webserver troubleshooting, If you consistently meet problems about missing residues that can not be fixed by PDBfixer, you are suggested to use predicted structures from AlphaFold2 https://alphafold.ebi.ac.uk/ (for example, right) instead of PDB bank version (for example, left). There will be some weird looking branches, but that is fine to carry on. And please delete any repeated chains if it has multiple chains, to increse simulation speed, also to minimise the chances to have unnecessary errors in relation to multiple chains.
![image](https://user-images.githubusercontent.com/75652473/171746366-5f17177f-b69f-42f4-815c-64b06bd2b074.png)

Warning2. Ambertools' "reduce" and open babel sometimes gives the wrong H number. For example, it was accidentally adding an H to a carbonyl group or adding an extra H to an aromatic ring it shouldn't. There will be an error saying "electro number is odd" in this case, you should carefully check the chemical structure after hydrogen addition. If "reduce" or Obabel keeps adding the wrong number, please consider using Pymol's "h_add" to add H to small molecules and compare to the result out of "reduce" or Obabel. The error is currently unclear why it happens, but the error always adds more H, not less, to the best of my knowledge.

<img width="766" alt="image" src="https://user-images.githubusercontent.com/75652473/171793595-575c067c-6de3-4f59-ae31-fdfc1021be18.png">


---------------------------------------------

This repository try to introduce molecular dynamics of protein-ligand complex to more people, especially those beginners, with all open-sourced resouces.
Ambertools (https://ambermd.org/AmberTools.php), H++ web server (http://newbiophysics.cs.vt.edu/H++/), openmm (https://openmm.org/), and py3Dmol (https://github.com/avirshup/py3dmol), as well as open babel (https://github.com/openbabel/openbabel) are the main components of this protocal. The force field used is Amber (https://ambermd.org/AmberModels.php) for protein and GAFF (http://ambermd.org/antechamber/gaff.html) for small molecule.

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

It is possible to use VMD to do all related analysis, but to me it is really tedious and there is a lack of beauty. I strongly recommend people to use Bio3D in Rstudio, so just download and install a package called Rstudio, it provides you with an R computer language environment, in that environment, install Bio3D, then finish all the plot there is really easy.

# MMGBSA/PBSA free energy calculation and per-residue decomposition

Energy related section is not included in the notebook since I added this later, I put it here instead. Note if some of the file names in your simulation has been modified you also need to modify the name of the files below inside the coding cell.

It is suggested for new users, GB based decomposition be tried before PB due to its difficulty and longer time would needed.
The following script takes 3RY2, biotin bound protein as an example, the simulation was finished by [making-it-rain ](https://github.com/pablo-arantes/making-it-rain/blob/main/Protein_ligand.ipynb) online for free. We can use exactly the same way here, just change the input name is fine, note the code below do the bindnig free energy decomposition to all you protein residues not on your bindng pocket residues only, so you might need to extract those binidng residues yourself for analysis.


1. Create a new file called mmpbsa.in, write inside. ( Copied from making-it-rain, the format is slightly different from that of Amber tutorial)

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

/
```
The decomposed data is saved in a file called FINAL_DECOMP_MMPBSA.dat

2. Run ante-MMPBSA.py

But first let's define Amber home


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


