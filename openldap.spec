#
# Conditional build:
# ldbm_type	- set to needed value (btree<default> or hash)
# _with_db3	- use old db3 package instead of db (and disable bdb backend)
# _without_sasl - don't build cyrus sasl support
# _without_odbc	- disable sql backend
# _without_perl	- disable perl backend
#
Summary:	Lightweight Directory Access Protocol clients/servers
Summary(es):	Clientes y servidor para LDAP
Summary(pl):	Klienci Lightweight Directory Access Protocol
Summary(pt_BR):	Clientes e servidor para LDAP
Summary(ru):	Образцы клиентов LDAP
Summary(uk):	Зразки кл╕╓нт╕в LDAP
Name:		openldap
Version:	2.1.12
Release:	1
License:	Artistic
Group:		Networking/Daemons
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
Source1:	ldap.init
Source2:	%{name}.sysconfig
Source3:	ldap.conf
Patch0:		%{name}-make_man_link.patch
Patch1:		%{name}-conffile.patch
Patch2:		%{name}-config.patch
#Patch3:		%{name}-sendbuf.patch
Patch4:		%{name}-sql.patch
Patch5:		%{name}-fast.patch
Patch6:		%{name}-cldap.patch
#Patch7:		%{name}-no_libnsl.patch
Patch8:		%{name}-ldapi_FHS.patch
Patch9:		%{name}-ac25x.patch
#Patch10:	%{name}-db41.patch
#Patch11:	%{name}-secpatch.patch
Patch12:	%{name}-link_no_static.patch
URL:		http://www.openldap.org/
%{!?_without_sasl:BuildRequires:	cyrus-sasl-devel}
%{?_with_db3:BuildRequires:	db3-devel}
%{!?_with_db3:BuildRequires:	db-devel}
BuildRequires:	libltdl-devel
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	pam-devel
BuildRequires:	ed
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
Serwery i klienci LDAP jak i interfejsy do innych protokoЁСw. Wiedz,
©e pakiet ten nie zawiera interfejsu slapd to X.500 i dlatego nie
wymaga pakietu ISODE.

Pakiet ten zawiera:
- biblioteki implementuj╠ce obsЁugЙ protokoЁu LDAP,
- dodatkowe narzedzia i przykЁadowe aplikacje klienckie LDAP.

%description -l pt_BR
OpenLDAP И um conjunto de ferramentas e aplicaГУes para construir um
servidor de diretСrios.

O conjunto completo contИm:
- bibliotecas implementando o protocolo LDAP utilitАrios,
- ferramentas e clientes.

Este pacote contИm apenas as bibliotecas usadas por alguns programas.
VocЙ provavelmente tambИm vai querer instalar o pacote
openldap-client.

%description -l ru
Образцы клиентов, поставляемые с LDAP.

%description -l uk
Зразки кл╕╓нт╕в, що поставляються з LDAP.

%package devel
Summary:	LDAP development files
Summary(es):	Bibliotecas de desarrollo y archivos de inclusiСn para OpenLDAP
Summary(pl):	Pliki dla developerСw LDAP
Summary(pt_BR):	Bibliotecas de desenvolvimento e arquivos de inclusЦo para o OpenLDAP
Summary(ru):	Файлы для программирования с LDAP
Summary(uk):	Файли для програмування з LDAP
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
Bibliotecas de desarrollo y archivos de inclusiСn de OpenLDAP.

%description devel -l pl
Pliki nagЁСwkowe i biblioteki konieczne do rozwoju aplikacji
u©ywaj╠cych LDAP.

%description devel -l pt_BR
Bibliotecas de desenvolvimento e arquivos de inclusЦo do OpenLDAP.
Instale este pacote se vocЙ for trabalhar com desenvolvimento em LDAP
ou desejar compilar algum programa que utilize LDAP.

%description devel -l ru
Хедеры и библиотеки, необходимые для разработки приложений,
использующих LDAP.

%description devel -l uk
Хедери та б╕бл╕отеки, необх╕дн╕ для розробки програм, що
використовують LDAP.

%package static
Summary:	LDAP static libraries
Summary(pl):	Biblioteki statyczne LDAP
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com openldap
Summary(ru):	Статические библиотеки LDAP
Summary(uk):	Статичн╕ б╕бл╕отеки LDAP
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
Bibliotecas estАticas para desenvolvimento com openldap.

%description static -l ru
Статические библиотеки, необходимые для разработки приложений,
использующих LDAP.

%description static -l uk
Статичн╕ б╕бл╕отеки, необх╕дн╕ для розробки програм, що використовують
LDAP.

%package servers
Summary:	LDAP servers
Summary(pl):	Serwery LDAP
Summary(pt_BR):	Arquivos para o servidor OpenLDAP
Summary(ru):	Сервера LDAP
Summary(uk):	Сервера LDAP
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

