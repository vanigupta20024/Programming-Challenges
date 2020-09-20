# take only single input character
# can also be "read -n1 input"
read -n 1 input

if [ $input = "y"] || [ $input = "Y" ];
then
    echo "YES"

else
    echo "NO"
fi
