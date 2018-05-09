import sys, os
import pdb
import zipfile
import shutil

def add0(item):
    if item < 10:
        return str(0) + str(item)
    else:
        return str(item)


def convert_tut(tut):
    return add0(tut)


def convert_assignment(assignment):
    assignment = int(assignment)
    return add0(assignment)


def isZip(zip, openHa):
    #if openHa.prename in zip and openHa.sirname in zip:
    if openHa.prename in zip:
        return True
    else:
        return False



class openHa:
    def __init__(self, assignment, prename, sirname):

        #settings
        self.mainpath = "/Users/alessandroschneider/Desktop/TuBerlin/Tutor/studis"
        self.zippath = "/Users/alessandroschneider/Desktop/TuBerlin/Tutor/studis/packs/"

        self.assignment = convert_assignment(assignment)
        self.pack = "SoSe18 Prog2 WINF-HA"+self.assignment

        self.prename = prename
        self.sirname = sirname

        try:
            self.zip = self.findZip()

        except Exception:
            print'File not found. Please check manually.'

        else:

            self.tut = self.getTut()

            self.unzip()

            self.moveToMain()

            self.open()


    def getTut(self):

        for i in range(14):

            if convert_tut(i) in self.zip:
                return "T" + convert_tut(i)


    def findZip(self):

        path = self.zippath + self.pack

        files = []

        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:

                if (isZip(name,self)):
                    return path + "/" + name

        raise Exception("No file found")





    def unzip(self):

        zip_ref = zipfile.ZipFile(self.zip, 'r')
        zip_ref.extractall(self.mainpath+"/tmp")
        zip_ref.close()


    def moveToMain(self):
        for item_path in os.listdir(self.mainpath+"/tmp"):
            try:
                shutil.move(os.path.join(self.mainpath+"/tmp", item_path), os.path.join(self.mainpath+"/" + self.findPath(), item_path))
            except:
                print ("not moving again, might stay in tmp")



    def open(self):
        path = self.mainpath + self.findPath()
        count_pom = 0
        pompaths= []
        for root, dirs, files in os.walk(path):
            for file in files:

                if file=="pom.xml" and "bin" not in root:
                    #pdb.set_trace()
                    count_pom = count_pom + 1
                    pompaths.append(root)

        #assume the shortest is the best:
        pompath = min(pompaths, key=len)


        if count_pom>1:
            print("More than 1 pom file found!")
        os.system("idea " + pompath)



    def findPath(self):
        return "/assignment" + str(self.assignment) + "-" + self.tut + "-" + self.prename + self.sirname


if __name__ == '__main__':
    assignment = sys.argv[1]
    prename =  sys.argv[2]

    if type(sys.argv[3])==str:
        lastname =  sys.argv[3]


    ha = openHa(assignment,prename, lastname)


