'------------------------------------------------------
'Create an instant System Restore Point under Windows 7
'------------------------------------------------------
If WScript.Arguments.Count = 0 Then
  Set oShell = CreateObject("Shell.Application")
  oShell.ShellExecute "wscript.exe", """"  &  WScript.ScriptFullName  &  """ Run", , "runas", 1
Else
  Set oWshShell = WScript.CreateObject("WScript.Shell")
  oWshShell.Popup "Creating a SystemRestore point. Please wait.", 2, "System Restore", 0
  swinmgmts = "winmgmts:\\.\root\default:Systemrestore"
  ddate = CStr(Year(Now) & "-" & Month(Now) & "-" & Day(Now) & "#" & Hour(Now) & ":" & Minute(Now) & ":" & Second(Now))
  dname = InputBox("Insert Name Of System Restore","Name Of System Restore",ddate)
  'GetObject(swinmgmts).CreateRestorePoint "Scheduled Restore Point", 0, 100
  'Do Until dname=OK AND !AbortedByUser
  '	GetObject(swinmgmts).CreateRestorePoint dname, 0, 100
  '	MsgBox "System Restore Point created", 0, "System Restore"
  'Loop
  If Len(dname) = 0 Then
    MsgBox "System Restore Point Caceled", 0, "System Restore"
  else
	GetObject(swinmgmts).CreateRestorePoint dname, 0, 100
	MsgBox "System Restore Point created", 0, "System Restore"
  End If
End If