Summary:	geotool converts IP adress to country name using GeoIP
Summary(pl):	geotool zamienia adres IP na nazwe kraju przy uzyciu GeoIP
Name:		geotool
Version:	0.9.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://download.berlios.de/rsstool/%{name}-%{version}-src.tar.gz
# Source0-md5:	abe22863b4ba5061683cd3db660a82d8
URL:		http://rsstool.berlios.de/
BuildRequires:	GeoIP-devel
Requires:	GeoIP
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
geotool inserts countries into the output of numerous command line
network tools, and reverses GeoIP.dat into a list of countries with
their IP ranges (guarding.p2p)

%description -l pl
geotool wstawia nazwy kraj�w w wyj�cie wielu narz�dzi sieciowych
dzia�aj�cych z linii polece� oraz potrafi zamieni� GeoIP.dat w liste
krajow wraz z ich zakresami IP (guarding.p2p)

%prep
%setup -q -n %{name}-%{version}-src

%build
cd src
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D src/geotool $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.html readme.html
%attr(755,root,root) %{_bindir}/*
