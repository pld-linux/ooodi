Summary:	A dictionary installer for OpenOffice.org
Summary (ru_RU.UTF-8):	Программа для установки дополнительных словарей OpenOffice.org
Name:		ooodi
Version:	0.65
Release:	0.1
License:	GPL
Group:		Office
URL:		http://ooodi.sourceforge.net/
Source0:	OOodi2-%{version}.tar.gz
Source1:	ru.po
Patch0:		configure.patch
BuildRequires:	XFree86-libs
BuildRequires:	curl-devel
BuildRequires:	fontconfig
BuildRequires:	freetype2
BuildRequires:	glib2-devel
BuildRequires:	libatk-devel
BuildRequires:	libexpat
BuildRequires:	libgtk+2-devel
BuildRequires:	libpango-devel
BuildRequires:	libpopt-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	rootfiles
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
%setup -q -n OOodi2-%version
cp %{SOURCE1} po
%patch0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang OOodi2

%files -f OOodi2.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/OOodi
%{_datadir}/OOodi2
