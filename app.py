import urllib2
import pandas as pd
from bokeh.plotting import figure,output_file,show
from flask import Flask, render_template, request, redirect,json

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
  if request.method=='GET':
	return render_template('index.html')
  else:
	app.vars['ticker']=request.form['ticker_lulu']
	
	#return render_template('index.html')
	return redirect ('/result')

@app.route('/result',methods=['GET'])
def result():
  #data=json.load(urllib2.urlopen#('https://www.quandl.com/api/v3/datasets/WIKI/'+app.vars['ticker']+'.json?#start_date=2016-05-03&end_date=2016-06-03&column_index=4'))
  #mylist=[0 for i in range(23)]
  #for i in range(23):
#	mylist[i]=data['dataset']['data'][i][1]	
  
  #p=figure(plot_width=400,plot_height=400)
  #p.line(range(23),mylist,line_width=2)
  #return p
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507,debug=True)
