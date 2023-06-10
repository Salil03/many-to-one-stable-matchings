# Lattice of Stable Matchings for the College-Admissions Problem

This tool generates the lattice of stable matchings for the College-Admissions Problem. This code is a slight modification of [Simon Mauras's excellent repo] for the stable marriage problem.

The table on the left shows the preferences for the canonical one-to-one instance. The graph in the middle shows the set of rotations and the graph on the right is the lattice of stable matchings arranged from firm-optimal(top) to worker-optimal(bottom).

* This tool requires dot (package graphviz on linux): https://www.graphviz.org/
* Edit the preferences of firms and workers(`vvi preffirm` and `vvi prefworker`) in `main.cpp`. 
* To generate an animation, just run `bash gen.sh` in a linux command line.
* Start a http server with `python3 -m http.server 8001` and then open `http://0.0.0.0:8001/result/`.

Example given in Gusfield and Irving's book:


