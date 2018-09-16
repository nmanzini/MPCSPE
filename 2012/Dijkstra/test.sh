for input in ./*in
do
	echo $input
	python3 main.py < $input > $input.out
	cat $input.out
	cmp ${input%.*}.ans $input.out || echo "${RED}ERROR${NC} Different OUTPUT\n"
done