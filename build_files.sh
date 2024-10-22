echo "BUILD START"
python 3.12 -m pip install -r requirementS.txt
python 3.12 manage.py collectstatic --noinput --cleaer
echo BUILD END"