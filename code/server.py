from flask import Flask, jsonify

app = Flask(__name__)
buzzers = [0,0,0,0,0,0]
active = 0
def save_buzzer(buzzer_name):
    with open('buzzers.txt', 'w') as f:
        f.write(buzzer_name + '\n')

@app.route('/b1', methods=['GET'])
def buzz_one():
    global active
    global buzzers
    print(active)
    print(buzzers)
    if(active == 0):
        buzzers[0] = 1
        active = 1
        save_buzzer('b1')
        return "1"
    else:
        return "0"

@app.route('/b2', methods=['GET'])
def buzz_two():
    global active
    global buzzers
    if(active == 0):
        buzzers[1] = 1
        active = 1
        save_buzzer('b2')
        return "1"
    else:
        return "0"
    
@app.route('/b3', methods=['GET'])
def buzz_three():
    global active
    global buzzers
    if(active == 0):
        buzzers[2] = 1
        active = 1
        save_buzzer('b3')
        return "1"
    else:
        return "0"

@app.route('/b4', methods=['GET'])
def buzz_four():
    global active
    global buzzers
    if(active == 0):
        buzzers[3] = 1
        active = 1
        save_buzzer('b4')
        return "1"
    else:
        return "0"

@app.route('/b5', methods=['GET'])
def buzz_five():
    global active
    global buzzers
    if(active == 0):
        buzzers[4] = 1
        active = 1
        save_buzzer('b5')
        return "1"
    else:
        return "0"

@app.route('/b6', methods=['GET'])
def buzz_six():
    global active
    global buzzers
    if(active == 0):
        buzzers[5] = 1
        active = 1
        save_buzzer('b6')
        return "1"
    else:
        return "0"
    

@app.route('/reset', methods=['GET'])
def get_books():
    global active
    global buzzers  
    for i in range(0,6):
        buzzers[i] = 0
    active = 0
    save_buzzer('b')
    return "2"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)