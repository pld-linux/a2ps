Summary:	Text to Postscript filter
Summary(ja.UTF-8):	テキスト→PostScript フィルタ
Summary(pl.UTF-8):	Filtr text/plain do Postscriptu
Summary(zh_CN.UTF-8):	纯文本到Postscript转换器
Name:		a2ps
Version:	4.14
Release:	3
License:	GPL v3+
Group:		Applications/Text
Source0:	https://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
# Source0-md5:	781ac3d9b213fa3e1ed0d79f986dc8c7
Source1:	ftp://ftp.enst.fr/pub/unix/a2ps/i18n-fonts-0.1.tar.gz
# Source1-md5:	fee1456d0e6e94af4fc5b5a1bb9687b7
Source2:	ogonkify.1.pl
Patch0:		%{name}-info.patch
Patch1:		%{name}-security.patch
Patch2:		%{name}-etc.patch
Patch3:		%{name}-flex.patch
Patch4:		%{name}-conf.patch
Patch5:		%{name}-glibcpaper.patch
Patch6:		%{name}-autoenc.patch
Patch7:		%{name}-i18n.patch
Patch8:		%{name}-ogonkify-xfig-fix.patch
Patch9:		%{name}-pl.po-update.patch
Patch10:	%{name}-locale-names.patch
Patch11:	%{name}-atan2.patch
Patch12:	format-security.patch
Patch13:	%{name}-texinfo.patch
URL:		http://www.gnu.org/software/a2ps/
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	gperf
BuildRequires:	libpaper-devel
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
Requires:	psutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/a2ps

%description
a2ps is a text to PostScript filter with pretty-printing capabilities.
It includes support for a wide number of programming languages,
encodings (ISO Latins, Cyrillic etc.), medias, and spoken languages
(for the interface). It has also the ability to delegate the
processing of some files to other applications, letting you print DVI,
PostScript etc. with the very same interface.

%description -l pl.UTF-8
A2ps jest programem pozwalającym na ładne drukowanie plików tekstowych
w PostScript. Posiada wsparcie dla wielu różnych języków
programowania, zestawów znaków (ISO Latins, Cyrilica etc.), wielkości
papieru, i języków komunikacji z użytkownikiem. Potrafi także
przekazać przetwarzanie plików do innych programów (tak, że można
wszystko drukować (DVI, PostScript) przy użyciu tego samego polecenia.
Zawiera program ,,ogonkify'' poprawiający błędnie zakodowany
PostScript zawierający polskie znaki.

%package devel
Summary:	Header files for a2ps library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki a2ps
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for a2ps library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki a2ps.

%package static
Summary:	a2ps static library
Summary(pl.UTF-8):	Biblioteka statyczna a2ps
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
a2ps static library.

%description static -l pl.UTF-8
Biblioteka statyczna a2ps.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%{__mv} po/{no,nb}.po

%build
cp -f /usr/share/automake/config.* auxdir
%configure \
	--with-gnu-gettext \
	--with-medium=_glibc  \
	--with-encoding=latin1 \
	--enable-shared \
	--enable-kanji
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/a2ps/{afm,fonts} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__perl} -pi -e 's/^lispdir = $/lispdir = \$(prefix)\/lib\/emacs\/site-lisp/g' contrib/emacs/Makefile

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install i18n-fonts-0.1/afm/*.afm $RPM_BUILD_ROOT%{_datadir}/a2ps/afm
install i18n-fonts-0.1/fonts/*.pfb $RPM_BUILD_ROOT%{_datadir}/a2ps/fonts
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1

# it doesn't belong here (part of glibc in PLD case)
%{__rm} $RPM_BUILD_ROOT%{_infodir}/regex.info

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
%doc AUTHORS ChangeLog NEWS README THANKS
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/a2ps.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/a2ps-site.cfg
%attr(755,root,root) %{_bindir}/a2ps
%attr(755,root,root) %{_bindir}/card
%attr(755,root,root) %{_bindir}/composeglyphs
%attr(755,root,root) %{_bindir}/fixnt
%attr(755,root,root) %{_bindir}/fixps
%attr(755,root,root) %{_bindir}/ogonkify
%attr(755,root,root) %{_bindir}/pdiff
%attr(755,root,root) %{_bindir}/psmandup
%attr(755,root,root) %{_bindir}/psset
%attr(755,root,root) %{_bindir}/texi2dvi4a2ps
%attr(755,root,root) %{_libdir}/liba2ps.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liba2ps.so.1
%{_mandir}/man1/a2ps.1*
%{_mandir}/man1/card.1*
%{_mandir}/man1/fixps.1*
%{_mandir}/man1/ogonkify.1*
%{_mandir}/man1/pdiff.1*
%{_mandir}/man1/psmandup.1*
%{_mandir}/man1/psset.1*
%{_mandir}/man1/texi2dvi4a2ps.1*
%lang(pl) %{_mandir}/pl/man1/ogonkify.1*
%{_infodir}/a2ps.info*
%{_infodir}/ogonkify.info*

%dir %{_datadir}/a2ps
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
%attr(755,root,root) %{_libdir}/liba2ps.so
%{_libdir}/liba2ps.la
%{_includedir}/liba2ps.h

%files static
%defattr(644,root,root,755)
%{_libdir}/liba2ps.a
