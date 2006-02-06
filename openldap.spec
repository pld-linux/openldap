#
# TODO:
# - package contribs?
# - complete & validate descriptions
#
# Conditional build:
# ldbm_type	- set to needed value (btree<default> or hash)
%bcond_without	odbc	# disable sql backend
%bcond_without	perl	# disable perl backend
%bcond_without	sasl 	# don't build cyrus sasl support
%bcond_without	slp	# disable SLP support
#
Summary:	Lightweight Directory Access Protocol clients/servers
Summary(es):	Clientes y servidor para LDAP
Summary(pl):	Klienci Lightweight Directory Access Protocol
Summary(pt_BR):	Clientes e servidor para LDAP
Summary(ru):	ïÂÒÁÚÃÙ ËÌÉÅÎÔÏ× LDAP
Summary(uk):	úÒÁÚËÉ ËÌ¦¤ÎÔ¦× LDAP
Name:		openldap
Version:	2.3.19
Release:	1
License:	OpenLDAP Public License
Group:		Networking/Daemons
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
# Source0-md5:	867ee197df0e4432fa00f2439e6094f6
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
BuildRequires:	rpmbuild(macros) >= 1.202
%{?with_odbc:BuildRequires:	unixODBC-devel}
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	openldap-clients
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
- dodatkowe narzêdzia i przyk³adowe aplikacje klienckie LDAP.

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

%package libs
Summary:	LDAP shared libraries
Summary(pl):	Biblioteki wspó³dzielone LDAP
Group:		Libraries
%{?with_sasl:Requires:	cyrus-sasl >= 2.1.15}
Conflicts:	openldap < 2.2.6-0.3

%description libs
LDAP shared libraries.

%description libs -l pl
Biblioteki wspó³dzielone LDAP.

%package devel
Summary:	LDAP development files
Summary(es):	Bibliotecas de desarrollo y archivos de inclusión para OpenLDAP
Summary(pl):	Pliki dla developerów LDAP
Summary(pt_BR):	Bibliotecas de desenvolvimento e arquivos de inclusão para o OpenLDAP
Summary(ru):	æÁÊÌÙ ÄÌÑ ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Ó LDAP
Summary(uk):	æÁÊÌÉ ÄÌÑ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Ú LDAP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
%{?with_sasl:Requires:	cyrus-sasl-devel >= 2.1.15}
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
Requires:	%{name}-devel = %{version}-%{release}

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

%package backend-bdb
Summary:	BDB backend to OpenLDAP server
Summary(pl):	Backend BDB do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-bdb
BDB backend to slapd, the OpenLDAP server.

%description backend-bdb -l pl
Backend BDB do slapd - serwera OpenLDAP.

%package backend-dnssrv
Summary:	DNS SRV backend to OpenLDAP server
Summary(pl):	Backend DNS SRV do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-dnssrv
DNS SRV backend to slapd, the OpenLDAP server.

%description backend-dnssrv -l pl
Backend DNS SRV do slapd - serwera OpenLDAP.

%package backend-hdb
Summary:	HDB (Hierarchical DB) backend to OpenLDAP server
Summary(pl):	Backend HDB (Hierarchical DB) do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-hdb
HDB (Hierarchical DB) backend to slapd, the OpenLDAP server.

%description backend-hdb -l pl
Backend HDB (Hierarchical DB) do slapd - serwera OpenLDAP.

%package backend-ldap
Summary:	LDAP backend to OpenLDAP server
Summary(pl):	Backend LDAP do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-ldap
LDAP backend to slapd, the OpenLDAP server.

%description backend-ldap -l pl
Backend LDAP do slapd - serwera OpenLDAP.

%package backend-ldbm
Summary:	LDBM backend to OpenLDAP server
Summary(pl):	Backend LDBM do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-ldbm
LDBM backend to slapd, the OpenLDAP server.

%description backend-ldbm -l pl
Backend LDBM do slapd - serwera OpenLDAP.

%package backend-meta
Summary:	Meta backend to OpenLDAP server
Summary(pl):	Backend Meta do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-meta
Meta backend to slapd, the OpenLDAP server.

%description backend-meta -l pl
Backend Meta do slapd - serwera OpenLDAP.

%package backend-monitor
Summary:	Monitor backend to OpenLDAP server
Summary(pl):	Backend Monitor do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-monitor
Meta backend to slapd, the OpenLDAP server.

%description backend-monitor -l pl
Backend Meta do slapd - serwera OpenLDAP.

