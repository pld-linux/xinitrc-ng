Summary:	The default startup scripts for the X Window System
Summary(pl):	Domy¶lne skrypty startowe X Window System
Name:		xinitrc-ng
Version:	0.5
Release:	1
License:	GPL
Group:		X11/XFree86
Source0:	ftp://ftp.pld-linux.org/software/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	3bc568039fd70a2d48e4873e3011b077
Requires:	XFree86
Requires:	/bin/sh
Requires:	twm
Requires:	which
Obsoletes:	xscripts
Obsoletes:	xinitrc
Provides:	xinitrc >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xinitrc-ng package contains the scripts which are used to start
a window manager and apropriate configuration files.

%description -l pl
Pakiet xinitrc-ng zawiera skrypty do uruchomienia zarz±dcy okien oraz
odpowiednie plik konfiguracyjne.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{X11/xinit/xinitrc.d,sysconfig}

install Xclients Xmodmap xinitdefs xinitrc $RPM_BUILD_ROOT/etc/X11/xinit/
install desktop $RPM_BUILD_ROOT/etc/sysconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir /etc/X11/xinit/xinitrc.d
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xinit/Xclients
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xinit/xinitrc
%config(noreplace) %verify(not md5 size mtime) /etc/X11/xinit/Xmodmap
%config(noreplace) %verify(not md5 size mtime) /etc/X11/xinit/xinitdefs
%config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/desktop
