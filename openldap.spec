# TODO:
# - package contribs?
# - complete & validate descriptions
#   /usr/share/man/man5/slapd-tcl.5.gz
#
# Conditional build:
# ldbm_type	- set to needed value (btree<default> or hash)
%bcond_without	odbc	# disable sql backend
%bcond_without	perl	# disable perl backend
%bcond_without	sasl 	# don't build cyrus sasl support
%bcond_without	slp	# disable SLP support

Summary:	Lightweight Directory Access Protocol clients/servers
Summary(es.UTF-8):	Clientes y servidor para LDAP
Summary(pl.UTF-8):	Klienci Lightweight Directory Access Protocol
Summary(pt_BR.UTF-8):	Clientes e servidor para LDAP
Summary(ru.UTF-8):	Образцы клиентов LDAP
Summary(uk.UTF-8):	Зразки клієнтів LDAP
Name:		openldap
Version:	2.3.43
Release:	3
License:	OpenLDAP Public License
Group:		Networking/Daemons
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
# Source0-md5:	1b25281086eb146b8e11ebd33de086dc
Source1:	ldap.init
Source2:	%{name}.sysconfig
Source3:	ldap.conf
Patch0:		%{name}-make_man_link.patch
Patch1:		%{name}-conffile.patch
Patch2:		%{name}-config.patch
Patch3:		%{name}-fast.patch
Patch4:		%{name}-cldap.patch
Patch5:		%{name}-ldapi_FHS.patch
Patch6:		%{name}-install.patch
Patch7:		%{name}-backend_libs.patch
Patch8:		%{name}-perl.patch
Patch9:		%{name}-pic.patch
Patch10:	%{name}-ltinstall-mode.patch
Patch11:	%{name}-whowhere.patch
Patch12:	%{name}-ldaprc.patch
Patch13:	%{name}-setugid.patch
Patch14:	%{name}-nosql.patch
Patch15:	%{name}-link.patch
#Patch12:	%{name}-sendbuf.patch
URL:		http://www.openldap.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_sasl:BuildRequires:	cyrus-sasl-devel >= 2.1.15}
BuildRequires:	db-devel >= 4.2
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libwrap-devel
%{?with_slp:BuildRequires:	openslp-devel}
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_perl:BuildRequires:	perl-devel}
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_odbc:BuildRequires:	unixODBC-devel}
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	openldap-clients
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_check_so	1

%define		_libexecdir	%{_sbindir}
%define		_localstatedir	/var/lib

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

%package backend-ldbm
Summary:	LDBM backend to OpenLDAP server
Summary(pl.UTF-8):	Backend LDBM do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description backend-ldbm
LDBM backend to slapd, the OpenLDAP server.

%description backend-ldbm -l pl.UTF-8
Backend LDBM do slapd - serwera OpenLDAP.

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
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')

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

%package overlay-denyop
Summary:	Denyop overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka zabraniająca wykonania operacji dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-denyop
This overlay provides a quick'n'easy way to deny selected operations
for a database whose backend implements the operations. It is intended
to be less expensive than ACLs because its evaluation occurs before
any backend specific operation is actually even initiated.

%description overlay-denyop -l pl.UTF-8
Ta nakładka udostępnia szybki i łatwy sposób na blokowanie wybranych
operacji dla bazy danych, której backend implementuje te operacje. Ma
być mniej kosztowna niż ACL-e, ponieważ obliczenia zachodzą przed
rozpoczęciem jakichkolwiek operacji specyficznych dla backendu.

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

%package overlay-lastmod
Summary:	Last Modification overlay for OpenLDAP server
Summary(pl.UTF-8):	Nakładka Last Modification dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	sed >= 4.0
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-lastmod
The lastmod overlay creates a service entry rooted at the suffix of
the database it's stacked onto, which holds the DN, the modification
type, the modifiersName and the modifyTimestamp of the last write
operation performed on that database.

