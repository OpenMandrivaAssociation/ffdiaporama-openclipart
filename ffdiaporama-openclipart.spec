Name:           ffdiaporama-openclipart
Summary:        This is ffDiaporama extension for Openclipart
Version:        1.0
Release:        1
License:        GPLv2
Group:          Graphics
URL:            http://ffdiaporama.tuxfamily.org/?page_id=9273

BuildArch:      noarch
BuildRequires:  openclipart = 0.18
BuildRequires:  ffdiaporama >= 2.2

Requires(preun):ffdiaporama >= 2.2
Requires:       openclipart = 0.18

%description
This extension allows you to use the openclipart database (version 0.18)
with ffDiaporama. This database contains nearly 13,000 free clipart in .svg
format (vector). These cliparts are available in ffDiaporama under the
"clipart" entry of the directory tree in multimedia file browser.

%prep
#nothing

%build
#nothing

%install
install -d %{buildroot}%{_datadir}/ffDiaporama/clipart/openclipart
ln -s %{_datadir}/clipart/openclipart/* %{buildroot}%{_datadir}/ffDiaporama/clipart/openclipart


%files
%{_datadir}/ffDiaporama/clipart/openclipart
