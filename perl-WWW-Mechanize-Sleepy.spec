%define upstream_name    WWW-Mechanize-Sleepy
%define upstream_version 0.7

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	WWW::Mechanize::Sleepy - A Sleepy Mechanize Agent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Sometimes when testing the behavior of a webserver it is important
to be able to space out your requests in order to simulate a
person reading, thinking (or sleeping) at the keyboard.

WWW::Mechanize::Sleepy subclasses WWW::Mechanize to provide pauses
between your server requests. Use it just like you would use
WWW::Mechanize.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

# make test don't work...
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Sleepy.pm
%{_mandir}/*/*


%changelog
* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.700.0-1mdv2011.0
+ Revision: 596700
- update to 0.7

* Sat Feb 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.600.0-1mdv2011.0
+ Revision: 505370
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2010.0
+ Revision: 430657
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.6-3mdv2009.0
+ Revision: 242155
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.6-1mdv2008.0
+ Revision: 20749
- 0.6


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.5-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5-1mdk
- initial Mandriva package

