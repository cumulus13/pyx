Set objShell = CreateObject("Shell.Application")
Set filesystem = CreateObject("scripting.Filesystemobject")
If filesystem.FileExists(Wscript.Arguments(0)) Then
 Set objFolder = objShell.Namespace(filesystem.GetParentFolderName(Wscript.Arguments(0)))
 Set objFolderItem = objFolder.ParseName(filesystem.GetFileName(WScript.Arguments(0)))
 Set colVerbs = objFolderItem.Verbs
 
 Select case WScript.Arguments(1)
  case 0
   For Each objVerb in colVerbs
    If Replace(objVerb.name, "&", "") = "UnPin from Start" Then objVerb.DoIt
   Next
  case 1
   For Each objVerb in colVerbs
    If Replace(objVerb.name, "&", "") = "Pin to Start" Then objVerb.DoIt
   Next
 End Select
End If

Wscript.timeout = 1
'wscript.echo("Success!")

'MsgBox "Custom Text",vbCritical,"Custom Title"



'Pin to Start Men&u
	'msgbox "Adding the item "&objFolderItem&" to start menu done!"