#!/usr/bin/env perl

use POSIX qw(strftime);
use Time::Local;
use strict;
use warnings;

# Choose 2001 as the first repeating year, as it is not a leap-year.
# $time = timegm( $sec, $min, $hour, $mday, $mon, $year );
my $date = timegm(0, 0, 0, 1, 0, 2001);

print "BEGIN:VCALENDAR\r\n";
print "VERSION:2.0\r\n";
print "PRODID:-//eng.churchinhongkong.org//NONSGML bible_reading.pl v1.0//EN\r\n";

while (my $l = <>) {
	chomp $l;

	my $ymd = POSIX::strftime "%Y%m%d", gmtime($date);
	print "BEGIN:VEVENT\r\n";
	printf "UID:%sT130000Z\@eng.churchinhongkong.org\r\n", $ymd;
	print "DTSTAMP:20170322T235959Z\r\n";
	printf "DTSTART;VALUE=DATE:%s\r\n", $ymd;
	printf "SUMMARY:%s\r\n", $l;
	print "TRANSP:TRANSPARENT\r\n";
	print "RRULE:FREQ=YEARLY\r\n";
	print "END:VEVENT\r\n";

	$date += 60 * 60 * 24;
}

print "END:VCALENDAR\r\n";
