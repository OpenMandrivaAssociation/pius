Name:      pius
Version:   2.0.9
Release:   1
Summary:   A tool for signing and emailing all UIDs on a set of PGP keys

Group:     Networking/Mail
License:   GPLv2
URL:       http://www.phildev.net/pius
Source0:   http://downloads.sourceforge.net/project/pgpius/pius/2.0.9/%{name}-%{version}.tar.bz2
BuildArch: noarch

BuildRequires:  python-devel
Requires:  python

%description
The PGP Individual UID Signer (PIUS) is a tool for individually
signing all of the UIDs on a set of keys and encrypt-emailing each
one to it's respective email address. This drastically reduces the time
and errors involved in signing keys after a key signing party.

%prep
%setup -q 

%build

%install
install -pdm 755 %{buildroot}%{_bindir}
install -p  %{name} %{name}-* -t %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-keyring-mgr
%{_bindir}/%{name}-party-worksheet
%doc README README.keyring-mgr COPYING %{name}.spec
