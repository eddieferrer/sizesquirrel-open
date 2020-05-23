import datetime
import re
import json
import requests

from sqlalchemy import func
from sizeSquirrel import app, db
from sizeSquirrel.models import User, Brand, Item
from flask import Flask, request, redirect, url_for, render_template, jsonify, abort, flash, g, send_from_directory

from .apiv2 import views

@app.route('/images/favicon/android-icon-96x96.png')
@app.route('/images/favicon/android-icon-192x192.png')
@app.route('/images/favicon/android-icon-144x144.png')
@app.route('/images/favicon/apple-touch-icon-120x120.png')
@app.route('/images/favicon/apple-touch-icon-120x120-precomposed.png')
@app.route('/images/favicon/apple-touch-icon-precomposed.png')
@app.route('/images/favicon/apple-touch-icon-152x152-precomposed.png')
@app.route('/images/favicon/apple-touch-icon-152x152.png')
@app.route('/images/favicon/apple-touch-icon.png')
@app.route('/images/SizeSquirrelLogoMainSquare.svg')
def static_from_root_image():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/favicon.ico')
@app.route('/robots.txt')
@app.route('/manifest.json')
@app.route('/service-worker.js')
@app.route('/googledd078f0b0c898aa8.html')
def static_for_misc_files():
    return send_from_directory(app.root_path + '/dist/', request.path[1:])


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    meta = {
        "title": "Climbing shoe sizing, recommendations, and deals | SizeSquirrel",
        "url": "https://www.sizesquirrel.com/" + path,
        "image": "https://www.sizesquirrel.com/static/images/OGImage1200x1200.jpg",
        "width": "1200",
        "height": "1200",
    }

    urlSegments = path.split('/')
    urlSegments = list(filter(None, urlSegments))  # fastest

    brand_id = ''
    if urlSegments:
        if urlSegments[0] == 'shoes':
            # @app.route('/shoes/<shoe_brand>/<shoe_model>/')
            if len(urlSegments) > 1:
                brand_url_segment = urlSegments[1].replace('-', ' ')
                brand = Brand.query.filter_by(name=brand_url_segment).first()
                if brand:
                    brand_id = brand.id

                meta["title"] = brand_url_segment.title() + \
                    " | SizeSquirrel"

            if len(urlSegments) > 2:
                model_url_segment = urlSegments[2].replace('-', ' ')
                model_url_segment = model_url_segment.lower()
                model = Item.query.filter(Item.brand_id == brand_id).filter(
                    func.replace(func.lower(Item.model), '-', ' ') == model_url_segment).first()
                if model:
                    meta["width"] = "300"
                    meta["height"] = "300"
                    meta["image"] = model.shoe_image
                    meta["title"] = brand_url_segment.title(
                    ) + ' ' + model.model.title() + " | SizeSquirrel"
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).content
    return render_template("index.html", meta=meta)

