system ('cls');
system ('echo.');
system ('echo.');
system ('echo.');

print "\t\t############ SendmailX #############\n";
print "\t\t#                                  #\n";
print "\t\t#        Sc1pt by B4L4CK1D         #\n";
print "\t\t#                                  #\n";
print "\t\t####################################\n\n";


print "\t\tEmail To = ";
$from = <STDIN>;
print "\n";
print "\t\tEmail From = ";
$to = <STDIN>;
print "\n";
print "\t\tSubject = ";
$sub = <STDIN>;
print "\n";
print "\t\tInsert youre words = ";
$words = <STDIN>;
print "\n";
#print "\t\tAttacment(if there) = ";
#$attactment = <STDIN>;
print "\n";


open (MAIL, "|sendmail -t");

#print MAIL "messagefile: $attactment\n";
print MAIL "To: $to <root\@blackid.net>\n";
print MAIL "From: $from <root\@blackid.net>\n";
print MAIL "Subject: $sub\n\n";

print MAIL "$words";
#print MAIL "This is line 2\n";
close (MAIL);

sleep 2;
#system ('pause > nul');
system ('cls');
system ('echo.');
system ('echo.');
system ('echo.');


print "\t\tEmail Succesfully send     : \n\n";
print "\t\tTo       : $to \n";
print "\t\tFrom     : $from \n";
print "\t\tSubject  : $sub \n";
print "\t\tContent  : $words \n";
print "\n";