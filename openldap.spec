Summary:	Lightweight Directory Access Protocol clients/servers
Name:		openldap
Version:	1.2.1
Release:	1
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Copyright:	Freely distributable
Source0:	ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/%{name}-%{version}.tgz
Source1:	ldap.init
Source2:	openldap.sysconfig
Patch0:		openldap-conf.patch
Patch1:		openldap-strdup.patch
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
Group(pl):      Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and libraries for developing applications that use LDAP.

%Package static
Summary:	LDAP static libraries
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
LDAP static libraries.

%package servers
Summary:	LDAP servers
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Prereq:		chkconfig


%description servers
The servers (daemons) that come with LDAP.

%prep
%setup  -q -n ldap
%patch0 -p1
%patch1 -p1

%build
#CPPFLAGS="-D_MIT_POSIX_THREADS -I/usr/include/ncurses" 
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CPPFLAGS="-I/usr/include/ncurses" \
./configure %{_target} \
	--prefix=/usr \
	--libexecdir=/usr/sbin \
	--sysconfdir=/etc/ldap \
	--localstatedir=/var/state \
	--with-subdir=ldap \
	--enable-cldap \
	--enable-phonetic \
	--with-wrappers \
	--with-threads \
	--enable-shared

make depend
make

%Install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/{ldap,sysconfig,rc.d/init.d},var/ldap}

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	libexecdir=$RPM_BUILD_ROOT/usr/sbin \
	sysconfdir=$RPM_BUILD_ROOT/etc/ldap

