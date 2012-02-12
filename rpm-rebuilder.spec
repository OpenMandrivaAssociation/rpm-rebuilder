Summary:	Tools to build/check distributions
Name:		rpm-rebuilder
Version:	0.28
Release:	7
License:	GPL
Group:		System/Configuration/Packaging
URL:		http://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		rpm-rebuilder-svn_fixes.diff
Requires:	rpmlint
Requires:	strace
Requires:	rpm-build
Requires:	diffutils
BuildArch:	noarch

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
%patch0 -p1

%build

%install

make install

%files
%doc AUTHORS README README.CVS ChangeLog
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/rpm-rebuilder
