# graphen-verstehen
Repo zum Seminar/Praktikum


# Grober Plan

## WP 1

* the distance matrix should be provided to the recognition algorithm in the form of history files
    * from this history file the standard recognition can reconstruct the distance matrix
        * erdbeermet.simulation.load(filename).distances()
    * our recognition algorithm can then use that distance matrix
    * the first 4 leaves of the simulation can also be read from the history file
        > Classify whether the final 4-leaf map after recognition matches the first 4 leaves of the simulation
        > Write a wrapper function that passes the first 4 or respectively 3 leaves of the simulation as B and benchmarks results as in WP2.
* several configs are needed
    * how about example_config.yaml ?
    * we can pass this to the recognition pipeline as input
        * this makes the parameters more readable and the executions more reproducible


# WP1: Simulation

What are these parameters?
## Circular
> If set to True, the resulting distance matrix is guaranteed to be a circular type R matrix. The default is False.

TODO Would that mean the resulting distance matrix could always be used to reconstruct the r-step history?

## Clockwise
> If set to True, the distance increment is equal for all items within each iteration (comprising a merge or branching event and the distance increments) and only varies between iteration. The default is False, in which case the increments are also drawn independently for the items within an iteration.



# Notiz 05.01. 14Uhr meeting

for every combination of ....
20.000 bedeutet 20.000 Datasets (history files)
 
6+ leaves verwenden


Measure the divergence of the reconstructed steps....

WP2
choose a random positive one if it exists
(das bezieht sich auch auf das classify whether the final 4 leaf map is correct)


Ergaenzung zu common triplets:
die alphas muessen wir nicht checken.
(die Annahme der Professoren ist, dass es nicht vorkommen kann, dass ein falsches alpha in der Recognition entsteht)
da wir uns nicht um die Alphas kuemmern, muessen wir auch nicht die Reihenfolge der Parents beachten.

Ein Check des Alphas waere eine gute Extraleistung, laut Professoren.


Freitag 14 Uhr nochmal

# Links
* [Erdbeermet Repo](https://github.com/david-schaller/Erdbeermet#generation-of-scenarios)
* [graphen-verstehen Repo](https://github.com/geschnee/graphen-verstehen)
* [Praktikumsdokumente](http://silo.bioinf.uni-leipzig.de/GTPraktikumRMaps/)
