Summary:	Text to Postscript filter.
Summary(pl):	Filtr text/plain do  Postscriptu
Name:		a2ps
Version:	4.10.4
Release:	6
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source:		ftp://ftp.enst.fr/pub/unix/a2ps/%{name}-%{version}.tar.bz2
Patch:		a2ps-info.patch
Prereq:		/sbin/ldconfig
URL:		http://www.inf.enst.fr/~demaille/a2ps/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
a2ps is a text to PostScript filter with pretty-printing capabilities.
It includes support for a wide number of programming languages,
encodings (ISO Latins, Cyrillic etc.), medias, and spoken languages
(for the interface).
It has also the ability to delegate the processing of some files to
other applications, letting you print DVI, PostScript etc. with the
very same interface.

%description -l pl 
A2ps jest programem pozwalajaj±cym na ³adne drukowanie plików tekstowych w 
PostScript. Posiada wsparcie dla wielu ró¿nych jêzyków programowania, 
zestawów znaków (ISO Latins, Cyrilica etc.), wielko¶ci papieru, i jêzyków 
komunikacji z u¿ytkownikiem. Potrafi tak¿e przekazaæ przetwarzanie plików 
do innych programów (tak, ¿e mo¿na wszystko drukowaæ (DVI, PostScript) przy 
u¿yciu tego samego polecenia. Zawiera program ,,ogonkify'' poprawiaj±cy 
b³êdnie zakodowany PostScript zawieraj±cy polskie znaki. 

%package	devel
Summary:	Header files and development documentation for a2ps
Summary(pl):	Pliki nag³ówkowe i dokunentacja do a2ps
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for a2ps.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do a2ps.

%package	static
Summary:	a2ps static libraries
Summary(pl):	Biblioteki statyczne do a2ps
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
a2ps static libraries.

%description static -l pl
Biblioteki statyczne do a2ps.

%prep
%setup -q 
%patch -p1

%build
autoheader
autoconf
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
./configure %{_target} \
	--with-included-gettext \
	--prefix=/usr \
	--sysconfdir=/etc \
	--with-medium=A4  \
	--with-encoding=latin1 \
	--enable-shared
make

%install
rm -rf $RPM_BUILD_ROOT

perl -pe 's/^lispdir = $/lispdir = {prefix}\/lib/g' contrib/emacs/Makefile >tmp

mv tmp contrib/emacs/Makefile
make prefix=$RPM_BUILD_ROOT/usr sysconfdir=$RPM_BUILD_ROOT/etc install

#chmod 755	$RPM_BUILD_ROOT/usr/lib/*.so.*
gzip -9nf $RPM_BUILD_ROOT/usr/info/* \
	$RPM_BUILD_ROOT/usr/man/man1/* \
	AUTHORS ChangeLog NEWS README THANKS

%post
/sbin/install-info /usr/info/a2ps.info.gz /etc/info-dir 
/sbin/install-info /usr/info/ogonkify.info.gz /etc/info-dir 
/sbin/ldconfig

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/a2ps.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/info/ogonkify.info.gz /etc/info-dir
fi

%postun 
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,THANKS}.gz

%config(noreplace) %verify(not size mtime md5) /etc/a2ps.cfg

%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/*.so.*
/usr/man/man1/*
/usr/info/a2ps*info*
/usr/info/ogonkify*info*

%lang(ca) /usr/share/locale/ca/LC_MESSAGES/a2ps.mo
%lang(cs) /usr/share/locale/cs/LC_MESSAGES/a2ps.mo
%lang(da) /usr/share/locale/da/LC_MESSAGES/a2ps.mo
%lang(de) /usr/share/locale/de/LC_MESSAGES/a2ps.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/a2ps.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/a2ps.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/a2ps.mo
%lang(ko) /usr/share/locale/ko/LC_MESSAGES/a2ps.mo
%lang(nl) /usr/share/locale/nl/LC_MESSAGES/a2ps.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/a2ps.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/a2ps.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/a2ps.mo
%lang(sl) /usr/share/locale/sl/LC_MESSAGES/a2ps.mo
%lang(sv) /usr/share/locale/sv/LC_MESSAGES/a2ps.mo
%lang(tr) /usr/share/locale/tr/LC_MESSAGES/a2ps.mo

%dir /usr/share/a2ps/afm
/usr/share/a2ps/afm/*.afm
/usr/share/a2ps/afm/*.map
%attr(755,root,root) /usr/share/a2ps/afm/*.sh

%dir /usr/share/a2ps/encoding
/usr/share/a2ps/encoding/*

%dir /usr/share/a2ps/fonts
/usr/share/a2ps/fonts/*

%dir /usr/share/a2ps/ogonkify
/usr/share/a2ps/ogonkify/*.enc
/usr/share/a2ps/ogonkify/*.ps

%dir /usr/share/a2ps/ppd
/usr/share/a2ps/ppd/*.ppd

%dir /usr/share/a2ps/ps
/usr/share/a2ps/ps/*

%dir /usr/share/a2ps/sheets
/usr/share/a2ps/sheets/*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) /usr/lib/lib*.so

/usr/include/*

%files static
%defattr(644,root,root,755)

/usr/lib/lib*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jan 31 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.10.3-5d]
- added missiong fonts.map ...
- autoheader && autoconf before configure,
- other 'extras' in %install section,
- added %dir for /usr/share/a2ps/*,
- added Group(pl),
- minor changes in %files *.

* Mon Dec 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.10.3-5]
- added %post, %postun with {un}registering info pages (added
  a2ps-info.patch),
- added compressed man pages.

* Thu Oct 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.10.3-4]
- simplification in files,
- removed regexp info pages,
- added stripping shared libraries,
- changed default encoding to latin1,
- added devel subpackage.

* Mon Sep 07 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
  [4.10.3-3d]
- based on Akim Demaille <demaille@inf.enst.fr> and 
  Dave Whitinger <dave@whitinger.net> specs, 
- added lang tag,
- added pl spec translation,
- more detailed %files,
- default medium == A4,
- default encoding == latin2,
- build against GNU libc-2.1.

* Mon Aug 07 1998 Soos Peter <sp@osb.hu>
- BuildRoot spec correction %dir /usr/share/a2ps
