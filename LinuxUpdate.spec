# TODO: source0-md5
Summary:	PLD automatic update notification and upgrade wizard
Summary(pl):	Program powiadamiania o aktualizacjach w PLD
Name:		LinuxUpdate
Version:	0.1
Release:	1
Epoch:		0
License:	GPL
Group:		X11/Applications
Vendor:		Patryk Zawadzki <patrys@pld-linux.org>
Source0:	http://wirusy.room-303.com/%{name}.tar.gz
# Source0-md5:	07bd255f8e34bbeefc3b92b1e895cd07
Requires:	perl-Gtk2
Requires:	perl-Gtk2-TrayIcon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD automatic update notification and upgrade wizard.

%description -l pl
Program powiadamiania o aktualizacjach w PLD.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir}/LinuxUpdate,%{_bindir}}

install *.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/LinuxUpdate
install LinuxUpdate $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/LinuxUpdate
