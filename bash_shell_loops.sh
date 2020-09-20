# Loops in bash script

# for loop
for i in {1..50};
do
    echo "${i}"
done

# while loop
count=1
while [ $count -le 50 ] ;
do
    echo "$count"
    count=$((count + 1))
done

# until loop
count=1
until [ $count -ge 51 ] ;
do
    echo "$count"
    count=$((count + 1))
done
