from flask import Flask,render_template,request

app = Flask(__name__)




@app.route("/")
@app.route("/home")
def hello():
    return render_template('/index.html')






def var_name_return(var_name):
    name_list = ["self."+ i +" " +  "=" + " " + i for i in var_name]
    return name_list 



@app.route('/', methods=['GET','POST'])

def constructor():
    text = request.form['text']
    class_name = request.form['class']
    parsed_text = text.split(",")
    parsed_list = var_name_return(parsed_text)
    list2 = ["class",class_name,"():","def __init__","(self,","):"]
    total_list  = list2+parsed_list
    return render_template('/index.html', var1 = total_list,var2 = parsed_text,var3 = class_name)



# @app.route("/about")

# def about():
#     return render_template('about.html')


if __name__ =="__main__":
    app.run(debug=True)




