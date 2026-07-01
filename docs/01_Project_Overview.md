# Project Overview

## Purpose

This document summarizes the project direction for the DACON AI Agent action prediction competition.

## Competition

- Competition: DACON AI Agent action prediction
- Task: Predict the next assistant action among 14 predefined classes
- Input: Session metadata, interaction history, and the current user prompt
- Output: One action label per sample
- Status: Planned

## Why This Matters

AI coding agents need to decide when to inspect files, search, edit, run commands, ask questions, or respond directly. This competition frames that decision process as a supervised classification problem.

## Project Goals

- Build a reliable baseline pipeline
- Analyze action patterns across metadata, history, and prompts
- Improve validation performance through feature engineering and model selection
- Keep a clear experiment trail for collaboration and portfolio review

## Scope

| Area | Status | Notes |
| --- | --- | --- |
| Data understanding | Planned | EDA notebook and documentation |
| Baseline reproduction | Planned | Compare with provided baseline submission |
| Feature engineering | Planned | Metadata, history, and text features |
| Model optimization | Planned | Classical ML and transformer-based approaches |
| Error analysis | Planned | Confusion matrix and mistake review |
| Final report | Planned | Competition summary and portfolio write-up |

## Links

- [Competition Rules](https://dacon.io/competitions/official/236694/overview/rules)
- [Competition Description](https://dacon.io/competitions/official/236694/overview/description)
- [Main README](../README.md)
