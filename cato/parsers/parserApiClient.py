import json
from graphql_client import ApiClient, CallApi
from graphql_client.api_client import ApiException
import logging
import pprint

def createRequest(args, configuration):
	params = vars(args)
	instance = CallApi(ApiClient(configuration))
	operationName = params["operation_name"]
	operation = loadJSON("models/"+operationName+".json")
	try:
		variablesObj = json.loads(params["json"])	
	except ValueError as e:
		print("ERROR: Query argument must be valid json in quotes. ",e,'\n\nExample: \'{"yourKey":"yourValue"}\'')
		exit()
	if "accountID" in operation["operationArgs"]:
		variablesObj["accountID"] = params["accountID"]	
	elif "accountId" in operation["args"]:
		variablesObj["accountId"] = params["accountID"]	
	isOk, invalidVars, message = validateArgs(variablesObj,operation)
	if isOk==True:
		body = generateGraphqlPayload(variablesObj,operation,operationName)
		if params["t"]==True:
			if params["p"]==True:
				print(json.dumps(body,indent=2,sort_keys=True).replace("\\n", "\n").replace("\\t", "  "))
			else:
				print(json.dumps(body).replace("\\n", " ").replace("\\t", " ").replace("    "," ").replace("  "," "))
			return None
		else:
			try:
				return instance.call_api(body,params)
			except ApiException as e:
				return e
	else:
		print("ERROR: "+message,", ".join(invalidVars))

def createRawRequest(args, configuration):
	params = vars(args)
	instance = CallApi(ApiClient(configuration))
	isOk = False
	try:
		body = json.loads(params["json"])
		isOk = True
		# if "variables" in body and "query" in body and "operationName" in body:
		# 	isOk = True
		# else:
		# 	print("Invalid request, argument must be valid json including 'variables', 'query', and 'operationName' keys")
	except ValueError as e:
		print("ERROR: Argument must be valid json. ",e)
		isOk=False	
	except Exception as e:
		isOk=False
		print("ERROR: ",e)
	if isOk==True:
		if params["t"]==True:
			if params["p"]==True:
				print(json.dumps(body,indent=2,sort_keys=True).replace("\\n", "\n").replace("\\t", "\t"))
			else:
				print(json.dumps(body).replace("\\n", " ").replace("\\t", " ").replace("    "," ").replace("  "," "))
			return None
		else:
			try:
				return instance.call_api(body,params)
			except ApiException as e:
				print(e)
				exit()

def generateGraphqlPayload(variablesObj,operation,operationName):
	indent = "	"
	queryStr = ""
	variableStr = ""
	for varName in variablesObj:
		if (varName in operation["operationArgs"]):
			variableStr += operation["operationArgs"][varName]["requestStr"]
	operationAry = operationName.split(".")
	operationType = operationAry.pop(0)
	queryStr = operationType + " "
	queryStr += renderCamelCase(".".join(operationAry))
	queryStr += " ( " + variableStr + ") {\n"
	queryStr += indent + operation["name"] + " ( "			
	for argName in operation["args"]:
		arg = operation["args"][argName]
		if arg["varName"] in variablesObj:
			queryStr += arg["responseStr"]
	queryStr += ") {\n" + renderArgsAndFields("", variablesObj, operation, operation["type"]["definition"], "		") + "	}"
	queryStr += indent + "\n}";
	body = {
		"query":queryStr,
		"variables":variablesObj,
		"operationName":renderCamelCase(".".join(operationAry)),
	}
	return body

def get_help(path):
	matchCmd = "cato "+path.replace("_"," ")
	import os
	pwd = os.path.dirname(__file__)
	doc = path+"/README.md"
	abs_path = os.path.join(pwd, doc)
	new_line = "\nEXAMPLES:\n"
	lines = open(abs_path, "r").readlines()
	for line in lines:
		if f"{matchCmd}" in line:
			clean_line = line.replace("<br /><br />", "").replace("`","")
			new_line += f"{clean_line}\n"
	# matchArg = path.replace("_",".")
	# for line in lines:
	# 	if f"`{matchArg}" in line:
	# 		clean_line = line.replace("<br /><br />", "").replace("`","")
	# 		new_line += f"{clean_line}\n"
	return new_line

# def renderParentOperation(pathStr):
# 	str = ""
# 	operationAry = pathStr.split(".")
# 	operationType = operationAry.pop(0)
# 	str = operationType + " "
# 	# str += operationType + " "
# 	# if (operationType == "query"):
# 	# 	str += operationAry[0]
# 	# else:
# 	# for operation in operationAry:
# 	# 	print("operation",operation)
# 		# str += operation[0].upper() + operation[1:]
# 	for i, operation in enumerate(operationAry):
# 		if i == 0:
# 			str += operation
# 		else:
# 			str += operation[0].upper() + operation[1:]
# 	return str

def validateArgs(variablesObj,operation):
	isOk = True
	invalidVars = []
	message = "Arguments are missing or have invalid values: "
	for varName in variablesObj:
		if varName not in operation["operationArgs"]:
			isOk = False
			invalidVars.append('"'+varName+'"')
			message = "Invalid argument names: "
	if isOk==True:
		for varName in operation["operationArgs"]:
			if operation["operationArgs"][varName]["required"] and varName not in variablesObj:
				isOk = False
				invalidVars.append('"'+varName+'"')
			else:
				if varName in variablesObj:
					value = variablesObj[varName]
					if operation["operationArgs"][varName]["required"] and value=="":
						isOk = False
						invalidVars.append('"'+varName+'":"'+str(value)+'"')
	return isOk, invalidVars, message

