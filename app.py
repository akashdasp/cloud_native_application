import psutil
from flask import Flask,render_template
app= Flask(__name__)
@app.route('/')
def index():
    cpu_percent=psutil.cpu_percent()
    vertual_memory=psutil.virtual_memory().percent
    message = None
    if cpu_percent >= 80 or vertual_memory >= 80:
        message = "High CPU utilization Detedcted Need to Scale up"
    return render_template ('index.html',cpu_percent=cpu_percent,vertual_memory=vertual_memory,message=message)
if __name__ =="__main__":
    app.run(debug=False,host='0.0.0.0')