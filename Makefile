all: ot.ics nt.ics

ot.ics: ot.txt
	bible_schedule.py < ot.txt > ot.ics

nt.ics: nt.txt
	bible_schedule.py < nt.txt > nt.ics

clean:
	rm -f ot.ics nt.ics
