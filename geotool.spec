Summary:	geotool - convert IP adress to country name using GeoIP
Summary(pl.UTF-8):	geotool - zamiana adresu IP na nazwę kraju przy użyciu GeoIP
Name:		geotool
Version:	0.9.1
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://download.berlios.de/rsstool/%{name}-%{version}-src.tar.gz
# Source0-md5:	abe22863b4ba5061683cd3db660a82d8
Patch0:		%{name}-lib64.patch
Patch1:		%{name}-dbpath.patch
Patch2:		%{name}-optflags.patch
URL:		http://rsstool.y7.ath.cx/
BuildRequires:	GeoIP-devel
Requires:	GeoIP
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
geotool inserts countries into the output of numerous command line
network tools, and reverses GeoIP.dat into a list of countries with
their IP ranges (guarding.p2p).

%description -l pl.UTF-8
geotool wstawia nazwy krajów w wyjście wielu narzędzi sieciowych
działających z linii poleceń oraz potrafi zamienić GeoIP.dat na listę
krajów wraz z ich zakresami IP (guarding.p2p).

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd src
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D src/geotool $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.html readme.html
%attr(755,root,root) %{_bindir}/*
