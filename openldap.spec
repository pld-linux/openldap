#
# Conditional build:
# ldbm_type	- set to needed value (btree<default> or hash)
# _with_db3	- use old db3 package instead of db
# _without_sasl - don't build cyrus sasl support
# _without_odbc	- disable sql support
#
%define		_with_db3	yes

Summary:	Lightweight Directory Access Protocol clients/servers
Summary(es):	Clientes y servidor para LDAP
Summary(pl):	Klienci Lightweight Directory Access Protocol
Summary(pt_BR):	Clientes e servidor para LDAP
Summary(ru):	ïÂÒÁÚÃÙ ËÌÉÅÎÔÏ× LDAP
Summary(uk):	úÒÁÚËÉ ËÌ¦¤ÎÔ¦× LDAP
Name:		openldap
Version:	2.0.27
Release:	3
License:	Artistic
Group:		Networking/Daemons
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
# Source0-md5:	a1e6508c471dd47205a3492cf57110a6
Source1:	ldap.init
Source2:	%{name}.sysconfig
# Taken from http://www.openldap.org/doc/admin/guide.html. Tarball includes images.
#Source3:	ldap-guide.tar.gz
Source5:	ldap.conf
Patch0:		%{name}-make_man_link.patch
Patch1:		%{name}-conffile.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-sql.patch
Patch4:		%{name}-sendbuf.patch
Patch5:		%{name}-syslog.patch
Patch6:		%{name}-fast.patch
Patch7:		%{name}-cldap.patch
Patch8:		%{name}-no_libnsl.patch
Patch9:		%{name}-ldapi_FHS.patch
Patch10:	%{name}-ac25x.patch
Patch11:	%{name}-db41.patch
Patch12:	%{name}-secpatch.patch
URL:		http://www.openldap.org/
%{!?_without_sasl:BuildRequires:	cyrus-sasl-devel}
%{?_with_db3:BuildRequires:	db3-devel}
%{!?_with_db3:BuildRequires:	db-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	readline-devel >= 4.2
%{!?_without_odbc:BuildRequires:	unixODBC-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc
%define		_libexecdir	%{_sbindir}
%define		_localstatedir	/var/lib

%description
LDAP servers and clients, as well as interfaces to other protocols.
Note that this does not include the slapd interface to X.500 and
therefore does not require the ISODE package.

The package includes:
- libraries implementing the LDAP protocol,
- utilities, tools, and sample clients.

%description -l es
Cliente y servidor LDAP.

%description -l pl
Serwery i klienci LDAP jak i interfejsy do innych protoko³ów. Wiedz,
¿e pakiet ten nie zawiera interfejsu slapd to X.500 i dlatego nie
wymaga pakietu ISODE.

Pakiet ten zawiera:
- biblioteki implementuj±ce obs³ugê protoko³u LDAP,
- dodatkowe narzedzia i przyk³adowe aplikacje klienckie LDAP.

%description -l pt_BR
OpenLDAP é um conjunto de ferramentas e aplicações para construir um
servidor de diretórios.

O conjunto completo contém:
- bibliotecas implementando o protocolo LDAP utilitários,
- ferramentas e clientes.

Este pacote contém apenas as bibliotecas usadas por alguns programas.
Você provavelmente também vai querer instalar o pacote
openldap-client.

%description -l ru
ïÂÒÁÚÃÙ ËÌÉÅÎÔÏ×, ÐÏÓÔÁ×ÌÑÅÍÙÅ Ó LDAP.

%description -l uk
úÒÁÚËÉ ËÌ¦¤ÎÔ¦×, ÝÏ ÐÏÓÔÁ×ÌÑÀÔØÓÑ Ú LDAP.

%package devel
Summary:	LDAP development files
Summary(es):	Bibliotecas de desarrollo y archivos de inclusión para OpenLDAP
Summary(pl):	Pliki dla developerów LDAP
Summary(pt_BR):	Bibliotecas de desenvolvimento e arquivos de inclusão para o OpenLDAP
Summary(ru):	æÁÊÌÙ ÄÌÑ ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Ó LDAP
Summary(uk):	æÁÊÌÉ ÄÌÑ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Ú LDAP
Group:		Development/Libraries
Requires:	%{name} = %{version}
%{!?_without_sasl:Requires:	cyrus-sasl-devel}
Requires:	pam-devel
%{?_with_db3:Requires:	db3-devel}
%{!?_with_db3:Requires:	db-devel}
Requires:	openssl-devel

%description devel
Header files and libraries for developing applications that use LDAP.

%description devel -l es
Bibliotecas de desarrollo y archivos de inclusión de OpenLDAP.

%description devel -l pl
Pliki nag³ówkowe i biblioteki konieczne do rozwoju aplikacji
u¿ywaj±cych LDAP.

%description devel -l pt_BR
Bibliotecas de desenvolvimento e arquivos de inclusão do OpenLDAP.
Instale este pacote se você for trabalhar com desenvolvimento em LDAP
ou desejar compilar algum programa que utilize LDAP.

%description devel -l ru
èÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ,
ÉÓÐÏÌØÚÕÀÝÉÈ LDAP.

%description devel -l uk
èÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ
×ÉËÏÒÉÓÔÏ×ÕÀÔØ LDAP.

%package static
Summary:	LDAP static libraries
Summary(pl):	Biblioteki statyczne LDAP
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com openldap
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ LDAP
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ LDAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package includes the development libraries and header files
needed for compilation of applications that are making use of the LDAP
internals. Install this package only if you plan to develop or will
need to compile cutomized LDAP clients.

%description static -l pl
Biblioteki statyczne LDAP.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com openldap.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ,
ÉÓÐÏÌØÚÕÀÝÉÈ LDAP.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ
LDAP.

%package servers
Summary:	LDAP servers
Summary(pl):	Serwery LDAP
Summary(pt_BR):	Arquivos para o servidor OpenLDAP
Summary(ru):	óÅÒ×ÅÒÁ LDAP
Summary(uk):	óÅÒ×ÅÒÁ LDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires(post,preun):	/sbin/chkconfig

%description servers
The openldap2-server package has the slapd daemon which is responsible
for handling the database and client queries.

The package includes:
- stand-alone LDAP server (slapd),
- stand-alone LDAP replication server (slurpd)

Install this package if you want to setup an OpenLDAP-2.x server.

%description servers -l pl
Serwery (demony) które przychodz± z LDAPem.

Pakiet ten zawiera:
- serwer LDAP (slapd)
- serwer replikacji bazy LDAP (slurpd)

Zainstaluj ten pakiet je¿eli potrzebujesz server OpenLDAP-2.x.

%description servers -l pt_BR
O pacote openldap-server contém o servidor slapd que é responsável por
receber as requisições dos clientes e por manter a base de dados do
diretório.

O conjunto completo contém:
- servidor LDAP (slapd),
- servidor de replicação (slurpd)

Instale este pacote se você desejar executar um servidor OpenLDAP.

%description servers -l ru
óÅÒ×ÅÒÁ (ÄÅÍÏÎÙ), ÐÏÓÔÁ×ÌÑÅÍÙÅ Ó LDAP.

%description servers -l uk
óÅÒ×ÅÒÁ (ÄÅÍÏÎÉ), ÝÏ ÐÏÓÔÁ×ÌÑÀÔØÓÑ Ú LDAP.

%prep
%setup -q -a 3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p0

%build
CPPFLAGS="-I%{_includedir}/ncurses -I%{_includedir}/db3"
CFLAGS="%{rpmcflags} -I%{_includedir}/db3"
%configure2_13 \
	--enable-syslog \
	--enable-proctitle \
	--enable-cache \
	--enable-referrals \
	--enable-ipv6 \
	--enable-local \
%{!?_without_sasl:--with-cyrus-sasl} \
%{!?_without_sasl:--enable-spasswd} \
	--with-readline \
	--with-threads \
	--with-tls \
	--with-yielding-select \
	--enable-slapd \
	--enable-crypt \
	--enable-multimaster \
	--enable-phonetic \
	--enable-rlookups \
	--enable-aci \
	--enable-wrappers \
	--enable-dynamic \
	--enable-modules \
	--enable-dnssrv \
	--with-dnssrv-module=dynamic \
	--enable-ldap \
	--with-ldap-module=dynamic \
	--enable-ldbm \
	--with-ldbm-module=static \
	--with-ldbm-api=berkeley \
	--with-ldbm-type=%{?ldbm_type:%{ldbm_type}}%{?!ldbm_type:btree} \
	--enable-passwd \
	--with-passwd-module=dynamic \
	--enable-shell \
	--with-shell-module=static \
	--enable-slurpd \
	--enable-shared \
	--enable-static \
%{!?_without_odbc:--enable-sql} \
%{!?_without_odbc:--with-sql-module=dynamic} 


# without this server won't start
#echo "#undef HAVE_GETADDRINFO" >> include/portable.h

%{__make} depend
%{__make}

# avoid relinking to allow build without openldap-devel already installed
for d in libraries/libldap/libldap.la libraries/libldap_r/libldap_r.la ; do
	perl -pi -e 's/^relink_command.*//' $d
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{sysconfig,rc.d/init.d},var/lib/openldap-ldbm} \
	$RPM_BUILD_ROOT%{_datadir}/openldap/schema

rm -f doc/rfc/rfc*

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libexecdir}/openldap $RPM_BUILD_ROOT%{_libdir}

