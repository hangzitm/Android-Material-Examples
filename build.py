import os
import sys
import time

def accBuild():
   
    BRANCH_NAME = sys.argv[4]


    os.system("git checkout " + BRANCH_NAME)
    os.system("git checkout .")
    os.system("git pull origin " + BRANCH_NAME)

		
def preBuild(type):
    print 'preBuild type=' + type

    #chmod
    os.system('chmod +x gradlew')
    os.system('chmod +x build.py')
    os.system('chmod +x mk.sh')

 
    #prebuild
    os.system('./gradlew clean')

    if type == 'debug':
        os.system('./gradlew assembleDebug')
    if type == 'release':
        os.system('./gradlew assembleRelease')

def excute():
    accBuild()

    JOB_NAME = sys.argv[1]
    BUILD_ID = sys.argv[2]
    BUILD_TYPE = sys.argv[3]
    BUILD_YMD = time.strftime("%Y%m%d%H%M%S")
  
    #pre build
    preBuild(BUILD_TYPE)

    #excute cmd
    cmd = ("bash cp.sh %s %s  %s %s") % (JOB_NAME, BUILD_ID, BUILD_TYPE, BUILD_YMD)
    print "cmd=" + cmd
    os.system(cmd)

if __name__ == "__main__":
    excute()