%package backend-passwd
Summary:	/etc/passwd backend to OpenLDAP server
Summary(pl):	Backend /etc/passwd do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-passwd
/etc/passwd backend to slapd, the OpenLDAP server.

%description backend-passwd -l pl
Backend /etc/passwd do slapd - serwera OpenLDAP.

%package backend-perl
Summary:	Perl backend to OpenLDAP server
Summary(pl):	Backend Perl do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')

%description backend-perl
Perl backend to slapd, the OpenLDAP server.

%description backend-perl -l pl
Backend Perl do slapd - serwera OpenLDAP.

%package backend-relay
Summary:	Relay backend to OpenLDAP server
Summary(pl):	Backend przekazuj±cy do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-overlay-rwm = %{version}-%{release}
Requires:	%{name}-servers = %{version}-%{release}

%description backend-relay
The primary purpose of this slapd(8) backend is to map a naming
context defined in a database running in the same slapd(8) instance
into a virtual naming context, with attributeType and objectClass
manipulation, if required. It requires the rwm overlay.

%description backend-relay -l pl
G³ównym celem tego backendu slapd(8) jest odwzorowywanie kontekstów
nazw zdefiniowanych w bazie danych dzia³aj±cej w tej samej instancji
slapd(8) na konteksty nazw wirtualnych z modyfikowaniem attributeType
i objectClass w razie potrzeby. Wymaga nak³adki rwm.

%package backend-shell
Summary:	Shell backend to OpenLDAP server
Summary(pl):	Backend Shell do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-shell
Shell backend to slapd, the OpenLDAP server.

%description backend-shell -l pl
Backend Shell do slapd - serwera OpenLDAP.

%package backend-sql
Summary:	SQL backend to OpenLDAP server
Summary(pl):	Backend SQL do serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description backend-sql
SQL backend to slapd, the OpenLDAP server.

%description backend-sql -l pl
Backend SQL do slapd - serwera OpenLDAP.

%package overlay-accesslog
Summary:	Accesslog overlay for OpenLDAP server
Summary(pl):	Nak³adka accesslog dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-accesslog
Accesslog overlay for OpenLDAP server.

%description overlay-accesslog -l pl
Nak³adka accesslog dla serwera OpenLDAP.

%package overlay-denyop
Summary:	Denyop overlay for OpenLDAP server
Summary(pl):	Nak³adka zabraniaj±ca wykonania operacji dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-denyop
This overlay provides a quick'n'easy way to deny selected operations
for a database whose backend implements the operations. It is intended
to be less expensive than ACLs because its evaluation occurs before
any backend specific operation is actually even initiated.

%description overlay-denyop -l pl
Ta nak³adka udostêpnia szybki i ³atwy sposób na blokowanie wybranych
operacji dla bazy danych, której backend implementuje te operacje. Ma
byæ mniej kosztowna ni¿ ACL-e, poniewa¿ obliczenia zachodz± przed
rozpoczêciem jakichkolwiek operacji specyficznych dla backendu.

%package overlay-dyngroup
Summary:	Dyngroup overlay for OpenLDAP server
Summary(pl):	Nak³adka dynamicznych grup dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-dyngroup
This overlay extends the Compare operation to detect members of a
dynamic group. It has no effect on any other operations. It must be
configured with a pair of attributes to trigger on, e.g. attrpair
member memberURL will cause compares on "member" to trigger a compare
on "memberURL".

%description overlay-dyngroup -l pl
Ta nak³adka rozszerza operacjê Compare, aby wykrywa³a cz³oników grupy
dynamicznej. Nie wp³ywa na ¿adne inne operacje. Musi byæ
skonfigurowana par± atrybutów, które maj± j± wyzwalaæ, np. attrpair
member memberURL spowoduje, ¿e porównania na "memberu" wyzwol±
porównania na "memberURL".

%package overlay-dynlist
Summary:	Dynnamic list overlay for OpenLDAP server
Summary(pl):	Nak³adka dynamicznych list dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-dynlist
The dynlist overlay allows expansion of dynamic groups and more.

%description overlay-dynlist -l pl
Nak³adka dynlist pozwala na rozwijanie dynamicznych grup i inne
operacje.

%package overlay-lastmod
Summary:	Last Modification overlay for OpenLDAP server
Summary(pl):	Nak³adka Last Modification dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-lastmod
The lastmod overlay creates a service entry rooted at the suffix of
the database it's stacked onto, which holds the DN, the modification
type, the modifiersName and the modifyTimestamp of the last write
operation performed on that database.

