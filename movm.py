#!/usr/bin/env python
import os
import subprocess
import shutil

homePath = os.path.expanduser("~")
vmPath = None
vbPath = os.environ.get('VBOX_MSI_INSTALL_PATH',None)
id = None
with open('./.vagrant/machines/default/virtualbox/id') as file:
	id = file.read()


def parseLine(line):
	result = None
	fields = line.split()
	if len(fields) > 2 and fields[0] in ('Log') and fields[1] in ('folder:'):
		result = fields[2]
	return result

def exportVM():
	global vbPath
	global id
	if vbPath is not None and id is not None:
		cmd = subprocess.Popen([vbPath+'VBoxManage', 'showvminfo', id], stdout=subprocess.PIPE)
		for line in cmd.stdout:
			if line:
				item = parseLine(line)
				if item is not None:
					vmPath = item[:item.rfind('\Logs')]
	if vmPath is not None:
		shutil.move(vmPath, os.getcwd())
		print "Export OK. :-)\n"

def importVM():
	global vbPath
	global id
	global homePath
	defaultMachineFolder = None
	partialName = None
	vmFolder = None
	vbPropertiesFile = homePath + '\\.VirtualBox\\VirtualBox.xml'
	with open(vbPropertiesFile) as file:
		for line in file:
			if 'SystemProperties' in line:
				fields = line.split()
				defaultMachineFolder = fields[1].split('=')
				defaultMachineFolder = defaultMachineFolder[1].replace('"','')
	with open('./.vagrant/machines/default/virtualbox/action_set_name') as file:
		partialName = file.read()
	pwd = os.getcwd()
	for name in os.listdir(pwd):
		if os.path.isdir(os.path.join(pwd,name)):
			if partialName in (name):
				vmFolder = name
				if defaultMachineFolder is not None:
					shutil.move('.\\'+vmFolder,defaultMachineFolder)
					print "Import OK."

importVM()