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
./configure %{_target_platform} \
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

#chmod 755	$RPM_BUILD_ROOT%{_libdir}/*.so.*
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README THANKS

%find_lang %{name}

%post
/sbin/install-info %{_infodir}/a2ps.info.gz /etc/info-dir 
/sbin/install-info %{_infodir}/ogonkify.info.gz /etc/info-dir 
/sbin/ldconfig

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete %{_infodir}/a2ps.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/ogonkify.info.gz /etc/info-dir
fi

%postun 
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,THANKS}.gz

%config(noreplace) %verify(not size mtime md5) /etc/a2ps.cfg

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%{_mandir}/man1/*
%{_infodir}/a2ps*info*
%{_infodir}/ogonkify*info*

%dir %{_datadir}/a2ps/afm
%{_datadir}/a2ps/afm/*.afm
%{_datadir}/a2ps/afm/*.map
%attr(755,root,root) %{_datadir}/a2ps/afm/*.sh

%dir %{_datadir}/a2ps/encoding
%{_datadir}/a2ps/encoding/*

%dir %{_datadir}/a2ps/fonts
%{_datadir}/a2ps/fonts/*

%dir %{_datadir}/a2ps/ogonkify
%{_datadir}/a2ps/ogonkify/*.enc
%{_datadir}/a2ps/ogonkify/*.ps

%dir %{_datadir}/a2ps/ppd
%{_datadir}/a2ps/ppd/*.ppd

%dir %{_datadir}/a2ps/ps
%{_datadir}/a2ps/ps/*

%dir %{_datadir}/a2ps/sheets
%{_datadir}/a2ps/sheets/*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_libdir}/lib*.so

%{_includedir}/*

%files static
%defattr(644,root,root,755)

%{_libdir}/lib*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jan 31 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.10.3-5d]
- added missiong fonts.map ...
- autoheader && autoconf before configure,
- other 'extras' in %install section,
- added %dir for %{_datadir}/a2ps/*,
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
- BuildRoot spec correction %dir %{_datadir}/a2ps
