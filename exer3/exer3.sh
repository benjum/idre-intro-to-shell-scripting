# What is the output of the following?

for f in *.txt
do
	ls *.txt
done

# and what is the output of this slight change?

for f in *.txt
do
	ls $f
done

# Comment/Uncomment each one and run to check that you understand the difference

