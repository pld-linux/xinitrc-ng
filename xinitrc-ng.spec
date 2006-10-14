Summary:	The default startup scripts for the X Window System
Summary(pl):	Domy¶lne skrypty startowe X Window System
Name:		xinitrc-ng
Version:	0.8
Release:	6
License:	GPL
Group:		X11
Source0:	ftp://ftp.pld-linux.org/software/xinitrc-ng/%{name}-%{version}.tar.bz2
# Source0-md5:	30760456eb96b5dea9fadcb7075e90f3
Requires:	/bin/sh
Requires:	which
Requires:	xorg-app-twm
Provides:	xinitrc >= 3.0
Obsoletes:	xinitrc
Obsoletes:	xscripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xinitrc-ng package contains the scripts which are used to start a
window manager and apropriate configuration files.

%description -l pl
Pakiet xinitrc-ng zawiera skrypty do uruchomienia zarz±dcy okien oraz
odpowiednie plik konfiguracyjne.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{X11/xinit/xinitrc.d,sysconfig,wmstyle}
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

install Xclients Xmodmap xinitdefs xinitrc $RPM_BUILD_ROOT/etc/X11/xinit
install desktop $RPM_BUILD_ROOT/etc/sysconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xclients
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/xinitrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xmodmap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/xinitdefs
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/desktop
