.\" 1999 PTM Przemek Borys
.TH OGONKIFY 1 "19 Feb 1997" "McKornik Jr."
.\" Time-stamp: <98/05/16 03:23:32 jec>
.SH NAZWA
ogonkify \- mi�dzynarodowe wsparcie PostScriptu
.SH SK�ADNIA
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
zajmuje si� przekszta�caniem plik�w PostScriptowych w swi�zku z drukowaniem
w r�nych j�zykach. Jego podstawowym zastosowaniem jest filtrowanie wyj�cia
Netscape, Mosaic i innych program�w w taki spos�b, by mo�liwe by�o
drukowanie w j�zykach nieu�ywaj�cych standardowego zachodnioeuropejskiego
kodowania ISO 8859-1.
.SH OG�LNE UWAGI
Instrukcja instalacji znajduje si� w pliku INSTALL. Zak�adaj�c, �e
zako�czy�e� instalacj� pomy�lnie, zachowaj przyk�adowy PostScript z 
Netscape lub Mosaic np. do pliku
.BR output.ps .
Nast�pnie spr�buj go wydrukowa� przy pomocy
.IP
% ogonkify \-AT \-N output.ps | lpr
.TP
w wypadku Netscape, lub
.IP
% ogonkify \-AT \-M output.ps | lpr
.TP
w wypadku Mosaic.
.LP
Mo�esz zmieni� opcj�
.B \-AT
na
.BR \-CT .
Spowoduje to u�ycie wysokiej jako�ci fontu Courier z IBM (za cen�
wolniejszego drukowania).

Innym sposobem na drukowanie z Netscape jest ustawienie komendy drukuj�cej w
odpowiednim oknie dialogowym na:
.IP
ogonkify \-AT \-N | lpr
.TP
Dla szczeg��w, zobacz sekcj� U�YTKOWANIE.
.SH OPCJE
.TP
.B \-p
W��cza podany zestaw procedur do pliku wyj�ciowego.
.TP
.B \-e
Ustaw kodowanie wyj�cia. Domy�lnie jest to
.B L2
(ISO 8859\-2, a.k.a. ISO Latin\-2). Inne mo�liwe warto�ci to
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
U�yj fontu
.I Nowy
zamiast
.IR Starego .
Mo�e to prowadzi� do brzydkich efekt�w gdy nie b�d� si� zgadza� metryki
font�w.
.TP
.B \-a
Dokonaj potrzebnych przemapowa� font�w dla u�ywania Courier\-Ogonki zamiast
Courier
(litera
.B a
oznacza Adobe Courier).  Zapobiega to �adowaniu font�w na drukark�.
.TP
.B \-c
Dokonaj potrzebnych przemapowa� font�w dla u�ywania IBM Courier zamiast
Adobe Courier.
.TP
.B \-t
Dokonaj potrzebnych przemapowa� font�w dla u�ywania Times\-Roman\-Ogonki 
zamiast Times\-Roman.
.TP
.B \-h
Dokonaj potrzebnych przemapowa� font�w dla u�ywania Helvetica\-Ogonki 
zamiast Helvetica.
.TP
.B \-A
Podobne do
.BR \-a ,
lecz dodatkowo �aduje fonty Courier\-Ogonki.
.TP
.B \-C
Podobne do
.BR \-c ,
lecz dodatkowo �aduje fonty IBM Courier.
.TP
.B \-H
Podobne do
.BR \-h ,
lecz dodatkowo �aduje fonty Helvetica\-xxx\-Ogonki.
.TP
.B \-T
Podobne do
.BR \-t ,
lecz dodatkowo �aduje fonty Times\-xxx\-Ogonki.
.TP
.B \-CT
R�wnowa�ne
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
Nie dzia�a z opcj�
.B -A
(u�yj zamiast niej
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
(dzia�a tylko dla polskich znak�w).
.TP
.B \-\-
Zako�cz opcje.
.SH U�YTKOWANIE
Za��my, �e chcesz wydrukowa� stron� WWW zakodowan� w ISO Latin\-2. Netscape
nalega na drukowanie w ISO Latin\-1. Korzystaj�c z komendy File->Print
wy�lij z Netscape wydruk do pliku alamakota.ps.

Poniewa� 
.B ogonkify
jest skonfigurowany domy�lnie na ISO Latin\-2, przekazanie mu PostScriptu
wygenerowanego przez Netscape spowoduje naprawienie kodowania font�w.
Wystarczy wykona�
.IP
% ogonkify \-N <alamakota.ps | lpr
.LP
Jednak�e wi�kszo�� drukarek nie ma font�w z wymaganymi znakami. Zamiast
Courier i Times\-Roman mo�na przy u�yciu opcji
.BR \-AT ,
u�y� i za�adowa� syntezowane fonty, a przy u�yciu
.BR \-CT
mo�na za�adowa� i u�y� bardzo dobrego fontu Courier z IBM.
Komenda b�dzie wi�c zwykle wygl�da�a tak:
.IP
% ogonkify \-N \-AT <alamakota.ps | lpr
.LP
lub mo�e
.IP
% ogonkify \-N \-CT <alamakota.ps | lpr
.LP
Typowe u�ycie z innymi programami:
.IP
.nf
% ogonkify \-M \-AT <alamakota.ps | lpr
% ogonkify \-mp \-AT <alamakota.ps | lpr
% ogonkify \-SO \-AT <alamakota.ps | lpr
% ogonkify \-AX \-ATH <alamakota.ps | lpr
% ogonkify \-XF \-ATH <alamakota.ps | lpr
.fi
.LP
.SH B��DY
Znaki z `ogonek' powinny by� konstruowane inaczej (np. `ogonek' u�ywany z
`a' powinien by� inaczej wykszta�cony ni� ten, u�ywany z `e'.)

Lepiej by�oby po�ata� programy, do kt�rych mamy �r�d�a ni� przetwarza�
wytworzony PostScript.

Program jest napisany w Perlu.
.SH UWAGI
Aby obejrze� wyj�cie w GhostScripcie, b�dziesz musia� uruchomi�
.B gs
z flag�
.BR \-dNOPLATFONTS ,
a
.B ghostview
z flag�
.B \-arguments 
.BR \-dNOPLATFONTS .

Netscape, IBM, Adobe, PostScript, StarOffice, ApplixWare, a tak�e by� mo�e i
inne nazwy s� zastrze�onymi znakami towarowymi.
.SH PODZI�KOWANIA
Wiele z danych mieszanych znak�w udost�pnili Primoz Peterlin, H. Turgut Uyar, 
Ricardas Cepas, Kristof Petrovay i Jan Prikryl.

Jacek Pliszka doda� obs�ug�
.BR StarOffice .  
Andrzej Baginski
doda� obs�ug�
.BR ApplixWare .
Piotr Kuszewski
doda� obs�ug�
.BR XFig .

Markku Rossi napisa�
.B genscript
i udost�pni� w dystrybucji wiele przydatnych wektor�w kodowa�.

Podczas pisania kodu Postscriptowego, u�ywa�em interpretera
.B ghostscript
napisanego przez Petera Deutscha.

Larry Wall napisa�
.BR perl ,
sk�adni� i semantyk�, kt�re s� nieko�cz�cym si� �r�d�em zak�opotania.
.SH AUTOR
Juliusz Chroboczek <jec@dcs.ed.ac.uk>, z pomoc� wielu innych ludzi.
