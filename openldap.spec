# TODO:
# - package contribs?
# - complete & validate descriptions
# - trigger for removed ldbm backend
# - trigger for removed overlays (denyop,lastmod)
# - ldap.conf.5 describes /etc/openldap/ldap.conf not /etc/ldap.conf, rename to ldaprc.5 ?
# - unpackaged:
#   /usr/lib64/evolution-openldap/lib/liblber.la
#   /usr/lib64/evolution-openldap/lib/libldap.la
#   /usr/lib64/evolution-openldap/lib/libldap_r.la
#   /usr/lib64/openldap/nssov.a
#   /usr/share/man/man5/slapd-ndb.5.gz
#
# Conditional build:
%bcond_without	exchange	# hacked version of library for Evolution Exchange support
%bcond_with	krb5		# build with MIT Kerberos instead of Heimdal
%bcond_without	odbc		# disable sql backend
%bcond_with	ndb		# enable MySQL NDB Cluster backend
%bcond_without	perl		# disable perl backend
%bcond_without	sasl 		# don't build cyrus sasl support
%bcond_without	slp		# disable SLP support
%bcond_with	system_db	# system Berkeley DB

# Never change or update Berkeley DB, it's there to isolate OpenLDAP
# from any future changes to the system-wide Berkeley DB library.
%define		db_version		4.6.21

%define evolution_exchange_prefix	%{_libdir}/evolution-openldap
%define evolution_exchange_includedir	%{evolution_exchange_prefix}/include
%define evolution_exchange_libdir	%{evolution_exchange_prefix}/lib

Summary:	Lightweight Directory Access Protocol clients/servers
Summary(es.UTF-8):	Clientes y servidor para LDAP
Summary(pl.UTF-8):	Klienci Lightweight Directory Access Protocol
Summary(pt_BR.UTF-8):	Clientes e servidor para LDAP
Summary(ru.UTF-8):	Образцы клиентов LDAP
Summary(uk.UTF-8):	Зразки клієнтів LDAP
Name:		openldap
Version:	2.4.23
Release:	1
License:	OpenLDAP Public License
Group:		Networking/Daemons
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
# Source0-md5:	90150b8c0d0192e10b30157e68844ddf
Source1:	http://download.oracle.com/berkeley-db/db-%{db_version}.tar.gz
# Source1-md5:	718082e7e35fc48478a2334b0bc4cd11
Source2:	ldap.init
Source3:	%{name}.sysconfig
Source4:	%{name}.conf
Source5:	ldap.conf
Source100:	%{name}-README.evolution
Patch0:		%{name}-make_man_link.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-fast.patch
Patch3:		%{name}-cldap.patch
Patch4:		%{name}-ldapi_FHS.patch
Patch5:		%{name}-install.patch
Patch6:		%{name}-backend_libs.patch
Patch7:		%{name}-perl.patch
Patch8:		%{name}-pic.patch
Patch9:		%{name}-ltinstall-mode.patch
Patch10:	%{name}-whowhere.patch
Patch11:	%{name}-ldaprc.patch
Patch12:	%{name}-db.patch
Patch13:	%{name}-nosql.patch
Patch14:	%{name}-smbk5pwd.patch
Patch15:	%{name}-ldapc++.patch
Patch16:	%{name}-pie.patch
Patch17:	%{name}-gethostbyXXXX_r.patch
Patch18:	%{name}-smbk5pwd-heimdal.patch
Patch19:	%{name}-smbk5pwd-shadowLastChange.patch
# Patch for the evolution library
Patch100:	%{name}-ntlm.diff
URL:		http://www.openldap.org/
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with sasl}
BuildRequires:	cyrus-sasl-devel >= 2.1.15
BuildRequires:	libicu-devel
%endif
%{?with_system_db:BuildRequires:	db-devel >= 4.2}
BuildRequires:	gcc >= 5:3.4
BuildRequires:	groff
%if %{with krb5}
BuildRequires:	krb5-devel
%else
BuildRequires:	heimdal-devel
%endif
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libwrap-devel
%{?with_ndb:BuildRequires:	mysql-devel}
%{?with_slp:BuildRequires:	openslp-devel}
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_perl:BuildRequires:	perl-devel}
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	uname(release) >= 2.6
%{?with_odbc:BuildRequires:	unixODBC-devel}
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	openldap-clients
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_sbindir}
%define		_localstatedir	/var/lib
%define		schemadir	%{_datadir}/openldap/schema

%undefine	configure_cache

%description
LDAP servers and clients, as well as interfaces to other protocols.
Note that this does not include the slapd interface to X.500 and
therefore does not require the ISODE package.

The package includes:
- libraries implementing the LDAP protocol,
- utilities, tools, and sample clients.

%description -l es.UTF-8
Cliente y servidor LDAP.

%description -l pl.UTF-8
Serwery i klienci LDAP jak i interfejsy do innych protokołów. Wiedz,
że pakiet ten nie zawiera interfejsu slapd to X.500 i dlatego nie
wymaga pakietu ISODE.

Pakiet ten zawiera:
- biblioteki implementujące obsługę protokołu LDAP,
- dodatkowe narzędzia i przykładowe aplikacje klienckie LDAP.

%description -l pt_BR.UTF-8
OpenLDAP é um conjunto de ferramentas e aplicações para construir um
servidor de diretórios.

O conjunto completo contém:
- bibliotecas implementando o protocolo LDAP utilitários,
- ferramentas e clientes.

Este pacote contém apenas as bibliotecas usadas por alguns programas.
Você provavelmente também vai querer instalar o pacote
openldap-client.

%description -l ru.UTF-8
Образцы клиентов, поставляемые с LDAP.

%description -l uk.UTF-8
Зразки клієнтів, що поставляються з LDAP.

%package nss-config
Summary:	Common configuration for nss_ldap and pam_ldap
Summary(pl.UTF-8):	Wspólna konfiguracja dla nss_ldap i pam_ldap
Group:		Base

%description nss-config
Common configuration for nss_ldap and pam_ldap.

%description nss-config -l pl.UTF-8
Wspólna konfiguracja dla nss_ldap i pam_ldap.

%package libs
Summary:	LDAP shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone LDAP
Group:		Libraries
%{?with_sasl:Requires:	cyrus-sasl >= 2.1.15}
Conflicts:	openldap < 2.2.6-0.3

%description libs
LDAP shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone LDAP.

%package devel
Summary:	LDAP development files
Summary(es.UTF-8):	Bibliotecas de desarrollo y archivos de inclusión para OpenLDAP
Summary(pl.UTF-8):	Pliki dla developerów LDAP
Summary(pt_BR.UTF-8):	Bibliotecas de desenvolvimento e arquivos de inclusão para o OpenLDAP
Summary(ru.UTF-8):	Файлы для программирования с LDAP
Summary(uk.UTF-8):	Файли для програмування з LDAP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
%{?with_sasl:Requires:	cyrus-sasl-devel >= 2.1.15}
Requires:	openssl-devel >= 0.9.7c
%if %{with krb5}
Requires:	krb5-devel
%else
Requires:	heimdal-devel
%endif

