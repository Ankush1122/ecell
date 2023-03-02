 
echo " BUILD START"
python3 -m pip install pipenv
python3 -m pip install django
python3 manage.py collectstatic --noinput --clear
echo " BUILD END"
