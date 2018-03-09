# -*- coding: utf-8 -*
from flask import Flask, render_template, request, abort
from esc import ESC

app = Flask(__name__)

esc=ESC()


handle_map = {
    'on':esc.on,
    'off': esc.off,
    'lel6': esc.lel6,
    'lel7': esc.lel7,
    'lel8' : esc.lel8,
    'lel7' : esc.lel9,
    
}


@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")


@app.route('/handle', methods=['GET'])
def handle():
    try:
        
        operation = request.args.get('type', '')
    except ValueError:
        abort(404)  
    else:
        if operation in handle_map.iterkeys():
            handle_map[operation]()
        else:
            abort(404)
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=False)