%description devel
Header files and libraries for developing applications that use LDAP.

%description devel -l es.UTF-8
Bibliotecas de desarrollo y archivos de inclusión de OpenLDAP.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki konieczne do rozwoju aplikacji
używających LDAP.

%description devel -l pt_BR.UTF-8
Bibliotecas de desenvolvimento e arquivos de inclusão do OpenLDAP.
Instale este pacote se você for trabalhar com desenvolvimento em LDAP
ou desejar compilar algum programa que utilize LDAP.

%description devel -l ru.UTF-8
Хедеры и библиотеки, необходимые для разработки приложений,
использующих LDAP.

%description devel -l uk.UTF-8
Хедери та бібліотеки, необхідні для розробки програм, що
використовують LDAP.

%package static
Summary:	LDAP static libraries
Summary(pl.UTF-8):	Biblioteki statyczne LDAP
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com openldap
Summary(ru.UTF-8):	Статические библиотеки LDAP
Summary(uk.UTF-8):	Статичні бібліотеки LDAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package includes the development libraries and header files
needed for compilation of applications that are making use of the LDAP
internals. Install this package only if you plan to develop or will
need to compile cutomized LDAP clients.

%description static -l pl.UTF-8
Biblioteki statyczne LDAP.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com openldap.

%description static -l ru.UTF-8
Статические библиотеки, необходимые для разработки приложений,
использующих LDAP.

%description static -l uk.UTF-8
Статичні бібліотеки, необхідні для розробки програм, що використовують
LDAP.

%package headers
Summary:	Development files for building OpenLDAP modules
Summary(pl.UTF-8):	Pliki służące do budowania modułów OpenLDAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description headers
Header files for developing OpenLDAP modules.

%description headers -l pl.UTF-8
Pliki nagłówkowe konieczne do rozwoju modułów OpenLDAP.

%package evolution-devel
Summary:	LDAP NTLM hack for the evolution-exchange
Summary(pl.UTF-8):	Hack NTLM dla pakietu evolution-exchange
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description evolution-devel
LDAP NTLM hack for the evolution-exchange.

%description evolution-devel -l pl.UTF-8
Hack NTLM dla pakietu evolution-exchange.

%package ldapc++
Summary:	LDAPv3 C++ Class Library
Summary(pl.UTF-8):	Biblioteka klas C++ LDAPv3
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description ldapc++
LDAPv3 C++ Class Library

%description ldapc++ -l pl.UTF-8
Biblioteka klas C++ LDAPv3.

%package ldapc++-devel
Summary:	LDAPv3 C++ Class Library development files
Summary(pl.UTF-8):	Pliki dla programistów C++ LDAPv3
Group:		Libraries
Requires:	%{name}-ldapc++ = %{version}-%{release}

%description ldapc++-devel
LDAPv3 C++ Class Library development files.

%description ldapc++-devel -l pl.UTF-8
Pliki dla programistów C++ LDAPv3.

%package ldapc++-static
Summary:	Static LDAPv3 C++ Class Library
Summary(pl.UTF-8):	Biblioteka statyczna klas C++ LDAPv3
Group:		Libraries
Requires:	%{name}-ldapc++-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description ldapc++-static
Static LDAPv3 C++ Class Library.

%description ldapc++-static -l pl.UTF-8
Biblioteka statyczna klas C++ LDAPv3.

%package backend-bdb
Summary:	BDB backend to OpenLDAP server
Summary(pl.UTF-8):	Backend BDB do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-bdb
BDB backend to slapd, the OpenLDAP server.

%description backend-bdb -l pl.UTF-8
Backend BDB do slapd - serwera OpenLDAP.

%package backend-dnssrv
Summary:	DNS SRV backend to OpenLDAP server
Summary(pl.UTF-8):	Backend DNS SRV do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-dnssrv
DNS SRV backend to slapd, the OpenLDAP server.

%description backend-dnssrv -l pl.UTF-8
Backend DNS SRV do slapd - serwera OpenLDAP.

%package backend-hdb
Summary:	HDB (Hierarchical DB) backend to OpenLDAP server
Summary(pl.UTF-8):	Backend HDB (Hierarchical DB) do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-hdb
HDB (Hierarchical DB) backend to slapd, the OpenLDAP server.

%description backend-hdb -l pl.UTF-8
Backend HDB (Hierarchical DB) do slapd - serwera OpenLDAP.

%package backend-ldap
Summary:	LDAP backend to OpenLDAP server
Summary(pl.UTF-8):	Backend LDAP do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-ldap
LDAP backend to slapd, the OpenLDAP server.

%description backend-ldap -l pl.UTF-8
Backend LDAP do slapd - serwera OpenLDAP.

%package backend-meta
Summary:	Meta backend to OpenLDAP server
Summary(pl.UTF-8):	Backend Meta do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-meta
Meta backend to slapd, the OpenLDAP server.

%description backend-meta -l pl.UTF-8
Backend Meta do slapd - serwera OpenLDAP.

%package backend-monitor
Summary:	Monitor backend to OpenLDAP server
Summary(pl.UTF-8):	Backend Monitor do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-monitor
Meta backend to slapd, the OpenLDAP server.

%description backend-monitor -l pl.UTF-8
Backend Meta do slapd - serwera OpenLDAP.

%package backend-ndb
Summary:	MySQL NDB Cluster backend to OpenLDAP server
Summary(pl.UTF-8):	Backend MySQL NDB Cluster do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-ndb
MySQL NDB Cluster backend to slapd, the OpenLDAP server.

%description backend-ndb -l pl.UTF-8
Backend MySQL NDB Cluster do slapd do serwera OpenLDAP.

%package backend-passwd
Summary:	/etc/passwd backend to OpenLDAP server
Summary(pl.UTF-8):	Backend /etc/passwd do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-passwd
/etc/passwd backend to slapd, the OpenLDAP server.

%description backend-passwd -l pl.UTF-8
Backend /etc/passwd do slapd - serwera OpenLDAP.

%package backend-perl
Summary:	Perl backend to OpenLDAP server
Summary(pl.UTF-8):	Backend Perl do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-perl
Perl backend to slapd, the OpenLDAP server.

%description backend-perl -l pl.UTF-8
Backend Perl do slapd - serwera OpenLDAP.

%package backend-relay
Summary:	Relay backend to OpenLDAP server
Summary(pl.UTF-8):	Backend przekazujący do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-overlay-rwm = %{version}-%{release}
Requires:	%{name}-servers = %{version}-%{release}

