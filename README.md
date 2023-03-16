# Ambertools-OpenMM-MD

#################### Trouble Shooting ################
From time to time, there might be some issue for openmm-setup to open correctly, these typically are caused by third party dependencies changes over time
You can update some certain dependencies if necessary, like 

```
conda update itsdangerous

````
############################################################
## step 1, Prepare protein in your browser  by providing a pdb bank structure

https://user-images.githubusercontent.com/75652473/202853115-39f5eb60-02b8-4571-bc41-cf30ec2e3e6c.mov

## Step 2, Continue prepare protein in your browser with the result from step 1 

https://user-images.githubusercontent.com/75652473/202853190-16beebc3-4b39-4a26-a488-a6893b086ba2.mov


## Why do you need just another simulation workflow, well, this one tries to allow you to click your mouse (sorry guys not 100% clicking) to finish an MD simulation instead of using crazy lines after lines of commands. (Only macOS and Linux are supported. This is a repository designed primarily for local use). 

## As you can see from the two clips, we try to do everything with your browser, so you don't have to install anything. (You do have to install the conda env but you can always delete them all by ```conda env remove```)

In a perfect world, there are only three things you need to change for your PDB bank structure. Afer that, techinically, all the other parts should be done by clicking your mouse.

1. your laptop's path

```
import sys
sys.path.append('/Users/quantaosun/opt/anaconda3/lib/python3.8/site-packages')
```
2. PDB ID 
```
PDB_ID = "7L10" ```
```

 3. Small molecule ID
 ```
 !awk '$4=="XEY"' 7L10.pdb > ligand1.pdb 
 ```

# Warning. This notebook will directly use your local CPU to run a Molecular Dynamic on your Mac or Linux for a learning purpose. But personally, I probably will not do that. It will get hot and slow. It may be fine for the short MD like this one, but generally, we do that job with cloud computing or computer clusters. 

This repository try to introduce molecular dynamics of the protein-ligand complex to more people, especially those beginners, with all open-sourced resources.
Ambertools (https://ambermd.org/AmberTools.php), H++ web server (http://newbiophysics.cs.vt.edu/H++/), openmm (https://openmm.org/), and py3Dmol (https://github.com/avirshup/py3dmol), as well as open babel (https://github.com/openbabel/openbabel) are the main components of this protocal. The force field used is Amber (https://ambermd.org/AmberModels.php) for protein and GAFF (http://ambermd.org/antechamber/gaff.html) for small molecule.

This is designed only for learning purposes. Anyone with commercial purposes might need to check out by themself if they need a commercial license for some certain package, even if these are all "open source".
 

# Usage
It is assumed you already got anaconda installed on your Linux/Mac computer. Visit https://docs.anaconda.com/# to get one if not installed.
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

# Result Analysis

It is possible to use VMD to do all related analyses, but to me, it is tedious, and there is a lack of beauty. I strongly recommend people use Bio3D in Rstudio, so download and install a package called Rstudio. It provides you with an R computer language environment. In that environment, installing Bio3D and then finishing all the plots there is easy.

# MMGBSA/PBSA free energy calculation and per-residue decomposition

The energy-related section is not included in the notebook since I added this later, I put it here instead. Note if some of the file names in your simulation have been modified, you also need to modify the name of the files below inside the coding cell.

It is suggested for new users, GB based decomposition be tried before PB due to its difficulty and longer time would need.
The following script takes 3RY2, biotin-bound protein as an example, the simulation was finished by [making-it-rain ](https://github.com/pablo-arantes/making-it-rain/blob/main/Protein_ligand.ipynb) online for free. We can use it the same way here. Changing the input name is fine. Note the code below does the binding free energy decomposition to all your protein residues, not on your binding pocket residues only, so you might need to extract those binding residues yourself for analysis.


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
## If you can not open your notebook for the very first time, try upgrading something as suggested in
https://github.com/jupyter/notebook/issues/5014 

```
pip install --upgrade jupyter_client
```
There will be some little things like if you use macOS, you need to deal with ```wget``` usually is not installed by default. so you may need to use ```brew``` to install ```wget```. Have a look at https://stackoverflow.com/questions/33886917/how-to-install-wget-in-macos

# Simulate with Google's free GPU if you don't have a good local computer to support you finish your work.
<img width="1015" alt="image" src="https://user-images.githubusercontent.com/75652473/171800298-8b9ca368-cdbc-440e-8a79-87ba10423bf7.png">

# WARNING 

Warning1, H++ webserver troubleshooting, If you consistently meet problems with missing residues that PDBfixer can not fix, you are suggested to use predicted structures from AlphaFold2 https://alphafold.ebi.ac.uk/ (for example, right) instead of PDB bank version (for example, left). There will be some weird-looking branches, but that is fine to carry on. And please delete any repeated chains if it has multiple chains to increase simulation speed, and also to minimise the chances of having unnecessary errors about multiple chains.
![image](https://user-images.githubusercontent.com/75652473/171746366-5f17177f-b69f-42f4-815c-64b06bd2b074.png)

Warning2. Ambertools' "reduce" and open babel sometimes gives the wrong H number. For example, it was accidentally adding an H to a carbonyl group or adding an extra H to an aromatic ring it shouldn't have. There will be an error saying, "electro number is odd" in this case, you should carefully check the chemical structure after hydrogen addition. If "reduce" or Obabel keeps adding the wrong number, please consider using Pymol's "h_add" to add H to small molecules and compare it to the result out of "reduce" or Obabel. The error is currently unclear why it happens, but the error always adds more H, not less, to the best of my knowledge.

<img width="766" alt="image" src="https://user-images.githubusercontent.com/75652473/171793595-575c067c-6de3-4f59-ae31-fdfc1021be18.png">
