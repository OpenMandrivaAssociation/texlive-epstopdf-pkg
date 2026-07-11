%global tl_name epstopdf-pkg
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.11
Release:	%{tl_revision}.1
Summary:	Call epstopdf on the fly
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/epstopdf-pkg
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf-pkg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf-pkg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epstopdf-pkg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(epstopdf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds support for EPS files in the graphicx package when
running under pdfTeX. If an EPS graphic is detected, the package spawns
a process to convert the EPS to PDF, using the script epstopdf. This of
course requires that shell escape is enabled for the pdfTeX run.

