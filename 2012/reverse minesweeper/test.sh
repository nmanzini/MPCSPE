for inp in ./*.in
do
	python3 main.py <$inp |tee $inp.out
	cmp $inp.out ${inp%.*}.ans
done