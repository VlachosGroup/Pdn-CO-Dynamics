# Palladium Nanocluster Lattice Kinetic Monte Carlo Simulation Sample Inputs

## Adsorption_only:
- Only CO adsorption and desorption events.
- Temperature: 700K
- Pressure: e-1 bar
- Configuration: Pd5_3d

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
	