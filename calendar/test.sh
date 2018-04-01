for file in find ./test_*
do
  python3 calendar_conondrum.py < "$file"
done
