from flask import jsonify, request
from flask import Flask, render_template
from amazon import send

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_node_ui():
    return render_template('amazon_phones.html')

@app.route('/process', methods=['POST'])

def process():
    name = request.form['name1']
    #dist=request.form['dist']
    
    value=send(name)
    
    name1=str(value[0][0])+"  "+"Distance: "+str(round(value[0][2],3))
    name2=str(value[1][0])+"  "+"Distance: "+str(round(value[1][2],3))
    name3=str(value[2][0])+"  "+"Distance: "+str(round(value[2][2],3))
    name4=str(value[3][0])+"  "+"Distance: "+str(round(value[3][2],3))
    name5=str(value[4][0])+"  "+"Distance: "+str(round(value[4][2],3))
    reviews=str(value[0][3])
    description=str(value[0][4])
    feats=str(value[0][5])
    
    
    return jsonify({'name1': name1, 'name2': name2, 'name3': name3, 'name4': name4, 'name5': name5, 
                    'reviews': reviews, 'description': description, 'features': feats, 'namess':name})


if __name__=='__main__':    
    app.run(host='127.0.0.1', port=5000)