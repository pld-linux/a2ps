Summary:	Text to Postscript filter
Summary(ja.UTF-8):	テキスト→PostScript フィルタ
Summary(pl.UTF-8):	Filtr text/plain do Postscriptu
Summary(zh_CN.UTF-8):	纯文本到Postscript转换器
Name:		a2ps
Version:	4.15.7
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	https://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
# Source0-md5:	c0b2187a56f9d60931227dc4678cbaea
# originally from ftp://ftp.enst.fr/pub/unix/a2ps/
Source1:	i18n-fonts-0.1.tar.gz
# Source1-md5:	fee1456d0e6e94af4fc5b5a1bb9687b7
Source2:	ogonkify.1.pl
Patch0:		%{name}-info.patch
Patch2:		%{name}-etc.patch
Patch4:		%{name}-conf.patch
Patch5:		%{name}-glibcpaper.patch
Patch6:		%{name}-autoenc.patch
Patch7:		%{name}-i18n.patch
Patch8:		%{name}-ogonkify-xfig-fix.patch
URL:		http://www.gnu.org/software/a2ps/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1:1.15
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gc-devel >= 7.2
BuildRequires:	gettext-tools >= 0.20.2
BuildRequires:	gperf
BuildRequires:	help2man
BuildRequires:	libpaper-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
Requires:	psutils
Suggests:	ImageMagick
Suggests:	ghostscript
# grog
Suggests:	groff-perl
Suggests:	gzip
Suggests:	html2ps
Suggests:	texlive-dvips
Obsoletes:	a2ps-devel < 4.15
Obsoletes:	a2ps-static < 4.15
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

%package -n emacs-a2ps
Summary:	Emacs support for a2ps
Summary(pl.UTF-8):	Wsparcie do pracy z a2ps w Emacsie
Group:		Applications/Editors
Requires:	%{name} = %{version}-%{release}
Requires:	emacs-common

%description -n emacs-a2ps
Emacs a2ps mode and printing hook.

%description -n emacs-a2ps -l pl.UTF-8
Tryb a2ps oraz obsługa drukowania przez a2ps dla Emacsa.

%prep
%setup -q -a1
%patch -P0 -p1
%patch -P2 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p0

%{__sed} -i -e '1s,/usr/bin/env sh,/bin/sh,' contrib/{card,fixps,lp2,pdiff}.in

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-encoding=latin1 \
	--with-lispdir=%{_datadir}/emacs/site-lisp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/a2ps/{afm,fonts} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install i18n-fonts-0.1/afm/*.afm $RPM_BUILD_ROOT%{_datadir}/a2ps/afm
install i18n-fonts-0.1/fonts/*.pfb $RPM_BUILD_ROOT%{_datadir}/a2ps/fonts
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1

# it doesn't belong here (part of glibc in PLD case)
%{__rm} $RPM_BUILD_ROOT%{_infodir}/regex.info

# a2ps and a2ps-gnulib domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/a2ps.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/a2ps-site.cfg
%attr(755,root,root) %{_bindir}/a2ps
%attr(755,root,root) %{_bindir}/a2ps-lpr-wrapper
%attr(755,root,root) %{_bindir}/card
%attr(755,root,root) %{_bindir}/composeglyphs
%attr(755,root,root) %{_bindir}/fixps
%attr(755,root,root) %{_bindir}/lp2
%attr(755,root,root) %{_bindir}/ogonkify
%attr(755,root,root) %{_bindir}/pdiff
%{_mandir}/man1/a2ps.1*
%{_mandir}/man1/a2ps-lpr-wrapper.1*
%{_mandir}/man1/card.1*
%{_mandir}/man1/fixps.1*
%{_mandir}/man1/lp2.1*
%{_mandir}/man1/ogonkify.1*
%{_mandir}/man1/pdiff.1*
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

%files -n emacs-a2ps
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/a2ps.el
%{_datadir}/emacs/site-lisp/a2ps-print.el
