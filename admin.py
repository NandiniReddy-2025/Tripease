from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import login_required, current_user
from models import db, Travel, Accommodation, Food, Sightseeing
import os
from werkzeug.utils import secure_filename

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required.')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# Example for Travel CRUD (repeat similar for others)
@admin_bp.route('/travel', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_travel():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        price = request.form['price']
        image = request.files.get('image')
        image_path = None
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join('uploads', filename)
            full_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(full_path)
            print(f"Image saved to: {full_path}")
            print(f"Image path stored: {image_path}")
        travel = Travel(name=name, location=location, description=description, price=price, image_path=image_path)
        db.session.add(travel)
        db.session.commit()
        flash('Travel option added!')
    travels = Travel.query.all()
    return render_template('admin_travel.html', travels=travels)

@admin_bp.route('/accommodation', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_accommodation():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        price = request.form['price']
        image = request.files.get('image')
        image_path = None
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join('uploads', filename)
            full_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(full_path)
            print(f"Image saved to: {full_path}")
            print(f"Image path stored: {image_path}")
        accommodation = Accommodation(name=name, location=location, description=description, price=price, image_path=image_path)
        db.session.add(accommodation)
        db.session.commit()
        flash('Accommodation option added!')
    accommodations = Accommodation.query.all()
    return render_template('admin_accommodation.html', accommodations=accommodations)

@admin_bp.route('/food', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_food():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        price = request.form['price']
        image = request.files.get('image')
        image_path = None
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join('uploads', filename)
            full_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(full_path)
            print(f"Image saved to: {full_path}")
            print(f"Image path stored: {image_path}")
        food = Food(name=name, location=location, description=description, price=price, image_path=image_path)
        db.session.add(food)
        db.session.commit()
        flash('Food option added!')
    foods = Food.query.all()
    return render_template('admin_food.html', foods=foods)

@admin_bp.route('/sightseeing', methods=['GET', 'POST'])
@login_required
@admin_required
def manage_sightseeing():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        price = request.form['price']
        image = request.files.get('image')
        image_path = None
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join('uploads', filename)
            full_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(full_path)
            print(f"Image saved to: {full_path}")
            print(f"Image path stored: {image_path}")
        sightseeing = Sightseeing(name=name, location=location, description=description, price=price, image_path=image_path)
        db.session.add(sightseeing)
        db.session.commit()
        flash('Sightseeing option added!')
    sightseeings = Sightseeing.query.all()
    return render_template('admin_sightseeing.html', sightseeings=sightseeings) 