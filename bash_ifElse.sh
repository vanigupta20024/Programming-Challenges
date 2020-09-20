# if else in bash shell

read num1
read num2

if [ $num1 -lt $num2 ] ;
then
    echo "X is less than Y"
elif [ $num1 -gt $num2 ] ;
then
    echo "X is greater than Y"
else 
    echo "X is equal to Y"
fi
