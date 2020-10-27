
include "globals.mzn"; 
   
% Parameters of the problems
int: n = 5;
array[1..n] of int: left_vision = [2,1,3,2,3];
array[1..n] of int: right_vision = [3,4,1,3,2];
array[1..n] of int: up_vision = [2,1,3,2,2];
array[1..n] of int: down_vision = [3,4,2,1,2];

% Variable: value for each cell
array[1..n,1..n] of var 1..n: city;

%constraint 1
constraint forall(i in 1..n, j in 1..n, k in 1..n where j != k) (city[i,j] != city[i,k]);
constraint forall(i in 1..n, j in 1..n, k in 1..n where j != k) (city[j,i] != city[k,i]);

%constraint 2
% Le principe est de reposer sur la fonction en pseudo-code suivante : 
% Pour chaque côté de vision, on choisit le numéro de vision (par exemple left_vision[1] égal à 2) : 
%   L : tableau de l'ordre des tailles des tours
%   max = L[1]
%   compteur = 1
%   pour j allant de 2 à n:
%     si L[j] > max :
%             max = L[j]
%             compteur = compteur + 1
% return compteur (on compare ce compteur au numéro de vision)


constraint forall(i in 1..n) (sum(j in 2..n) (bool2int(city[i,j] > max(city[i,1..j-1])) ) = left_vision[i] - 1);
constraint forall(i in 1..n) (sum(j in 1..n-1) (bool2int(city[i,j] > max(city[i,j+1..n])) ) = right_vision[i] - 1);
constraint forall(j in 1..n) (sum(i in 2..n) (bool2int(city[i,j] > max(city[1..i-1,j])) ) = up_vision[j] - 1);
constraint forall(j in 1..n) (sum(i in 1..n-1) (bool2int(city[i,j] > max(city[i+1..n,j])) ) = down_vision[j] - 1);



output
["city:"]++
[
  if j = 1 then "\n" else " " endif ++
    show(city[i,j])
  | i in 1..n, j in 1..n
];
