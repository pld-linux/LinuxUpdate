Summary:	PLD automatic update notification and upgrade wizard
Summary(pl):	Program powiadamiania o aktualizacjach w PLD
Name:		LinuxUpdate
Version:	0.3.1
Release:	2
Epoch:		0
License:	GPL
Group:		X11/Applications
Vendor:		Patryk Zawadzki <patrys@pld-linux.org>
Source0:	http://patrys.qns.pl/linux/LinuxUpdate/%{name}-%{version}.tar.gz
# Source0-md5:	2436c7c01462076e7b5c85caaf29d3c0
Source1:	%{name}.desktop
Requires:	perl-Gtk2
Requires:	perl-Gtk2-TrayIcon
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD automatic update notification and upgrade wizard.

%description -l pl
Program powiadamiania o aktualizacjach w PLD.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir}/LinuxUpdate,%{_bindir},%{_desktopdir}}

install *.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/LinuxUpdate
install LinuxUpdate $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_desktopdir}/*
%{_pixmapsdir}/LinuxUpdate
