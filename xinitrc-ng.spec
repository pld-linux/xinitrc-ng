# TODO
# - slim, entrance, wdm support as XDM
Summary:	The default startup scripts for the X Window System
Summary(pl.UTF-8):	Domyślne skrypty startowe X Window System
Name:		xinitrc-ng
Version:	1.1
Release:	2
License:	GPL
Group:		X11
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	f369317256368bf00dd07957929d5a63
Patch0:		lightdm-no-to-nodaemon.patch
URL:		http://svn.pld-linux.org/trac/svn/wiki/packages/xinitrc-ng
Requires:	/bin/sh
Requires:	which
Requires:	xorg-app-setxkbmap
Requires:	xorg-app-twm
Requires:	xorg-app-xmodmap
Requires:	xorg-app-xrdb
Provides:	xinitrc >= 3.0
Obsoletes:	xinitrc < 3.0
Obsoletes:	xscripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xinitrc-ng package contains the scripts which are used to start a
window manager and apropriate configuration files.

%description -l pl.UTF-8
Pakiet xinitrc-ng zawiera skrypty do uruchomienia zarządcy okien oraz
odpowiednie plik konfiguracyjne.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sysconfdir}/X11/xinit/Xclients
%attr(755,root,root) %{_sysconfdir}/X11/xinit/xinitrc
%attr(755,root,root) %{_sysconfdir}/X11/xinit/prefdm
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xmodmap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xresources
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/xinitdefs
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/desktop
