---
documentclass: pprai
title: "Text data mining: a case study of Reddit"
author: 
# - "Piotr Sokołowski$^{1[0009-0005-8181-6275]}$"
- "Piotr Sokołowski$^{1}$"
- "Marcin Kosiba$^{2}$"
- "Michał Pałucki$^{3}$"
numberSections: true
autoSectionLabels: true
codeBlockCaptions: true
bibliography:
- src/bibliografia.bib
- from-doi.bib
abstract: |
  The article describes the progress of a project on text data mining performed by software engineering students. The article presents information about the source of the text data, how it was acquired and cleaned. The process of selecting classifiers for categorizing posts is described, and the results of different models are compared.
header-includes:
- \graphicspath{{./src/}}
- \usepackage{tikz}
- \usepackage{txfonts}
- \usepackage{subfig}
- \input{pprai_proc.inc}
- \headauthor{P. Sokołowski, M. Kosiba and M. Pałucki}
- "\\headtitle{Text data mining: a case study of Reddit}"
- |
  \affiliation{%
    $^{1,2,3}$AGH University of Krakow\\
    Department of Applied Computer Science\\
    Al. Mickiewicza 30, 30-059 Kraków, Poland\\
    $^1$psokolowski@student.agh.edu.pl, $^2$mkosiba@student.agh.edu.pl, $^3$palucki@student.agh.edu.pl}
- \keywords{data mining, reddit, classification, clustering, scikit-learn, tensorflow, machine learning}
---