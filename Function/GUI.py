
# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import * 
from tkinter.ttk import *


from tkinter import messagebox as mb
import TestCreation
import Report
import subprocess

  
# importing askopenfile function 
# from class filedialog 

from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os 
  
root = Tk() 
root.title("MiniReactis")
root.geometry('200x200') 


  
# This function will be used to browse files and get its path
# file in read mode and only CSV files 
# will be opened 
def cleanformat(path,ext):
	
	text_files = [f for f in os.listdir(path) if f.endswith(ext)]
	for x in text_files:
		os.remove(x) 
	

def OpenFile_Type():
	global TypeFile
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.csv')]) 
	TypeFile=file.name 
	#print(TypeFile)

def OpenFile_CSV():
	global CSV
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.csv')]) 
	CSV=file.name 
	#print(CSV)
def OpenFile_File():
	global CFile
	filename = filedialog.askdirectory()
	CFile=filename
	#print(CSV)

# Run Button 
def RunButton():
	global CSV
	global TypeFile
	global CFile
	cwd = os.getcwd()
	text_files = [f for f in os.listdir(CFile) if f.endswith('.c')]
	Files=''
	for x in text_files:
		Files=Files+x+' '


	
	TestCreation.testFunction(CSV,TypeFile,FunctionName.get(),HeaderName.get(),OutputName.get(),CFile)
	
	print(CSV)
	print(TypeFile)
	print(FunctionName.get())
	print(HeaderName.get())
	print(OutputName.get())
	print(CFile)
	CFile_Split = CFile
	relative_path = os.path.relpath(CFile+"/demofile2.c",cwd)
	relative_pathou = os.path.relpath(CFile+"/outputfile",cwd)
	GccOutput="cd "+CFile+";gcc -fprofile-arcs -ftest-coverage -fPIC -O0 demofile2.c "+Files+" -o  outputfile"
	#print(GccOutput)

	GccCoverageOutput="cd "+CFile+";gcovr -r . -e demofile2.c --html --html-details -o "+str(OutputName.get())+".html"

	print(GccCoverageOutput)
	
	GccTerminal=subprocess.getstatusoutput(GccOutput)
	#os.remove(CFile_Split[0]+"/demofile2.c")
	Satus=0
	if GccTerminal[0] !=0:
		mb.showinfo('Output Status 1', 'Following is the ERROR while Building:'+GccTerminal[1])
				
	else:
		Satus=1
		mb.showinfo('Output Status 1', 'Succesfully Outputfile Built')

	
		
	if Satus==1:
		GccOutput='cd '+CFile_Split+'; ./outputfile; cd '+cwd
		GccTerminal=subprocess.getstatusoutput(GccOutput)
		
		if GccTerminal[0] !=0:
			mb.showinfo('Output Status 2', 'Following is the ERROR while Execution:'+GccTerminal[1])
		else:
			mb.showinfo('Output Status 2', 'Succesfully Outputfile Created ')
			Satus=2
	if Satus==2:
		GccTerminal=subprocess.getstatusoutput(GccCoverageOutput)
		GccTerminal1=subprocess.getstatusoutput('cd '+cwd)
		if GccTerminal[0] !=0:
			mb.showinfo('Output Status 3', 'Following is the ERROR while Execution:'+GccTerminal[1])
		else:
			mb.showinfo('Output Status 3', 'Succesfully Outputfile Created ')
			Report.ReportGeneration(CSV,CFile+"/"+OutputName.get())

	cwd = os.getcwd()
	os.chdir(CFile) 

	cleanformat(CFile,'.gcda')
	cleanformat(CFile,'.gcno')
	os.remove('demofile2.c')
	os.remove('outputfile')

	os.chdir(cwd)
	

	
  

#For the Type File
TypeText = Label(root,text="Type File ")
TypeText.pack()
TypeText.place(x=0,y=0)
TypeBrowse = Button(root, text ='Open', command = lambda:OpenFile_Type()) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=110,y=0)


#For the Type File
TypeText = Label(root,text="CSV Test File ")
TypeText.pack()
TypeText.place(x=0,y=30)
TypeBrowse = Button(root, text ='Open', command = lambda:OpenFile_CSV()) 
TypeBrowse.pack(side = TOP, pady = 10) 
TypeBrowse.place(x=110,y=30)

#Get Function Name
TypeText = Label(root,text="Function Name")
TypeText.pack()
TypeText.place(x=0,y=60)
FunctionName = Entry(root, width=10)
FunctionName.pack()
FunctionName.place(x=110,y=60)

#Get File  Name
TypeText = Label(root,text="CFile Name ")
TypeText.pack()
TypeText.place(x=0,y=85)
FileName = Button(root, text ='Open', command = lambda:OpenFile_File()) 
FileName.pack(side = TOP, pady = 10) 
FileName.place(x=110,y=85)


#Get Header Name
TypeText = Label(root,text="Header Name")
TypeText.pack()
TypeText.place(x=0,y=110)
HeaderName = Entry(root, width=10)
HeaderName.pack()
HeaderName.place(x=110,y=110)

#Get OutputFile Name
TypeText = Label(root,text="Output csvName")
TypeText.pack()
TypeText.place(x=0,y=135)
OutputName = Entry(root, width=10)
OutputName.pack()
OutputName.place(x=110,y=135)

#Build/Run Button
Run = Button(root, text ="Run", command = RunButton)
Run.pack()
Run.place(x=110,y=160)

mainloop()
