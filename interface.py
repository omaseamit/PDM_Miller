from utils import Preddictive_maintanace
from flask import Flask, jsonify, render_template, request
#import config

app = Flask(__name__)

##################################################################################
 ################################# Base API #####################################
##################################################################################

@app.route('/')
def Perdiction_model():
    print('Welcome to Preddictive Maintanace Model')
    return render_template('index.html')

##################################################################################
 ################################# Model API #####################################
##################################################################################

@app.route('/preddictive_maintanace',methods = ['POST','GET'])
def Get_preddictive_maintanace():
    if request.method == 'POST':
        print('We are using POST Method')
        data = request.form
        Air_temperature = data['Air_temperature']
        Process_temperature = data['Process_temperature']
        Rotational_speed = data['Rotational_speed']
        Torque = data['Torque']
        Tool_wear = data['Tool_wear']
        
        
        prd_main = Preddictive_maintanace(Air_temperature,Process_temperature, Rotational_speed, Torque,Tool_wear)
        output = prd_main.get_Preddictive_maintanace()
        #return render_template('result.html', prediction=my_prediction)
        return render_template('result.html', output=output)

    else:
        print('We are in GET Method')
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5007, debug= True)
