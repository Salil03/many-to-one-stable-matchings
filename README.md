# Lattice of Stable Matchings for the College-Admissions Problem

This tool generates the lattice of stable matchings for the College-Admissions Problem. This code is a modification of [Simon Mauras's repo](https://github.com/simon-mauras/stable-matchings/tree/master/Lattice) for the stable marriage problem. Check it out for more such tools.

The table on the left shows the preferences for the canonical one-to-one instance. The graph in the middle shows the set of rotations and the graph on the right is the lattice of stable matchings arranged from firm-optimal(top) to worker-optimal(bottom).

* This tool requires dot (package graphviz on linux): https://www.graphviz.org/
<!-- * Edit the preferences of firms and workers(`vvi preffirm` and `vvi prefworker`) and capacities (`vi capacity`) in `main.cpp`.  -->
* Edit the instance (preferences and capacities) in `instance.txt`. For reference on what the format for specifying the instance is, refer to `instanceFormat.txt`.
<!-- * To generate an animation, just run `bash gen.sh` in a linux command line. -->
* Run `python manage.py` and then open `http://localhost:8000/`. 
* Modify capacities using the + and - symbols for each of the firm. Please allow some time for new lattice to be calculated and displayed.

Example given in Gusfield and Irving's book:


![example](https://github.com/Salil03/many-to-one-stable-matchings/assets/32109637/ed22a47a-d7d2-4005-a651-2455f84334a8)
