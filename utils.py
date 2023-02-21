import pickle
import json
# import config
import numpy as np

class Preddictive_maintanace():

    def __init__(self,Air_temperature,Process_temperature,Rotational_speed,Torque,Tool_wear,):

       self.Air_temperature = Air_temperature
       self.Process_temperature = Process_temperature
       self.Rotational_speed = Rotational_speed
       self.Torque = Torque
       self.Tool_wear = Tool_wear
        

    def load_model(self):
        with open(r'E:\Velocity\Predictive Main\Project_Data\Linear_model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        
        with open(r'E:\Velocity\Predictive Main\Project_Data\project_data.json', 'r') as f:
            self.json_data = json.load(f)

    def get_Preddictive_maintanace(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.Air_temperature
        test_array[1] = self.Process_temperature
        test_array[2] = self.Rotational_speed
        test_array[3] = self.Torque
        test_array[4] = self.Tool_wear

        test_array

        print('Test Array :', test_array)
        preddictive_maintanace = np.around(self.model.predict([test_array]))
        #print('Medical Insurance charges are : RS.',predicted_charges)
        return preddictive_maintanace
if __name__ == '__main__':

    Air_temperature = 5
    Process_temperature = 145
    Rotational_speed = 74
    Torque = 30
    Tool_wear = 0
    
    med_ins = Preddictive_maintanace(Air_temperature,Process_temperature,Rotational_speed,Torque,Tool_wear)
    med_ins.get_Preddictive_maintanace()