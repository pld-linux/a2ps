Summary:	Text to Postscript filter.
Summary(pl):	Filtr text/plain do  Postscriptu
Name:		a2ps
Version:	4.13b
Release:	2
License:	GPL
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Source0:	ftp://ftp.enst.fr/pub/unix/a2ps/%{name}-%{version}.tar.gz
Patch0:		a2ps-info.patch
Prereq:		/sbin/ldconfig
URL:		http://www.inf.enst.fr/~demaille/a2ps/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/a2ps

%description
a2ps is a text to PostScript filter with pretty-printing capabilities.
It includes support for a wide number of programming languages,
encodings (ISO Latins, Cyrillic etc.), medias, and spoken languages
(for the interface). It has also the ability to delegate the
processing of some files to other applications, letting you print DVI,
PostScript etc. with the very same interface.

%description -l pl 
A2ps jest programem pozwalajaj±cym na ³adne drukowanie plików
tekstowych w PostScript. Posiada wsparcie dla wielu ró¿nych jêzyków
programowania, zestawów znaków (ISO Latins, Cyrilica etc.), wielko¶ci
papieru, i jêzyków komunikacji z u¿ytkownikiem. Potrafi tak¿e
przekazaæ przetwarzanie plików do innych programów (tak, ¿e mo¿na
wszystko drukowaæ (DVI, PostScript) przy u¿yciu tego samego polecenia.
Zawiera program ,,ogonkify'' poprawiaj±cy b³êdnie zakodowany
PostScript zawieraj±cy polskie znaki.

%package devel
Summary:	Header files and development documentation for a2ps
Summary(pl):	Pliki nag³ówkowe i dokunentacja do a2ps
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for a2ps.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do a2ps.

%package static
Summary:	a2ps static libraries
Summary(pl):	Biblioteki statyczne do a2ps
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
a2ps static libraries.

%description static -l pl
Biblioteki statyczne do a2ps.

%prep
%setup  -q -n %{name}-4.13 
%patch0 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-gnu-gettext \
	--with-medium=A4  \
	--with-encoding=latin1 \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

perl -pe 's/^lispdir = $/lispdir = \$(prefix)\/lib\/emacs\/site-lisp/g' contrib/emacs/Makefile >tmp

mv tmp contrib/emacs/Makefile
%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README THANKS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,THANKS}.gz

%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/a2ps.cfg
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/a2ps-site.cfg

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*
%{_infodir}/a2ps*info*
%{_infodir}/ogonkify*info*

%dir %{_datadir}/a2ps/afm
%{_datadir}/a2ps/afm/*.afm
%{_datadir}/a2ps/afm/*.map
%attr(755,root,root) %{_datadir}/a2ps/afm/*.sh

%{_datadir}/a2ps/encoding
%{_datadir}/a2ps/fonts
%{_datadir}/a2ps/ppd
%{_datadir}/a2ps/ps
%{_datadir}/a2ps/sheets

%dir %{_datadir}/ogonkify
%{_datadir}/ogonkify/*.enc
%{_datadir}/ogonkify/*.ps
%{_datadir}/ogonkify/afm
%{_datadir}/ogonkify/fonts

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
