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
    elif dice_type == 'd10':
        rolls = [random.randint(1, 10) for _ in range(multiplier)]
    elif dice_type == 'd20':
        rolls = [random.randint(1, 20) for _ in range(multiplier)]
    elif dice_type == 'd3':
        rolls = [random.randint(1, 3) for _ in range(multiplier)]
    elif dice_type == 'd5':
        rolls = [random.randint(1, 5) for _ in range(multiplier)]
    elif dice_type == 'd7':
        rolls = [random.randint(1, 7) for _ in range(multiplier)]
    elif dice_type == 'd9':
        rolls = [random.randint(1, 9) for _ in range(multiplier)]
    elif dice_type.startswith('dx_'):
        sides = int(dice_type.split('_')[1])
        rolls = [random.randint(1, sides) for _ in range(multiplier)]
    total = sum(rolls)
    return total, rolls

def coin_toss(multiplier=1):
    results = [random.choice(['Heads', 'Tails']) for _ in range(multiplier)]
    return results

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

@app.route('/d10')
def roll_d10():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d10', multiplier)
    return render_template('dice_roll.html', dice_type='D10', result=result, rolls=rolls)

@app.route('/d20')
def roll_d20():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d20', multiplier)
    return render_template('dice_roll.html', dice_type='D20', result=result, rolls=rolls)

@app.route('/d3')
def roll_d3():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d3', multiplier)
    return render_template('dice_roll.html', dice_type='D3', result=result, rolls=rolls)

@app.route('/d5')
def roll_d5():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d5', multiplier)
    return render_template('dice_roll.html', dice_type='D5', result=result, rolls=rolls)

@app.route('/d7')
def roll_d7():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d7', multiplier)
    return render_template('dice_roll.html', dice_type='D7', result=result, rolls=rolls)

@app.route('/d9')
def roll_d9():
    multiplier = int(request.args.get('multiplier', 1))
    result, rolls = roll_dice('d9', multiplier)
    return render_template('dice_roll.html', dice_type='D9', result=result, rolls=rolls)

@app.route('/dx')
def roll_custom_dice():
    sides = int(request.args.get('sides', 100))
    multiplier = int(request.args.get('multiplier', 1))
    # Ensure sides is at least 2
    sides = max(2, sides)
    result, rolls = roll_dice(f'dx_{sides}', multiplier)
    return render_template('dice_roll.html', dice_type=f'D{sides}', result=result, rolls=rolls)

@app.route('/coin')
def toss_coin():
    multiplier = int(request.args.get('multiplier', 1))
    results = coin_toss(multiplier)
    return render_template('coin_toss.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
