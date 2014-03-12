#!/usr/bin/env python
#-------------------------------
# gPyCompile v0.1.1
#-------------------------------
# Written by Alec Hussey
# License: General Public License
#-------------------------------

import os, compiler
from wx import stc
from wxPython.wx import *

ID_OPEN = 100
ID_SAVE = 105
ID_EXIT = 110
ID_COMPILE = 120
ID_SYNTAXCHECK = 125
ID_RUNPROGRAM = 130
ID_ABOUT = 150

class gpycFrame(wxFrame):
	def __init__(self, parent, ID, title):
		wxFrame.__init__(self, parent, ID, title, wxDefaultPosition, wxSize(700, 500))
		self.Filename = ""
		self.Directory = ""
		self.TextControl = stc.StyledTextCtrl(self, 1, style=wxTE_MULTILINE)
		self.CreateStatusBar()
		
		fileMenu = wxMenu()
		fileMenu.Append(ID_OPEN, "&Open", "Open a file.")
		fileMenu.Append(ID_SAVE, "&Save", "Save the current file.")
		fileMenu.AppendSeparator()
		fileMenu.Append(ID_EXIT, "E&xit", "Terminate the application.")
		sourceMenu = wxMenu()
		sourceMenu.Append(ID_COMPILE, "Compile", "Compile the program to bytecode.")
		sourceMenu.Append(ID_SYNTAXCHECK, "Syntax Check", "Check syntax of the program.")
		sourceMenu.Append(ID_RUNPROGRAM, "Run Program", "Run the newly compiled program.")
		helpMenu = wxMenu()
		helpMenu.Append(ID_ABOUT, "&About", "More information about the program.")
		
		menuBar = wxMenuBar()
		menuBar.Append(fileMenu, "&File")
		menuBar.Append(sourceMenu, "S&ource")
		menuBar.Append(helpMenu, "&Help")
		
		self.SetMenuBar(menuBar)
		self.Show(True)
		
		EVT_MENU(self, ID_OPEN, self.OnOpen)
		EVT_MENU(self, ID_SAVE, self.OnSave)
		EVT_MENU(self, ID_EXIT, self.OnExit)
		EVT_MENU(self, ID_COMPILE, self.OnCompile)
		EVT_MENU(self, ID_SYNTAXCHECK, self.OnSyntaxCheck)
		EVT_MENU(self, ID_RUNPROGRAM, self.OnRunProgram)
		EVT_MENU(self, ID_ABOUT, self.OnAbout)
	def OnOpen(self, event):
		opendialog = wxFileDialog(self, "Choose a File", self.Directory, "", "*.py", wxOPEN)
		if opendialog.ShowModal() == wxID_OK:
			self.Filename = opendialog.GetFilename()
			self.Directory = opendialog.GetDirectory()
			try:
				try:
					fopen = open(os.path.join(self.Directory, self.Filename), "r")
					self.TextControl.ClearAll()
					self.TextControl.AddText(fopen.read())
				except IOError:
					msgdialog = wxMessageDialog(self, "An exception was triggered. Couldn't open file.", "IO Error", wxOK | wxICON_ERROR)
					msgdialog.ShowModal()
					msgdialog.Destroy()
			except UnicodeDecodeError:
				msgdialog = wxMessageDialog(self, "An exception was triggered. Invalid encoding or encoding not supported.", "Unicode Decode Error", wxOK | wxICON_ERROR)
				msgdialog.ShowModal()
				msgdialog.Destroy()
			fopen.close()
	def OnSave(self, event):
		if self.Filename != "" and self.Directory != "":
			try:
				fopen = open(os.path.join(self.Directory, self.Filename), "w+")
				fopen.write(self.TextControl.GetText())
			except IOError:
				msgdialog = wxMessageDialog(self, "An exception was triggered. Couldn't write to file.", "IO Error", wxOK | wxICON_INFORMATION)
				msgdialog.ShowModal()
				msgdialog.Destroy()
			fopen.close()
	def OnExit(self, event):
		self.Close(True)
	def OnCompile(self, event):
		if self.Filename != "" and self.Directory != "":
			self.SetStatusText("Compiling program...")
			compiler.compileFile(str(os.path.join(self.Directory, self.Filename)))
			self.SetStatusText("Complete")
			# Show message dialog
			msgdialog = wxMessageDialog(self, "File was compiled successfully.", "Information", wxOK | wxICON_INFORMATION)
			msgdialog.ShowModal()
			msgdialog.Destroy()
		else:
			msgdialog = wxMessageDialog(self, "You don't have any files open.", "Information", wxOK | wxICON_INFORMATION)
			msgdialog.ShowModal()
			msgdialog.Destroy()
	def OnSyntaxCheck(self, event):
		if self.Filename != "" and self.Directory != "":
			self.SetStatusText("Checking syntax...")
			try:
				compiler.parse(self.TextControl.GetText())
			except SyntaxError:
				errdialog = wxMessageDialog(self, "An error was found in your code.\n\n"+`compiler.ast.Module`, "Syntax Error", wxOK | wxICON_ERROR)
				errdialog.ShowModal()
				errdialog.Destroy()
				return False
			msgdialog = wxMessageDialog(self, "No errors were found in your code.", "Information", wxOK | wxICON_INFORMATION)
			msgdialog.ShowModal()
			msgdialog.Destroy()
			self.SetStatusText("Complete")
		else:
			msgdialog = wxMessageDialog(self, "You don't have any files open.", "Information", wxOK)
			msgdialog.ShowModal()
			msgdialog.Destroy()
	def OnRunProgram(self, event):
		if self.Filename != "" and self.Directory != "":
			self.SetStatusText("Running program...")
			self.filecheck = open(os.path.join(self.Directory, self.Filename))
			if not self.filecheck:
				msgdialog = wxMessageDialog(self, "Either you have deleted the compiled program or you have not yet compiled it.", "Information", wxOK | wxICON_ERROR)
				msgdialog.ShowModal()
				msgdialog.Destroy()
				self.SetStatusText("Error Running Program")
			else:
				try:
					os.popen("python " + os.path.join(self.Directory, self.Filename+"c"))
				except:
					msgdialog = wxMessageDialog(self, "An error occured while running the program.", "Information", wxOK | wxICON_ERROR)
					msgdialog.ShowModal()
					msgdialog.Destroy()
					self.SetStatusText("Error Running Program")
				self.SetStatusText("Complete")
		else:
			msgdialog = wxMessageDialog(self, "You don't have any files open.", "Information", wxOK)
			msgdialog.ShowModal()
			msgdialog.Destroy()
			self.SetStatusText("Complete")
	def OnAbout(self, event):
		dialog = wxMessageDialog(self, "gPyCompile 0.1.1 \n\n"
										"A simple GUI for the Python bytecode compiler.\n\n"
										"Writen by Alec Hussey\n"
										"Contact: admin.maddog39@gmail.com",
										"About", wxOK | wxICON_INFORMATION)
		dialog.ShowModal()
		dialog.Destroy()

class gpycApp(wxApp):
	def OnInit(self):
		frame = gpycFrame(NULL, -1, "gPyCompile")
		frame.Show(True)
		self.SetTopWindow(frame)
		return True

application = gpycApp(0)
application.MainLoop()
