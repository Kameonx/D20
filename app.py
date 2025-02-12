from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def roll_dice(dice_type, multiplier):
    rolls = []
    if dice_type == 'd4':
        rolls = [random.randint(1, 4) for _ in range(multiplier)]
    elif dice_type == 'd6':
        rolls = [random.randint(1, 6) for _ in range(multiplier)]
    elif dice_type == 'd8':
        rolls = [random.randint(1, 8) for _ in range(multiplier)]
    elif dice_type == 'd20':
        rolls = [random.randint(1, 20) for _ in range(multiplier)]
    total = sum(rolls)
    return total, rolls

@app.route('/d4')
def roll_d4():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d4', multiplier)
    return render_template('dice_roll.html', dice_type='D4', result=result, rolls=rolls)

@app.route('/d6')
def roll_d6():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d6', multiplier)
    return render_template('dice_roll.html', dice_type='D6', result=result, rolls=rolls)

@app.route('/d8')
def roll_d8():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d8', multiplier)
    return render_template('dice_roll.html', dice_type='D8', result=result, rolls=rolls)

@app.route('/d20')
def roll_d20():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d20', multiplier)
    return render_template('dice_roll.html', dice_type='D20', result=result, rolls=rolls)

if __name__ == '__main__':
    app.run(debug=True)