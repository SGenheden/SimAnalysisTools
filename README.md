SimAnalysisTools
=========

A tool to analyze molecular simulations

Description
===========
SimAnalysisTools is a package for analyzing your molecular simulations.

Foremost, it is a wrapper for the [MDAnalysis](http://www.mdanalysis.org/) package to perform several analysis of coordinate trajectories. This program is called `simanalysis`

It also contains other tools. 

Installation
============
To install this tool, clone or download the git repository. Change to the downloaded directory and install the software with

```
python setup.py install
```

Examples
========

To find the available commands

```
simanalysis -h
```

To find the help of individual commands

```
simanalysis rmsd -h
```

To analyze the RMSD of a protein

```
simanalysis rmsd -f sim.txtc -s struct.gro
```

To analyze common membrane properties

```
simanalysis memprop -f sim.txt -s struct.gro --lipidmask "resname DOPC"
```
