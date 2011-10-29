Summary:	A dictionary installer for OpenOffice.org
Summary (ru_RU.UTF-8):	Программа для установки дополнительных словарей OpenOffice.org
Name:		ooodi
Version:	0.68
Release:	1
License:	GPL
Group:		X11/Applications
URL:		http://ooodi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/ooodi/OOodi2-%{version}.tar.gz
# Source0-md5:	47adb912d678a107370c5d1814d6e5fa
BuildRequires:	atk-devel
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	fontconfig
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	openssl-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	unzip
Obsoletes:	openoffice-dictinstall

%description
The Dictionary Installer attempts to download additional spelling and
hyphenation dictionaries from <http://dict.progbits.com> and installs
them.

%description -l ru_RU.UTF-8
Программа для установки словарей OpenOffice.org может скачивать и
подключать дополнительные словари проверки правописания и расстановки
переносов с сервера <http://dict.progbits.com>.

%prep
%setup -q -n OOodi2-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# one executable is enough
%{__rm} $RPM_BUILD_ROOT%{_bindir}/OOodi

%find_lang OOodi2

%clean
rm -rf $RPM_BUILD_ROOT

%files -f OOodi2.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ooodi
%{_datadir}/OOodi2
