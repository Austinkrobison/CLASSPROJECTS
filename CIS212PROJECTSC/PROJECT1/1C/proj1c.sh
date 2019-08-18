FIRST_90=$(fgrep -n 91 passwd_212)
F_LINE_DIG=$(echo $FIRST_90 | cut -b 1,2)
head -n$((F_LINE_DIG-1)) passwd_212 > passwd_212_no90s
LAST_90=$(fgrep -n 99 passwd_212)
L_LINE_DIG=$(echo $LAST_90 | cut -b 1,2)
MAX_LINES=$(wc -l passwd_212 | cut -b 1,2)
tail -n$((MAX_LINES - L_LINE_DIG)) passwd_212 >> passwd_212_no90s


grep bin passwd_212_no90s | cut -d ':' -f7| sort| uniq -c