%description overlay-lastmod -l pl
Nak³adka lastmod tworzy wpis us³ugi zaczynaj±cy siê od przyrostka
bazy danych, na której jest oparty, trzymaj±cy DN, rodzaj modyfikacji,
modifiersName i modifyTimestamp dla ostatniej operacji zapisu
wykonywanej na tej bazie.

%package overlay-pcache
Summary:	Proxy cache overlay for OpenLDAP server
Summary(pl):	Nak³adka proxy cache dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-pcache
The proxy cache overlay allows caching of LDAP search requests
(queries) in a local database.

%description overlay-pcache -l pl
Nak³adka proxy cache pozwalaj±ca buforowaæ zapytania LDAP w lokalnej
bazie.

%package overlay-ppolicy
Summary:	Password Policy overlay for OpenLDAP server
Summary(pl):	Nak³adka do polityki hase³ dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-ppolicy
The ppolicy overlay is an implementation of the most recent IETF
Password Policy proposal for LDAP. When instantiated, it intercepts,
decodes and applies specific password policy controls to overall use
of a backend database, changes to user password fields, etc.

%description overlay-ppolicy -l pl
Nak³adka ppolicy jest implementacj± najnowszej propozycji IETF
Password Policy dla LDAP. Kiedy zostanie u¿yta, przechwytuje, dekoduje
i aplikuje okre¶lone regulacje polityki hase³ do ogólnego u¿ywania
bazy danych, zmiany pól hase³ u¿ytkowników itp.

%package overlay-refint
Summary:	Referential Integrity overlay for OpenLDAP server
Summary(pl):	Nak³adka sprawdzaj± integralno¶æ odwo³añ dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-refint
The Referential Integrity overlay can be used to maintain the
cohesiveness of a schema which utilizes reference attributes.

%description overlay-refint -l pl
Nak³adka Referential Integrity mo¿e byæ u¿ywana do utrzymywania
spójno¶ci schematu wykorzystuj±cego atrybuty referencji.

%package overlay-retcode
Summary:	Return code overlay for OpenLDAP server
Summary(pl):	Nak³adka obs³uguj±ca zwracane warto¶ci dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-retcode
The retcode overlay to slapd is useful to test the behavior of clients
when server-generated erroneous and/or unusual responses occur, e.g.
error codes, referrals, excessive response times and so on.

%description overlay-retcode -l pl
Nak³adka retcode dla slapd jest przydatna do sprawdzania zachowania
klientów w przypadku wyst±pienia wygenerowanych przez serwer b³êdnych
i/lub nienormalnych odpowiedzi, np. kodów b³êdów, odniesieñ, d³ugich
czasów odpowiedzi itp.

%package overlay-rwm
Summary:	Rewrite/remap overlay for OpenLDAP server
Summary(pl):	Nak³adka mapuj±ca dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-rwm
The rwm overlay performs basic DN/data rewrite and
object-Class/attributeType mapping. Its usage is mostly intended to
provide virtual views of existing data either remotely, in conjunction
with the proxy backend or locally, in conjunction with the relay
backend.

%description overlay-rwm -l pl
Nak³adka rwm wykonuje podstawowe przepisywanie DN na dane i
odwzorowywanie klas obiektów na attributeType. Jej zastosowania to
przede wszystkim dostarczanie wirtualnych widoków danych istniej±cych
albo zdalnie, w po³±czeniu z backendem proxy, albo lokalnie, w
po³±czeniu z backendem relay.

%package overlay-syncprov
Summary:	Syncrepl Provider overlay for OpenLDAP server
Summary(pl):	Nak³adka Syncrepl Provider dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-syncprov
The Syncrepl Provider overlay implements the provider-side support for
syncrepl replication, including persistent search functionality. The
overlay can be used with any backend that maintains entryCSN and
entryUUID attributes for its entries. It also creates a contextCSN
attribute in the root entry of the database.

%description overlay-syncprov -l pl
Nak³adka SyncRepl Provider implementuje obs³ugê replikacji syncrepl
po stronie dostarczyciela, w³±cznie z ci±g³o¶ci± funkcjonalno¶ci
wyszukiwania. Nak³adka mo¿e byæ u¿ywana z dowolnym backendem
utrzymuj±cym atrybuty entryCSN i entryUUID dla swoich wpisów. Tworzy
tak¿e atrybut contextCSN w g³ównym elemencie bazy.

%package overlay-translucent
Summary:	Translucent Proxy overlay for OpenLDAP server
Summary(pl):	Nak³adka Translucent Proxy dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-translucent
The Translucent Proxy overlay can be used with a backend database such
as slapd-bdb(5) to create a "translucent proxy". Entries retrieved
from a remote LDAP server may have some or all attributes overridden,
or new attributes added, by entries in the local database before being
presented to the client.

