# $Id $

# Authority: dries
# Upstream: 

Summary: Print source code in a variety of languages to postscript
Name: trueprint
Version: 5.3
Release: 1
License: GPL
URL: http://www.gnu.org/software/trueprint/trueprint.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://ftp.gnu.org/gnu/trueprint/trueprint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
GNU Trueprint takes C source files and other text files and prints them on
PostScript printers. It is intended to be used by programmers; therefore, it
includes features like diff-marking, indentation count, function and file
indices, and many others that are useful when printing source code. 

It currently supports C and has more limited support for other languages,
including C++, Java, and Perl.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc

%changelog
* Thu Apr 22 2004 Dries Verachtert <dries@ulyssis.org> 5.3-1
- Initial package