chmod a+x $RPM_BUILD_ROOT/usr/lib/*.so.*.*
strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/*.so.*.*
strip $RPM_BUILD_ROOT/usr/{bin,sbin}/* || :

rm -f $RPM_BUILD_ROOT/usr/man/man1/ldapadd.1
echo ".so ldapmodify.1" > $RPM_BUILD_ROOT/usr/man/man1/ldapadd.1

(cd $RPM_BUILD_ROOT/usr/man/man3/;
rm -f cldap.3 \
      ld_errno.3 \
      ldap_8859_to_t61.3 \
      ldap_add_s.3 \
      ldap_bind_s.3 \
      ldap_simple_bind.3 \
      ldap_simple_bind_s.3 \
      ldap_kerberos_bind_s.3 \
      ldap_kerberos_bind1.3 \
      ldap_kerberos_bind1_s.3 \
      ldap_kerberos_bind2.3 \
      ldap_kerberos_bind2_s.3 \
      ldap_unbind.3 \
      ldap_unbind_s.3 \
      ldap_set_rebind_proc.3 \
      ldap_enable_cache.3 \
      ldap_disable_cache.3 \
      ldap_destroy_cache.3 \
      ldap_flush_cache.3 \
      ldap_uncache_entry.3 \
      ldap_uncache_request.3 \
      ldap_set_cache_options.3 \
      ldap_set_string_translators.3 \
      ldap_enable_translation.3 \
      ldap_translate_from_t61.3 \
      ldap_translate_to_t61.3 \
      ldap_t61_to_8859.3 \
      ldap_compare_s.3 \
      ldap_delete_s.3 \
      ldap_init_templates.3 \
      ldap_init_templates_buf.3 \
      ldap_free_templates.3 \
      ldap_init_templates_buf.3 \
      ldap_free_templates.3 \
      ldap_first_disptmpl.3 \
      ldap_next_disptmpl.3 \
      ldap_oc2template.3 \
      ldap_tmplattrs.3 \
      ldap_first_tmplrow.3 \
      ldap_next_tmplrow.3 \
      ldap_first_tmplcol.3 \
      ldap_next_tmplcol.3 \
      ldap_entry2text_search.3 \
      ldap_vals2text.3 \
      ldap_vals2html.3 \
      ldap_perror.3 \
      ldap_result2error.3 \
      ldap_next_attribute.3 \
      ldap_next_entry.3 \
      ldap_friendly_name.3 \
      ldap_is_dns_dn.3 \
      ldap_init_getfilter.3 \
      ldap_init_getfilter_buf.3 \
      ldap_getfilter_free.3 \
      ldap_getfirstfilter.3 \
      ldap_getnextfilter.3 \
      ldap_setfilteraffixes.3 \
      ldap_get_values_len.3 \
      ldap_value_free.3 \
      ldap_value_free_len.3 \
      ldap_modify_s.3 \
      ldap_mods_free.3 \
      ldap_modrdn_s.3 \
      ldap_search_s.3 \
      ldap_search_st.3 \
      ldap_sort_entries.3 \
      ldap_sort_values.3 \
      ldap_sort_strcasecmp.3 \
      ldap_ufn_search_s.3 \
      ldap_ufn_search_c.3 \
      ldap_ufn_search_ct.3 \
      ldap_ufn_setprefix.3 \
      ldap_ufn_setfilter.3 \
      ldap_ufn_timeout.3 \
      ldap_url_parse.3 \
      ldap_url_search.3 \
      ldap_url_search_s.3 \
      ldap_url_search_st.3
)      
       
echo ".so cldap.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap.3
echo ".so ldap_error.3" > $RPM_BUILD_ROOT/usr/man/man3/ld_errno.3
echo ".so ldap_charset.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_8859_to_t61.3
echo ".so ldap_add.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_add_s.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_bind_s.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_simple_bind.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_simple_bind_s.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_kerberos_bind_s.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_kerberos_bind1.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_kerberos_bind1_s.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_kerberos_bind2.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_kerberos_bind2_s.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_unbind.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_unbind_s.3
echo ".so ldap_bind.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_set_rebind_proc.3
echo ".so ldap_cache.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_enable_cache.3
echo ".so ldap_cache.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_disable_cache.3
echo ".so ldap_cache.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_destroy_cache.3
echo ".so ldap_cache.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_flush_cache.3
echo ".so ldap_cache.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_uncache_entry.3
echo ".so ldap_cache.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_uncache_request.3
echo ".so ldap_cache.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_set_cache_options.3
echo ".so ldap_charset.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_set_string_translators.3
echo ".so ldap_charset.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_enable_translation.3
echo ".so ldap_charset.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_translate_from_t61.3
echo ".so ldap_charset.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_translate_to_t61.3
echo ".so ldap_charset.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_t61_to_8859.3
echo ".so ldap_compare.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_compare_s.3
echo ".so ldap_delete.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_delete_s.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_init_templates.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_init_templates_buf.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_free_templates.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_first_disptmpl.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_next_disptmpl.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_oc2template.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_tmplattrs.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_first_tmplrow.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_next_tmplrow.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_first_tmplcol.3
echo ".so ldap_disptmpl.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_next_tmplcol.3
echo ".so ldap_entry2text.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_entry2text_search.3
echo ".so ldap_entry2text.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_vals2text.3
echo ".so ldap_entry2html.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_vals2html.3
echo ".so ldap_error.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_perror.3
echo ".so ldap_error.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_result2error.3
echo ".so ldap_first_attribute.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_next_attribute.3
echo ".so ldap_first_entry.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_next_entry.3
echo ".so ldap_friendly.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_friendly_name.3
echo ".so ldap_get_dn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_is_dns_dn.3
echo ".so ldap_getfilter.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_init_getfilter.3
echo ".so ldap_getfilter.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_init_getfilter_buf.3
echo ".so ldap_getfilter.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_getfilter_free.3
echo ".so ldap_getfilter.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_getfirstfilter.3
echo ".so ldap_getfilter.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_getnextfilter.3
echo ".so ldap_getfilter.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_setfilteraffixes.3
echo ".so ldap_get_values.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_get_values_len.3
echo ".so ldap_get_values.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_value_free.3
echo ".so ldap_get_values.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_value_free_len.3
echo ".so ldap_modify.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_modify_s.3
echo ".so ldap_modify.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_mods_free.3
echo ".so ldap_modrdn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_modrdn_s.3
echo ".so ldap_search.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_search_s.3
echo ".so ldap_search.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_search_st.3
echo ".so ldap_sort.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_sort_entries.3
echo ".so ldap_sort.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_sort_values.3
echo ".so ldap_sort.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_sort_strcasecmp.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_ufn_search_s.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_ufn_search_c.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_ufn_search_ct.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_ufn_setprefix.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_ufn_setfilter.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_ufn_timeout.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_url_parse.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_url_search.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_url_search_s.3
echo ".so ldap_ufn.3" > $RPM_BUILD_ROOT/usr/man/man3/ldap_url_search_st.3

rm -f $RPM_BUILD_ROOT/usr/man/man8/{fax500,ldif2id2children,ldif2id2entry,ldif2index}.8
echo ".so mail500.8" > $RPM_BUILD_ROOT/usr/man/man8/fax500.8
echo ".so ldif2ldbm.8" > $RPM_BUILD_ROOT/usr/man/man8/ldif2id2children.8
echo ".so ldif2ldbm.8" > $RPM_BUILD_ROOT/usr/man/man8/ldif2id2entry.8
echo ".so ldif2ldbm.8" > $RPM_BUILD_ROOT/usr/man/man8/ldif2index.8

(
	cd $RPM_BUILD_ROOT/usr/sbin/
	sed -e "s|^#! /bin/sh|#!/bin/sh|g" < xrpcomp >xrpcomp.work
	mv xrpcomp.work xrpcomp
	chmod a+x xrpcomp
)

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ldap
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ldap

echo "localhost" > $RPM_BUILD_ROOT/etc/ldap/ldapserver

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/* \
	ANNOUNCEMENT CHANGES COPYRIGHT INSTALL README \
	doc/rfc/rfc*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post servers
chkconfig --add ldap
if test -r /var/run/ldap.pid; then
        /etc/rc.d/init.d/ldap stop >&2
        /etc/rc.d/init.d/ldap start >&2
else
        echo "Run \"/etc/rc.d/init.d/ldap start\" to start sldap server."
fi
			
%postun servers
if [ "$1" = "0" ] ; then
	chkconfig --del ldap
	/etc/rc.d/init.d/ldap stop
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCEMENT,CHANGES,COPYRIGHT,INSTALL,README}.gz
%doc doc/rfc/rfc*
%dir /etc/ldap
%config /etc/ldap/ldapfilter.conf
%config /etc/ldap/ldapserver
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
%attr(640,root,root) %config %verify(not size mtime md5) /etc/ldap/slapd.conf
%config %verify(not size mtime md5) /etc/ldap/slapd.oc.conf
%config %verify(not size mtime md5) /etc/ldap/slapd.at.conf
%config %verify(not size mtime md5) /etc/sysconfig/ldap
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
