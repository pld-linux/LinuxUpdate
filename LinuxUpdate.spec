Summary:	PLD automatic update notification and upgrade wizard
Summary(pl):	Program powiadamiania o aktualizacjach w PLD
Name:		LinuxUpdate
Version:	0.5
Release:	1
Epoch:		0
License:	GPL
Group:		X11/Applications
Source0:	http://patrys.qns.pl/linux/LinuxUpdate/%{name}-%{version}.tar.gz
# Source0-md5:	720daf8db7476e367c85bc2609c7cc8d
Source1:	%{name}.desktop
Requires:	perl-Gtk2
Requires:	perl-Gtk2-TrayIcon
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD automatic update notification and upgrade wizard. This program
lets you know when new packages are ready for upgrade and allows you
to update selected components.

%description -l pl
Program powiadamiania o aktualizacjach w PLD i umo¿liwia dokonanie
aktualizacji wybranych pakietów.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_bindir},%{_desktopdir}}

install *.svg $RPM_BUILD_ROOT%{_pixmapsdir}
install LinuxUpdate $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
