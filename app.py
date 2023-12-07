from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS= [
{
  'id':1,  
  'title':"Data Analyst",
  'location':"Poland, Warsaw",
  'salary':  10000  
} ,
  {
    'id':2,  
    'title':"Data Scientist",
    'location':"Poland, Gdansk",
    'salary':  15000
  },
  {
    'id':3,  
    'title':"Frontend Engineer",
    'location':"Remote"
    
  },
  {
    'id':4,  
    'title':"Backend Engineer",
    'location':"USA, San Francisco",
    'salary':  25000  
  }  
  
]

@app.route("/")
def hello_rem():
  #in render_template we passing variables
  #return html
    return render_template('home.html',
                           jobs=JOBS,
                          company_name="First Repo")
  
  #api - applicaiton programming interface (NON HTML template)
  #api basicly means that server return NOT html but json
  #json is a standart for transmitting data between clients and servers
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if(__name__=="__main__"):
  app.run(debug=True,host='0.0.0.0')
  
