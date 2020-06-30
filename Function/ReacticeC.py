import TestCreation
import Report
import subprocess
import os

def cleanformat(path,ext):
	
	text_files = [f for f in os.listdir(path) if f.endswith(ext)]
	for x in text_files:
		os.remove(x) 

cwd = os.getcwd()
f = open("DataInput.csv", "r")
R=f.read()
R1=R.split()
T=R1[0].split(',')
CFile = cwd+'/'+T[1]
T=R1[1].split(',')
CSV =cwd+'/'+ T[1]
T=R1[2].split(',')
TypeFile =cwd+'/'+ T[1]
T=R1[3].split(',')
FunctionName = T[1]
T=R1[4].split(',')
HeaderName = T[1]
T=R1[5].split(',')
OutputName = T[1]


text_files = [f for f in os.listdir(CFile) if f.endswith('.c')]
Files=''
for x in text_files:
	Files=Files+x+' '


TestCreation.testFunction(CSV,TypeFile,FunctionName,HeaderName,OutputName,CFile)	

CFile_Split = CFile
relative_path = os.path.relpath(CFile+"/demofile2.c",cwd)
relative_pathou = os.path.relpath(CFile+"/outputfile",cwd)
GccOutput="cd "+CFile+";gcc -fprofile-arcs -ftest-coverage -fPIC -O0 demofile2.c "+Files+" -o  outputfile"

GccCoverageOutput="cd "+CFile+";gcovr -r . -e demofile2.c --html --html-details -o "+str(OutputName)+".html"

print(GccCoverageOutput)
GccTerminal=subprocess.getstatusoutput(GccOutput)
Satus=0

if GccTerminal[0] !=0:
	print('Output Status 1', 'Following is the ERROR while Building:'+GccTerminal[1])
else:
	Satus=1
	print('Output Status 1', 'Succesfully Outputfile Built')

if Satus==1:
	GccOutput='cd '+CFile_Split+'; ./outputfile; cd '+cwd
	GccTerminal=subprocess.getstatusoutput(GccOutput)
	if GccTerminal[0] !=0:
		print('Output Status 2', 'Following is the ERROR while Execution:'+GccTerminal[1])
	else:
		print('Output Status 2', 'Succesfully Outputfile Created ')
		Satus=2
if Satus==2:
	GccTerminal=subprocess.getstatusoutput(GccCoverageOutput)
	GccTerminal1=subprocess.getstatusoutput('cd '+cwd)
	if GccTerminal[0] !=0:
		print('Output Status 3', 'Following is the ERROR while Execution:'+GccTerminal[1])
	else:
		print('Output Status 3', 'Succesfully Outputfile Created ')
		Report.ReportGeneration(CSV,CFile+"/"+str(OutputName))

cwd = os.getcwd()
os.chdir(CFile) 
cleanformat(CFile,'.gcda')
cleanformat(CFile,'.gcno')
os.remove('demofile2.c')
os.remove('outputfile')

os.chdir(cwd)
	

	
