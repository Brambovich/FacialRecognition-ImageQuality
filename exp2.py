from listfunctions import sumlist, average
from matplotlib import pyplot as plt
import face_recognition
import collections

def differentperson_differentres(person_dictionary, no_persons, no_faces, no_res, no_gaus):



    temp = list()
    keys = list()
    personal_distance = list()
    face_recog = list()
    facedep_distance = list()
    final_distance_different = list()
    resdistances_same = collections.defaultdict(list)
    final_distance = dict()
    ## --------------------------------
    ## DIFFERENT PERSON - DIFFERENT RES
    ## --------------------------------  
    #loop through all persons and generate an number with it
    for person in person_dictionary.values():
        known = person.faces[1].orig
        # loop through all DIFFERENT person than the "known" one
        for person_diff in person_dictionary.values():
            if person_diff != person:
            #loop through all faces of the different person
                for face in person_diff.faces.values():
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
                    
                    face_recog.extend(face_distances)
                    
                    
                    temp = list()     
                #per person averaged distances 
                facedep_distance.extend(sumlist(face_recog,no_res,no_faces))
                face_recog = list()
        #print(facedep_distance,"\n\n")
        personal_distance.extend(sumlist(facedep_distance,no_res,no_persons-1))
        facedep_distance = list()
    #total averaged distances
    final_distance_different = (sumlist(personal_distance,no_res,no_persons))
    personal_distance = list()
    keys = list()

    plt.figure(2)
    keys = list(range(0,10))
    print(keys)
    plt.plot(keys,final_distance_different)
    #plt.ylim(0,1)
    plt.title('Different person - different resolution')
    plt.xlabel('Resolution number')
    plt.ylabel('Distance')    
    plt.ylim(0, 1)