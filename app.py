from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session

API="https://pokeapi.co/api/v2/pokemon/"

app = Flask(__name__)

app.secret_key="Ali091903"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/pokemon', methods=['POST'])
def pokemon():
    pokemon=request.form.get('pokemon', '').strip().lower()
    if not pokemon:
        flash ('Por favor, ingresa un nombre de Pokemon', 'error')
        
    return redirect("url_for(index)")

pkemon_info={
    'name': pokemon_data ['name'].title(),
    'types': [t['type']['name']].title()for t in pokemon_data['types']],
}

if __name__ == '__main__':
    app.run(debug=True)