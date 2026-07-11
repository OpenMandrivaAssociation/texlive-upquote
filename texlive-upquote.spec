%global tl_name upquote
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Show realistic quotes in verbatim
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/upquote
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upquote.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upquote.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/upquote.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typewriter-style fonts are best for program listings, but Computer
Modern Typewriter prints ` and ' as bent opening and closing single
quotes. Other fonts, and most programming languages, print ` as a grave
accent and ' upright; ' is used both to open and to close quoted
strings. The package switches the typewriter font to Computer Modern
Typewriter in OT1 encoding, and modifies the behaviour of verbatim,
verbatim*, \verb, and \verb* to print in the "` and ' way". It does this
regardless of other fonts or encodings in use, so long as the package is
loaded after the other fonts were. The package does not affect \tt,
\texttt, etc.

