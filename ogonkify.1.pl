.\" 1999 PTM Przemek Borys
.TH OGONKIFY 1 "19 Feb 1997" "McKornik Jr."
.\" Time-stamp: <98/05/16 03:23:32 jec>
.SH NAZWA
ogonkify \- miêdzynarodowe wsparcie PostScriptu
.SH SK£ADNIA
.B ogonkify
.RB [ \-p
.IR zestawprocedur ]
.RB [ \-e
.IR kodowanie ]
.RB [ \-r
.IR Stary=Nowy ]
.RB [ \-a ]
.RB [ \-c ]
.RB [ \-h ]
.RB [ \-t ]
.RB [ \-A ]
.RB [ \-C ]
.RB [ \-H ]
.RB [ \-T ]
.RB [ \-AT ]
.RB [ \-CT ]
.RB [ \-ATH ]
.RB [ \-CTH ]
.RB [ \-N ]
.RB [ \-M ]
.RB [ \-mp ]
.RB [ \-SO ]
.RB [ \-AX ]
.RB [ \-F ]
.RB [ \-\- ]
.I plik ...
.SH OPIS
.B ogonkify
zajmuje siê przekszta³caniem plików PostScriptowych w swi±zku z drukowaniem
w ró¿nych jêzykach. Jego podstawowym zastosowaniem jest filtrowanie wyj¶cia
Netscape, Mosaic i innych programów w taki sposób, by mo¿liwe by³o
drukowanie w jêzykach nieu¿ywaj±cych standardowego zachodnioeuropejskiego
kodowania ISO 8859-1.
.SH OGÓLNE UWAGI
Instrukcja instalacji znajduje siê w pliku INSTALL. Zak³adaj±c, ¿e
zakoñczy³e¶ instalacjê pomy¶lnie, zachowaj przyk³adowy PostScript z 
Netscape lub Mosaic np. do pliku
.BR output.ps .
Nastêpnie spróbuj go wydrukowaæ przy pomocy
.IP
% ogonkify \-AT \-N output.ps | lpr
.TP
w wypadku Netscape, lub
.IP
% ogonkify \-AT \-M output.ps | lpr
.TP
w wypadku Mosaic.
.LP
Mo¿esz zmieniæ opcjê
.B \-AT
na
.BR \-CT .
Spowoduje to u¿ycie wysokiej jako¶ci fontu Courier z IBM (za cenê
wolniejszego drukowania).

Innym sposobem na drukowanie z Netscape jest ustawienie komendy drukuj±cej w
odpowiednim oknie dialogowym na:
.IP
ogonkify \-AT \-N | lpr
.TP
Dla szczegó³ów, zobacz sekcjê U¯YTKOWANIE.
.SH OPCJE
.TP
.B \-p
W³±cza podany zestaw procedur do pliku wyj¶ciowego.
.TP
.B \-e
Ustaw kodowanie wyj¶cia. Domy¶lnie jest to
.B L2
(ISO 8859\-2, a.k.a. ISO Latin\-2). Inne mo¿liwe warto¶ci to
.B L1
(ISO 8859\-1, a.k.a. ISO Latin\-1),
.B L3
(ISO 8859\-3, a.k.a. ISO Latin\-3), 
.B L4
(ISO 8859\-4, a.k.a. ISO Latin\-4),
.B L5
(ISO 8859\-9, a.k.a. ISO Latin\-5),
.B L6
(ISO 8859\-10, a.k.a. ISO Latin\-6),
.B CP1250
(Microsoft Code Page 1250, a.k.a. CeP),
.B ibmpc
(Oryginalne kodowanie IBM-PC),
.B mac
(kodowanie Apple Macintosh) and
.B hp
(kodowanie HP Roman).
.TP
.B \-r
U¿yj fontu
.I Nowy
zamiast
.IR Starego .
Mo¿e to prowadziæ do brzydkich efektów gdy nie bêd± siê zgadzaæ metryki
fontów.
.TP
.B \-a
Dokonaj potrzebnych przemapowañ fontów dla u¿ywania Courier\-Ogonki zamiast
Courier
(litera
.B a
oznacza Adobe Courier).  Zapobiega to ³adowaniu fontów na drukarkê.
.TP
.B \-c
Dokonaj potrzebnych przemapowañ fontów dla u¿ywania IBM Courier zamiast
Adobe Courier.
.TP
.B \-t
Dokonaj potrzebnych przemapowañ fontów dla u¿ywania Times\-Roman\-Ogonki 
zamiast Times\-Roman.
.TP
.B \-h
Dokonaj potrzebnych przemapowañ fontów dla u¿ywania Helvetica\-Ogonki 
zamiast Helvetica.
.TP
.B \-A
Podobne do
.BR \-a ,
lecz dodatkowo ³aduje fonty Courier\-Ogonki.
.TP
.B \-C
Podobne do
.BR \-c ,
lecz dodatkowo ³aduje fonty IBM Courier.
.TP
.B \-H
Podobne do
.BR \-h ,
lecz dodatkowo ³aduje fonty Helvetica\-xxx\-Ogonki.
.TP
.B \-T
Podobne do
.BR \-t ,
lecz dodatkowo ³aduje fonty Times\-xxx\-Ogonki.
.TP
.B \-CT
Równowa¿ne
.B \-C
.BR \-T .
.TP
.B \-N
Dokonaj przetwarzania typu
.BR Netscape .
.TP
.B \-M
Dokonaj przetwarzania typu
.BR Mosaic .
.TP
.B \-mp
Dokonaj przetwarzania
.BR mp .
Nie dzia³a z opcj±
.B -A
(u¿yj zamiast niej
.BR -C ).
.TP
.B \-SO
Dokonaj przetwarzania typu
.BR StarOffice .
.TP
.B \-AX
Dokonaj przetwarzania typu
.B ApplixWare .
.TP
.B \-F
Dokonaj przetwarzania typu
.B XFig
(dzia³a tylko dla polskich znaków).
.TP
.B \-\-
Zakoñcz opcje.
.SH U¯YTKOWANIE
Za³ó¿my, ¿e chcesz wydrukowaæ stronê WWW zakodowan± w ISO Latin\-2. Netscape
nalega na drukowanie w ISO Latin\-1. Korzystaj±c z komendy File->Print
wy¶lij z Netscape wydruk do pliku alamakota.ps.