%description backend-relay
The primary purpose of this slapd(8) backend is to map a naming
context defined in a database running in the same slapd(8) instance
into a virtual naming context, with attributeType and objectClass
manipulation, if required. It requires the rwm overlay.

%description backend-relay -l pl.UTF-8
Głównym celem tego backendu slapd(8) jest odwzorowywanie kontekstów
nazw zdefiniowanych w bazie danych działającej w tej samej instancji
slapd(8) na konteksty nazw wirtualnych z modyfikowaniem attributeType
i objectClass w razie potrzeby. Wymaga nakładki rwm.

%package backend-shell
Summary:	Shell backend to OpenLDAP server
Summary(pl.UTF-8):	Backend Shell do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-shell
Shell backend to slapd, the OpenLDAP server.

%description backend-shell -l pl.UTF-8
Backend Shell do slapd - serwera OpenLDAP.

%package backend-sock
Summary:	Socket backend to OpenLDAP server
Summary(pl.UTF-8):	Backend Socket do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-sock
Socket backend to slapd, the OpenLDAP server.

%description backend-sock -l pl.UTF-8
Backend Socket do slapd - serwera OpenLDAP.

%package backend-sql
Summary:	SQL backend to OpenLDAP server
Summary(pl.UTF-8):	Backend SQL do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-sql
SQL backend to slapd, the OpenLDAP server.

%description backend-sql -l pl.UTF-8
Backend SQL do slapd - serwera OpenLDAP.

%package overlay-accesslog
Summary:	Accesslog overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka accesslog dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-accesslog
Accesslog overlay for OpenLDAP server.

%description overlay-accesslog -l pl.UTF-8
Nakładka accesslog dla serwera OpenLDAP.

%package overlay-auditlog
Summary:	Auditlog overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka auditog dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-auditlog
The Audit Logging overlay can be used to record all changes on a given
backend database to a specified log file. Changes are logged as
standard LDIF, with an additional comment header giving the timestamp
of the change and the identity of the user making the change.

%description overlay-auditlog -l pl.UTF-8
Nakładka Audit Logging może być używana do zapisywania wszystkich
zmian w danej bazie danych do podanego pliki loga. Zmiany są logowane
jako standardowy LDIF z dodatkowym nagłówkiem komentarza podającym
czas zmiany i identyfikującym użytkownika, który dokonał zmiany.

%package overlay-collect
Summary:	Collect overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka collect dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-collect
The collect overlay is used to provide a relatively coarse
implementation of RFC 3671 collective attributes.

%description overlay-collect -l pl.UTF-8
Nakładka collect jest używana do dostarczenia atrybutów wg RFC 3671.

%package overlay-constraint
Summary:	Constraint overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka constraint dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-constraint
This overlay limits the values which can be placed into an attribute,
over and above the limits placed by the schema. It traps only LDAP
adds and modify commands (and only seeks to control the add and modify
value mods of a modify)

%description overlay-constraint -l pl.UTF-8
Ta nakładka ogranicza wartości, które można umieszczać w atrybucie,
ponad limity umieszczone w schemacie. Przechwytuje jedynie polecenia
dodawania i modyfikowania LDAP (i kontroluje tylko wartości dodawania
i modyfikowania).

%package overlay-dds
Summary:	Dynamic Directory Services overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka DDS dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-dds
The dds overlay implements dynamic objects as per RFC 2589. The name
dds stands for Dynamic Directory Services. It allows to define dynamic
objects, characterized by the dynamicObject objectClass.

%description overlay-dds -l pl.UTF-8
Nakładka dds implementuje obiekty dynamicznie zgodnie z RFC 2589.
Nazwa dds oznacza Dynamic Directory Services (dynamiczne usługi
katalogowe). Pozwala definiować obiekty dynamiczne, opisywane przez
klasę dynamicObject objectClass.

%package overlay-deref
Summary:	Dereference Control overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka Dereference Control dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-deref
Dereference Control overlay for OpenLDAP server.

%description overlay-deref -l pl.UTF-8
Nakładka Dereference Control dla serwera OpenLDAP.

%package overlay-dyngroup
Summary:	Dyngroup overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka dynamicznych grup dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-dyngroup
This overlay extends the Compare operation to detect members of a
dynamic group. It has no effect on any other operations. It must be
configured with a pair of attributes to trigger on, e.g. attrpair
member memberURL will cause compares on "member" to trigger a compare
on "memberURL".

%description overlay-dyngroup -l pl.UTF-8
Ta nakładka rozszerza operację Compare, aby wykrywała członików grupy
dynamicznej. Nie wpływa na żadne inne operacje. Musi być
skonfigurowana parą atrybutów, które mają ją wyzwalać, np. attrpair
member memberURL spowoduje, że porównania na "memberu" wyzwolą
porównania na "memberURL".

%package overlay-dynlist
Summary:	Dynnamic list overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka dynamicznych list dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-dynlist
The dynlist overlay allows expansion of dynamic groups and more.

%description overlay-dynlist -l pl.UTF-8
Nakładka dynlist pozwala na rozwijanie dynamicznych grup i inne
operacje.

%package overlay-memberof
Summary:	Reverse Group Membership overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka memberof dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-memberof
The memberof overlay allows automatic reverse group membership
maintenance. Any time a group entry is modified, its members are
modified as appropriate in order to keep a DN-valued "is member of"
attribute updated with the DN of the group.

%description overlay-memberof -l pl.UTF-8
Nakładka memberof pozwala automatycznie utrzymywać odwrotne
członkostwo grup. Zawsze przy modyfikacji wpisu grupy jej członkowie
są modyfikowani w odpowiedniej kolejności, aby utrzymać opisany w DN
atrybut "jest członkiem grupy", uaktualniany wraz z DN grupy.

%package overlay-nssov
Summary:	NSS overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka NSS dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}
Conflicts:	openldap-schema-pam_ldap
Provides:	nslcd

%description overlay-nssov
The nssov overlay handles NSS lookup requests through a local Unix
Domain socket. It uses the same IPC protocol as Arthur de Jong's
nss-ldapd.

%description overlay-nssov -l pl.UTF-8
Nakładka nssov obsługuje żądania wyszukiwania NSS poprzez lokalne
gniazdo Unix Domain. Używa tego samego protokołu IPC, co nss-ldapd
Arthura de Jong.

%package overlay-pcache
Summary:	Proxy cache overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka proxy cache dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-pcache
The proxy cache overlay allows caching of LDAP search requests
(queries) in a local database.

%description overlay-pcache -l pl.UTF-8
Nakładka proxy cache pozwalająca buforować zapytania LDAP w lokalnej
bazie.

