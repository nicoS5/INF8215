include "globals.mzn"; 

int: n;
array[1..n, 1..n] of var 0..1: grid; % var is used in order to take into account the "not-bounded case" _
 
% decision variables: mine or not on the specific cell
array[1..n, 1..n] of var 0..1: x;


% initializing the grid: '_' values on the grid correspond to variables not already set (i.e. the choices you have to make)
constraint forall(i in 1..n, j in 1..n)(x[i,j] = grid[i,j]);

output [
   if j = 1 then "\n" else " " endif ++
     show(x[i,j])
   | i,j in 1..n
];