%description overlay-translucent -l pl
Nak³adka Translucent Proxy mo¿e byæ u¿ywana wraz z baz± danych tak±
jak slapd-bdb(5) do stworzenia "przezroczystego proxy". Wpisy
otrzymane ze zdalnego serwera LDAP mog± mieæ nadpisane niektóre lub
wszystkie atrybuty, albo dodane nowe atrybuty poprzez wpisy w lokalnej
bazie danych przed przekazaniem do klienta.

%package overlay-unique
Summary:	Uniqueness overlay for OpenLDAP server
Summary(pl):	Nak³adka sprawdzaj±ca unikatowo¶æ dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-unique
The Attribute Uniqueness overlay can be used to enforce the uniqueness
of some or all attributes within a subtree.

%description overlay-unique -l pl
Nak³adka sprawdzaj±ca unikatowo¶æ s³u¿y do wymuszania unikatowo¶ci
atrybutów w poddrzewie LDAP.

%package overlay-valsort
Summary:	Valsort overlay for OpenLDAP server
Summary(pl):	Nak³adka valsort dla serwera OpenLDAP
Group:		Networking/Daemons
Requires(post,preun):	/bin/ed
Requires:	%{name}-servers = %{version}-%{release}

%description overlay-valsort
This overlay sorts the values of multi-valued attributes when
returning them in a search response.

%description overlay-valsort -l pl
Ta nak³adka sortuje warto¶ci wielowarto¶ciowych atrybutów przy
zwracaniu ich jako odpowied¼ przy wyszukiwaniu.

%package servers
Summary:	LDAP servers
Summary(pl):	Serwery LDAP
Summary(pt_BR):	Arquivos para o servidor OpenLDAP
Summary(ru):	óÅÒ×ÅÒÁ LDAP
Summary(uk):	óÅÒ×ÅÒÁ LDAP
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getent
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(pre):	textutils
Requires(post):	/usr/sbin/usermod
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Provides:	group(slapd)
Provides:	user(slapd)
Obsoletes:	openldap-overlay-glue

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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
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
	--with-ldbm-api=berkeley \
	--with-ldbm-type=%{?ldbm_type:%{ldbm_type}}%{!?ldbm_type:btree} \
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

%{__make} depend
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

%post	libs	-p /sbin/ldconfig
%postun	libs	-p /sbin/ldconfig

%pre servers
%groupadd -P %{name}-servers -g 93 slapd
%useradd -P %{name}-servers -u 93 -s /bin/false -g slapd -c "OpenLDAP server" -d /var/lib/openldap-data slapd

%post servers
/sbin/chkconfig --add ldap
if [ -f /var/lock/subsys/ldap ]; then
	/etc/rc.d/init.d/ldap restart >&2
else
	echo "Run '/etc/rc.d/init.d/ldap start' to start OpenLDAP server." >&2
fi

%triggerpostun servers -- openldap-servers < 2.1.12
if [ "`/usr/bin/getent passwd slapd | cut -d: -f6`" = "/var/lib/openldap-ldbm" ]; then
	/usr/sbin/usermod -d /var/lib/openldap-data slapd
fi

%preun servers
if [ "$1" = "0" ] ; then
	if [ -f /var/lock/subsys/ldap ]; then
		/etc/rc.d/init.d/ldap stop >&2 || :
	fi
	/sbin/chkconfig --del ldap || :
fi

%postun servers
if [ "$1" = "0" ]; then
	%userremove slapd
	%groupremove slapd
fi

%define	ldap_module_add() \
%{__sed} -i -e 's/^#[[:blank:]]*moduleload[[:blank:]]\+%1[[:blank:]]*$/moduleload	%1/' %{_sysconfdir}/openldap/slapd.conf \
if [ -f /var/lock/subsys/ldap ]; then \
	/etc/rc.d/init.d/ldap restart >&2 \
fi

%define	ldap_module_remove() \
%{__sed} -i -e 's/^[[:blank:]]*moduleload[[:blank:]]\+%1[[:blank:]]*$/# moduleload   %1/' %{_sysconfdir}/openldap/slapd.conf \
if [ -f /var/lock/subsys/ldap ]; then \
	/etc/rc.d/init.d/ldap restart >&2 \
fi

%post backend-bdb
%ldap_module_add back_bdb.la

%preun backend-bdb
if [ "$1" = 0 ]; then
	%ldap_module_remove back_bdb.la
fi

