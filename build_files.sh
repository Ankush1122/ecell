 
echo " BUILD START"
python3 -m pip install pipenv
pip install pipenv
pipenv shell
pipenv install django
python3 manage.py collectstatic --noinput --clear
echo " BUILD END"