You will also need some backend for server, so install some
openldap-backend package. The bdb backend is recommended.

%description servers -l pl
Serwery (demony) ktСre przychodz╠ z LDAPem.

Pakiet ten zawiera:
- serwer LDAP (slapd)
- serwer replikacji bazy LDAP (slurpd)

Zainstaluj ten pakiet je©eli potrzebujesz server OpenLDAP-2.x.

Potrzebny te© jest jaki╤ backend dla serwera, dlatego nale©y
zainstalowaФ odpowiedni pakiet openldap-backend. Zalecany jest backend
bdb.

%description servers -l pt_BR
O pacote openldap-server contИm o servidor slapd que И responsАvel por
receber as requisiГУes dos clientes e por manter a base de dados do
diretСrio.

O conjunto completo contИm:
- servidor LDAP (slapd),
- servidor de replicaГЦo (slurpd)

Instale este pacote se vocЙ desejar executar um servidor OpenLDAP.

%description servers -l ru
Сервера (демоны), поставляемые с LDAP.

%description servers -l uk
Сервера (демони), що поставляються з LDAP.

%package backend-bdb
Summary:	BDB backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-bdb
BDB backend to slapd, the OpenLDAP server.

%package backend-dnssrv
Summary:	DNS SRV backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-dnssrv
DNS SRV backend to slapd, the OpenLDAP server.

#%package backend-ldap #Summary: LDAP backend to Openldap server
#Group: Networking/Daemons #PreReq: rc-scripts #Requires(post,pre):
/bin/ed # #%description backend-ldap #LDAP backend to slapd, the
OpenLDAP server.

%package backend-ldbm
Summary:	LDBM backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-ldbm
LDBM backend to slapd, the OpenLDAP server.

%package backend-meta
Summary:	Meta backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-meta
Meta backend to slapd, the OpenLDAP server.

%package backend-monitor
Summary:	Monitor backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-monitor
Meta backend to slapd, the OpenLDAP server.

%package backend-passwd
Summary:	/etc/passwd backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-passwd
/etc/passwd backend to slapd, the OpenLDAP server.

%package backend-perl
Summary:	Perl backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-perl
Perl backend to slapd, the OpenLDAP server.

%package backend-shell
Summary:	Shell backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-shell
Shell backend to slapd, the OpenLDAP server.

%package backend-sql
Summary:	SQL backend to Openldap server
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed

%description backend-sql
SQL backend to slapd, the OpenLDAP server.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1

%patch5 -p1
%patch6 -p1
#%patch7 -p1
%patch8 -p1
%patch9 -p1
#%patch10 -p1
#%patch11 -p0
%patch12 -p1

%build
CPPFLAGS="-I%{_includedir}/ncurses %{?_with_db3:-I%{_includedir}/db3}"
CFLAGS="%{rpmcflags} %{?_with_db3:-I%{_includedir}/db3}"
LDFLAGS="%{rpmldflags} %{?_with_db3:-ldb3}"
%configure2_13 \
	--enable-syslog \
	--enable-cache \
	--enable-referrals \
	--enable-ipv6 \
	--enable-local \
%{!?_without_sasl:--with-cyrus-sasl} \
	--with-readline \
	--with-threads \
	--with-tls \
	--with-yielding-select \
	--enable-aci \
	--enable-crypt \
	--enable-lmpasswd \
%{!?_without_sasl:--enable-spasswd} \
	--enable-modules \
	--enable-phonetic \
	--enable-rewrite \
	--enable-rlookups \
	--disable-slp \
	--enable-wrappers \
%{?!_with_db3:--enable-bdb}%{?_with_db3:--disable-bdb} \
%{?!_with_db3:--with-bdb-module=dynamic} \
	--enable-dnssrv \
	--with-dnssrv-module=dynamic \
	--enable-ldap \
	--with-ldap-module=dynamic \
	--enable-ldbm \
	--with-ldbm-module=dynamic \
	--with-ldbm-api=berkeley \
	--with-ldbm-type=%{?ldbm_type:%{ldbm_type}}%{?!ldbm_type:btree} \
	--enable-meta \
	--with-meta-module=dynamic \
	--enable-monitor \
	--with-monitor-module=dynamic \
	--enable-null \
	--with-null-module=static \
	--enable-passwd \
	--with-passwd-module=dynamic \
%{!?_without_perl:--enable-perl} \
%{!?_without_perl:--with-perl-module=dynamic} \
	--enable-shell \
	--with-shell-module=dynamic \
%{!?_without_odbc:--enable-sql} \
%{!?_without_odbc:--with-sql-module=dynamic} \
	--enable-slurpd \
	--enable-shared \
	--enable-static


%{__make} depend
%{__make}

# avoid relinking to allow build without openldap-devel already installed
for d in libraries/libldap/libldap.la libraries/libldap_r/libldap_r.la ; do
	ed $d <<EOF
