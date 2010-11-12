%define upstream_name    WWW-Mechanize-Sleepy
%define upstream_version 0.7

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	WWW::Mechanize::Sleepy - A Sleepy Mechanize Agent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# make test don't work...
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Sleepy.pm
%{_mandir}/*/*
