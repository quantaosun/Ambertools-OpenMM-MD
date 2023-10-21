# This script is written by Quantao/quantaosun@gmail.com or Github:quantaosun for OpenMM simulation,2023.

from simtk.openmm import *
from simtk.openmm.app import *
from simtk.unit import *
from sys import stdout
from openmm.app import PDBFile # for final frame pdb generation

# Input Files

prmtop = AmberPrmtopFile('SYS_gaff2.prmtop')
inpcrd = AmberInpcrdFile('SYS_gaff2.crd')

# System Configuration

nonbondedMethod = PME
nonbondedCutoff = 1.0*nanometers
ewaldErrorTolerance = 0.0005
constraints = HBonds
rigidWater = True
constraintTolerance = 0.000001

# Integration Options

dt = 0.002*picoseconds
temperature = 300*kelvin
friction = 1.0/picosecond
pressure = 1.0*atmospheres
barostatInterval = 25

# Simulation Options

# long simulation (default)
#minimizationSteps = 10000
#productionSteps = 50000000  # 100 ns
#equilibrationSteps = 20000000  # 20 ns
###################################################
# medium simulation
minimizationSteps = 10000
productionSteps = 25000000  # 50 ns
equilibrationSteps = 10000000  # 10 ns
###################################################
# short simulation
#minimizationSteps = 10000
#productionSteps = 10000000  # 10 ns
#equilibrationSteps = 4000000  # 2 ns
##################################################

platform = Platform.getPlatformByName('CUDA')
platformProperties = {'Precision': 'single'}
dcdReporter = DCDReporter('prot_lig_prod.dcd', 10000)

minimizationDataReporter = StateDataReporter('stdout', 100, totalSteps=minimizationSteps,
    step=True, time=True, speed=True, progress=True, remainingTime=True, potentialEnergy=True, temperature=True, separator='\t')

equilibrationDataReporter = StateDataReporter(stdout, 5000, totalSteps=equilibrationSteps,
    step=True, time=True, speed=True, progress=True, remainingTime=True, potentialEnergy=True, temperature=True, separator='\t')
productionReporter = StateDataReporter(stdout, 5000, totalSteps=productionSteps,
    step=True, time=True, speed=True, progress=True, remainingTime=True, temperature=True, separator='\t')

dataReporter = StateDataReporter('prot_lig_prod.log', 1000, totalSteps=productionSteps,
    step=True, time=True, speed=True, progress=True, remainingTime=True, potentialEnergy=True, temperature=True, separator='\t')

# Prepare the Simulation

print('Starting molecular dynamics simulaiton......')
print('############################################################################')
print('##   This script written by Quantao Sun based with official OpenMM documentation/Github:quantaosun. Please cite OpenMM paper, and consider cite my github repo link if used in any publications  ####') 
print('Initialising molecular dynamics....')
print ('With GPU like RTX3080 or above, the simulaiton speed for a typical kinase protein should be greater than 200 ns/day')

import time
# Sleep for 10 seconds
time.sleep(20)

print('############################################################################')
print('Building system...')
topology = prmtop.topology
positions = inpcrd.positions
system = prmtop.createSystem(nonbondedMethod=nonbondedMethod, nonbondedCutoff=nonbondedCutoff,
    constraints=constraints, rigidWater=rigidWater, ewaldErrorTolerance=ewaldErrorTolerance)
system.addForce(MonteCarloBarostat(pressure, temperature, barostatInterval))
integrator = LangevinIntegrator(temperature, friction, dt)
integrator.setConstraintTolerance(constraintTolerance)
simulation = Simulation(topology, system, integrator, platform, platformProperties)
simulation.context.setPositions(positions)
if inpcrd.boxVectors is not None:
    simulation.context.setPeriodicBoxVectors(*inpcrd.boxVectors)

#########################################################

content = """
# Simulation Options
###################################################
# medium simulation
minimizationSteps = 10000
productionSteps = 25000000  # 50 ns
equilibrationSteps = 10000000  # 10 ns
###################################################
##################################################

If you wish to change the simulation time, please modify
these three parameters inside the .py file

If you have not changed anything the default setting is 10000
steps of minimisation, followed by 10 ns of equilibration and 
then 50 ns of produciton.

At the end of this simulation, the final frame will be saved as
prot_lig_1.pdb, the trajecotry will be saved as prot_lig.dcd.

You can view the trajectory with pymol by loading SYS_gaff2.prmtop
and the trajectory file.
"""

print(content)


# Minimize and Equilibrate

print('Performing energy minimization...')
#simulation.minimizeEnergy()
simulation.minimizeEnergy(maxIterations=minimizationSteps)
simulation.reporters.clear()
print('##############################################')
print('Starting Equilibrating...')
simulation.context.setVelocitiesToTemperature(temperature)
simulation.reporters.append(equilibrationDataReporter)
simulation.step(equilibrationSteps) 
simulation.reporters.clear()

# Production Simulate
print('##############################################')
print('Production Simulating...')
simulation.reporters.append(productionReporter) # on screen display.
simulation.reporters.append(dcdReporter)
simulation.reporters.append(dataReporter)
simulation.currentStep = 0
simulation.step(productionSteps)
print('##############################################')
# Write the last frame as a PDB file
print('Saving the last frame as PDB file...')
positions = simulation.context.getState(getPositions=True).getPositions()
PDBFile.writeFile(topology, positions, open('prod_lig_1.pdb', 'w'))
