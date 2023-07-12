import os
import shutil

# replace the student ids below with your student ids
t1 = [19015884,19046103,19010544,19038851]

t2 = [19028476,19019068,19043825,19028458]

t3 = [19009825,19041528,19043192,19046242]

t4 = [19016271,19024989,19014821,19006618]

t5 = [19006547,19007582,19003063,19009352]

students = [t1, t2, t3, t4, t5]

files = os.listdir('.')

# remove empty folder
for afile in files:
    # check that the file is a directory
    if os.path.isdir(afile):
        # remove directory, only empty directory can be removed
        try:
            os.rmdir(afile)
        except OSError:
            pass


# create team folder
for i in range(1, 6):
    filename = "Team " + str(i)
    if not os.path.exists (filename):
        os.mkdir(filename)
        
# copy folder
count = 1
for tt in students:
    for t in tt:
        t = str(t)
        
        for f in files:
            if f.find(t) != -1:
                t = f
        
        if os.path.exists(t):
            desc = 'Team ' + str(count) + '/' + t + '/'
            print(desc)
            if not os.path.exists(desc):
                shutil.copytree(t,desc)
        
        # remove student folder
        if os.path.exists(t):
            shutil.rmtree(t)
    
    count+=1
            
            
            

