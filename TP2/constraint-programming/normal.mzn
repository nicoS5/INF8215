include "globals.mzn"; 

int: n;
array[1..n, 1..n] of var 0..1: grid; % var is used in order to take into account the "not-bounded case" _
 
% decision variables: mine or not on the specific cell
array[1..n, 1..n] of var 0..1: x;


% initializing the grid: '_' values on the grid correspond to variables not already set (i.e. the choices you have to make)
constraint forall(i in 1..n, j in 1..n)(x[i,j] = grid[i,j]);


% constraint 1
constraint forall(i in 1..n) (sum(j in 1..n)(x[i,j]) = n div 2);
constraint forall(j in 1..n) (sum(i in 1..n)(x[i,j]) = n div 2);

% constraint 2
constraint forall(i in 1..n-2, j in 1..n-2) (x[i,j] + x[i,j+1] + x[i,j+2] >= 1);
constraint forall(i in 1..n-2, j in 1..n-2) (x[i,j] + x[i+1,j] + x[i+2,j] >= 1);


% constraint 3
constraint forall(i in 1..n-2, j in 1..n-2) (x[i,j] + x[i,j+1] + x[i,j+2] < 3);
constraint forall(i in 1..n-2, j in 1..n-2) (x[i+1,j] + x[i,j] + x[i+2,j] < 3);


% constraint 4
constraint forall(i in 1..n, j in 1..n where i != j) (sum(k in 1..n)(abs(x[i,k] - x[j,k])) != 0);

% constraint 5
constraint forall(i in 1..n, j in 1..n where i != j) (sum(k in 1..n)(abs(x[k,i] - x[k,j])) != 0);

% constraint 6 (commenter si on choisit un fichier dans "data")
% constraint x[1,1] = 0;
% constraint x[10,1] = 0;
% constraint x[10,10] = 1;

output [
   if j = 1 then "\n" else " " endif ++
     show(x[i,j])
   | i,j in 1..n
];