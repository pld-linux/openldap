Summary:	Lightweight Directory Access Protocol clients/servers
Summary(pl):	Klienci Lightweight Directory Access Protocol
Name:		openldap
Version:	1.2.6
Release:	2
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Copyright:	Artistic
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
Source1:	ldap.init
Source2:	openldap.sysconfig
Source3:	http://www.padl.com/download/MigrationTools.tgz
Source4:	MigrationTools.txt
Patch0:		openldap-man.patch
Patch1:		openldap-make_man_link.patch
Patch2:		openldap-migrate_passwd.patch
Patch3:		openldap-config.patch
URL:		http://www.openldap.org/
BuildRequires:	ncurses-devel
BuildRequires:	libwrap-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_sysconfdir	/etc
%define		_libexecdir	%{_sbindir}
%define		_localstatedir	/var/run

%description
LDAP servers and clients, as well as interfaces to other protocols.
Note that this does not include the slapd interface to X.500 and
therefore does not require the ISODE package.

The package includes:
- stand-alone LDAP server (slapd),
- stand-alone LDAP replication server (slurpd),
- libraries implementing the LDAP protocol,
- utilities, tools, and sample clients.

%description -l pl
Serwery i klienci LDAP jak i interfejsy do innych protoko³ów.
Wiedz, ¿e pakiet ten nie zawiera interfejsu slapd to X.500 i dlatego
nie wymaga pakietu ISODE.

Pakiet ten zawiera:
- serwer LDAP (slapd)
- serwer replikacji bazy LDAP (slurpd),
- biblioteki implementuj±ce obs³ugê protoko³u LDAP,
- dodatkowe narzedzia i przyk³adowe aplikacje klienckie LDAP.

%package devel
Summary:	LDAP development files
Summary(pl):	Pliki dla developerów LDAP
Group:		Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and libraries for developing applications that use LDAP.

%description -l pl devel
Pliki nag³ówkowe i biblioteki konieczne do rozwoju aplikacji
u¿ywaj±cych LDAP.

%package static
Summary:	LDAP static libraries
Summary(pl):	Biblioteki statyczne LDAP
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
LDAP static libraries.

%description -l pl static
Biblioteki statyczne LDAP.

%package servers
Summary:	LDAP servers
Summary(pl):	Serwery LDAP
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		chkconfig

%description servers
The servers (daemons) that come with LDAP.

%description -l pl servers
Serwery (daemons) które przychodz± z LDAPem.

%prep
%setup  -q -n ldap -a 3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

install %{SOURCE4} .

%build
autoconf
LDFLAGS="-s"
CPPFLAGS="-I%{_includedir}/ncurses"
export CPPFLAGS LDFLAGS
%configure \
	--enable-cldap \
	--enable-passwd \
	--enable-shell \
	--enable-phonetic \
	--with-wrappers \
	--with-threads \
	--enable-shared

make depend
make

%Install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{sysconfig,rc.d/init.d},var/ldap,%{_datadir}/openldap/migration}

make install TMPROOT=$RPM_BUILD_ROOT

# hack the default config files
perl -pi -e "s|%{buildroot}||g" $RPM_BUILD_ROOT%{_sysconfdir}/openldap//slapd.conf

(
cd $RPM_BUILD_ROOT%{_sbindir}/
sed -e "s|^#! /bin/sh|#!/bin/sh|g" < xrpcomp >xrpcomp.work
mv xrpcomp.work xrpcomp
)

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ldap

echo "localhost" > $RPM_BUILD_ROOT%{_sysconfdir}/openldap//ldapserver

# deal with the migration tools
install MigrationTools-*/migrate_* \
	$RPM_BUILD_ROOT%{_datadir}/openldap/migration
cp MigrationTools-*/README README.migration

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	ANNOUNCEMENT CHANGES COPYRIGHT INSTALL README \
	README.migration MigrationTools.txt doc/rfc/rfc*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post servers
chkconfig --add ldap
if test -r /var/lock/subsys/ldap; then
	/etc/rc.d/init.d/ldap restart >&2
else
	echo "Run \"/etc/rc.d/init.d/ldap start\" to start sldap server."
fi
			
%postun servers
if [ "$1" = "0" ] ; then
	chkconfig --del ldap
	/etc/rc.d/init.d/ldap stop
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCEMENT,CHANGES,COPYRIGHT,INSTALL,README,README.migration}.gz
%doc MigrationTools.txt.gz doc/rfc/rfc*
%dir %{_sysconfdir}/openldap/
%config %{_sysconfdir}/openldap/ldapfilter.conf
%config %{_sysconfdir}/openldap/ldapserver
%config %{_sysconfdir}/openldap/ldaptemplates.conf
%config %{_sysconfdir}/openldap/ldapsearchprefs.conf
%config %{_sysconfdir}/openldap/ldap.conf
%attr(755,root,root) %{_sbindir}/xrpcomp
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/openldap
%dir %{_datadir}/openldap/migration
%attr(755,root,root) %{_datadir}/openldap/migration/*.pl
%attr(755,root,root) %{_datadir}/openldap/migration/*.sh
%{_datadir}/openldap/migration/*.ph

%{_mandir}/man1/*
%{_mandir}/man5/ldap.conf.5*
%{_mandir}/man5/ldapfilter.conf.5*
%{_mandir}/man5/ldapfriendly.5*
%{_mandir}/man5/ldapsearchprefs.conf.5*
%{_mandir}/man5/ldaptemplates.conf.5*
%{_mandir}/man5/ud.conf.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files servers
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/openldap/slapd.conf
%config %verify(not size mtime md5) %{_sysconfdir}/openldap/slapd.oc.conf
%config %verify(not size mtime md5) %{_sysconfdir}/openldap/slapd.at.conf
%config %verify(not size mtime md5) /etc/sysconfig/ldap
%attr(754,root,root) /etc/rc.d/init.d/ldap
%attr(700,root,root) /var/ldap
%{_datadir}/openldap/*.help
%{_datadir}/openldap/ldapfriendly
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man5/ldif.5*
%{_mandir}/man5/slapd.conf.5*
%{_mandir}/man5/slapd.replog.5*
%{_mandir}/man8/*
