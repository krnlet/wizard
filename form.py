# importing Flask and other modules
from flask import Flask, request, render_template
import csv
# Flask constructor
app = Flask(__name__, static_folder='/Users/krnlet/Desktop/gfg')

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    file=open("results.csv", "a")
    writer=csv.writer(file)
    file1=open("results1.csv", "a")
    writer1=csv.writer(file1)
    file2=open("results2.csv", "a") 
    writer2=csv.writer(file2)
        

    if request.method == "POST":
            name = request.form.get("name")
            if(request.form.get("version")!='other'):
                version = request.form.get("version")
            else:
                version = request.form.get("version_other")
            
            if(request.form.get("techniques")!='other'):
                techniques=request.form.get("techniques")
            else:
                techniques=request.form.get("techniques_other")

            if(request.form.get("task_tech")!='other'):
                task=request.form.get("task_tech")
            else:
                task=request.form.get("tt_other")

            if(request.form.get("features")!='other'):
                features=request.form.get("features")
            else:
                features=request.form.get("features_other")

            if(request.form.get("users")!='other'):
                users=request.form.get("users")
            else:
                users=request.form.get("users_other")
            
            tl=request.form.get("tl")
            al=request.form.get("al")
            appl=request.form.get("appl")
            issues=request.form.get("issues")
            benefits=request.form.get("benefits")
            negatives=request.form.get("negatives")
            
            
            
            tf=request.form.get("tf")
            su=request.form.get("su")
            d=request.form.get("d")
            issues2=request.form.get("issues2")
            byn=request.form.get("benandneg")
            
            if(name):
                writer.writerow([name, version,techniques, task, features, users])
                
            elif(tl):
                writer1.writerow([tl,al,appl,issues,benefits,negatives])
            elif(tf):    
                writer2.writerow([tf,su,d,issues2,byn])
                #return "Your name is "+name + version
    return render_template("form.html")
    

            
            

if __name__=='__main__':
    app.run()

