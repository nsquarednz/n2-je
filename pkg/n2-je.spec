Name: %(echo $PACKAGE)
Version: %(echo $VERSION)
# Release is passed through to our script. We concatenate on the dist flag.
# Dist is a magic variable that will populate our version. I.E. EL8.
Release: %(echo $RELEASE)%{?dist}
Summary: Pure Perl ECMAScript (JavaScript) engine.
Group: Development/Languages/Perl
License: Perl
URL: https://metacpan.org/pod/JE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%global _binaries_in_noarch_packages_terminate_build 0

#BuildProvides:
# Define the export that this module provides.
Provides: perl(JE)

#BuildRequires:
# No current additional dependencies.

%description
N-Squared Software fork of 0.0XX of the Perl JE library.

%post

#
# All build steps are done by build-packages.sh.
#

%prep

#
# All build steps are done by build-packages.sh.
#

%build

#
# All build steps are done by build-packages.sh.
#

%install

rm -rf %{buildroot}
cp -r %{_builddir} %{buildroot}
find %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)

# Include core files needed to execute the library code.
/usr/local/share/perl5/JE.pm
/usr/local/share/perl5/JE/Boolean.pm
/usr/local/share/perl5/JE/Code.pm
/usr/local/share/perl5/JE/Destroyer.pm
/usr/local/share/perl5/JE/LValue.pm
/usr/local/share/perl5/JE/Null.pm
/usr/local/share/perl5/JE/Number.pm
/usr/local/share/perl5/JE/Object.pm
/usr/local/share/perl5/JE/Object/Array.pm
/usr/local/share/perl5/JE/Object/Boolean.pm
/usr/local/share/perl5/JE/Object/Date.pm
/usr/local/share/perl5/JE/Object/Error.pm
/usr/local/share/perl5/JE/Object/Error/RangeError.pm
/usr/local/share/perl5/JE/Object/Error/ReferenceError.pm
/usr/local/share/perl5/JE/Object/Error/SyntaxError.pm
/usr/local/share/perl5/JE/Object/Error/TypeError.pm
/usr/local/share/perl5/JE/Object/Error/URIError.pm
/usr/local/share/perl5/JE/Object/Function.pm
/usr/local/share/perl5/JE/Object/Math.pm
/usr/local/share/perl5/JE/Object/Number.pm
/usr/local/share/perl5/JE/Object/Number/maxvalue.pl
/usr/local/share/perl5/JE/Object/Proxy.pm
/usr/local/share/perl5/JE/Object/RegExp.pm
/usr/local/share/perl5/JE/Object/String.pm
/usr/local/share/perl5/JE/Parser.pm
/usr/local/share/perl5/JE/Scope.pm
/usr/local/share/perl5/JE/String.pm
/usr/local/share/perl5/JE/Types.pod
/usr/local/share/perl5/JE/Undefined.pm
/usr/local/share/perl5/JE/_FieldHash.pm
/usr/local/share/perl5/JE/escape.pl
/usr/local/share/perl5/JE/toperl.pl
/usr/local/share/perl5/JavaScript/Engine.pm

# Bundle the JE man pages.
/usr/local/share/man/man3/JE.3pm
/usr/local/share/man/man3/JE::Boolean.3pm
/usr/local/share/man/man3/JE::Code.3pm
/usr/local/share/man/man3/JE::Destroyer.3pm
/usr/local/share/man/man3/JE::LValue.3pm
/usr/local/share/man/man3/JE::Null.3pm
/usr/local/share/man/man3/JE::Number.3pm
/usr/local/share/man/man3/JE::Object.3pm
/usr/local/share/man/man3/JE::Object::Array.3pm
/usr/local/share/man/man3/JE::Object::Boolean.3pm
/usr/local/share/man/man3/JE::Object::Date.3pm
/usr/local/share/man/man3/JE::Object::Error.3pm
/usr/local/share/man/man3/JE::Object::Error::RangeError.3pm
/usr/local/share/man/man3/JE::Object::Error::ReferenceError.3pm
/usr/local/share/man/man3/JE::Object::Error::SyntaxError.3pm
/usr/local/share/man/man3/JE::Object::Error::TypeError.3pm
/usr/local/share/man/man3/JE::Object::Error::URIError.3pm
/usr/local/share/man/man3/JE::Object::Function.3pm
/usr/local/share/man/man3/JE::Object::Math.3pm
/usr/local/share/man/man3/JE::Object::Number.3pm
/usr/local/share/man/man3/JE::Object::Proxy.3pm
/usr/local/share/man/man3/JE::Object::RegExp.3pm
/usr/local/share/man/man3/JE::Object::String.3pm
/usr/local/share/man/man3/JE::Parser.3pm
/usr/local/share/man/man3/JE::Scope.3pm
/usr/local/share/man/man3/JE::String.3pm
/usr/local/share/man/man3/JE::Types.3pm
/usr/local/share/man/man3/JE::Undefined.3pm
/usr/local/share/man/man3/JE::_FieldHash.3pm
/usr/local/share/man/man3/JavaScript::Engine.3pm

%changelog
