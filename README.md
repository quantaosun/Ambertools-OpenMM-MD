# OpenMM_AMBERTOOLS

# Usage
It is assumed you already got anaconda installed on your linux computer, visit https://docs.anaconda.com/# to get one.
```
git clone https://github.com/quantaosun/OpenMM_AMBERTOOLS
```
```
cd NAMD-MD
```
Create a new Conda environment named "OpnenMM_AMBERTOOLS"
```
conda create -n NAMD-MD python=3.7
```
Activate the new environment 
```
conda activate OpnenMM_AMBERTOOLS
```
Install openmm
```
conda install -c conda-forge openmm
```

Install Ambertools
```
conda install -c conda-forge ambertools=21 compilers
```

```
In the new environment, install jupyter notebook
```
conda install jupyter
```
Start jupyter notebook and run the "Amber_local.ipynb"
```
jupyter notebook NAMD-MD_local.ipynb
```
