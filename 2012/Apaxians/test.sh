for sample in ./*.in
do
  python3 main.py < $sample 
  cat ${sample%.*}.ans
done