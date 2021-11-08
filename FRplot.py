import face_recognition
from matplotlib import pyplot as plt
from matplotlib.cm import get_cmap
from timeit import default_timer as timer
import pickle
import collections
from dataclasses import person
from dataclasses import face
from exp1 import sameperson_differentres
from exp2 import differentperson_differentres
from exp3 import differentperson_differentres2
from listfunctions import sumlist, average


def printtime(timer,start_time):
    end_time = timer()
    hours, rem = divmod(end_time-start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print("done in = {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))



def main():
    start_time = timer()

    no_persons = 20
    no_faces = 5
    no_res= 10
    no_gaus = 10
    person_dictionary = dict()

    with open('face_data.pkl', 'rb') as input:
        person_dictionary = pickle.load(input)

    sameperson_differentres(person_dictionary, no_persons, no_faces, no_res, no_gaus)
    #differentperson_differentres(person_dictionary, no_persons, no_faces, no_res, no_gaus)
    #differentperson_differentres2(person_dictionary, no_persons, no_faces, no_res, no_gaus)


    #distance = face_recognition.face_distance(unknown, known)

    printtime(timer,start_time)

    





    #purely for time demonstration
 
    # the histogram of the data
    #print(resdistances[1])

    #legendls = []

    #for i in range(3):
    #    plt.hist(resdistances[3*i+1],30)
    #    legendls.append(str(3*i+1))
    #plt.legend(legendls)
    #plt.show()
    #print(final_distance_same )

    #plot of same person however different face and different resolution

    #plt.show()


    #plt.show()




    plt.show()



    


if __name__ == '__main__':
    main()
