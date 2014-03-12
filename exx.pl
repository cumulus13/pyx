if (@ARGV == 1)
{
  my $ex = $ARGV[0];
  #system ("Explorer", $ex.":\\");*/
  system("Explorer", $ex);
}
if(@ARGV == 0)
{
  system("explorer %CD%");
}
else {
  print "\n\n\n";
  print "\t\tPerl $0 (Directory to Explorer) \n\n";
}