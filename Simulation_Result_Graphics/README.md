# Palladium Nanocluster Lattice Kinetic Monte Carlo Simulation Results

Included are graphics based on the results of simulations.
Simulations are sorted by three replicates with CO pressure (Dup0, Dup1, Dup2) and without (Pd Only).
The output files fromZacros were too large to be included.

Information about each simulation can be found in the folder name or README.

## The results of each simulation include some or all of the following graphics and data CSVs:
Naming of the files may also include identifying information of the simulation
### Graphics:
- CO_count - count of CO in each site at the end of the simulation
- CO_timeline - plot of the change in CO and Pd counts throughout the simulation
- CO_timeline_limited - plot of the change in CO and Pd counts throughout 60 seconds at 300K or 1 second at 700K	
- COratio_timeline - plot of the change in CO per Pd ratio throughout the simulation
- COratio_timeline_limited - plot of the change in CO per Pd ratio throughout 60 seconds at 300K or 1 second at 700K
- event_count - number of times each event occuredevent_count_R#
- number of times each event occured in the Rth round of the simulation
- event_waits_avg - average time per event across all rounds
- event_waits_first - average time per event for the first round each event occurs
- event_waits_250 - average time per event for the first round each event occurs at least 250 times
- event_waits_R# - average time per event for the Rth round of the simulation
- event_waits_unscaled_avg - average time per event accounting for differences in scaling of pre-exponential factors
- Site_Ratio_timeline - change in counts of Pd and CO in each site type throughout the simulation, along with the CO per Pd ratio
- Site_Ratio_timeline_limited - change in counts of Pd and CO in each site type throughout 60 seconds at 300K or 1 second at 700K, along with the CO per Pd ratio
- Site_timeline - change in counts of Pd and CO in each site type throughout the simulation
- Site_timeline_limited - change in counts of Pd and CO in each site type throughout 60 seconds at 300K or 1 second at 700K
	
### Data:
- CO_Pd_ratio_(Simulation) - change in the CO per Pd ratio throughout the simulation
- Event_count_(Simulation) - number of times each event occured in each round of the simulation
- Event_scale_(Simulation) - Pre-exponential factors of each Pd event throughout each round of the simulation
- Event_wait_(Simulation) - time per event for each event for each round of the simulation
- Site_timeline_full_(Simulation) - counts of Pd and CO in each site type, with CO sites separated by level
- Site_timeline_(Simulation) - counts of Pd and CO in each site type, with CO sites separated by Pd coordination number

## Lattice Gifs
Animations showing development of nanoclusters
- 20 Single Pd atoms at 300K, 0.1 bar
- 6 Pd4_3d clusters at 300K, 0.1 bar
- Pd20 pyramid at 0 bar
