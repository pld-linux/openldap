Summary:	Lightweight Directory Access Protocol clients/servers
Name:		openldap
Version:	1.2.1
Release:	1
Group:		Server/Network
Copyright:	Freely distributable
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
Source1:	ldap.init
Patch:		openldap-conf.patch
Prereq:		/sbin/chkconfig
URL:		http://www.openldap.org/
BuildPrereq:	ncurses-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%Description
LDAP servers and clients, as well as interfaces to other protocols.
Note that this does not include the slapd interface to X.500 and
therefore does not require the ISODE package.

%Package devel
Summary:	LDAP development files
Group:		Development/Libraries

%description devel
Header files and libraries for developing applications that use LDAP.

%Package static
Summary:	LDAP static libraries
Group:		Development/Libraries

%description static
LDAP static libraries.

%package servers
Summary:	LDAP servers
Group:		Server/Network

%description servers
The servers (daemons) that come with LDAP.

%prep
%setup -q -n ldap

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CPPFLAGS="$RPM_OPT_FLAGS -D_MIT_POSIX_THREADS"
./configure \
	--prefix=/usr \
	--libexecdir=/usr/sbin \
	--sysconfdir=/etc \
	--localstatedir=/var/run \
	--with-subdir=ldap \
	--enable-cldap \
	--enable-phonetic \
	--with-wrappers \
	--without-threads \
	--enable-shared

make depend
make

%Install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/{ldap,rc.d/init.d},var/ldap}

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	libexecdir=$RPM_BUILD_ROOT/usr/sbin \
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
echo "localhost" > $RPM_BUILD_ROOT/etc/ldap/ldapserver

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post servers
chkconfig --add ldap

%postun servers
if [ "$1" = "0" ] ; then
	chkconfig --del ldap
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCEMENT CHANGES COPYRIGHT INSTALL README
%doc doc/rfc/rfc*
%dir /etc/ldap
%config /etc/ldap/ldapfilter.conf
%config /etc/ldap/ldapserver
%config /etc/ldap/ldapfriendly
%config /etc/ldap/ldaptemplates.conf
%config /etc/ldap/ldapsearchprefs.conf
%config /etc/ldap/ldap.conf
%attr(755,root,root) /usr/sbin/xrpcomp
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/lib*.so.*.*.*
/usr/man/man1/*
/usr/man/man5/ldap.conf.5.gz
/usr/man/man5/ldapfilter.conf.5.gz
/usr/man/man5/ldapfriendly.5.gz
/usr/man/man5/ldapsearchprefs.conf.5.gz
/usr/man/man5/ldaptemplates.conf.5.gz
/usr/man/man5/ud.conf.5.gz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so
/usr/include/*
/usr/man/man3/*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%files servers
%defattr(644,root,root,755)
%config /etc/ldap/slapd.conf
%config /etc/ldap/slapd.oc.conf
%config /etc/ldap/slapd.at.conf
%config /etc/ldap/go500gw.help
%config /etc/ldap/rcpt500.help
%config /etc/rc.d/init.d/ldap
%attr(754,root,root) /etc/rc.d/init.d/ldap
%attr(700,root,root) /var/ldap
/usr/share/ldap
/usr/sbin/*
/usr/man/man5/ldif.5.gz
/usr/man/man5/slapd.conf.5.gz
/usr/man/man5/slapd.replog.5.gz
/usr/man/man8/*

%ChangeLog
* Thu Apr 22 1999 Arne Coucheron <arneco@online.no>
  [1.2.1-1]
- using %%{name} and %%{version} macros
- added -q parameter to %setup
- added URL tag
- using chkconfig to activate init script and added Prereq: for it
- devel package requires openldap
- fixed the path names in the man pages
- using %defattr in %files section
- simplified the use %files
- some changes in the init script (check that networking is up etc)
