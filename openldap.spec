#
# Conditional build:
# ldbm_type	- set to needed value (btree<default> or hash)
%bcond_with	db3	# use old db3 package instead of db (and disable bdb backend)
%bcond_without	sasl 	# don't build cyrus sasl support
%bcond_without	odbc	# disable sql backend
%bcond_without	perl	# disable perl backend
%bcond_without	slp  	# disable SLP support
#
Summary:	Lightweight Directory Access Protocol clients/servers
Summary(es):	Clientes y servidor para LDAP
Summary(pl):	Klienci Lightweight Directory Access Protocol
Summary(pt_BR):	Clientes e servidor para LDAP
Summary(ru):	ïÂÒÁÚÃÙ ËÌÉÅÎÔÏ× LDAP
Summary(uk):	úÒÁÚËÉ ËÌ¦¤ÎÔ¦× LDAP
Name:		openldap
Version:	2.1.25
Release:	1
License:	Artistic
Group:		Networking/Daemons
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
# Source0-md5:	7e3e53a44230bedd66152f4bdb08f50b
Source1:	ldap.init
Source2:	%{name}.sysconfig
Source3:	ldap.conf
Patch0:		%{name}-make_man_link.patch
Patch1:		%{name}-conffile.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-nolibbind.patch
Patch5:		%{name}-fast.patch
Patch6:		%{name}-cldap.patch
Patch7:		%{name}-ldapi_FHS.patch
Patch8:		%{name}-ac25x.patch
Patch10:	%{name}-backend_libs.patch
#Patch11:	%{name}-sendbuf.patch
Patch12:	%{name}-perl.patch
URL:		http://www.openldap.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_sasl:BuildRequires:	cyrus-sasl-devel}
%{?with_db3:BuildRequires:	db3-devel}
%{!?with_db3:BuildRequires:	db-devel >= 4.2}
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libwrap-devel
%{?with_slp:BuildRequires:	openslp-devel}
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	pam-devel
BuildRequires:	readline-devel >= 4.2
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{?with_sasl:Requires:	cyrus-sasl-devel}
Requires:	pam-devel
%if %{with db3}
Requires:	db3-devel
%else
Requires:	db-devel >= 4.2
%endif
Requires:	openssl-devel >= 0.9.7c

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
Requires(pre):	/usr/bin/getent
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	textutils
Requires(post):	/usr/sbin/usermod
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
Serwery (demony) które przychodz± z LDAPem.

Pakiet ten zawiera:
- serwer LDAP (slapd)
- serwer replikacji bazy LDAP (slurpd)

Zainstaluj ten pakiet je¿eli potrzebujesz server OpenLDAP-2.x.

Potrzebny te¿ jest jaki¶ backend dla serwera, dlatego nale¿y
zainstalowaæ odpowiedni pakiet openldap-backend. Zalecany jest backend
bdb.

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

%package backend-bdb
Summary:	BDB backend to OpenLDAP server
Summary(pl):	Backend BDB do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-bdb
BDB backend to slapd, the OpenLDAP server.

%description backend-bdb -l pl
Backend BDB do slapd - serwera OpenLDAP.

%package backend-dnssrv
Summary:	DNS SRV backend to OpenLDAP server
Summary(pl):	Backend DNS SRV do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-dnssrv
DNS SRV backend to slapd, the OpenLDAP server.

%description backend-dnssrv -l pl
Backend DNS SRV do slapd - serwera OpenLDAP.

#%package backend-ldap
#Summary:	LDAP backend to OpenLDAP server
#Summary(pl):	Backend LDAP do serwera OpenLDAP
#Group:		Networking/Daemons
#PreReq:		rc-scripts
#Requires(post,pre):	/bin/ed
#
#%description backend-ldap
#LDAP backend to slapd, the OpenLDAP server.
#
#%description backend-ldap -l pl
#Backend LDAP do slapd - serwera OpenLDAP.

%package backend-ldbm
Summary:	LDBM backend to OpenLDAP server
Summary(pl):	Backend LDBM do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-ldbm
LDBM backend to slapd, the OpenLDAP server.

%description backend-ldbm -l pl
Backend LDBM do slapd - serwera OpenLDAP.

%package backend-meta
Summary:	Meta backend to OpenLDAP server
Summary(pl):	Backend Meta do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-meta
Meta backend to slapd, the OpenLDAP server.

%description backend-meta -l pl
Backend Meta do slapd - serwera OpenLDAP.

%package backend-monitor
Summary:	Monitor backend to OpenLDAP server
Summary(pl):	Backend Monitor do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-monitor
Meta backend to slapd, the OpenLDAP server.

%description backend-monitor -l pl
Backend Meta do slapd - serwera OpenLDAP.

%package backend-passwd
Summary:	/etc/passwd backend to OpenLDAP server
Summary(pl):	Backend /etc/passwd do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-passwd
/etc/passwd backend to slapd, the OpenLDAP server.

%description backend-passwd -l pl
Backend /etc/passwd do slapd - serwera OpenLDAP.

%package backend-perl
Summary:	Perl backend to OpenLDAP server
Summary(pl):	Backend Perl do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-perl
Perl backend to slapd, the OpenLDAP server.

%description backend-perl -l pl
Backend Perl do slapd - serwera OpenLDAP.

%package backend-shell
Summary:	Shell backend to OpenLDAP server
Summary(pl):	Backend Shell do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-shell
Shell backend to slapd, the OpenLDAP server.

%description backend-shell -l pl
Backend Shell do slapd - serwera OpenLDAP.

%package backend-sql
Summary:	SQL backend to OpenLDAP server
Summary(pl):	Backend SQL do serwera OpenLDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,pre):	/bin/ed
Requires:	%{name}-servers = %{version}

