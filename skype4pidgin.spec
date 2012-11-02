Name:           skype4pidgin
Version:        0.0
Release:        0.4.20121031svn641%{?dist}
Summary:        Skype plugin for libpurple messengers

Group:          Applications/Internet
License:        GPLv3+
URL:            http://eion.robbmob.com/
Source0:        %{name}-20121031svn641.tar.bz2
Patch0:         %{name}-makefile.patch

BuildRequires:  glib2-devel
BuildRequires:  libX11-devel
BuildRequires:  gettext
BuildRequires:  libpurple-devel
Requires:       libpurple
Requires:       skype

%description
Skype API Plugin for Empathy/Pidgin/libpurple/Adium. Very good to use
with GNOME Shell.


%prep
%setup -q -n %{name}
%patch0 -p0 -b .fix-makefile
chmod 0644 *.c *.h *.m *.nsi icons/*/*.png
chmod 0644 CHANGELOG.txt COPYING.txt Makefile README.txt TODO.txt


%build
make %{?_smp_mflags} LINUX_LIBDIR=%{_libdir} all
make %{?_smp_mflags} LINUX_LIBDIR=%{_libdir} locales


%install
make LINUX_LIBDIR=%{_libdir} DESTDIR=%{buildroot} install

# strip binaries
strip %{buildroot}%{_libdir}/purple-2/*.so
sed -i 's/\r//' README.txt


%files
%defattr(-,root,root,-)
%doc CHANGELOG.txt COPYING.txt README.txt TODO.txt
%attr(755, root, root) %{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/skype*.png
%{_datadir}/pixmaps/pidgin/emotes/skype/theme


%changelog
* Wed Oct 31 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0-0.4.20121031svn641.R
- update to svn641

* Wed Apr  4 2012 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0-0.3.20120216svn628.R
- update to svn628

* Tue Dec 13 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0-0.2.20111209svn625.R
- update to svn625

* Sun Oct  2 2011 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0-0.1.20110927svn615.R
- update to svn615

* Thu Nov 28 2010 Alexei Panov <elemc@atisserv.ru> - 20101128svn603-1
- Initial build
