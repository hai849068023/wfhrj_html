# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/9/24 13:32'
from flask import Blueprint, render_template

farmers = Blueprint('farmers', __name__)


@farmers.route('/farmers')
def farmer():
    return render_template('admin/admin_farmers_lists.html')

