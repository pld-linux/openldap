Summary:	Lightweight Directory Access Protocol clients/servers
Summary(pl):	Klienci Lightweight Directory Access Protocol
Name:		openldap
Version:	2.0.1
Release:	1
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Copyright:	Artistic
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
Source1:	ldap.init
Source2:	%{name}.sysconfig
Source3:	http://www.openldap.org/doc/admin/guide.html
Source5:	ldap.conf
Patch0:		%{name}-make_man_link.patch
Patch1:		%{name}-conffile.patch
Patch2:		%{name}-config.patch
URL:		http://www.openldap.org/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libwrap-devel
BuildRequires:	perl
BuildRequires:	openssl-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	unixODBC-devel
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
Group(de):	Entwicklung/Libraries
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
Group(de):	Entwicklung/Libraries
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
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Prereq:		chkconfig
Requires:	rc-scripts

%description servers
The servers (daemons) that come with LDAP.

%description -l pl servers
Serwery (daemons) które przychodz± z LDAPem.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
install %{SOURCE3} .
perl -pi -e 's/AC_PREREQ.*//' configure.in 

%build
autoconf
CPPFLAGS="-I%{_includedir}/ncurses"
%configure \
	--enable-syslog \
	--enable-proctitle \
	--enable-cache \
	--enable-referrals \
	--enable-ipv6 \
	--enable-local \
	--with-cyrus-sasl \
	--with-readline \
	--with-threads \
	--with-tls \
	--with-yielding-select \
	--enable-slapd \
	--enable-crypt \
	--enable-spasswd \
	--enable-multimaster \
	--enable-phonetic \
	--enable-modules \
	--enable-rlookups \
	--enable-aci \
	--enable-wrappers \
	--enable-dynamic \
	--enable-dnssrv \
	--with-dnssrv-module=static \
	--enable-ldap \
	--with-ldap-module=static \
	--enable-ldbm \
	--with-ldbm-module=static \
	--enable-passwd \
	--with-passwd-module=dynamic \
	--enable-shell \
	--with-shell-module=static \
	--enable-sql \
	--with-sql-module=static \
	--enable-slurpd \
	--enable-shared \
	--enable-static

%{__make} depend
%{__make}

%Install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{sysconfig,rc.d/init.d},var/lib/openldap-ldbm,%{_datadir}/openldap/schema}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libexecdir}/openldap $RPM_BUILD_ROOT%{_libdir}

# hack the default config files
perl -pi -e "s|%{buildroot}||g" $RPM_BUILD_ROOT%{_sysconfdir}/openldap//slapd.conf

perl -pi -e "s|^#! /bin/sh|#!/bin/sh|g" $RPM_BUILD_ROOT%{_sbindir}/xrpcomp 

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ldap

install $RPM_SOURCE_DIR/ldap.conf $RPM_BUILD_ROOT%{_sysconfdir}/ldap.conf

echo "localhost" > $RPM_BUILD_ROOT%{_sysconfdir}/openldap/ldapserver

# Standard schemas should not be changed by users
mv $RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/* $RPM_BUILD_ROOT%{_datadir}/openldap/schema/

# create slapd.access.conf
echo "# This is a good plase to put slapd access-control directives" > \
	$RPM_BUILD_ROOT%{_sysconfdir}/openldap/slapd.access.conf

# create local.schema
echo "# This is a good plase to put your schema definitions " > \
	$RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/local.schema

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	ANNOUNCEMENT CHANGES COPYRIGHT README \
	doc/rfc/* doc/drafts/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%pre servers
grep -q slapd %{_sysconfdir}/group || (
	/usr/sbin/groupadd -g 93 -r -f slapd 1>&2 || :
)
grep -q slapd %{_sysconfdir}/passwd || (
	/usr/sbin/useradd -M -o -r -u 93 \
        -g slapd -c "OpenLDAP server" -d /var/lib/openldap-ldbm slapd 1>&2 || :
)

%post servers
chkconfig --add ldap
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
else
	echo "Run '/etc/rc.d/init.d/ipsec start' to start IPSEC services." >&2
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
%doc *.gz
%doc doc/rfc doc/drafts
%dir %{_sysconfdir}/openldap/
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapfilter.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapsearchprefs.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldaptemplates.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapserver
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ldap.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/openldap
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
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files servers
%defattr(644,root,root,755)
%doc guide.html
%dir %{_sysconfdir}/openldap/schema
%attr(640,root,slapd) %config %verify(not size mtime md5) %{_sysconfdir}/openldap/slapd.conf
%attr(640,root,slapd) %config %verify(not size mtime md5) %{_sysconfdir}/openldap/slapd.access.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/schema/*.schema
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/ldap
%attr(754,root,root) /etc/rc.d/init.d/ldap
%attr(770,root,slapd) %{_localstatedir}/lib/openldap-ldbm
%{_datadir}/openldap/*.help
%{_datadir}/openldap/ldapfriendly
%{_datadir}/openldap/schema
%dir %{_libdir}/openldap/
%attr(755,root,root) %{_libdir}/openldap/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man5/ldif.5*
%{_mandir}/man5/slapd.conf.5*
%{_mandir}/man5/slapd.replog.5*
%{_mandir}/man8/*
