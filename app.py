import urllib2
import pandas as pd
from bokeh.plotting import figure,output_file,show
from flask import Flask, render_template, request, redirect,json,flash,url_for
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
#from bokeh.templates import RESOURCES
from bokeh.util.string import encode_utf8



app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
  if request.method=='GET':
	#return redirect('\result')
	return render_template('index.html')
  else:
	my_var=request.form['ticker_lulu']
	
	#session['my_ticker']=app.vars['ticker']
	#return render_template('layout.html',t_value=app.vars['ticker'])
	#return redirect (url_for('result',ticker='john'))
	return redirect('/result')
  	
@app.route('/result',methods=['GET','POST'])
def result():
  #data=json.load(urllib2.urlopen('https://www.quandl.com/api/v3/datasets/WIKI/'+app.vars['ticker']+'.json?#start_date=2016-05-03&end_date=2016-06-03&column_index=4'))
  data=json.load(urllib2.urlopen('https://www.quandl.com/api/v3/datasets/WIKI/AA.json?start_date=2016-05-03&end_date=2016-06-03&column_index=4'))
  mylist=[0 for i in range(23)]
  for i in range(23):
	mylist[i]=data['dataset']['data'][i][1]	
  
  p=figure(plot_width=400,plot_height=400)
  p.line(range(23),mylist,line_width=2)
  plot_resources = RESOURCES.render(
        js_raw=INLINE.js_raw,
        css_raw=INLINE.css_raw,
        js_files=INLINE.js_files,
        css_files=INLINE.css_files,
    )
  script, div = components(fig, INLINE)
  html = flask.render_template(
        'embed.html',
        plot_script=script, plot_div=div, plot_resources=plot_resources)
  return encode_utf8(html)
  #return p
  #my_var=session.get('my_ticker',None)
  #messages=request.args['messages']
  if request.method=='POST':
	return "HELLO"
  return render_template('index.html')	
#  return render_template('index.html',messages=json.loads(messages))

if __name__ == '__main__':
  app.run(port=33507)