,s/^relink_command.*//
w
q
EOF
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{sysconfig,rc.d/init.d},var/lib/openldap-data} \
	$RPM_BUILD_ROOT%{_datadir}/openldap/schema

rm -f doc/rfc/rfc*

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libexecdir}/openldap/ $RPM_BUILD_ROOT%{_libdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/openldap/*.a

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ldap

install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/ldap.conf

echo "localhost" > $RPM_BUILD_ROOT%{_sysconfdir}/openldap/ldapserver

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/openldap/{*.default,ldap.conf}

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
		-c "OpenLDAP server" -d /var/lib/openldap-data slapd 1>&2
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

%if %{!?_with_db3:1}%{?_with_db3:0}
%post backend-bdb
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_bdb.la[[:blank:]]*$/moduleload    back_bdb.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-bdb
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^# moduleload    back_bdb.la[[:blank:]]*$/# moduleload    back_bdb.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi
%endif

%post backend-dnssrv
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_dnssrv.la[[:blank:]]*$/moduleload    back_dnssrv.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-dnssrv
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^# moduleload    back_dnssrv.la[[:blank:]]*$/# moduleload    back_dnssrv.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

#%%post backend-ldap
#ed -s %%{_sysconfdir}/openldap/slapd.conf << EOF || :
#,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_ldap.la[[:blank:]]*$/moduleload    back_ldap.la/
#wq
#EOF
#if [ -f /var/lock/subsys/ldap ]; then
#	/etc/rc.d/init.d/ldap restart >&2
#fi
#
#%%preun backend-ldap
#ed -s %%{_sysconfdir}/openldap/slapd.conf << EOF || :
#,s/^# moduleload    back_ldap.la[[:blank:]]*$/# moduleload    back_ldap.la/
#wq
#EOF
#if [ -f /var/lock/subsys/ldap ]; then
#	/etc/rc.d/init.d/ldap restart >&2
#fi

%post backend-ldbm
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_ldbm.la[[:blank:]]*$/moduleload    back_ldbm.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-ldbm
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^# moduleload    back_ldbm.la[[:blank:]]*$/# moduleload    back_ldbm.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%post backend-meta
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_meta.la[[:blank:]]*$/moduleload    back_meta.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-meta
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^# moduleload    back_meta.la[[:blank:]]*$/# moduleload    back_meta.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%post backend-monitor
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_monitor.la[[:blank:]]*$/moduleload    back_monitor.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-monitor
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^# moduleload    back_monitor.la[[:blank:]]*$/# moduleload    back_monitor.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%post backend-passwd
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_passwd.la[[:blank:]]*$/moduleload    back_passwd.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-passwd
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :

,s/^# moduleload    back_passwd.la[[:blank:]]*$/# moduleload    back_passwd.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%post backend-perl
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_perl.la[[:blank:]]*$/moduleload    back_perl.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-perl
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^# moduleload    back_perl.la[[:blank:]]*$/# moduleload    back_perl.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%post backend-shell
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_shell.la[[:blank:]]*$/moduleload    back_shell.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-shell
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^# moduleload    back_shell.la[[:blank:]]*$/# moduleload    back_shell.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%post backend-sql
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^#[[:blank:]]*moduleload[[:blank:]]\\+back_sql.la[[:blank:]]*$/moduleload    back_sql.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%preun backend-sql
ed -s %{_sysconfdir}/openldap/slapd.conf << EOF || :
,s/^# moduleload    back_sql.la[[:blank:]]*$/# moduleload    back_sql.la/
wq
EOF
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
fi

%files
%defattr(644,root,root,755)
%doc ANNOUNCEMENT CHANGES COPYRIGHT README
%doc doc/{drafts,rfc}
%dir %{_sysconfdir}/openldap
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/openldap/ldapserver
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ldap.conf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/openldap
%{_datadir}/openldap/*
%{_mandir}/man1/*
%{_mandir}/man5/ldap.*
%{_mandir}/man5/ldif.*

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
%attr(770,root,slapd) %{_localstatedir}/openldap-data
%attr(770,root,slapd) %{_localstatedir}/openldap-slurp
%dir %{_datadir}/openldap/schema
%{_datadir}/openldap/schema/*.schema
%dir %{_libdir}/openldap/
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man5/slapd*
%{_mandir}/man8/*

%if %{!?_with_db3:1}%{?_with_db3:0}
%files backend-bdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_bdb*
%endif

%files backend-dnssrv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_dnssrv*

#%files backend-ldap
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/openldap/back_ldap*

%files backend-ldbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_ldbm*

%files backend-meta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_meta*

%files backend-monitor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_monitor*

%files backend-passwd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_passwd*

%if %{!?_without_perl:1}%{?_without_perl:0}
%files backend-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_perl*
%endif

%files backend-shell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_shell*

%if %{!?_without_odbc:1}%{?_without_perl:0}
%files backend-sql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_sql*
%endif
