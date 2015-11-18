from flask import Blueprint, render_template, request
from ..models.model import User
from ..helper import *

bp = Blueprint('bp_index', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    user = None

    if request.method == 'GET':
        user = current_user_data()
    ''' <pre>page_name</pre> is for the property \
    	<pre>data-main</pre> required by requirejs,\
    	it should be the name of a specific js file,\
    	or a path to the js file which is relative \
    	to the js folder within the static folder '''
    return render_template('index.html', page_name='index', user=user)
