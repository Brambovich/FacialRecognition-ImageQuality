from listfunctions import sumlist, average
from matplotlib import pyplot as plt
import face_recognition
import collections
import numpy as np
import plotly.express as px
import pandas as pd

def sameperson_differentres(person_dictionary, no_persons, no_faces, no_res, no_gaus):

    #print(distance)
    temp = list()
    keys = list()
    personal_distance = list()
    face_recog = list()
    facedep_distance = list()
    final_distance_different = list()
    resdistances_same = collections.defaultdict(list)
    final_distance = dict()
    ## --------------------------------  
    ## SAME PERSON - DIFFERENT RES 
    ## --------------------------------  
    #loop through all persons
    for person in person_dictionary.values():
        known = person.faces[1].orig
        #loop through all faces of that person
        for face in person.faces.values():
            # loop through all resolutions of that face
            for key, value in face.gaus.items():
                aKey = key
                aValue = value
                temp.append(aValue)
                keys.append(aKey)
                aValue = ""
                aKey = ""

            face_distances = face_recognition.face_distance(temp, known)
            #make a dictionary with all the face_distances in it
            for key, value in zip(keys,face_distances):
                resdistances_same[key].append(value)
            
            face_recog.append(face_distances)

            
            temp = list()     
        #per person averaged distances 
        numpy_facerecog = np.asarray(face_recog)
        average_facerecog = (np.mean(numpy_facerecog, axis=0).tolist())
        personal_distance.append(average_facerecog)

        face_recog = list()
    #total averaged distances
    final_distance_same_np = np.asarray(personal_distance)
    final_distance_same = np.mean(final_distance_same_np, axis=0)
    #final_distance_same = (sumlist(personal_distance,no_res,no_persons))
    personal_distance = list()
    keys = list()
    final_distance_same = final_distance_same.transpose()
    print(final_distance_same.tonumpy().shape)
    print(final_distance_same.transpose())
    df = pd.DataFrame(data=final_distance_same.tonumpy(), index=["0"], columns=["res 0", "res 1", "res 2", "res 3", "res 4", "res 5", "res 6", "res 7", "res 8", "res 9"])
    fig = px.line(df, x=final_distance_same.columns, y="Result", title='SAME PERSON - DIFFERENT RES')
    fig.write_html("./output.html", auto_open=True)



    #plt.figure(1)
    #keys = list(range(0,10))
    #plt.plot(keys,final_distance_same)
    #plt.title('Same person - different resolution')
    #plt.xlabel('Resolution number')
    #plt.ylabel('Distance')

    #plt.ylim(0, 1)