%description overlay-lastmod -l pl.UTF-8
Nakładka lastmod tworzy wpis usługi zaczynający się od przyrostka bazy
danych, na której jest oparty, trzymający DN, rodzaj modyfikacji,
modifiersName i modifyTimestamp dla ostatniej operacji zapisu
wykonywanej na tej bazie.

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
Provides:	group(slapd)
Provides:	user(slapd)
Obsoletes:	openldap-overlay-glue
# for the posttrans scriptlet, conflicts because in vserver environment rpm package is not installed.
Conflicts:	rpm < 4.4.2-0.2

%description servers
The openldap-server package has the slapd daemon which is responsible
for handling the database and client queries.

The package includes:
- stand-alone LDAP server (slapd),
- stand-alone LDAP replication server (slurpd)

Install this package if you want to setup an OpenLDAP-2.x server.

You will also need some backend for server, so install some
openldap-backend package. The bdb backend is recommended.

%description servers -l pl.UTF-8
Serwery (demony) które przychodzą z LDAPem.

Pakiet ten zawiera:
- serwer LDAP (slapd)
- serwer replikacji bazy LDAP (slurpd)

Zainstaluj ten pakiet jeżeli potrzebujesz server OpenLDAP-2.x.

Potrzebny też jest jakiś backend dla serwera, dlatego należy
zainstalować odpowiedni pakiet openldap-backend. Zalecany jest backend
bdb.

%description servers -l pt_BR.UTF-8
O pacote openldap-server contém o servidor slapd que é responsável por
receber as requisições dos clientes e por manter a base de dados do
diretório.

O conjunto completo contém:
- servidor LDAP (slapd),
- servidor de replicação (slurpd)

Instale este pacote se você desejar executar um servidor OpenLDAP.

%description servers -l ru.UTF-8
Сервера (демоны), поставляемые с LDAP.

%description servers -l uk.UTF-8
Сервера (демони), що поставляються з LDAP.

%prep
%setup -q
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
%patch14 -p1
%patch15 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	ac_cv_header_sys_epoll_h=no \
	--enable-syslog \
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
%else
	--without-cyrus-sasl \
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
	--enable-bdb=mod \
	--enable-dnssrv=mod \
	--enable-hdb=mod \
	--enable-ldap=mod \
	--enable-overlays=mod \
	--enable-ldbm=mod \
	--enable-ldbm-api=berkeley \
	--enable-ldbm-type%{?ldbm_type:%{ldbm_type}}%{!?ldbm_type:btree} \
	--enable-meta=mod \
	--enable-monitor=mod \
	--enable-null \
	--enable-passwd=mod \
	--enable-relay=mod \
%if %{with perl}
	--enable-perl=mod \
%endif
	--enable-shell=mod \
%if %{with odbc}
	--enable-sql=mod \
%endif
	--enable-slurpd \
	--enable-dynamic

%{__make} -j1 depend
%{__make}
%{__make} -C servers/slapd/overlays syncprov.la

