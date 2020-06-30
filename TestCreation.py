import pandas as pd
import os

def testFunction(CSVTestCase,CSVTestDataType,FunctionName,HeaderName,OutputFile,InputFile):

	# _D:Declaration
	DfDeclaration=pd.read_csv(CSVTestDataType)
	DfTesting=pd.read_csv(CSVTestCase)
	
	InputFile_Split = InputFile 
	
	#VariablesDataType = DfDeclaration['DataType']
	#VariablesName_D = DfDeclaration['Name']
	SIZE,NoVariables=DfTesting.shape
	VariablesName = DfTesting.columns
	VariablesName_List=VariablesName.tolist()
	TimeIndex=VariablesName_List.index('___t___')


	f = open(InputFile_Split+"/demofile2.c", "w")
	f.write("#include \""+HeaderName+"\"\n" )
	f.write("#include <stdio.h>\n" )
	for x in range(TimeIndex):
		f.write(str(DfDeclaration['DataType'][x])+" In_"+str(DfDeclaration['Name'][x])+"["+str(SIZE)+"];\n")
		
	f.write("void Declaration()\n" )
	f.write("{\n")

	for x in DfTesting.index:
		for y in range(TimeIndex):
			f.write("\tIn_"+str(VariablesName_List[y])+"["+str(x)+"]="+str(DfTesting.iloc[x,y])+";\n" )
		f.write("\n")
	f.write("}\n")
	f.write("int main()\n")
	f.write("{\n")

	f.write("\tFILE *fp;\n")
	f.write("\tfp = fopen(\""+OutputFile+".csv\", \"w+\");\n")

	for x in range(TimeIndex+1,NoVariables):
		f.write("\tfprintf(fp,\" "+str(VariablesName_List[x])+",\");\n")
	
	f.write("\tfprintf(fp,\" \\n \");\n")
	
	f.write("\tDeclaration();\n")	
	f.write("\tfor(int i=0;i<"+str(SIZE)+str(";i++)\n"))
	f.write("\t{\n")
	for x in range(TimeIndex):
		f.write("\t\t"+str(VariablesName_List[x])+"=In_"+str(VariablesName_List[x])+"[i];\n")

	f.write("\t\t"+FunctionName+"();\n")


	for x in range(TimeIndex+1,NoVariables):
		f.write("\t\tfprintf(fp,\"%d,\","+str(VariablesName_List[x])+");\n")

	f.write("\t\tfprintf(fp,\" \\n \");\n")
	f.write("\t}\n")
	f.write("}\n")
	f.close()
	'''
	# For Test File
	df=pd.read_csv('test.csv')
	VariablesName = df.columns
	VariablesName_List=VariablesName.tolist()
	TimeIndex=VariablesName_List.index('___t___')
	print(TimeIndex)
	'''
