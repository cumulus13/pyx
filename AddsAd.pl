print "Angka Batas Awal= ";
$a = <STDIN>;
chomp($a);

print "\n\n";

print "Angka Batas Akhir = ";
$b = <STDIN>;
chomp($b);

print "\n\n";

#print "Kalimat / Kata / Nama Host / Contoh (127.0.0.1		u1.eset.com) = ";
#$c = <STDIN>;
#chomp($c);

while ($a <= $b) {
        print "127.0.0.1","\t\tu".$a."eset.com \n";
        $a++;
}