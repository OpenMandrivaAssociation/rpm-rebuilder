%define name	rpm-rebuilder
%define version	0.28
%define release 13

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tools to build/check distributions
URL:		http://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		System/Configuration/Packaging
Requires:	rpmlint
Requires:	strace
Requires:	rpm-build
Requires:	diffutils
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The rpm-rebuilder package contains a set of tools written in bourne
shell, python and perl to rebuild/check large sets of rpm source packages.

check-distrib: checks if a set of source and binary rpms are in sync.

rpm-rebuilder: build a set of rpms from a set of srpms.

compute-build-requires: trace an rpm build command to find the BuildRequires
it needs.

compute-compile-order: from the sets of binary and sources rpms, find the order
in which the source rpms must be recompiled.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README README.CVS ChangeLog
%_bindir/*
%_sbindir/*
%_datadir/rpm-rebuilder



%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.28-6mdv2011.0
+ Revision: 669436
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.28-5mdv2011.0
+ Revision: 607375
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.28-4mdv2010.1
+ Revision: 523929
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.28-3mdv2010.0
+ Revision: 426960
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.28-2mdv2009.0
+ Revision: 225333
- rebuild

* Thu Jan 17 2008 Pixel <pixel@mandriva.com> 0.28-1mdv2008.1
+ Revision: 154078
- 0.28
- rpm-rebuilder (Arnaud Patard):
  o Add check on SRPMS_DIRS environment variable:
    rpm-rebuilder is checking that this variable is set but doesn't
    check if it exists. This leads to strange errors so it's better to fail.
  o Don't use urpmf to find provides:
    urpmf is working nicely but gives also packages that are not
    installed on your box. Use rpm instead.
  o Fix /dev/null usage:
    Use /dev/null for redirecting output and /dev/zero for input.
    This was breaking python test_file test.
  o Fix check for the build success log presence:
    The variable containing the package name is $NAME and not $p
    ($p contains the filename of the package)
- install-chroot-tar.sh (Warly):
  o remove rpm database temporary file
  o use urpmi --use-distrib

* Mon Jan 07 2008 Anne Nicolas <ennael@mandriva.org> 0.27-3mdv2008.1
+ Revision: 146279
- new release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 08 2007 Adam Williamson <awilliamson@mandriva.org> 0.27-2mdv2008.0
+ Revision: 37170
- rebuild for new era (does anyone still use this?)


* Sat Nov 05 2005 Frederic Lepied <flepied@mandriva.com> 0.27-1mdk
- rpm-rebuilder: added support for clean chroot build.

* Thu Oct 06 2005 Guillaume Rousse <guillomovitch@zarb.org> 0.26-1mdk
- split rpmbuildupdate in its own package
- %%mkrel
- spec cleanup
- drop prefix

* Sun Sep 11 2005 Frederic Lepied <flepied@mandriva.com> 0.25-1mdk
- add missing diffrpm and diffsrcrpm scripts and use them in rebuild-rpm
- fix increment-release.py to support mkrel
- chrooted-install: add support for bind mount and --use-distrib
for urpmi (Arnaud).
- rpmbuildupdate: add .tar.Z to the list of extension to download
and test ( buchan request ) (Michael Scherer)

* Tue Aug 30 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.24-1mdk
- make it possible to move -debug packages into RPM_DEBUG_DEST_DIR

* Tue Jun 21 2005 Frederic Lepied <flepied@mandriva.com> 0.23-1mdk
- chrooted-install: 
	* fix deplist.ordered path.
	* Use urpmi by default to install the minimal
	  system (use --no-urpmi to have the old behaviour).  Add --media
	  option to be able to specify which urpmi media to use for
	  bootstrapping.
	* added -f to force even if the directory already
	  exists.  allow to pass 0 as the ssh port to avoid ssh support.

* Sat Jun 11 2005 Frederic Lepied <flepied@mandriva.com> 0.22-1mdk
- chrooted-install: declare every mount point in fstab instead of
 explicitely mounting them in the service.

- rpmbuildupdate (Michael Scherer):
	* new sourceforge mirror, thanks to Götz Waschk
	* fix %%mkrel still being incremented when a new
	  version is build.
	* fix cvs Id expansion