%description backend-sql
SQL backend to slapd, the OpenLDAP server.

%description backend-sql -l pl
Backend SQL do slapd - serwera OpenLDAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1
#%patch10 -p1
%patch12 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
CPPFLAGS="-I%{_includedir}/ncurses %{?with_db3:-I%{_includedir}/db3}"
CFLAGS="%{rpmcflags} %{?with_db3:-I%{_includedir}/db3}"
LDFLAGS="%{rpmldflags} %{?with_db3:-ldb3}"
%configure \
	--enable-syslog \
	--enable-cache \
	--enable-referrals \
	--enable-ipv6 \
	--enable-local \
	--with-readline \
	--with-threads \
	--with-tls \
	--with-yielding-select \
	--enable-aci \
	--enable-crypt \
	--enable-lmpasswd \
%if %{with sasl}
	--with-cyrus-sasl \
	--enable-spasswd \
%endif
	--enable-modules \
	--enable-phonetic \
	--enable-rewrite \
	--enable-rlookups \
%if %{with slp}
	--enable-slp \
%else
	--disable-slp \
%endif
	--enable-wrappers \
%if %{with db3}
	--disable-bdb \
%else
	--enable-bdb \
	--with-bdb-module=dynamic \
%endif
	--enable-dnssrv \
	--with-dnssrv-module=dynamic \
	--enable-ldap \
	--with-ldap-module=dynamic \
	--enable-ldbm \
	--with-ldbm-module=dynamic \
	--with-ldbm-api=berkeley \
	--with-ldbm-type=%{?ldbm_type:%{ldbm_type}}%{!?ldbm_type:btree} \
	--enable-meta \
	--with-meta-module=dynamic \
	--enable-monitor \
	--with-monitor-module=dynamic \
	--enable-null \
	--with-null-module=static \
	--enable-passwd \
	--with-passwd-module=dynamic \
%if %{with perl}
	--enable-perl \
	--with-perl-module=dynamic \
%endif
	--enable-shell \
	--with-shell-module=dynamic \
%if %{with odbc}
	--enable-sql \
	--with-sql-module=dynamic \
%endif
	--enable-slurpd \
	--enable-shared \
	--enable-dynamic \
	--enable-static

%{__make} depend
%{__make}

rm -f doc/rfc/rfc*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{sysconfig,rc.d/init.d},var/lib/openldap-data} \
	$RPM_BUILD_ROOT%{_datadir}/openldap/schema

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
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/* $RPM_BUILD_ROOT%{_datadir}/openldap/schema

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

%triggerpostun servers -- openldap-servers < 2.1.12
if [ "`getend passwd slapd | cut -d: -f6`" = "/var/lib/openldap-ldbm" ]; then
	/usr/sbin/usermod -d /var/lib/openldap-data slapd
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

%if ! %{with db3}
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

%if %{with perl}
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
%endif

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

%if %{with odbc}
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
%endif

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
%{_mandir}/man5/slapd.*
%{_mandir}/man5/slapd-null.*
%{_mandir}/man5/slapd-ldap.*
%{_mandir}/man8/*

%if ! %{with db3}
%files backend-bdb
%defattr(644,root,root,755)
%{_libdir}/openldap/back_bdb.la
%attr(755,root,root) %{_libdir}/openldap/back_bdb.s*
%{_mandir}/man5/slapd-bdb.*
%endif

%files backend-dnssrv
%defattr(644,root,root,755)
%{_libdir}/openldap/back_dnssrv.la
%attr(755,root,root) %{_libdir}/openldap/back_dnssrv.s*
%{_mandir}/man5/slapd-dnssrv.*

#%files backend-ldap
#%defattr(644,root,root,755)
#%%{_libdir}/openldap/back_ldap.la
#%attr(755,root,root) %{_libdir}/openldap/back_ldap.s*

%files backend-ldbm
%defattr(644,root,root,755)
%{_libdir}/openldap/back_ldbm.la
%attr(755,root,root) %{_libdir}/openldap/back_ldbm.s*
%{_mandir}/man5/slapd-ldbm.*

%files backend-meta
%defattr(644,root,root,755)
%{_libdir}/openldap/back_meta.la
%attr(755,root,root) %{_libdir}/openldap/back_meta.s*
%{_mandir}/man5/slapd-meta.*

%files backend-monitor
%defattr(644,root,root,755)
%doc servers/slapd/back-monitor/README
%{_libdir}/openldap/back_monitor.la
%attr(755,root,root) %{_libdir}/openldap/back_monitor.s*

%files backend-passwd
%defattr(644,root,root,755)
%{_libdir}/openldap/back_passwd.la
%attr(755,root,root) %{_libdir}/openldap/back_passwd.s*
%{_mandir}/man5/slapd-passwd.*

%if %{with perl}
%files backend-perl
%defattr(644,root,root,755)
%doc servers/slapd/back-perl/*.pm
%{_libdir}/openldap/back_perl.la
%attr(755,root,root) %{_libdir}/openldap/back_perl.s*
%{_mandir}/man5/slapd-perl.*
%endif

%files backend-shell
%defattr(644,root,root,755)
%{_libdir}/openldap/back_shell.la
%attr(755,root,root) %{_libdir}/openldap/back_shell.s*
%{_mandir}/man5/slapd-shell.*

%if %{with odbc}
%files backend-sql
%defattr(644,root,root,755)
%doc servers/slapd/back-sql/docs/*
%{_libdir}/openldap/back_sql.la
%attr(755,root,root) %{_libdir}/openldap/back_sql.s*
%{_mandir}/man5/slapd-sql.*
%endif
