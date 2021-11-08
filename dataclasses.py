import face_recognition
from matplotlib import pyplot
from timeit import default_timer as timer
import pickle


class face:
    def __init__(self,base_path,face_num,person_num,no_res,no_gaus):
        self.face_num = face_num
        self.person_num = person_num
        original_path = base_path + "original/s" + str(self.person_num) + "_or_" + str(face_num) + ".png"
        self.orig = face_recognition.face_encodings(face_recognition.load_image_file(original_path))[0]
        
        self.reso = dict()
        self.reso[0] = self.orig
        for it_res in range(no_res):
            path = base_path + "res" + str(it_res+1) + "/" + str(face_num) + ".png"
            self.reso[it_res+1] = face_recognition.face_encodings(face_recognition.load_image_file(path))[0]

        
        self.gaus = dict()
        self.gaus[0] = self.orig
        for it_gaus in range(no_gaus):
            path = base_path + "gaus" + str(it_gaus+1) + "/" + str(face_num) + ".png"
            self.gaus[it_gaus+1] = face_recognition.face_encodings(face_recognition.load_image_file(path))[0]

class person:
    def __init__(self,path,person_num,no_faces,no_res,no_gaus):
        self.faces = dict()
        self.person_num = person_num
        for face_num in range(no_faces):
            self.faces[face_num+1] = face(path,face_num+1,person_num,no_res,no_gaus)

def main():
    start_time = timer()

    no_persons = 20
    no_faces = 5
    no_res= 9
    no_gaus = 9
    person_dictionary = dict()
    print("Start")
    for it_person in range(no_persons):
        print("Putting person", it_person+1, "into the database...")
        path = "Database/s" + str(it_person+1) + "/"
        person_dictionary[it_person+1] = person(path,it_person+1,no_faces,no_res,no_gaus)

    with open('face_data.pkl', 'wb') as output:
        pickle.dump(person_dictionary, output, pickle.HIGHEST_PROTOCOL)

    end_time = timer()
    hours, rem = divmod(end_time-start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print("done creating the classes in = {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
##run this file to save the complete class structure
if __name__ == '__main__':
    main()