%post backend-dnssrv
%ldap_module_add back_dnssrv.la

%preun backend-dnssrv
if [ "$1" = 0 ]; then
	%ldap_module_remove back_dnssrv.la
fi

%post backend-hdb
%ldap_module_add back_hdb.la

%preun backend-hdb
if [ "$1" = 0 ]; then
	%ldap_module_remove back_hdb.la
fi

%post backend-ldap
%ldap_module_add back_ldap.la

%preun backend-ldap
if [ "$1" = 0 ]; then
	%ldap_module_remove back_ldap.la
fi

%post backend-ldbm
%ldap_module_add back_ldbm.la

%preun backend-ldbm
if [ "$1" = 0 ]; then
	%ldap_module_remove back_ldbm.la
fi

%post backend-meta
%ldap_module_add back_meta.la

%preun backend-meta
if [ "$1" = 0 ]; then
	%ldap_module_remove back_meta.la
fi

%post backend-monitor
%ldap_module_add back_monitor.la

%preun backend-monitor
if [ "$1" = 0 ]; then
	%ldap_module_remove back_monitor.la
fi

%post backend-passwd
%ldap_module_add back_passwd.la

%preun backend-passwd
if [ "$1" = 0 ]; then
	%ldap_module_remove back_passwd.la
fi

%if %{with perl}
%post backend-perl
%ldap_module_add back_perl.la

%preun backend-perl
if [ "$1" = 0 ]; then
	%ldap_module_remove back_perl.la
fi
%endif

%post backend-relay
%ldap_module_add back_relay.la

%preun backend-relay
if [ "$1" = 0 ]; then
	%ldap_module_remove back_relay.la
fi

%post backend-shell
%ldap_module_add back_shell.la

%preun backend-shell
if [ "$1" = 0 ]; then
	%ldap_module_remove back_shell.la
fi

%if %{with odbc}
%post backend-sql
%ldap_module_add back_sql.la/

%preun backend-sql
if [ "$1" = 0 ]; then
	%ldap_module_remove back_sql.la
fi
%endif

%post overlay-pcache
%ldap_module_add pcache.la

%preun overlay-pcache
if [ "$1" = 0 ]; then
	%ldap_module_remove pcache.la
fi

%post overlay-accesslog
%ldap_module_add accesslog.la

%preun overlay-accesslog
if [ "$1" = 0 ]; then
	%ldap_module_remove accesslog.la
fi

%post overlay-denyop
%ldap_module_add denyop.la

%preun overlay-denyop
if [ "$1" = 0 ]; then
	%ldap_module_remove denyop.la
fi

%post overlay-dyngroup
%ldap_module_add dyngroup.la

%preun overlay-dyngroup
if [ "$1" = 0 ]; then
	%ldap_module_remove dyngroup.la
fi

%post overlay-dynlist
%ldap_module_add dynlist.la

%preun overlay-dynlist
if [ "$1" = 0 ]; then
	%ldap_module_remove dynlist.la
fi

%post overlay-lastmod
%ldap_module_add lastmod.la

%preun overlay-lastmod
if [ "$1" = 0 ]; then
	%ldap_module_remove lastmod.la
fi

%post overlay-ppolicy
%ldap_module_add ppolicy.la

%preun overlay-ppolicy
if [ "$1" = 0 ]; then
	%ldap_module_remove ppolicy.la
fi

%post overlay-refint
%ldap_module_add refint.la

%preun overlay-refint
if [ "$1" = 0 ]; then
	%ldap_module_remove refint.la
fi

%post overlay-retcode
%ldap_module_add retcode.la

%preun overlay-retcode
if [ "$1" = 0 ]; then
	%ldap_module_remove retcode.la
fi

%post overlay-rwm
%ldap_module_add rwm.la

%preun overlay-rwm
if [ "$1" = 0 ]; then
	%ldap_module_remove rwm.la
fi

%post overlay-syncprov
%ldap_module_add syncprov.la

%preun overlay-syncprov
if [ "$1" = 0 ]; then
	%ldap_module_remove syncprov.la
fi

%post overlay-translucent
%ldap_module_add translucent.la

%preun overlay-translucent
if [ "$1" = 0 ]; then
	%ldap_module_remove translucent.la
fi

%post overlay-unique
%ldap_module_add unique.la

%preun overlay-unique
if [ "$1" = 0 ]; then
	%ldap_module_remove unique.la
fi

%post overlay-valsort
%ldap_module_add valsort.la

%preun overlay-valsort
if [ "$1" = 0 ]; then
	%ldap_module_remove valsort.la
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

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
