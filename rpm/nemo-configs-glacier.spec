Name:       nemo-configs-glacier
Summary:    Qt/QQC configs for nemo-configs-glacier
Version:    0.0.0
Release:    0
Group:      Configs
License:    Public Domain
URL:        https://github.com/nemomobile-ux/nemo-configs-glacier
Source0:    %{name}-%{version}.tar.gz

%description
Qt/QQC configs for nemo-configs-glacier

%prep
%setup -q -n %{name}-%{version}

%install

# conf
install -m 0644 conf/70-nemo-mobile-glacier.conf %{buildroot}/var/lib/environment/nemo/

%files
%defattr(-,root,root,-)
%config /var/lib/environment/nemo/70-nemo-mobile-glacier.conf