def loadJSON(file):
	CONFIG = {}
	try:
		with open(file, 'r') as data:
			CONFIG = json.load(data)
			# logging.warning("Loaded "+file+" data")
			return CONFIG
	except:
		logging.warning("File \""+file+"\" not found.")
		exit()

def renderCamelCase(pathStr):
	str = "";
	pathAry = pathStr.split(".") 
	for i, path in enumerate(pathAry):
		if i == 0:
			str += path
		else:
			str += path[0].upper() + path[1:]
	return str	

def renderArgsAndFields(responseArgStr, variablesObj, curOperation, definition, indent):
	for fieldName in definition['fields']:
		field = definition['fields'][fieldName]
		field_name = field['alias'] if 'alias' in field else field['name']				
		responseArgStr += indent + field_name
		if field.get("args") and not isinstance(field['args'], list):
			if (len(list(field['args'].keys()))>0):
				argsPresent = False
				argStr = " ( "
				for argName in field['args']:
					arg = field['args'][argName]
					if arg["varName"] in variablesObj:
						argStr += arg['responseStr'] + " "
						argsPresent = True
				argStr += ") "
				if argsPresent==True:
					responseArgStr += argStr
		if field.get("type") and field['type'].get('definition') and field['type']['definition']['fields'] is not None:
			responseArgStr += " {\n"
			for subfieldIndex in field['type']['definition']['fields']:
				subfield = field['type']['definition']['fields'][subfieldIndex]
				subfield_name = subfield['alias'] if 'alias' in subfield else subfield['name']				
				responseArgStr += indent + "	" + subfield_name
				if subfield.get("args") and len(list(subfield["args"].keys()))>0:
					argsPresent = False
					subArgStr = " ( "
					for argName in subfield['args']:
						arg = subfield['args'][argName]
						if arg["varName"] in variablesObj:
							argsPresent = True
							subArgStr += arg['responseStr'] + " "
					subArgStr += " )"
					if argsPresent==True:
						responseArgStr += subArgStr
				if subfield.get("type") and subfield['type'].get("definition") and (subfield['type']['definition'].get("fields") or subfield['type']['definition'].get('inputFields')):
					responseArgStr += " {\n"
					responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, subfield['type']['definition'], indent + "		")
					if subfield['type']['definition'].get('possibleTypes'):
						for possibleTypeName in subfield['type']['definition']['possibleTypes']:
							possibleType = subfield['type']['definition']['possibleTypes'][possibleTypeName]
							responseArgStr += indent + "		... on " + possibleType['name'] + " {\n"
							if possibleType.get('fields') or possibleType.get('inputFields'):
								responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, possibleType, indent + "			")
							responseArgStr += indent + "		}\n"
					responseArgStr += indent + "	}"
				elif subfield.get('type') and subfield['type'].get('definition') and subfield['type']['definition'].get('possibleTypes'):
					responseArgStr += " {\n"
					responseArgStr += indent + "		__typename\n"
					for possibleTypeName in subfield['type']['definition']['possibleTypes']:
						possibleType = subfield['type']['definition']['possibleTypes'][possibleTypeName]						
						responseArgStr += indent + "		... on " + possibleType['name'] + " {\n"
						if possibleType.get('fields') or possibleType.get('inputFields'):
							responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, possibleType, indent + "			")
						responseArgStr += indent + "		}\n"
					responseArgStr += indent + " 	}\n"
				responseArgStr += "\n"
			if field['type']['definition'].get('possibleTypes'):
				for possibleTypeName in field['type']['definition']['possibleTypes']:
					possibleType = field['type']['definition']['possibleTypes'][possibleTypeName]
					responseArgStr += indent + "	... on " + possibleType['name'] + " {\n"
					if possibleType.get('fields') or possibleType.get('inputFields'):
						responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, possibleType, indent + "		")
					responseArgStr += indent + "	}\n"
			responseArgStr += indent + "}\n"
		if field.get('type') and field['type'].get('definition') and field['type']['definition'].get('inputFields'):
			responseArgStr += " {\n"
			for subfieldName in field['type']['definition'].get('inputFields'):
				subfield = field['type']['definition']['inputFields'][subfieldName]
				subfield_name = subfield['alias'] if 'alias' in subfield else subfield['name']
				responseArgStr += indent + "	" + subfield_name
				if subfield.get('type') and subfield['type'].get('definition') and (subfield['type']['definition'].get('fields') or subfield['type']['definition'].get('inputFields')):
					responseArgStr += " {\n"
					responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, subfield['type']['definition'], indent + "		")
					responseArgStr += indent + "	}\n"
			if field['type']['definition'].get('possibleTypes'):
				for possibleTypeName in field['type']['definition']['possibleTypes']:
					possibleType = field['type']['definition']['possibleTypes'][possibleTypeName]
					responseArgStr += indent + "... on " + possibleType['name'] + " {\n"
					if possibleType.get('fields') or possibleType.get('inputFields'):
						responseArgStr = renderArgsAndFields(responseArgStr, variablesObj, curOperation, possibleType, indent + "		")
					responseArgStr += indent + "	}\n"
			responseArgStr += indent + "}\n"
		responseArgStr += "\n"
	return responseArgStr
