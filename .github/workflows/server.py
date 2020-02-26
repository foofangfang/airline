from flask import Flask,render_template, request
import sqlite3

app=Flask(__name__)

db=sqlite3.connect('airline.db')


@app.route('/')
def index():
    db=sqlite3.connect('airline.db')
    c=db.cursor()
    c.execute('''SELECT id,origin,destination FROM flights''')
    flights=c.fetchall()
    return render_template("index.html",flights=flights)


@app.route('/book', methods=["POST"])
def book():
    username=request.form.get("name")
    user_flight_id=int(request.form.get("flight_id"))

    db=sqlite3.connect('airline.db')
    c=db.cursor()
    c.execute('''INSERT INTO passengers (name,flight_id) VALUES (:name, :flight_id)''',\
              {"name":username,"flight_id": user_flight_id})
    db.commit()
    
    return render_template("success.html",
                           message= "You have successfully booked your flight.")


@app.route('/check')
def check():
    db=sqlite3.connect('airline.db')
    c=db.cursor()
    c.execute('''SELECT id,origin,destination FROM flights''')
    flights=c.fetchall()
    
    return render_template("flights.html", all_data= flights)


@app.route('/check/<int:flight_id>')
def check1(flight_id):
    db=sqlite3.connect('airline.db')
    c=db.cursor()
    c.execute('''SELECT * FROM flights WHERE id=:id''', {"id":flight_id})
    flight=c.fetchone()
    c.execute('''SELECT name FROM passengers WHERE flight_id=:flight_id''', {"flight_id": flight_id})
    passengers=c.fetchall()
    return render_template("flight.html",flight=flight, passengers=passengers)


db.close()
app.run(debug=True,port=5000)




















