import sys
import site

site.addsitedir('C:/Users/hp/PycharmProjects/projet_stage/venv/Lib/site-packages')

sys.path.insert(0, 'C:/Users/hp/PycharmProjects/projet_stage')

from flask_app import app as application