from flask import render_template, request, redirect
from . import public

@public.route('/')
def public():
    return '/public'
