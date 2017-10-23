#use Cwd;

#$directory = cwd;

#$size = -s $directory;

#print $size;

#!/usr/bin/perl
##Get the current directory location
use Cwd;

##Setting variable to database name
$directory = cwd ;

##assign the variable file
$file = "$directory" ;

##using if then and the -e switch to find if file exists
if ( -e $file ) 
{ 
print "ceksize file at $directory exists\n" ;
 } 

##if the file does not exist then print this
else 
{ 
print "ceksize does not exist\n" ;
 } 

##using the -s switch to find out the files size
$size = -f $file ;

##printing out the file size
print "ceksize is $size bytes\n" ;

print $directory;
exit;
