# Palladium Nanocluster Lattice Kinetic Monte Carlo Simulation Sample Inputs

## PdCO:
Simulations of Pd as both scattered single atoms and Pd4_3d clusters on a lattice with CO pressure.
- Temperature: 300K
- Pressure: e-1 bar
- Configuration: Pd4_3d x6

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
	