from flask import Blueprint, render_template, request, make_response
from models import Travel, Accommodation, Food, Sightseeing
from datetime import datetime

planner_bp = Blueprint('planner', __name__)

@planner_bp.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')

@planner_bp.route('/plan', methods=['GET', 'POST'])
def plan():
    if request.method == 'POST':
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        location = request.form['location']
        budget = float(request.form['budget'])
        # Budget allocation
        travel_budget = budget * 0.25
        accommodation_budget = budget * 0.30
        food_budget = budget * 0.20
        sightseeing_budget = budget * 0.25
        # Fetch options within budget and location
        travel_options = Travel.query.filter(Travel.location==location, Travel.price<=travel_budget).all()
        accommodation_options = Accommodation.query.filter(Accommodation.location==location, Accommodation.price<=accommodation_budget).all()
        food_options = Food.query.filter(Food.location==location, Food.price<=food_budget).all()
        sightseeing_options = Sightseeing.query.filter(Sightseeing.location==location, Sightseeing.price<=sightseeing_budget).all()
        return render_template('plan_result.html',
            checkin=checkin, checkout=checkout, location=location, budget=budget,
            travel_options=travel_options,
            accommodation_options=accommodation_options,
            food_options=food_options,
            sightseeing_options=sightseeing_options,
            travel_budget=travel_budget,
            accommodation_budget=accommodation_budget,
            food_budget=food_budget,
            sightseeing_budget=sightseeing_budget)
    return render_template('planner_form.html')

@planner_bp.route('/download_plan')
def download_plan():
    # Get trip details from request args
    checkin = request.args.get('checkin')
    checkout = request.args.get('checkout')
    location = request.args.get('location')
    budget = request.args.get('budget')
    
    # Get options from database
    travel_options = Travel.query.filter_by(location=location).limit(3).all()
    accommodation_options = Accommodation.query.filter_by(location=location).limit(3).all()
    food_options = Food.query.filter_by(location=location).limit(3).all()
    sightseeing_options = Sightseeing.query.filter_by(location=location).limit(3).all()
    
    # Generate trip plan content
    content = 'TRIP EASE - YOUR PERFECT TRIP PLAN\n'
    content += '=' * 50 + '\n\n'
    
    # Trip Summary
    content += 'TRIP SUMMARY\n'
    content += '-' * 20 + '\n'
    content += f'Check-in Date: {checkin}\n'
    content += f'Check-out Date: {checkout}\n'
    content += f'Destination: {location}\n'
    content += f'Total Budget: ${budget}\n\n'
    
    # Travel Options
    content += 'TRAVEL OPTIONS\n'
    content += '-' * 20 + '\n'
    if travel_options:
        for i, option in enumerate(travel_options, 1):
            content += f'{i}. {option.name}\n'
            content += f'   Description: {option.description}\n'
            content += f'   Price: ${option.price}\n\n'
    else:
        content += 'No travel options found.\n\n'
    
    # Accommodation Options
    content += 'ACCOMMODATION OPTIONS\n'
    content += '-' * 20 + '\n'
    if accommodation_options:
        for i, option in enumerate(accommodation_options, 1):
            content += f'{i}. {option.name}\n'
            content += f'   Description: {option.description}\n'
            content += f'   Price: ${option.price}\n\n'
    else:
        content += 'No accommodation options found.\n\n'
    
    # Food Options
    content += 'FOOD OPTIONS\n'
    content += '-' * 20 + '\n'
    if food_options:
        for i, option in enumerate(food_options, 1):
            content += f'{i}. {option.name}\n'
            content += f'   Description: {option.description}\n'
            content += f'   Price: ${option.price}\n\n'
    else:
        content += 'No food options found.\n\n'
    
    # Sightseeing Options
    content += 'SIGHTSEEING OPTIONS\n'
    content += '-' * 20 + '\n'
    if sightseeing_options:
        for i, option in enumerate(sightseeing_options, 1):
            content += f'{i}. {option.name}\n'
            content += f'   Description: {option.description}\n'
            content += f'   Price: ${option.price}\n\n'
    else:
        content += 'No sightseeing options found.\n\n'
    
    # Budget Summary
    content += 'BUDGET SUMMARY\n'
    content += '-' * 20 + '\n'
    total_travel = sum(float(option.price) for option in travel_options)
    total_accommodation = sum(float(option.price) for option in accommodation_options)
    total_food = sum(float(option.price) for option in food_options)
    total_sightseeing = sum(float(option.price) for option in sightseeing_options)
    total_cost = total_travel + total_accommodation + total_food + total_sightseeing
    
    content += f'Travel: ${total_travel:.2f}\n'
    content += f'Accommodation: ${total_accommodation:.2f}\n'
    content += f'Food: ${total_food:.2f}\n'
    content += f'Sightseeing: ${total_sightseeing:.2f}\n'
    content += f'Total Cost: ${total_cost:.2f}\n'
    content += f'Budget: ${budget}\n'
    content += f'Remaining: ${float(budget) - total_cost:.2f}\n\n'
    
    content += 'Generated by Trip Ease\n'
    content += f'Date: {datetime.now().strftime("%Y-%m-%d")}\n'
    content += f'Time: {datetime.now().strftime("%H:%M:%S")}\n'
    
    # Create response
    response = make_response(content)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Content-Disposition'] = f'attachment; filename=trip_plan_{location}_{checkin}.txt'
    
    return response 

@planner_bp.route('/accommodation_only', methods=['GET', 'POST'])
def accommodation_only():
    if request.method == 'POST':
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        location = request.form['location']
        budget = float(request.form['budget'])
        accommodation_options = Accommodation.query.filter(Accommodation.location==location, Accommodation.price<=budget).all()
        return render_template('accommodation_only.html',
            checkin=checkin, checkout=checkout, location=location, budget=budget,
            accommodation_options=accommodation_options)
    return render_template('accommodation_only.html', accommodation_options=None) 