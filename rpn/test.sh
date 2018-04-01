input=".in"
output=".out"
answer=".ans"

RED='\033[0;31m'
NC='\033[0m' # No Color

for sample in samples/rpn*.in 
do
	filename="${sample%.*}"
	echo Testing $filename 
	python3 rpn.py < $filename$input | tee $filename$output
	cmp  $filename$answer $filename$output || echo "${RED}ERROR${NC} Different OUTPUT\n"
done