%package overlay-ppolicy
Summary:	Password Policy overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka do polityki haseł dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-ppolicy
The ppolicy overlay is an implementation of the most recent IETF
Password Policy proposal for LDAP. When instantiated, it intercepts,
decodes and applies specific password policy controls to overall use
of a backend database, changes to user password fields, etc.

%description overlay-ppolicy -l pl.UTF-8
Nakładka ppolicy jest implementacją najnowszej propozycji IETF
Password Policy dla LDAP. Kiedy zostanie użyta, przechwytuje, dekoduje
i aplikuje określone regulacje polityki haseł do ogólnego używania
bazy danych, zmiany pól haseł użytkowników itp.

%package overlay-refint
Summary:	Referential Integrity overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka sprawdzają integralność odwołań dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-refint
The Referential Integrity overlay can be used to maintain the
cohesiveness of a schema which utilizes reference attributes.

%description overlay-refint -l pl.UTF-8
Nakładka Referential Integrity może być używana do utrzymywania
spójności schematu wykorzystującego atrybuty referencji.

%package overlay-retcode
Summary:	Return code overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka obsługująca zwracane wartości dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-retcode
The retcode overlay to slapd is useful to test the behavior of clients
when server-generated erroneous and/or unusual responses occur, e.g.
error codes, referrals, excessive response times and so on.

%description overlay-retcode -l pl.UTF-8
Nakładka retcode dla slapd jest przydatna do sprawdzania zachowania
klientów w przypadku wystąpienia wygenerowanych przez serwer błędnych
i/lub nienormalnych odpowiedzi, np. kodów błędów, odniesień, długich
czasów odpowiedzi itp.

%package overlay-rwm
Summary:	Rewrite/remap overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka mapująca dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-rwm
The rwm overlay performs basic DN/data rewrite and
object-Class/attributeType mapping. Its usage is mostly intended to
provide virtual views of existing data either remotely, in conjunction
with the proxy backend or locally, in conjunction with the relay
backend.

%description overlay-rwm -l pl.UTF-8
Nakładka rwm wykonuje podstawowe przepisywanie DN na dane i
odwzorowywanie klas obiektów na attributeType. Jej zastosowania to
przede wszystkim dostarczanie wirtualnych widoków danych istniejących
albo zdalnie, w połączeniu z backendem proxy, albo lokalnie, w
połączeniu z backendem relay.

%package overlay-seqmod
Summary:	Sequenced modifies overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka seqmod dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-seqmod
This overlay serializes concurrent attempts to modify a single entry.

%description overlay-seqmod -l pl.UTF-8
Ta nakładka serializuje jednoczesne próby zmodyfikowania tego samego
wpisu.

%package overlay-smbk5pwd
Summary:	smbk5pwd overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka smbk5pwd dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-smbk5pwd
smbk5pwd overlay extends the PasswordModify Extended Operation to
update Kerberos keys and Samba password hashes for an LDAP user.

%description overlay-smbk5pwd -l pl.UTF-8
Nakładka smbk5pwd rozszerza rozszerzoną operację PasswordModify o
uaktualnianie kluczy Kerberosa i skrótów haseł Samby dla użytkownika
LDAP.

%package overlay-sssvlv
Summary:	Server Side Sorting and Virtual List View overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka sortowania po stronie serwera i wirtualnego widoku list dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-sssvlv
This overlay implements the LDAP Server Side Sorting (RFC2891) control
as well as the Virtual List View control. It also replaces the default
implementation of the LDAP PagedResults (RFC2696) control, to ensure
that it works with Sorting. The overlay can be used with any backend
or globally for all backends.

%description overlay-sssvlv -l pl.UTF-8
Ta nakładka implementuje sortowanie po stronie serwera (Server Side
Sorting, RFC2891) oraz wirtualne widoki list (Virtual List View).
Zastępuje również domyślną implementację stronnicowanych wyników
(PagedResults, RFC2696), aby zapewnić ich działanie z sortowaniem.
Nakładka może być użyta w dowolnym backendzie albo globalnie dla
wszystkich backendów.

%package overlay-syncprov
Summary:	Syncrepl Provider overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka Syncrepl Provider dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-syncprov
The Syncrepl Provider overlay implements the provider-side support for
syncrepl replication, including persistent search functionality. The
overlay can be used with any backend that maintains entryCSN and
entryUUID attributes for its entries. It also creates a contextCSN
attribute in the root entry of the database.

%description overlay-syncprov -l pl.UTF-8
Nakładka SyncRepl Provider implementuje obsługę replikacji syncrepl po
stronie dostarczyciela, włącznie z ciągłością funkcjonalności
wyszukiwania. Nakładka może być używana z dowolnym backendem
utrzymującym atrybuty entryCSN i entryUUID dla swoich wpisów. Tworzy
także atrybut contextCSN w głównym elemencie bazy.

%package overlay-translucent
Summary:	Translucent Proxy overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka Translucent Proxy dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-translucent
The Translucent Proxy overlay can be used with a backend database such
as slapd-bdb(5) to create a "translucent proxy". Entries retrieved
from a remote LDAP server may have some or all attributes overridden,
or new attributes added, by entries in the local database before being
presented to the client.

%description overlay-translucent -l pl.UTF-8
Nakładka Translucent Proxy może być używana wraz z bazą danych taką
jak slapd-bdb(5) do stworzenia "przezroczystego proxy". Wpisy
otrzymane ze zdalnego serwera LDAP mogą mieć nadpisane niektóre lub
wszystkie atrybuty, albo dodane nowe atrybuty poprzez wpisy w lokalnej
bazie danych przed przekazaniem do klienta.

%package overlay-unique
Summary:	Uniqueness overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka sprawdzająca unikatowość dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-unique
The Attribute Uniqueness overlay can be used to enforce the uniqueness
of some or all attributes within a subtree.

%description overlay-unique -l pl.UTF-8
Nakładka sprawdzająca unikatowość służy do wymuszania unikatowości
atrybutów w poddrzewie LDAP.

%package overlay-valsort
Summary:	Valsort overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka valsort dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-valsort
This overlay sorts the values of multi-valued attributes when
returning them in a search response.

%description overlay-valsort -l pl.UTF-8
Ta nakładka sortuje wartości wielowartościowych atrybutów przy
zwracaniu ich jako odpowiedź przy wyszukiwaniu.

%package servers
Summary:	LDAP servers
Summary(pl.UTF-8):	Serwery LDAP
Summary(pt_BR.UTF-8):	Arquivos para o servidor OpenLDAP
Summary(ru.UTF-8):	Сервера LDAP
Summary(uk.UTF-8):	Сервера LDAP
Group:		Networking/Daemons
Requires(post):	/usr/sbin/usermod
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getent
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	textutils
Requires:	%{name} = %{version}-%{release}
Requires:	/sbin/chkconfig
Requires:	rc-scripts
Requires:	uname(release) >= 2.6
Suggests:	%{name}-backend-hdb = %{version}-%{release}
Provides:	group(slapd)
Provides:	user(slapd)
Obsoletes:	openldap-backend-ldbm
Obsoletes:	openldap-overlay-denyop
Obsoletes:	openldap-overlay-glue
Obsoletes:	openldap-overlay-lastmod
Conflicts:	kernel24
Conflicts:	kernel24-smp
# for the posttrans scriptlet, conflicts because in vserver environment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2

