%define Name		openldap
%define Version		1.1.2
%define Release		1
%define Dist		OL

Summary		: Lightweight Directory Access Protocol clients/servers
Name		: %{Name}
Version		: %{Version}
Release		: %{Release}
Group		: Server/Network

Copyright	: Freely distributable
Packager	: edo@calderasystems.com (Ed Orcutt)
Icon		: dummy.xpm
URL		: http://www.openldap.org/

#Requires	: gdbm

BuildRoot	: /tmp/%{Name}-%{Version}

Source0: ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/openldap-1.1.2.tgz
Source9: fixup.pl
Patch0: openldap-%{Version}-%{Dist}.patch

%define fixUP   %{SOURCE9}
%define prefix /usr
%define ldap_subdir ldap
%define bindir %{prefix}/bin
#%define datadir /etc
%define datadir  %{prefix}/share/%{ldap_subdir}
%define datadirC %{prefix}/share
%define sbindir %{prefix}/sbin
%define libdir %{prefix}/lib
%define libexecdir %{prefix}/sbin
%define sysconfdir  /etc/%{ldap_subdir}
%define sysconfdirC /etc
%define localstatedir /var/run


%Package devel
Summary		: LDAP development files
Group		: Development/Libraries


%Package servers
Summary		: LDAP servers
Group		: Server/Network


%Description
LDAP servers and clients, as well as interfaces to other protocols.
Note that this does not include the slapd interface to X.500 and
therefore does not require the ISODE package.


%Description devel
Header files and libraries for developing applications that use LDAP.


%Description servers
The servers (daemons) that come with LDAP.


%Prep
%setup -n ldap
%patch -p1


%Build

# How to build with Threads under Linux (esp. OpenLinux)
# OpenLDAP FAQ: http://www.openldap.org/faq/data/cache/19.html
# This did *not* work ... build without-threads -edo
# CPPFLAGS="-D_MIT_POSIX_THREADS"; export CPPFLAGS

./configure --prefix=%{prefix} --enable-cldap --enable-phonetic \
  --libexecdir=%{libexecdir} --sysconfdir=%{sysconfdirC} \
  --localstatedir=%{localstatedir} --datadir=%{datadirC} \
  --with-wrappers --without-threads --with-subdir=%{ldap_subdir}

make depend
make


%Install
DESTDIR=$RPM_BUILD_ROOT; export DESTDIR
[ -n "`echo $DESTDIR | sed -n 's:^/tmp/[^.].*$:OK:p'`" ] && rm -rf $DESTDIR ||
(echo "Invalid BuildRoot: '$DESTDIR'! Check this .spec ..."; exit 1) || exit 1

# In order to install into the "BUILDIR", and yet have the correct
# substitutions performed ... we will have to do it ourselves first! -edo

%{fixUP} -vT clients/fax500/xrpcomp -e 's:%LIBEXECDIR%:%{libexecdir}:g;'
for i in servers/slapd/*.conf; do
  %{fixUP} -vT $i -e 's:%SYSCONFDIR%:%{sysconfdir}:g;'
done
for i in doc/man/man1/*.1 doc/man/man3/*.3 doc/man/man5/*.5 doc/man/man8/*.8 ; do
  %{fixUP} -vT $i -e '
    s:ETCDIR:%{sysconfdir}:g +
    s:DATADIR:%{datadir}:g +
    s:SBINDIR:%{sbindir}:g +
    s:BINDIR:%{bindir}:g +
    s:LIBDIR:%{libdir}:g +
    s:LIBEXECDIR:%{libexecdir}:g +
    s:SYSCONFDIR:%{sysconfdir}:g;
'
done

make install \
	prefix=$DESTDIR%{prefix} \
	libexecdir=$DESTDIR%{libexecdir} \
	sysconfdir=$DESTDIR%{sysconfdir} \
	datadir=$DESTDIR%{datadir}

strip `file $DESTDIR/usr/{bin,sbin}/* | grep ELF | cut -d':' -f 1`
mkdir -p $DESTDIR/etc/rc.d/init.d
cp openldap.init $DESTDIR/etc/rc.d/init.d/ldap
chmod 755 $DESTDIR/etc/rc.d/init.d/ldap

mkdir -p $DESTDIR/var/ldap

%{fixManPages}


%Clean
DESTDIR=$RPM_BUILD_ROOT;export DESTDIR;[ -n "$UID" ]&&[ "$UID" -gt 0 ]&&exit 0
[ -n "`echo $DESTDIR | sed -n 's:^/tmp/[^.].*$:OK:p'`" ] && rm -rf $DESTDIR ||
(echo "Invalid BuildRoot: '$DESTDIR'! Check this .spec ..."; exit 1) || exit 1


%Post servers
lisa --SysV-init install ldap S91 3:4:5 K09 0:1:2:6


%PostUn servers
lisa --SysV-init remove ldap $1


%Files
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


%Files devel
/usr/include/*
/usr/lib/*a
/usr/man/man3/*


%Files servers
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
