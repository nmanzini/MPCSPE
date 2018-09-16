for input in ./*in
do
	echo /////testing $input
	python3 main.py < $input  | tee $input.out
	cmp $input.out  ${input%.*}.ans || echo "failed"
done