#!/usr/bin/env python
#this is the slightly modified version of example from gudhi library
# It can be used to generate persistent diagram and persistent barcode as well as the number of simplices.
import argparse
import gudhi
import time
import numpy as np
""" This file is part of the Gudhi Library - https://gudhi.inria.fr/ - which is released under MIT.
    See file LICENSE or go to https://gudhi.inria.fr/licensing/ for full license details.
    Author(s):       Vincent Rouvreau

    Copyright (C) 2016 Inria

    Modification(s):
      - YYYY/MM Author: Description of the modification
	  max_dimension provides the maximal betti number we need to compute
"""

__author__ = "Vincent Rouvreau"
__copyright__ = "Copyright (C) 2016 Inria"
__license__ = "MIT"

parser = argparse.ArgumentParser(
    description="RipsComplex creation from " "a distance matrix read in a csv file.",
    epilog="Example: "
    "example/rips_complex_diagram_persistence_from_distance_matrix_file_example.py "
    "-f ../data/distance_matrix/lower_triangular_distance_matrix.csv -s , -e 12.0 -d 3"
    "- Constructs a Rips complex with the "
    "distance matrix from the given csv file.",
)
parser.add_argument("-f", "--file", type=str, required=True, default="matrix_test.csv")
parser.add_argument("-s", "--separator", type=str, required=True, default=",")
parser.add_argument("-e", "--max_edge_length", type=int, default=56)
# max_edge_length type from float to int
parser.add_argument("-d", "--max_dimension", type=int, default=5) 
parser.add_argument("-b", "--band", type=int, default=0.0)
parser.add_argument(
    "--no-diagram",
    default=False,
    action="store_true",
    help="Flag for not to display the diagrams",
)

args = parser.parse_args()

print("#####################################################################")
print("RipsComplex creation from distance matrix read in a csv file")

message = "RipsComplex with max_edge_length=" + repr(args.max_edge_length)
print(message)
start = time.process_time()

distance_matrix = gudhi.read_lower_triangular_matrix_from_csv_file(csv_file=args.file, separator=args.separator)

rips_complex = gudhi.RipsComplex(
    distance_matrix=distance_matrix, max_edge_length=args.max_edge_length
)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=args.max_dimension)



message1 = "Number of simplices=" + repr(simplex_tree.num_simplices())
print(message1)
message2 = "Number of vertices=" + repr(simplex_tree.num_vertices())
print(message2)
#compute the number of s-simplices for s=0,1,2,...,5
dimension_counts = {i: 0 for i in range(0, 6)}  

for simplex in simplex_tree.get_skeleton(5):  
    dimension = len(simplex[0]) - 1  
    if 0 <= dimension <= 5:
        dimension_counts[dimension] += 1

print("Number of simplices by dimension (0 to 5):", dimension_counts)
simplex_tree.compute_persistence(homology_coeff_field=2)
diag = simplex_tree.persistence(homology_coeff_field=2)
print("Collapse, expansion and persistence computation took ", time.process_time() - start, " sec.")
print("betti_numbers()=")
print(simplex_tree.betti_numbers())
#compute persistent barcode
gudhi.plot_persistence_barcode(diag)
if args.no_diagram == False:
    import matplotlib.pyplot as plot
    gudhi.plot_persistence_diagram(diag, band=args.band)
    plot.show()


