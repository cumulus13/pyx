#--------------------------------------------------------------------------------- 
#The sample scripts are not supported under any Microsoft standard support 
#program or service. The sample scripts are provided AS IS without warranty  
#of any kind. Microsoft further disclaims all implied warranties including,  
#without limitation, any implied warranties of merchantability or of fitness for 
#a particular purpose. The entire risk arising out of the use or performance of  
#the sample scripts and documentation remains with you. In no event shall 
#Microsoft, its authors, or anyone else involved in the creation, production, or 
#delivery of the scripts be liable for any damages whatsoever (including, 
#without limitation, damages for loss of business profits, business interruption, 
#loss of business information, or other pecuniary loss) arising out of the use 
#of or inability to use the sample scripts or documentation, even if Microsoft 
#has been advised of the possibility of such damages 
#--------------------------------------------------------------------------------- 

#requires -Version 3.0

Function Set-OSCPin
{
<#
 	.SYNOPSIS
        Set-OSCPin is an advanced function which can be used to pin a item or more items to the Start menu.
    .DESCRIPTION
        Set-OSCPin is an advanced function which can be used to pin a item or more items to the Start menu.
    .PARAMETER  <Path>
		Specifies a path to one or more locations.
    .EXAMPLE
        C:\PS> Set-OSCPin -Path "C:\Windows"
		
        Pin "Windows" to the Start menu sucessfully.

		This command shows how to pin the "shutdown.exe" file to the Start menu.
    .EXAMPLE
        C:\PS> Set-OSCPin -Path "C:\Windows","C:\Windows\System32\shutdown.exe"
		
        Pin "Windows" to the Start menu sucessfully.
        Pin "shutdown.exe" to the Start menu sucessfully.

		This command shows how to pin the "Windows" folder and "shutdown.exe" file to the Start menu.
#>
    [CmdletBinding()]
    Param
    (
        [Parameter(Mandatory,Position=0)]
        [Alias('p')]
        [String[]]$Path
    )

    $Shell = New-Object -ComObject Shell.Application
	$Desktop = $Shell.NameSpace(0X0)
    $WshShell = New-Object -comObject WScript.Shell
    $Flag=0

    Foreach($itemPath in $Path)
    {
        $itemName = Split-Path -Path $itemPath -Leaf
        #pin application to windows Start menu
        $ItemLnk = $Desktop.ParseName($itemPath)
        $ItemVerbs = $ItemLnk.Verbs()
        Foreach($ItemVerb in $ItemVerbs)
        {
            If($ItemVerb.Name.Replace("&","") -match "Pin to Start")
            {
                $ItemVerb.DoIt()
                $Flag=1
            }
        }
        
        If($Flag=1)
        {
            Write-Host "Pin ""$ItemName"" to the Start menu sucessfully." -ForegroundColor Green
        }
        Else
        {
            Write-Host "The ""$ItemName"" cannot pin to the Start menu." -ForegroundColor Red
        }
    }
}