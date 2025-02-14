from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Expense
from collections import defaultdict

@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    description = request.form['description']
    
    new_expense = Expense(amount=amount, category=category, date=date, description=description)
    db.session.add(new_expense)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)  # Find expense by ID
    db.session.delete(expense)  # Delete from database
    db.session.commit()  # Save changes
    return redirect(url_for('index'))  # Refresh the page

@app.route('/')
def index():
    expenses = Expense.query.all()

    # Aggregate totals for each category
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category] += expense.amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Debugging: Print to terminal to check data
    print("Categories:", categories)
    print("Amounts:", amounts)

    return render_template('index.html', expenses=expenses, categories=categories, amounts=amounts)