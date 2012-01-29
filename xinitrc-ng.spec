Summary:	The default startup scripts for the X Window System
Summary(pl.UTF-8):	Domyślne skrypty startowe X Window System
Name:		xinitrc-ng
Version:	0.9
Release:	3
License:	GPL
Group:		X11
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	6c63c305529d783f9603e662bf451edb
URL:		http://svn.pld-linux.org/trac/svn/wiki/packages/xinitrc-ng
Patch0:		%{name}-Xft.patch
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
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xclients
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/xinitrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xmodmap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/Xresources
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/xinit/xinitdefs
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/desktop
