# -*- coding utf-8 -*-
# classes/views/frontend.py


from flask import Module, jsonify, request, render_template, redirect,\
                url_for, g, current_app

from swtstore.classes.models import Sweet, User


frontend = Module(__name__)

@frontend.route('/', methods=['GET'])
def index():
    sweets = Sweet.getFrontendSwts()
    sweets = [sweet.to_dict() for sweet in sweets]

    return render_template('frontend/index.html', sweets=sweets)


# Create a new sweet context
@frontend.route('/contexts/create', methods=['GET', 'POST'])
def createContext():
    pass
