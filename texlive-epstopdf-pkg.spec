Name:		texlive-epstopdf-pkg
Version:	71084
Release:	1
Summary:	Call epstopdf "on the fly"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epstopdf-pkg
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf-pkg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf-pkg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf-pkg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds support for EPS files in the graphicx package
when running under pdfTeX. If an EPS graphic is detected, the
package spawns a process to convert the EPS to PDF, using the
script epstopdf. This of course requires that shell escape is
enabled for the pdfTeX run.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/epstopdf-pkg
%{_texmfdistdir}/tex/latex/epstopdf-pkg
%doc %{_texmfdistdir}/doc/latex/epstopdf-pkg

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
