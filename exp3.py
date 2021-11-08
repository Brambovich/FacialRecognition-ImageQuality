from listfunctions import sumlist, average
from matplotlib import pyplot as plt
import face_recognition
import collections

def differentperson_differentres2(person_dictionary, no_persons, no_faces, no_res, no_gaus):
    #print(distance)
    temp = list()
    keys = list()
    personal_distance = list()
    face_recog = list()
    facedep_distance = list()
    #final_distance_different = list()
    #resdistances_same = collections.defaultdict(list)
    final_distance = dict()
        ## --------------------------------
        ## DIFFERENT PERSON - DIFFERENT RES PER DIFFERENT RES ORIGINAL FACE
        ## --------------------------------  
    temp1 = list()
    temp1.append(person_dictionary[1].faces[1].reso[8])
    known1 = person_dictionary[1].faces[1].reso[1]
    #print(face_recognition.face_distance(temp1, known1))

    for it_res in range(no_res):
        for person_it,person in enumerate(person_dictionary.values()):
            known = person.faces[1].reso[it_res]
            for person_diff in (list(person_dictionary.values())[:person_it]+list(person_dictionary.values())[person_it+1:]):
                #loop through all faces of the different person
                for face in person_diff.faces.values():
                    for key, value in face.reso.items():
                        aKey = key
                        aValue = value
                        temp.append(aValue)
                        keys.append(aKey)
                        aValue = ""
                        aKey = ""
                    
                    face_distances = face_recognition.face_distance(temp, known)
                    #make a dictionary with all the face_distances in it
                    face_recog.extend(face_distances)

                    temp = list()     
                #per person averaged distances 
                facedep_distance.extend(sumlist(face_recog,no_res,no_faces))
                face_recog = list()
            #print(facedep_distance,"\n\n")
            personal_distance.extend(sumlist(facedep_distance,no_res,no_persons-1))
            
            facedep_distance = list()
        #total averaged distances
        final_distance[it_res] = sumlist(personal_distance,no_res,no_res)
        keys = list()
    

    plt.figure(3)
    keys = list(range(0,10))
    legendls = list()
    for number in range(9):
        plt.plot(keys,final_distance[number+1])
        legendls.append(number)

    plt.legend(legendls)


