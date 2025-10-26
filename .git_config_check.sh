#!/bin/bash
# Script para verificar y configurar git
cd /Users/joseassizalcarazbaxter/Developer/iphone/app

echo "=== GIT STATUS ===" > git_info.txt
git status 2>&1 >> git_info.txt

echo "" >> git_info.txt
echo "=== GIT LOG ===" >> git_info.txt
git log --oneline -5 2>&1 >> git_info.txt

echo "" >> git_info.txt
echo "=== GIT BRANCH ===" >> git_info.txt
git branch -a 2>&1 >> git_info.txt

echo "" >> git_info.txt
echo "=== GIT REMOTE ===" >> git_info.txt
git remote -v 2>&1 >> git_info.txt

echo "Info written to git_info.txt"

