##
function dist( i, j, K: integer ) :=
   min( abs(j-i), K-abs(j-i) );

Assign( input, '27-142b.txt' );
var (N, K, M) := ReadInteger3;
var D := 20;
var data := |0|*K;

for var i:=1 to N do begin
  var (p, x):= ReadInteger2;
  data[p mod K] := x > 0 ? (x-1) div D + 1 : 0;
end;     

var (minCost, pos) := (MaxInt, -1);
for var i:=0 to K-1 do begin
  var s := (0..K-1).Select( j-> dist(i,j,K)*data[j] ).Sum;
  if data[i] = 0 then begin
    var sumMM := (i-M+1..i+M-1).Select( j->data[ (j+K) mod K] ).Sum;
    if (sumMM = 0) and (s < minCost)  then begin 
      minCost := s;
      pos := i;
    end;  
  end;
end;      

Print( pos, minCost );