# hack the default config files
perl -pi -e "s|%{buildroot}||g" $RPM_BUILD_ROOT%{_sysconfdir}/openldap/slapd.conf

perl -pi -e "s|^#! /bin/sh|#!/bin/sh|g" $RPM_BUILD_ROOT%{_sbindir}/xrpcomp

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ldap

install $RPM_SOURCE_DIR/ldap.conf $RPM_BUILD_ROOT%{_sysconfdir}/ldap.conf

echo "localhost" > $RPM_BUILD_ROOT%{_sysconfdir}/openldap/ldapserver

# Standard schemas should not be changed by users
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/* $RPM_BUILD_ROOT%{_datadir}/openldap/schema/

# create slapd.access.conf
echo "# This is a good place to put slapd access-control directives" > \
	$RPM_BUILD_ROOT%{_sysconfdir}/openldap/slapd.access.conf

# create local.schema
echo "# This is a good place to put your schema definitions " > \
	$RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/local.schema

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%pre servers
if [ -n "`getgid slapd`" ]; then
	if [ "`getgid slapd`" != "93" ]; then
		echo "Error: group slapd doesn't have gid=93. Correct this before installing openldap." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 93 -r -f slapd
fi
if [ -n "`id -u slapd 2>/dev/null`" ]; then
	if [ "`id -u slapd`" != "93" ]; then
		echo "Error: user slapd doesn't have uid=93. Correct this before installing openldap." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -M -r -u 93 -s /bin/false -g slapd \
		-c "OpenLDAP server" -d /var/lib/openldap-ldbm slapd 1>&2
fi

%post servers
/sbin/chkconfig --add ldap
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
else
	echo "Run '/etc/rc.d/init.d/ldap start' to start OpenLDAP server." >&2
fi

%preun servers
if [ "$1" = "0" ] ; then
	if [ -f /var/lock/subsys/ldap ]; then
		/etc/rc.d/init.d/ldap stop >&2
	fi
	/sbin/chkconfig --del ldap
fi

%postun servers
if [ "$1" = "0" ]; then
	/usr/sbin/userdel slapd
	/usr/sbin/groupdel slapd
fi

%files
%defattr(644,root,root,755)
%doc ANNOUNCEMENT CHANGES COPYRIGHT README
%doc doc/{drafts,rfc}
#%%doc guide
%dir %{_sysconfdir}/openldap
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapfilter.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapsearchprefs.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldaptemplates.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapserver
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ldap.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/openldap
%{_datadir}/openldap/*
%{_mandir}/man1/*
%{_mandir}/man5/ldap.conf.5*
%{_mandir}/man5/ldapfilter.conf.5*
%{_mandir}/man5/ldapfriendly.5*
%{_mandir}/man5/ldapsearchprefs.conf.5*
%{_mandir}/man5/ldaptemplates.conf.5*
%{_mandir}/man5/ldif.5*
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
%dir %{_sysconfdir}/openldap/schema
%attr(640,root,slapd) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/slapd.conf
%attr(640,root,slapd) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/slapd.access.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/schema/*.schema
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/ldap
%attr(754,root,root) /etc/rc.d/init.d/ldap
%attr(770,root,slapd) %{_localstatedir}/openldap-ldbm
%attr(770,root,slapd) %{_localstatedir}/openldap-slurp
%{_datadir}/openldap/*.help
%dir %{_datadir}/openldap/schema
%{_datadir}/openldap/schema/*.schema
%dir %{_libdir}/openldap/
%attr(755,root,root) %{_libdir}/openldap/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man5/slapd.conf.5*
%{_mandir}/man5/slapd.replog.5*
%{_mandir}/man8/*