Poniewa¿ 
.B ogonkify
jest skonfigurowany domy¶lnie na ISO Latin\-2, przekazanie mu PostScriptu
wygenerowanego przez Netscape spowoduje naprawienie kodowania fontów.
Wystarczy wykonaæ
.IP
% ogonkify \-N <alamakota.ps | lpr
.LP
Jednak¿e wiêkszo¶æ drukarek nie ma fontów z wymaganymi znakami. Zamiast
Courier i Times\-Roman mo¿na przy u¿yciu opcji
.BR \-AT ,
u¿yæ i za³adowaæ syntezowane fonty, a przy u¿yciu
.BR \-CT
mo¿na za³adowaæ i u¿yæ bardzo dobrego fontu Courier z IBM.
Komenda bêdzie wiêc zwykle wygl±da³a tak:
.IP
% ogonkify \-N \-AT <alamakota.ps | lpr
.LP
lub mo¿e
.IP
% ogonkify \-N \-CT <alamakota.ps | lpr
.LP
Typowe u¿ycie z innymi programami:
.IP
.nf
% ogonkify \-M \-AT <alamakota.ps | lpr
% ogonkify \-mp \-AT <alamakota.ps | lpr
% ogonkify \-SO \-AT <alamakota.ps | lpr
% ogonkify \-AX \-ATH <alamakota.ps | lpr
% ogonkify \-XF \-ATH <alamakota.ps | lpr
.fi
.LP
.SH B£ÊDY
Znaki z `ogonek' powinny byæ konstruowane inaczej (np. `ogonek' u¿ywany z
`a' powinien byæ inaczej wykszta³cony ni¿ ten, u¿ywany z `e'.)

Lepiej by³oby po³ataæ programy, do których mamy ¼ród³a ni¿ przetwarzaæ
wytworzony PostScript.

Program jest napisany w Perlu.
.SH UWAGI
Aby obejrzeæ wyj¶cie w GhostScripcie, bêdziesz musia³ uruchomiæ
.B gs
z flag±
.BR \-dNOPLATFONTS ,
a
.B ghostview
z flag±
.B \-arguments 
.BR \-dNOPLATFONTS .

Netscape, IBM, Adobe, PostScript, StarOffice, ApplixWare, a tak¿e byæ mo¿e i
inne nazwy s± zastrze¿onymi znakami towarowymi.
.SH PODZIÊKOWANIA
Wiele z danych mieszanych znaków udostêpnili Primoz Peterlin, H. Turgut Uyar, 
Ricardas Cepas, Kristof Petrovay i Jan Prikryl.

Jacek Pliszka doda³ obs³ugê
.BR StarOffice .  
Andrzej Baginski
doda³ obs³ugê
.BR ApplixWare .
Piotr Kuszewski
doda³ obs³ugê
.BR XFig .

Markku Rossi napisa³
.B genscript
i udostêpni³ w dystrybucji wiele przydatnych wektorów kodowañ.

Podczas pisania kodu Postscriptowego, u¿ywa³em interpretera
.B ghostscript
napisanego przez Petera Deutscha.

Larry Wall napisa³
.BR perl ,
sk³adniê i semantykê, które s± niekoñcz±cym siê ¼ród³em zak³opotania.
.SH AUTOR
Juliusz Chroboczek <jec@dcs.ed.ac.uk>, z pomoc± wielu innych ludzi.