%description servers
The openldap-server package contains the slapd daemon which is
responsible for handling the database and client queries.

Install this package if you want to setup an OpenLDAP-2.x server.

You will also need some backend for server, so install some
openldap-backend package. The bdb backend is recommended.

%description servers -l pl.UTF-8
Ten pakiet zawiera demona slapd odpowiadającego za obsługę bazy danych
i zapytania klientów.

Aby uruchomić serwer OpenLDAP 2.x należy zainstalować ten pakiet.

Potrzebny też jest jakiś backend dla serwera, dlatego należy
zainstalować odpowiedni pakiet openldap-backend. Zalecany jest backend
bdb.

%description servers -l pt_BR.UTF-8
O pacote openldap-server contém o servidor slapd que é responsável por
receber as requisições dos clientes e por manter a base de dados do
diretório.

O conjunto completo contém:
- servidor LDAP (slapd),

Instale este pacote se você desejar executar um servidor OpenLDAP.

%description servers -l ru.UTF-8
Сервера (демоны), поставляемые с LDAP.

%description servers -l uk.UTF-8
Сервера (демони), що поставляються з LDAP.

%prep
%setup -q -c %{!?with_system_db:-a1}
cd %{name}-%{version}
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
%patch12 -p1
%patch13 -p1
%if %{with krb5}
%patch14 -p1
%else
%patch18 -p1
%endif
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch19 -p0

ln -s ../../../contrib/slapd-modules/smbk5pwd/smbk5pwd.c servers/slapd/overlays/smbk5pwd.c
cd ..

%if %{without system_db}
install -d db-%{db_version}/build-rpm
%endif

%if %{with exchange}
# Set up a build tree for a static version of libldap with the hooks for the
# non-standard NTLM bind type which is needed to connect to Win2k GC servers
# (Win2k3 supports SASL with DIGEST-MD5, so this shouldn't be needed for those
# servers, though as of version 1.4 the exchange doesn't try SASL first).
if ! cp -al %{name}-%{version} evo-%{name}-%{version} ; then
	rm -fr evo-%{name}-%{version}
	cp -a %{name}-%{version} evo-%{name}-%{version}
fi
cd evo-%{name}-%{version}
%patch100 -p0
%endif

%build
%if %{without system_db}
dbdir=`pwd`/db-instroot
cd db-%{db_version}/build-rpm

CC="%{__cc}"
CXX="%{__cxx}"
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
LDFLAGS="%{rpmcflags} %{rpmldflags}"
export CC CXX CFLAGS CXXFLAGS LDFLAGS

../dist/%configure \
	--disable-compat185 \
	--disable-dump185 \
	--disable-java \
	--disable-tcl \
	--disable-cxx \
	--with-pic \
	--disable-static \
	--enable-shared \
	--with-uniquename=_openldap \
	--prefix=${dbdir} \
	--exec-prefix=${dbdir} \
	--bindir=${dbdir}/bin \
	--includedir=${dbdir}/include \
	--libdir=${dbdir}/%{_lib}

%{__make} \
	libdb_base=libslapd_db \
	libso_base=libslapd_db
%{__make} install \
	libdb_base=libslapd_db \
	libso_base=libslapd_db \
	strip="false"
ln -sf libslapd_db.so ${dbdir}/%{_lib}/${subdir}/libdb.so

cd ../..
%endif

cd %{name}-%{version}

CPPFLAGS="%{!?with_system_db:-I${dbdir}/include -D__lock_getlocker=__lock_getlocker_openldap }-I/usr/include/ncurses"
CFLAGS="%{rpmcflags} $CPPFLAGS -D_REENTRANT -fPIC -D_GNU_SOURCE"
CXXFLAGS="%{rpmcflags} $CPPFLAGS -D_REENTRANT -fPIC"
LDFLAGS="%{rpmcflags} %{rpmldflags}%{!?with_system_db: -L${dbdir}/%{_lib}}"
export CFLAGS CPPFLAGS CXXFLAGS LDFLAGS
%if %{without system_db}
export LD_LIBRARY_PATH=${dbdir}/%{_lib}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%endif

%{__libtoolize} --install
%{__aclocal}
%{__autoconf}
%configure \
	--enable-dynamic \
	--enable-syslog \
	--enable-ipv6 \
	--enable-local \
	--enable-slapd \
	--enable-dynacl \
	--enable-aci \
	--enable-crypt \
	--enable-lmpasswd \
	--enable-modules \
	--enable-rewrite \
	--enable-rlookups \
	--enable-slapi \
%if %{with sasl}
	--with-cyrus-sasl \
	--enable-spasswd \
%else
	--without-cyrus-sasl \
%endif
%if %{with slp}
	--enable-slp \
%else
	--disable-slp \
%endif
	--enable-wrappers \
	--enable-bdb=mod \
	--enable-dnssrv=mod \
	--enable-hdb=mod \
	--enable-ldap=mod \
	--enable-meta=mod \
	--enable-monitor=mod \
%if %{with ndb}
	--enable-ndb=mod \
%endif
	--enable-null \
	--enable-passwd=mod \
%if %{with perl}
	--enable-perl=mod \
%endif
	--enable-relay=mod \
	--enable-shell=mod \
	--enable-sock=mod \
%if %{with odbc}
	--enable-sql=mod \
	--with-odbc=unixodbc \
%endif
	--enable-overlays=mod \
	--with-threads \
	--with-tls \
	--with-yielding-select \
	--with-gssapi \
	--with-mp=longlong

%{__make} -j1 depend
%{__make}

%{__make} -j1 -C contrib/slapd-modules/nssov \
	libdir=%{_libdir}/openldap \
	CC="%{__cc}" \
	OPT="%{rpmcflags} %{rpmldflags} -L../../../libraries/libldap_r" \
	nssov.la

install -d libs
for d in liblber libldap libldap_r ; do
	ln -sf ../libraries/$d/.libs/$d.la libs/$d.la
	ln -sf ../libraries/$d/.libs/$d.so libs/$d.so
done

__topdir=`pwd`
%if %{with sasl}
cd contrib/ldapc++
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-libldap=$__topdir/libs \
	--with-ldap-includes=$__topdir/include
%{__make}
%endif

%if %{with exchange}
# Build evolution-specific clients just as we would normal clients,
# except with a different installation directory in mind
# and no shared libraries.
cd ../../../evo-%{name}-%{version}

