# -*- coding: latin-1 -*-

from saagieapi import SaagieApi
import os
import requests
import sys
import base64

def CreateSaagieContext():
		CST_saagie_url = 'https://demo-workspace.a4.saagie.io/'
		saagie = SaagieApi(url_saagie=CST_saagie_url,
						id_platform="2",
						user="ESTIAM_G10_johnny.hu",
						password="Goyave2020",
					realm="demo")
		return saagie

def SetValue_to_GlobalEnvVariable(hEnvSaagie,VariableName,Value,Description,isPassword):
	ListVarEnvSaagie = hEnvSaagie.get_global_env_vars()
	ListVarName=[]
	for vecteur in ListVarEnvSaagie["globalEnvironmentVariables"] :
		ListVarName.append(vecteur['name'])

	print(ListVarName)
	if VariableName in ListVarName:
		hEnvSaagie.delete_global_env_var(VariableName)
	hEnvSaagie.create_global_env_var(VariableName,Value,Description,isPassword)
		
	return 0	

def SetValue_to_ProjectEnvVariable(hEnvSaagie,UUIDProject,VariableName,Value,Description,isPassword):
	ListVarEnvSaagie = hEnvSaagie.get_project_env_vars(UUIDProject)
	ListVarName=[]
	for vecteur in ListVarEnvSaagie["projectEnvironmentVariables"] :
		ListVarName.append(vecteur['name'])

	if VariableName in ListVarName:
		hEnvSaagie.delete_project_env_var(UUIDProject,VariableName)
	hEnvSaagie.create_project_env_var(UUIDProject,VariableName,Value,Description,isPassword)
		
	return 0	
def GetValue_from_ProjectEnvVariable(hEnvSaagie,UUIDProject,VariableName):
	ListVarEnvSaagie = hEnvSaagie.get_project_env_vars(UUIDProject)
	ListVarName=[]
	ValueEnvVariable="NIL"
	for vecteur in ListVarEnvSaagie["projectEnvironmentVariables"] :
		if (vecteur['name']) == VariableName:
			ValueEnvVariable = vecteur['value']
		
	
	return ValueEnvVariable

def Run_Pipeline(hEnvSaagie,IdPipeline):
	PipelineInformation = hEnvSaagie.run_pipeline(IdPipeline)
	return PipelineInformation