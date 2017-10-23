use Win32::Process;


if (@ARGV == 1)
{
    $ex = $ARGV[0];

    Win32::Process::Create($Process, "C:\\Program Files\\CoderTools\\TotalEdit\\TEditStd.exe", "TEditStd  $ex",  0, 
        DETACHED_PROCESS, ".") || die "Create: $!";
    #system("C:\\Program Files\\CoderTools\\TotalEdit\\TEditStd.exe", $ex);

}
else{
        print "\n\n";
        print "\t\t Usage2  : $0 File \n";
        print "\n";
}