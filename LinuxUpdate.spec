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
Requires:	perl-Gtk2
Requires:	perl-Gtk2-Trayicon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT{,/usr/share/pixmaps/LinuxUpdate,%{_bindir}}
cp *.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/LinuxUpdate
cp LinuxUpdate $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%dir /usr/share/pixmaps/LinuxUpdate
%attr(644,root,root) /usr/share/pixmaps/LinuxUpdate/*.xpm
%attr(755,root,root) %{_bindir}/*