rm -f doc/rfc/rfc*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{sysconfig,rc.d/init.d},/var/lib/openldap-data} \
	$RPM_BUILD_ROOT/var/run/slapd \
	$RPM_BUILD_ROOT%{_datadir}/openldap/schema

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/openldap/*.a

install servers/slapd/overlays/.libs/syncprov{.la,*.so*} $RPM_BUILD_ROOT%{_libdir}/openldap

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ldap

install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/ldap.conf

echo "localhost" > $RPM_BUILD_ROOT%{_sysconfdir}/openldap/ldapserver

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/openldap/{*.{default,example},ldap.conf,schema/README}

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

%post	libs	-p /sbin/ldconfig
%postun	libs	-p /sbin/ldconfig

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

%post backend-ldbm
%ldap_module_add back_ldbm.la

%preun backend-ldbm
%ldap_module_remove back_ldbm.la

%post backend-meta
%ldap_module_add back_meta.la

%preun backend-meta
%ldap_module_remove back_meta.la

%post backend-monitor
%ldap_module_add back_monitor.la

%preun backend-monitor
%ldap_module_remove back_monitor.la

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

%post overlay-denyop
%ldap_module_add denyop.la

%preun overlay-denyop
%ldap_module_remove denyop.la

%post overlay-dyngroup
%ldap_module_add dyngroup.la

%preun overlay-dyngroup
%ldap_module_remove dyngroup.la

%post overlay-dynlist
%ldap_module_add dynlist.la

%preun overlay-dynlist
%ldap_module_remove dynlist.la

%post overlay-lastmod
%ldap_module_add lastmod.la

%preun overlay-lastmod
%ldap_module_remove lastmod.la

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
%doc ANNOUNCEMENT CHANGES COPYRIGHT README LICENSE
%doc doc/{drafts,rfc}
%dir %{_sysconfdir}/openldap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/ldapserver
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ldap.conf
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/openldap
%{_mandir}/man1/ldap*.1*
%{_mandir}/man5/ldap.conf.5*
%{_mandir}/man5/ldif.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblber-2.3.so.*.*.*
%attr(755,root,root) %{_libdir}/libldap-2.3.so.*.*.*
%attr(755,root,root) %{_libdir}/libldap_r-2.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblber-2.3.so.0
%attr(755,root,root) %ghost %{_libdir}/libldap-2.3.so.0
%attr(755,root,root) %ghost %{_libdir}/libldap_r-2.3.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblber.so
%attr(755,root,root) %{_libdir}/libldap.so
%attr(755,root,root) %{_libdir}/libldap_r.so
%{_libdir}/liblber.la
%{_libdir}/libldap.la
%{_libdir}/libldap_r.la
%{_includedir}/*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/liblber.a
%{_libdir}/libldap.a
%{_libdir}/libldap_r.a

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

%files backend-ldbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_ldbm*.so*
%{_libdir}/openldap/back_ldbm.la
%{_mandir}/man5/slapd-ldbm.5*

%files backend-meta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_meta*.so*
%{_libdir}/openldap/back_meta.la
%{_mandir}/man5/slapd-meta.5*

%files backend-monitor
%defattr(644,root,root,755)
%doc servers/slapd/back-monitor/README
%attr(755,root,root) %{_libdir}/openldap/back_monitor*.so*
%{_libdir}/openldap/back_monitor.la
%{_mandir}/man5/slapd-monitor.5*

%files backend-passwd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/back_passwd*.so*
%{_libdir}/openldap/back_passwd.la
%{_mandir}/man5/slapd-passwd.5*

%if %{with perl}
%files backend-perl
%defattr(644,root,root,755)
%doc servers/slapd/back-perl/*.pm
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

%if %{with odbc}
%files backend-sql
%defattr(644,root,root,755)
%doc servers/slapd/back-sql/docs/*
%doc servers/slapd/back-sql/rdbms_depend
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

%files overlay-denyop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/denyop*.so*
%{_libdir}/openldap/denyop.la

%files overlay-dyngroup
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/dyngroup*.so*
%{_libdir}/openldap/dyngroup.la

%files overlay-dynlist
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/dynlist*.so*
%{_libdir}/openldap/dynlist.la
%{_mandir}/man5/slapo-dynlist.5*

%files overlay-lastmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/openldap/lastmod*.so*
%{_libdir}/openldap/lastmod.la
%{_mandir}/man5/slapo-lastmod.5*

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
%dir %{_sysconfdir}/openldap/schema
%attr(640,root,slapd) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/slapd.conf
%attr(640,root,slapd) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/slapd.access.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/openldap/schema/*.schema
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ldap
%attr(754,root,root) /etc/rc.d/init.d/ldap
%attr(770,root,slapd) %{_var}/run/slapd
%attr(770,root,slapd) %{_localstatedir}/openldap-data
%attr(770,root,slapd) %{_localstatedir}/openldap-slurp
%dir %{_datadir}/openldap/schema
%{_datadir}/openldap/schema/*.ldif
%{_datadir}/openldap/schema/*.schema
%dir %{_libdir}/openldap/
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man5/slapd.*.5*
%{_mandir}/man5/slapd-ldif.5*
%{_mandir}/man5/slapd-null.5*
%{_mandir}/man8/*
