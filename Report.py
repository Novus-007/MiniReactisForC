import pandas as pd

import html

def ReportGeneration(InFile,OuFile):

	InTesting=pd.read_csv(InFile)
	OuTesting=pd.read_csv(OuFile+".csv")

	SIZE,NoVariables=InTesting.shape
	VariablesName = InTesting.columns
	VariablesName_List=VariablesName.tolist()
	TimeIndex=VariablesName_List.index('___t___')
	
	Var=[]
	In=[]
	Ou=[]
	Dif=[]
	Step=[]
	for x in InTesting.index:
		for y in range(TimeIndex+1,NoVariables):
			if InTesting.iloc[x,y]!=OuTesting.iloc[x,y-TimeIndex-1]:
				Step.append(x)
				In.append(InTesting.iloc[x,y])
				Ou.append(OuTesting.iloc[x,y-TimeIndex-1])
				Dif.append(InTesting.iloc[x,y]-OuTesting.iloc[x,y-TimeIndex-1])
				Var.append(VariablesName[y])
	df_marks = pd.DataFrame({'Setp':Step,'Variable':Var,'Input':In,'Output':Ou,'Difference':Dif})

	html = df_marks.to_html()


	text_file = open(OuFile+"Difference.html", "w")
	text_file.write(html)
	text_file.close()
