# Palladium Nanocluster Lattice Kinetic Monte Carlo Simulation Sample Inputs

These folders contain sample Zacros simulation inputs and simple graphics produced from outputs 
for Pd nanocluster formation simulations.

## Adsorption_only:
- Preset cluster of Pd5_3d including only CO adsorption and desorption events.

## Pd_only:
- Simulations of Pd as both scattered single atoms and Pd4_3d clusters on a lattice without CO pressure.

## PdCO:
- Simulations of Pd as both scattered single atoms and Pd4_3d clusters on a lattice with CO pressure.
	
## Included Files:
### Inputs:
- energetics_input - energy interactions between static molecules
- lattice_input - size and sites of unit cell
- mechanism_input - how molecules can move
- simulation_input - simulation conditions, including temperature, pressure, data collection, and end conditions
- state_input - initial positioning of molecules
	
### Graphics:
- lattice_frames_3D - series of snapshots of lattice state
- elem_step_freqs - counts of how many times each event occured
- gas_spec_vs_time - change in gas species throughout simulation
- lattice - empty lattice, shows unit cell locations
- surf_spec_vs_time - shows change in surface species throughout simulation
	
While the names of simulation folders reflect their conditions, additional information is provided in the accompanying README.