Summary:	Lightweight Directory Access Protocol clients/servers
Summary(pl):	Klienci Lightweight Directory Access Protocol
Name:		openldap
Version:	1.2.10
Release:	2
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Copyright:	Artistic
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
Source1:	ldap.init
Source2:	openldap.sysconfig
Source3:	http://www.padl.com/download/MigrationTools.tgz
Source4:	MigrationTools.txt
Source5:	ldap.conf
Source6:	slapd.at-rfc2307.conf
Source7:	slapd.oc-rfc2307.conf
Source8:	ldapsetupdb
Patch0:		openldap-man.patch
Patch1:		openldap-make_man_link.patch
Patch2:		openldap-migrate_passwd.patch
Patch3:		openldap-config.patch
Patch4:		openldap-conffile.patch
Patch5:		openldap-secretfile.patch
URL:		http://www.openldap.org/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libwrap-devel
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc
%define		_libexecdir	%{_sbindir}
%define		_localstatedir	/var

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
Serwery i klienci LDAP jak i interfejsy do innych protoko³ów. Wiedz,
¿e pakiet ten nie zawiera interfejsu slapd to X.500 i dlatego nie
wymaga pakietu ISODE.

Pakiet ten zawiera:
- serwer LDAP (slapd)
- serwer replikacji bazy LDAP (slurpd),
- biblioteki implementuj±ce obs³ugê protoko³u LDAP,
- dodatkowe narzedzia i przyk³adowe aplikacje klienckie LDAP.

%package devel
Summary:	LDAP development files
Summary(pl):	Pliki dla developerów LDAP
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
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
Group(fr):	Development/Librairies
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
Requires:	rc-scripts

%description servers
The servers (daemons) that come with LDAP.

%description -l pl servers
Serwery (daemons) które przychodz± z LDAPem.

%prep
%setup  -q -a 3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 
%patch4 -p1
%patch5 -p1
perl -pi -e 's/AC_PREREQ.*//' configure.in 

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

%{__make} depend
make

%Install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{sysconfig,rc.d/init.d},var/lib/openldap,%{_datadir}/openldap/migration}

%{__make} install TMPROOT=$RPM_BUILD_ROOT

# hack the default config files
perl -pi -e "s|%{buildroot}||g" $RPM_BUILD_ROOT%{_sysconfdir}/openldap//slapd.conf

perl -pi -e "s|^#! /bin/sh|#!/bin/sh|g" $RPM_BUILD_ROOT%{_sbindir}/xrpcomp 

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ldap

install $RPM_SOURCE_DIR/ldap.conf $RPM_BUILD_ROOT%{_sysconfdir}/ldap.conf

echo "localhost" > $RPM_BUILD_ROOT%{_sysconfdir}/openldap//ldapserver
touch $RPM_BUILD_ROOT%{_sysconfdir}/openldap/secret

# move oc.conf and at.conf files to proper place
install %{SOURCE6} %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/openldap
mv $RPM_BUILD_ROOT%{_sysconfdir}/openldap/{slapd.at.conf,slapd.oc.conf} \
		$RPM_BUILD_ROOT%{_datadir}/openldap

# create slapd.access.conf
echo "# This is a good plase to put slapd access-control directives" \
         > $RPM_BUILD_ROOT%{_sysconfdir}/openldap/slapd.access.conf

# deal with the migration tools
install MigrationTools-*/migrate_* \
	$RPM_BUILD_ROOT%{_datadir}/openldap/migration
cp MigrationTools-*/README README.migration

# deal with ldapsetupdb
install %{SOURCE8} $RPM_BUILD_ROOT%{_sbindir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	ANNOUNCEMENT CHANGES COPYRIGHT INSTALL README \
	README.migration MigrationTools.txt doc/rfc/rfc*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post servers
chkconfig --add ldap
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
else
	echo "Run \"ldapsetupdb\" to configure and start sldap server."
fi
			
%preun servers
if [ "$1" = "0" ] ; then
	if [ -f /var/lock/subsys/ldap ]; then
		/etc/rc.d/init.d/ldap stop >&2
	fi
	chkconfig --del ldap
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCEMENT,CHANGES,COPYRIGHT,INSTALL,README,README.migration}.gz
%doc MigrationTools.txt.gz doc/rfc/rfc*
%dir %{_sysconfdir}/openldap/
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapfilter.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapserver
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldaptemplates.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapsearchprefs.conf
%attr(700,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/secret
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ldap.conf
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
%attr(640,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/openldap/slapd.access.conf
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/ldap
%attr(754,root,root) /etc/rc.d/init.d/ldap
%attr(700,root,root) %{_localstatedir}/lib/openldap
%{_datadir}/openldap/*.help
%{_datadir}/openldap/ldapfriendly
%{_datadir}/openldap/*.conf
%attr(755,root,root) %{_sbindir}/centipede
%attr(755,root,root) %{_sbindir}/fax500
%attr(755,root,root) %{_sbindir}/go500
%attr(755,root,root) %{_sbindir}/go500gw
%attr(755,root,root) %{_sbindir}/in.xfingerd
%attr(755,root,root) %{_sbindir}/ldapsetupdb
%attr(755,root,root) %{_sbindir}/ldbmcat
%attr(755,root,root) %{_sbindir}/ldbmtest
%attr(755,root,root) %{_sbindir}/ldif
%attr(755,root,root) %{_sbindir}/ldif2id2children
%attr(755,root,root) %{_sbindir}/ldif2id2entry
%attr(755,root,root) %{_sbindir}/ldif2index
%attr(755,root,root) %{_sbindir}/ldif2ldbm
%attr(755,root,root) %{_sbindir}/mail500
%attr(755,root,root) %{_sbindir}/rcpt500
%attr(755,root,root) %{_sbindir}/rp500
%attr(755,root,root) %{_sbindir}/slapd
%attr(755,root,root) %{_sbindir}/slurpd

%{_mandir}/man5/ldif.5*
%{_mandir}/man5/slapd.conf.5*
%{_mandir}/man5/slapd.replog.5*
%{_mandir}/man8/*
