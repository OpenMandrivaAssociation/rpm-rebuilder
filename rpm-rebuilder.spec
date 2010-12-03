%define name	rpm-rebuilder
%define version	0.28
%define release %mkrel 5

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

