#!/bin/bash
# This a FOR loop example which allows the code to run through the range provided which is between 1 to 10.

# The code below displays the range
for n in {1..10}
do
   echo $n
   sleep 1
done

echo "This is outside the for loop"

# The script below will check for any .log file in the BashTurorial folder,
# then zip the files that have .log extension
for file in BashTutorial/*.log
do 
   tar -- czvf $file.tar.gz $file
done