%{__libtoolize} --install
%{__aclocal}
%{__autoconf}
%configure \
	--includedir=%{evolution_exchange_includedir} \
	--libdir=%{evolution_exchange_libdir} \
	--disable-dynamic \
	--disable-slapd \
	--disable-shared \
	--enable-static \
	--enable-syslog \
	--enable-ipv6 \
	--enable-local \
	--enable-dynacl \
	--enable-aci \
	--enable-crypt \
	--enable-lmpasswd \
	--enable-modules \
	--enable-rewrite \
	--enable-rlookups \
	--enable-slapi \
%if %{with sasl}
	--with-cyrus-sasl \
	--enable-spasswd \
%else
	--without-cyrus-sasl \
%endif
%if %{with slp}
	--enable-slp \
%else
	--disable-slp \
%endif
	--enable-wrappers \
	--enable-backends=no \
	--enable-overlays=no \
%if %{with odbc}
	--with-odbc=unixodbc \
%endif
	--with-threads \
	--with-tls \
	--with-yielding-select \
	--with-gssapi \
	--with-mp=longlong

%{__make} -j1 depend
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{sysconfig,rc.d/init.d},/var/lib/openldap-data} \
	$RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{schemadir}} \
	$RPM_BUILD_ROOT/var/run/{slapd,nslcd}

