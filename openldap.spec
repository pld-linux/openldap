Summary:	Lightweight Directory Access Protocol clients/servers
Name:		openldap
Version:	1.2.0
Release:	1
Group:		Server/Network
Copyright:	Freely distributable
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
Patch0:		openldap-%{Version}-%{Dist}.patch
URL:		http://www.openldap.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%Description
LDAP servers and clients, as well as interfaces to other protocols.
Note that this does not include the slapd interface to X.500 and
therefore does not require the ISODE package.

%Package devel
Summary:	LDAP development files
Group:		Development/Libraries

%Description devel
Header files and libraries for developing applications that use LDAP.

%Package servers
Summary:	LDAP servers
Group:		Server/Network

%Description servers
The servers (daemons) that come with LDAP.

%prep
%setup -q -n ldap

%build

# How to build with Threads under Linux (esp. OpenLinux)
# OpenLDAP FAQ: http://www.openldap.org/faq/data/cache/19.html
# This did *not* work ... build without-threads -edo
# CPPFLAGS="-D_MIT_POSIX_THREADS"; export CPPFLAGS

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CPPFLAGS="$RPM_OPT_FLAGS -D_MIT_POSIX_THREADS"
./configure \
	--prefix=/usr \
	--enable-cldap \
	--enable-phonetic \
	--sysconfdir=/etc \
	--localstatedir=/var/run \
	--with-wrappers \
	--without-threads \
	--with-subdir=ldap

make depend
make

%Install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/rc.d/init.d,var/ldap}

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	sysconfdir=$RPM_BUILD_ROOT/etc

strip $RPM_BUILD_ROOT/usr/{bin,sbin}/*

rm -f $RPM_BUILD_ROOT/usr/man/man1/ldapadd.1
echo ".so ldapmodify.1" > $RPM_BUILD_ROOT/usr/man/man1/ldapadd.1

$RPM_BUILD_ROOT/usr/man/man3/{cldap,ld_errno,ldap_8859_to_t61}.3
echo ".so cldap.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap.3
echo ".so ldap_error.3" > $RPM_BUILD_ROOT/usr/man/man3/ld_errno.3
echo ".so ldap_charset.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_8859_to_t61.3

$RPM_BUILD_ROOT/usr/man/man8/{fax500,ldif2id2children,ldif2id2entry,ldif2index}.8
echo ".so mail500.8" > $RPM_BUILD_ROOT/usr/man/man8/fax500.8
echo ".so ldif2ldbm.8" > $RPM_BUILD_ROOT/usr/man/man8/ldif2id2children.8
echo ".so ldif2ldbm.8" > $RPM_BUILD_ROOT/usr/man/man8/ldif2id2entry.8
echo ".so ldif2ldbm.8" > $RPM_BUILD_ROOT/usr/man/man8/ldif2index.8

insyall openldap.init $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%post servers
lisa --SysV-init install ldap S91 3:4:5 K09 0:1:2:6

%postun servers
lisa --SysV-init remove ldap $1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ANNOUNCEMENT CHANGES COPYRIGHT LICENSE README
%config /etc/ldap/*
%dir /etc/ldap
/usr/sbin/xrpcomp
/usr/bin/*
/usr/man/man1/*
/usr/man/man5/ldap.conf.5.gz
/usr/man/man5/ldapfilter.conf.5.gz
/usr/man/man5/ldapfriendly.5.gz
/usr/man/man5/ldapsearchprefs.conf.5.gz
/usr/man/man5/ldaptemplates.conf.5.gz
/usr/man/man5/ud.conf.5.gz

%files devel
/usr/include/*
/usr/lib/*a
/usr/man/man3/*

%files servers
%config /etc/ldap/*
%dir /etc/ldap
/etc/rc.d/init.d/ldap
/var/ldap
/usr/share/ldap
/usr/sbin/*
/usr/man/man5/ldif.5.gz
/usr/man/man5/slapd.conf.5.gz
/usr/man/man5/slapd.replog.5.gz
/usr/man/man8/*

%ChangeLog
* Fri Jan 08 1999 ...
Initial build
