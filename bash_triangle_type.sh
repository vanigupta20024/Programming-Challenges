# check triangle

read side1
read side2
read side3

if [[ $side1 -eq $side2 && $side1 -eq $side3 ]] ;
then 
    echo "EQUILATERAL"
elif [[ $side1 -eq $side2 || $side1 -eq $side3 || $side2 -eq $side3 ]] ;
then 
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