%if %{with exchange}
# Install evolution hack first and remove everything but devel stuff
%{__make} -C evo-%{name}-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT{%{_sysconfdir}/openldap,%{_bindir},%{_mandir}}/*
install %{SOURCE100} $RPM_BUILD_ROOT%{evolution_exchange_prefix}/README.evolution
%endif

%if %{without system_db}
dbdir=`pwd`/db-instroot
cd db-instroot
install %{_lib}/libslapd_db-*.*.so $RPM_BUILD_ROOT%{_libdir}
cd bin
for binary in db_* ; do
	install -m755 ${binary} $RPM_BUILD_ROOT%{_sbindir}/slapd_${binary}
done

cd ../..
%endif

cd %{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/openldap/*.a

%{__make} -C contrib/slapd-modules/nssov install \
	moduledir=%{_libdir}/openldap \
	schemadir=%{schemadir} \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/slapd-modules/nssov/slapo-nssov.5 $RPM_BUILD_ROOT%{_mandir}/man5

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/ldap

# Config for openldap library
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/openldap/ldap.conf
# Config for nss_ldap and pam_ldap
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/ldap.conf

echo "localhost" > $RPM_BUILD_ROOT%{_sysconfdir}/openldap/ldapserver

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/openldap/{*.{default,example},schema/README}

# Standard schemas should not be changed by users
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/* $RPM_BUILD_ROOT%{_datadir}/openldap/schema

# create slapd.access.conf
echo "# This is a good place to put slapd access-control directives" > \
	$RPM_BUILD_ROOT%{_sysconfdir}/openldap/slapd.access.conf

# create local.schema
echo "# This is a good place to put your schema definitions " > \
	$RPM_BUILD_ROOT%{_sysconfdir}/openldap/schema/local.schema

%if %{with sasl}
%{__make} -C contrib/ldapc++ install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{without system_db}
find $RPM_BUILD_ROOT -name \*.la | xargs sed -i -e "s|-L${dbdir}/%{_lib}||g"
%endif

# files for -headers subpackage
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}/ac
cp -a include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}
cp -a include/ac/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/ac

# remove headers, that are provided by -devel package
for I in $RPM_BUILD_ROOT%{_includedir}/*.h; do
  rm $RPM_BUILD_ROOT%{_includedir}/%{name}/$(basename $I)
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs	-p /sbin/ldconfig
%postun	libs	-p /sbin/ldconfig

%post	ldapc++	-p /sbin/ldconfig
%postun	ldapc++	-p /sbin/ldconfig

%pre servers
%groupadd -P %{name}-servers -g 93 slapd
%useradd -P %{name}-servers -u 93 -s /bin/false -g slapd -c "OpenLDAP server" -d /var/lib/openldap-data slapd

%post servers
/sbin/chkconfig --add ldap

# minimizing restarts logics. we restart server:
#
# 1. at the end of transaction. (posttrans, feature from rpm 4.4.2)
# 2. first install of module (post: $1 == 1)
# 2. uninstall of module (postun: $1 == 0)
#
# the strict internal deps between modules and
# server package are very important for all this to work.

%posttrans servers
%service ldap restart "OpenLDAP server"

%preun servers
if [ "$1" = "0" ] ; then
	%service ldap stop
	/sbin/chkconfig --del ldap || :
fi

%postun servers
if [ "$1" = "0" ]; then
	%userremove slapd
	%groupremove slapd
fi

%define	ldap_module_add() \
%{__sed} -i -e 's/^#[[:blank:]]*moduleload[[:blank:]]\\+%1[[:blank:]]*$/moduleload	%1/' %{_sysconfdir}/openldap/slapd.conf \
if [ "$1" = "1" ]; then \
	%service ldap restart "OpenLDAP server" \
fi \
%{nil}

%define	ldap_module_remove() \
if [ "$1" = "0" ]; then \
	%{__sed} -i -e 's/^[[:blank:]]*moduleload[[:blank:]]\\+%1[[:blank:]]*$/# moduleload	%1/' %{_sysconfdir}/openldap/slapd.conf \
	%service ldap restart "OpenLDAP server" \
fi \
%{nil}

%post backend-bdb
%ldap_module_add back_bdb.la

%preun backend-bdb
%ldap_module_remove back_bdb.la

%post backend-dnssrv
%ldap_module_add back_dnssrv.la

%preun backend-dnssrv
%ldap_module_remove back_dnssrv.la

%post backend-hdb
%ldap_module_add back_hdb.la

%preun backend-hdb
%ldap_module_remove back_hdb.la

%post backend-ldap
%ldap_module_add back_ldap.la

%preun backend-ldap
%ldap_module_remove back_ldap.la

%post backend-meta
%ldap_module_add back_meta.la

%preun backend-meta
%ldap_module_remove back_meta.la

%post backend-monitor
%ldap_module_add back_monitor.la

%preun backend-monitor
%ldap_module_remove back_monitor.la

%post backend-ndb
%ldap_module_add back_ndb.la

%preun backend-ndb
%ldap_module_remove back_ndb.la

%post backend-passwd
%ldap_module_add back_passwd.la

%preun backend-passwd
%ldap_module_remove back_passwd.la

%post backend-perl
%ldap_module_add back_perl.la

%preun backend-perl
%ldap_module_remove back_perl.la

%post backend-relay
%ldap_module_add back_relay.la

%preun backend-relay
%ldap_module_remove back_relay.la

%post backend-shell
%ldap_module_add back_shell.la

%preun backend-shell
%ldap_module_remove back_shell.la

%post backend-sock
%ldap_module_add back_sock.la

%preun backend-sock
%ldap_module_remove back_sock.la

%post backend-sql
%ldap_module_add back_sql.la

%preun backend-sql
%ldap_module_remove back_sql.la

%post overlay-pcache
%ldap_module_add pcache.la

%preun overlay-pcache
%ldap_module_remove pcache.la

%post overlay-accesslog
%ldap_module_add accesslog.la

%preun overlay-accesslog
%ldap_module_remove accesslog.la

%post overlay-auditlog
%ldap_module_add auditlog.la

%preun overlay-auditlog
%ldap_module_remove auditlog.la

%post overlay-collect
%ldap_module_add collect.la

%preun overlay-collect
%ldap_module_remove collect.la

%post overlay-constraint
%ldap_module_add constraint.la

%preun overlay-constraint
%ldap_module_remove constraint.la

%post overlay-dds
%ldap_module_add dds.la

%preun overlay-dds
%ldap_module_remove dds.la

%post overlay-deref
%ldap_module_add deref.la

%preun overlay-deref
%ldap_module_remove deref.la

%post overlay-dyngroup
%ldap_module_add dyngroup.la

%preun overlay-dyngroup
%ldap_module_remove dyngroup.la

%post overlay-dynlist
%ldap_module_add dynlist.la

%preun overlay-dynlist
%ldap_module_remove dynlist.la

%post overlay-memberof
%ldap_module_add memberof.la

%preun overlay-memberof
%ldap_module_remove memberof.la

%post overlay-nssov
%ldap_module_add nssov.la
%openldap_schema_register %{schemadir}/ldapns.schema
%service -q ldap restart

%preun overlay-nssov
%ldap_module_remove nssov.la

%postun overlay-nssov
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/ldapns.schema
	%service -q ldap restart
fi

%post overlay-ppolicy
%ldap_module_add ppolicy.la

%preun overlay-ppolicy
%ldap_module_remove ppolicy.la

%post overlay-refint
%ldap_module_add refint.la

%preun overlay-refint
%ldap_module_remove refint.la

%post overlay-retcode
%ldap_module_add retcode.la

%preun overlay-retcode
%ldap_module_remove retcode.la

%post overlay-rwm
%ldap_module_add rwm.la

%preun overlay-rwm
%ldap_module_remove rwm.la

%post overlay-smbk5pwd
%ldap_module_add smbk5pwd.la

%preun overlay-smbk5pwd
%ldap_module_remove smbk5pwd.la

%post overlay-seqmod
%ldap_module_add seqmod.la

%preun overlay-seqmod
%ldap_module_remove seqmod.la

%post overlay-sssvlv
%ldap_module_add sssvlv.la

%preun overlay-sssvlv
%ldap_module_remove sssvlv.la

%post overlay-syncprov
%ldap_module_add syncprov.la

%preun overlay-syncprov
%ldap_module_remove syncprov.la

%post overlay-translucent
%ldap_module_add translucent.la

%preun overlay-translucent
%ldap_module_remove translucent.la

%post overlay-unique
%ldap_module_add unique.la

%preun overlay-unique
%ldap_module_remove unique.la

%post overlay-valsort
%ldap_module_add valsort.la

%preun overlay-valsort
%ldap_module_remove valsort.la

%triggerpostun servers -- openldap-servers < 2.1.12
if [ "`/usr/bin/getent passwd slapd | cut -d: -f6`" = "/var/lib/openldap-ldbm" ]; then
	/usr/sbin/usermod -d /var/lib/openldap-data slapd
fi

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/{ANNOUNCEMENT,CHANGES,COPYRIGHT,README,LICENSE}
%doc %{name}-%{version}/doc/{drafts,rfc}
%dir %{_sysconfdir}/openldap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/ldapserver
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/ldap.conf
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/openldap
%{_mandir}/man1/ldap*.1*
%{_mandir}/man5/ldap.conf.5*
%{_mandir}/man5/ldif.5*

%files nss-config
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ldap.conf

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblber-2.4.so.*.*.*
%attr(755,root,root) %{_libdir}/libldap-2.4.so.*.*.*
%attr(755,root,root) %{_libdir}/libldap_r-2.4.so.*.*.*
%attr(755,root,root) %{_libdir}/libslapi-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblber-2.4.so.2
%attr(755,root,root) %ghost %{_libdir}/libldap-2.4.so.2
%attr(755,root,root) %ghost %{_libdir}/libldap_r-2.4.so.2
%attr(755,root,root) %ghost %{_libdir}/libslapi-2.4.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblber.so
%attr(755,root,root) %{_libdir}/libldap.so
%attr(755,root,root) %{_libdir}/libldap_r.so
%attr(755,root,root) %{_libdir}/libslapi.so
%{_libdir}/liblber.la
%{_libdir}/libldap.la
%{_libdir}/libldap_r.la
%{_libdir}/libslapi.la
%{_includedir}/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/liblber.a
%{_libdir}/libldap.a
%{_libdir}/libldap_r.a
%{_libdir}/libslapi.a

%files headers
%defattr(644,root,root,755)
%{_includedir}/%{name}

%if %{with exchange}
%files evolution-devel
%defattr(644,root,root,755)
%dir %{evolution_exchange_prefix}
%dir %{evolution_exchange_includedir}
%dir %{evolution_exchange_libdir}
%{evolution_exchange_prefix}/README*
%{evolution_exchange_includedir}/*.h
%{evolution_exchange_libdir}/*.a
%endif

%files ldapc++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libldapcpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libldapcpp.so.0

%files ldapc++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libldapcpp.so
%{_libdir}/libldapcpp.la
%{_includedir}/ldapc++

%files ldapc++-static
%defattr(644,root,root,755)
%{_libdir}/libldapcpp.a

%files backend-bdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_bdb*.so*
%{_libdir}/openldap/back_bdb.la
%{_mandir}/man5/slapd-bdb.5*

%files backend-dnssrv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_dnssrv*.so*
%{_libdir}/openldap/back_dnssrv.la
%{_mandir}/man5/slapd-dnssrv.5*

%files backend-hdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_hdb*.so*
%{_libdir}/openldap/back_hdb.la
%{_mandir}/man5/slapd-hdb.5*

%files backend-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_ldap*.so*
%{_libdir}/openldap/back_ldap.la
%{_mandir}/man5/slapd-ldap.5*
%{_mandir}/man5/slapo-chain.5*
%{_mandir}/man5/slapo-pbind.5*

%files backend-meta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_meta*.so*
%{_libdir}/openldap/back_meta.la
%{_mandir}/man5/slapd-meta.5*

%files backend-monitor
%defattr(644,root,root,755)
%doc %{name}-%{version}/servers/slapd/back-monitor/README
%attr(755,root,root) %{_libdir}/openldap/back_monitor*.so*
%{_libdir}/openldap/back_monitor.la
%{_mandir}/man5/slapd-monitor.5*

%if %{with ndb}
%files backend-ndb
%defattr(644,root,root,755)
%doc %{name}-%{version}/servers/slapd/back-ndb/README
%attr(755,root,root) %{_libdir}/openldap/back_ndb*.so*
%{_libdir}/openldap/back_ndb.la
%{_mandir}/man5/slapd-ndb.5*
%endif

%files backend-passwd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_passwd*.so*
%{_libdir}/openldap/back_passwd.la
%{_mandir}/man5/slapd-passwd.5*

%if %{with perl}
%files backend-perl
%defattr(644,root,root,755)
%doc %{name}-%{version}/servers/slapd/back-perl/*.pm
%attr(755,root,root) %{_libdir}/openldap/back_perl*.so*
%{_libdir}/openldap/back_perl.la
%{_mandir}/man5/slapd-perl.5*
%endif

%files backend-relay
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_relay*.so*
%{_libdir}/openldap/back_relay.la
%{_mandir}/man5/slapd-relay.5*

%files backend-shell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_shell*.so*
%{_libdir}/openldap/back_shell.la
%{_mandir}/man5/slapd-shell.5*

%files backend-sock
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_sock*.so*
%{_libdir}/openldap/back_sock.la
%{_mandir}/man5/slapd-sock.5*

%if %{with odbc}
%files backend-sql
%defattr(644,root,root,755)
%doc %{name}-%{version}/servers/slapd/back-sql/docs/*
%doc %{name}-%{version}/servers/slapd/back-sql/rdbms_depend
%attr(755,root,root) %{_libdir}/openldap/back_sql*.so*
%{_libdir}/openldap/back_sql.la
%{_mandir}/man5/slapd-sql.5*
%endif

%files overlay-accesslog
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/accesslog*.so*
%{_libdir}/openldap/accesslog.la
%{_mandir}/man5/slapo-accesslog.5*

%files overlay-auditlog
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/auditlog*.so*
%{_libdir}/openldap/auditlog.la
%{_mandir}/man5/slapo-auditlog.5*

%files overlay-collect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/collect*.so*
%{_libdir}/openldap/collect.la
%{_mandir}/man5/slapo-collect.5*

%files overlay-constraint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/constraint*.so*
%{_libdir}/openldap/constraint.la
%{_mandir}/man5/slapo-constraint.5*

%files overlay-dds
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/dds*.so*
%{_libdir}/openldap/dds.la
%{_mandir}/man5/slapo-dds.5*

%files overlay-deref
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/deref*.so*
%{_libdir}/openldap/deref.la

%files overlay-dyngroup
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/dyngroup*.so*
%{_libdir}/openldap/dyngroup.la
%{_mandir}/man5/slapo-dyngroup.5*

%files overlay-dynlist
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/dynlist*.so*
%{_libdir}/openldap/dynlist.la
%{_mandir}/man5/slapo-dynlist.5*

%files overlay-memberof
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/memberof*.so*
%{_libdir}/openldap/memberof.la
%{_mandir}/man5/slapo-memberof.5*

%files overlay-nssov
%defattr(644,root,root,755)
%doc %{name}-%{version}/contrib/slapd-modules/nssov/README
%attr(755,root,root) %{_libdir}/openldap/nssov*.so*
%{_libdir}/openldap/nssov.la
%{schemadir}/ldapns.schema
%{_mandir}/man5/slapo-nssov.5*
%attr(755,slapd,slapd) %dir /var/run/nslcd

%files overlay-pcache
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/pcache*.so*
%{_libdir}/openldap/pcache.la
%{_mandir}/man5/slapo-pcache.5*

%files overlay-ppolicy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/ppolicy*.so*
%{_libdir}/openldap/ppolicy.la
%{_mandir}/man5/slapo-ppolicy.5*

%files overlay-refint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/refint*.so*
%{_libdir}/openldap/refint.la
%{_mandir}/man5/slapo-refint.5*

%files overlay-retcode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/retcode*.so*
%{_libdir}/openldap/retcode.la
%{_mandir}/man5/slapo-retcode.5*

%files overlay-rwm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/rwm*.so*
%{_libdir}/openldap/rwm.la
%{_mandir}/man5/slapo-rwm.5*

%files overlay-smbk5pwd
%defattr(644,root,root,755)
%doc %{name}-%{version}/contrib/slapd-modules/smbk5pwd/README
%attr(755,root,root) %{_libdir}/openldap/smbk5pwd*.so*
%{_libdir}/openldap/smbk5pwd.la

%files overlay-seqmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/seqmod*.so*
%{_libdir}/openldap/seqmod.la

%files overlay-sssvlv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/sssvlv*.so*
%{_libdir}/openldap/sssvlv.la
%{_mandir}/man5/slapo-sssvlv.5*

%files overlay-syncprov
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/syncprov*.so*
%{_libdir}/openldap/syncprov.la
%{_mandir}/man5/slapo-syncprov.5*

%files overlay-translucent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/translucent*.so*
%{_libdir}/openldap/translucent.la
%{_mandir}/man5/slapo-translucent.5*

%files overlay-unique
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/unique*.so*
%{_libdir}/openldap/unique.la
%{_mandir}/man5/slapo-unique.5*

%files overlay-valsort
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/valsort*.so*
%{_libdir}/openldap/valsort.la
%{_mandir}/man5/slapo-valsort.5*

%files servers
%defattr(644,root,root,755)
%if %{without system_db}
# not used by slapd directly, but by two different backends (bdb,hdb), so include here
%doc db-%{db_version}/LICENSE
%attr(755,root,root) %{_libdir}/libslapd_db-4.6.so
%endif
%dir %{_sysconfdir}/openldap/schema
%attr(640,root,slapd) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/slapd.conf
%attr(640,root,slapd) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/slapd.access.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/schema/*.schema
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ldap
%attr(754,root,root) /etc/rc.d/init.d/ldap
%attr(770,root,slapd) %{_var}/run/slapd
%dir %attr(770,root,slapd) %{_localstatedir}/openldap-data
%attr(660,root,slapd) %{_localstatedir}/openldap-data/*
%dir %{schemadir}
%{schemadir}/*.ldif
%{schemadir}/*.schema
%exclude %{schemadir}/ldapns.schema
%dir %{_libdir}/openldap
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man5/slapd.*.5*
%{_mandir}/man5/slapd-config.5*
%{_mandir}/man5/slapd-ldbm.5*
%{_mandir}/man5/slapd-ldif.5*
%{_mandir}/man5/slapd-null.5*
%{_mandir}/man8/slap*
