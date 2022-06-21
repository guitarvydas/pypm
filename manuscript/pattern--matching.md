{id: pattern--matching}
---
tags:
- pm
---
[pm introduction](#pm--introduction)
[SCN](#scn)
[ww-book-parsing Idioms/scn](#ww-book-parsing--idioms/scn)
# Parsing Basics 
    [Parsing Basics](#parsing--basics)
    [Control Flow in Parsing](#control--flow--in--parsing)
    [Parser Overview](#parser--overview)
    [Parse Tree](#parse--tree)
    [Parse Tree With Holes](#parse--tree--with--holes)
    [Parsers Are Tree Builders](#parsers--are--tree--builders)
    [Parsers Help With Tree-Walking](#parsers--help--with--tree-walking)
    [Parsing - Creating Semantics Dynamically](#parsing-----creating--semantics--dynamically)
    [Bare Parse Tree](#bare--parse--tree)
    [One Parse Tree Approach](#one--parse--tree--approach)
    [Pipeline of Many Parse Trees Approach](#pipeline--of--many--parse--trees--approach)
    [regex](#regex)

# Getting Started
[pm Getting started](#pm--getting--started)
[pm Small steps](#pm--small--steps)
[pm Hamburger Workbench](#pm--hamburger--workbench)
# Idioms
[pm Idioms](#pm--idioms)
# Advanced Idioms
## Syntax Stacks
[pm Syntax Stacks](#pm--syntax--stacks)
## Verbatim
[pm Verbatim Code](#pm--verbatim--code)
## Symbols Containing Whitespace
[pm compound identifiers](#pm--compound--identifiers)
# Examples
[pm math](#pm--math)
[pm Parsing C](#pm--parsing--c)
[pm Transpiling Scheme to JavaScript](#pm--transpiling--scheme--to--javascript)
# Macros
[pm Macros](#pm--macros)
[pm Prep](#pm--prep)
# Components
[2022-06-17-Ohm As A Component](#2022-06-17-ohm--as--a--component)
- [ ] PROLOG for backtracking
- [ ] Ohm has backtracking, too - is that good enough?
- [ ] miniKanren maybe for exhaustive search
# Other Features
[pm Other Features of Ohm-JS](#pm--other--features--of--ohm-js)
# Exercises
[pm Exercises](#pm--exercises)
# Appendix - Using Ohm-JS
[ww-book-parsing Idioms/pm using Ohm](#ww-book-parsing--idioms/pm--using--ohm)
[pm Ohm Editor Brief Introduction](#pm--ohm--editor--brief--introduction)
# Appendix - What Is So Good About Ohm-JS?
[ww-book-Hamburger Workbench - A Gentle Introduction to Ohm-JS/Why You Need To Learn Ohm-JS](#ww-book-hamburger--workbench-----a--gentle--introduction--to--ohm-js/why--you--need--to--learn--ohm-js)
[whyohm](#whyohm)
# Appendix - Other Parsing Technologies
[pm Appendix Other Technologies](#pm--appendix--other--technologies)
# Appendix - Various Issues Related to Pattern Matching
[pm Interpreting vs. Compiling](#pm--interpreting--vs.--compiling)
- [ ] syntax-driven programming, sequencing
- [ ] diagram parsing

# Appendix - Ohm-JS
[ohmjs.org](https://ohmjs.org()
# Appendix - Language Theory vs. PEG
[[ww-book-parsing Idioms/Language Theory vs PEG]]