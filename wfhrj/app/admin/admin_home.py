# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/9/20 15:46'
from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)


@admin.route('/')
def home():
    return render_template('admin/admin_home.html')

