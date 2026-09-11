# Agent FSM Guardrails

A finite-state-machine validation layer that constrains LLM agent behavior to prevent invalid or off-script actions.

## Problem

LLM agents can drift off-task or skip steps. This project validates agent actions against a defined set of states and allowed transitions before they're executed.

## Status

Early WIP — building out the core FSM logic and a first demo scenario.

## Tech Stack

Python, LLM API, pytest
