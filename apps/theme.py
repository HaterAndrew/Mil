"""Shared USAREUR-AF branding theme for all MSS Training Analytics dashboards.

Injects custom CSS matching the MSS Training Hub (index.html) and
Dependency Map visual identity: Navy (#0C2340) + Gold (#C8971A).
"""

from __future__ import annotations

import streamlit as st

# ---------------------------------------------------------------------------
# USAREUR-AF Command Color Palette
# ---------------------------------------------------------------------------
NAVY = "#0C2340"
NAVY_DARK = "#071628"
NAVY_LIGHT = "#163A6C"
NAVY_MID = "#1E4A88"
NAVY_PALE = "#EEF2FA"

GOLD = "#C8971A"
GOLD_LIGHT = "#E0B840"
GOLD_DARK = "#9A7010"
GOLD_PALE = "#FDF5DC"

WHITE = "#FFFFFF"
OFF_WHITE = "#F3F5FA"
GRAY_50 = "#EFF1F8"
GRAY_100 = "#E0E4EF"
GRAY_200 = "#C4CAE0"
GRAY_400 = "#7A88A8"
GRAY_600 = "#485878"
GRAY_700 = "#303C58"
GRAY_900 = "#0A1628"

WARNING_RED = "#8A1A1A"
CAUTION_AMBER = "#B86810"
NOTE_TEAL = "#0A5C70"
GREEN_OK = "#1A5C28"
CUI_PURPLE = "#502B85"

# RAG status colors (military standard)
RAG_GREEN = "#1A5C28"
RAG_AMBER = "#B86810"
RAG_RED = "#8A1A1A"

# ---------------------------------------------------------------------------
# USAREUR-AF Insignia (base64 SVG for embedding)
# ---------------------------------------------------------------------------
_INSIGNIA_B64 = (
    "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iNDEwLjEzIiBoZWlnaHQ9IjUzNy44MyIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMjQ2LjA4IDMyMi43IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJtMTIzLjA0IDEuMjAwMmMtNjYuNzc0LTAuMTAzMzctMTIxLjg0IDM2LjEyOS0xMjEuODQgMzYuMTI5cy0wLjQxOTM2IDEwMi44MSAzMS42MzUgMTY3Ljg2YzM4LjU0MiA3OC4yMjEgODcuOTU1IDExNC41MyA5MC4wMTQgMTE2LjAydjAuMjg3MTFzMC4xNzgzNi0wLjEzNjU2IDAuMTg5NDUtMC4xNDQ1M2MwLjAxMTEgOGUtMyAwLjE4OTQ1IDAuMTQ0NTMgMC4xODk0NSAwLjE0NDUzdi0wLjI4NzExYzIuMDU4My0xLjQ5MSA1MS40NzEtMzcuNzk5IDkwLjAxNC0xMTYuMDIgMzIuMDU0LTY1LjA1MyAzMS42MzUtMTY3Ljg2IDMxLjYzNS0xNjcuODZzLTU1LjA2NC0zNi4yMzItMTIxLjg0LTM2LjEyOXoiIGZpbGw9IiMxNzE2OTUiLz4KPHBhdGggZD0ibTEyMy45NyA3NS4xNzljLTM4LjIzOC0wLjAzOTc4LTc4LjcxNyAyMi4wMzMtMTAyLjgzIDUxLjcxMSAxOC4xNjEgMTA5LjM5IDEwMi44MyAxNzguODYgMTAyLjgzIDE3OC44NnM4NC42NjctNjkuNDYxIDEwMi44My0xNzguODZjLTI0LjExMS0yOS42NzgtNjQuNTktNTEuNzUxLTEwMi44My01MS43MTF6IiBmaWxsPSJub25lIiBzdHJva2U9IiMyNTI1NDEiIHN0cm9rZS13aWR0aD0iMiIvPgo8cGF0aCBkPSJtMTE3LjY1IDIwMC4xNWMwLjIyMjc2LTI0LjE2MyAwLjcyNDI5LTQ4LjMzMSAwLjc2NDc0LTcyLjQ5MS0zLjQwOTMtMi43MTYtNi4xNzcxLTcuMDUtNS43ODU2LTExLjU0NiAxLjk3ODktNS45NTk3IDEuNzQ0My0xMy44MDMtMy45NTgyLTE3LjYzNiAxLjg0MzMgNS4wMTcxIDAuMjY2NDUgMTAuMzI1LTIuMDMyMSAxNC44OTMtMy4yMjYgNi44MTI0LTMuMjUxNCAxNS44MjYgMi4zNDE3IDIxLjQ4IDMuNzY1NyAzLjU0NDIgNC44OTQyIDguOTI4NCA0LjEzMzggMTMuODg4LTAuOTA3MDEtNC4xNTkyLTMuMTg1NC04LjI2OS03LjA1OTItMTAuNDUzLTIuNjg1OC0xLjQyMzItNi4wOTM1LTIuMjAxMi03LjY4LTUuNDMwMy0xLjg0NTUtNC42MjI4IDAuNTc3MTktMTAuODgzLTMuNjY0LTE0LjY1NS0yLjExNTMtMi43NTQzLTAuNjA5OTIgMi44NDg4LTEuNDUyMyA2LjAwNS0yLjcyMjcgNi45OTc1LTIuNzM2IDE2LjY4OCAzLjk1MTggMjEuNDIxIDcuMDIwMyAzLjA1MSAxMS45MyAxMC4zNDcgMTQuMjQ0IDE3LjY0NCAwLjY0MDUzIDIuODU3MyAzLjYzNTMgOS44MjktMS4wMjYgNS4wOTQ5LTIuMDg2Ny0xLjQ0NTItNC43NjM0LTEuNTM2NC03LjIwMzMtMi4xOTYtMi4yMTExLTAuOTc2MTktNC42NDg0LTIuMTUzNS01Ljg2NDctNC42MzA3LTEuMjUyNS02Ljc1NTktMy42NDM5IDMuMDk1OS0yLjUzNTQgNS43OTc1IDAuNzUwMTIgMy4yODU4IDMuNTQxNSA1Ljg2ODYgNi41MzY4IDYuNzg5MiA1LjM2NTcgMi40NjAyIDEwLjAxMyA3LjY2MDEgMTEuNDE2IDEzLjY1OCAxLjQ4OTUgMy45MzA0IDAuMDM0MyAxLjg3NjctMi4zNDk1IDEuNDg4Mi00LjE2MzYtMC42Nzg1Mi04LjcwMDktMS4xMTI1LTguNjYyNi02LjM5MzUtMS41NTg4IDIuNjQzOS0wLjM1NzM1IDkuOTQ2MiAzLjI2NzQgMTIuNzgxIDQuMTgwNCAzLjkyNTMgOC41MDE0IDguNjY3OCA3Ljc5MTIgMTQuODQ4LTEuMzQyNi0xLjA2NzgtMy40NDQ5LTYuNDE1Ny02LjY2MjItOC4wMDg2LTIuNTkxMy0xLjI4My01LjUxOTQtMS42OTA5LTguNDI2Ny0xLjkyLTQuMjYyOC0wLjMzNTk2LTUuNTIzNi03LjA3NTgtNi4yNzgtOC4xNi0yLjEzNTMgNi4yODQyLTEuNzQ3NCAxNC4zNjEgNC4xNDQ3IDE4LjQgMS44NzQ1IDEuMzkwMiAzLjg2NjIgMS45NjYyIDUuNzYgMy4yIDYuMTIzNCAzLjYxNiAxMi41NDEgOS4xNTk4IDEyLjg2NiAxNi44NzYtMi4xOTI2LTEuNTE3Ni00LjM1OS0xLjk5NjMtNi44OTMxLTIuNTQ4OC01LjEyNDQtMS4xNjE2LTYuMzgyOC0zLjIxMzYtNy42MTczLTUuNjA1NC0xLjQwNjggMy43Mzg1LTEuNDA3NiA5LjA0NyAyLjYwNCAxMS4zMzIgMi4zMDkyIDEuMjM2NCA1LjA0OTkgMS42NTE5IDcuMzYgMi43NzMzIDMuMjkwMyAxLjUyOTQgNi4xNyA0LjUxMTYgNy41MzY4IDcuOTU0MiAwLjE2MTM4LTE0Ljg4MyAwLjI0NTY5LTI5Ljc2NiAwLjQzMDgxLTQ0LjY0OHptMTEuNzg3IDQ0LjM2YzIuMDUyOC0zLjQzMjUgNS45MTc1LTYuMTMwNiA5LjI1ODItNy42NjY1IDMuMTY0NC0xLjcwODggNS40NjAxLTUuMjU2NCA2LjQxMjYtOC44NjMzIDAuOTc4Mi0yLjU0OTYgMy4xNDA2LTQuNjg2MyA1LjUzNDEtNS41MTkyLTEuNDU5NS0yLjM2MzUtNy43MTQ1LTEuMDE2MS04Ljk3NDQgMi4yMjI2LTEuMjQwMiAyLjE5NDEtMi4wMTg2IDYuMjM5NS00Ljg1MzggNi42MDAyLTEuODM4Ni00Ljc4MTggMS44MzkxLTkuMzIyOCA1LjcyMTYtMTEuNzIgNC43NTEtMi43MTczIDUuOTQwMy04LjQ4MjIgNS42NjgxLTEzLjU2MS0wLjQ3MzIzLTIuNjYyOCAzLjU5NTYtNy40Mzc2LTAuOTc0NzctNC43ODYyLTMuMzgwNiAyLjE5NDgtMy45OTQ5IDYuMjIxOS02LjQ1OTYgOC45Ni0xLjczMjMgMS4yODQ2LTYuNjE4OSA1LjE2NjEtNC45MjA2IDAuMjYwMS0wLjE1Mzg2LTYuMjE2NSA2LjIzMTgtOS4zODA4IDcuNjQyNS0xNS4wMDkgMi4wMTgyLTUuMzg0MSAxLjM5OTItMTIuMTQ5IDYuMzYyNi0xNi4wMDMgMS4xNTgxLTEuMzMwOSAzLjcyOTItMS40NTEzIDQuNDcxNy0yLjQ2NTMtMi42NDA5LTAuODE5NTYtNS42NTEzLTEuOTc4Mi04LjQ4MzMtMC45MTYtNC4wMTM1IDAuOTUwNC01LjgxMjMgNS42MDg2LTYuODUwOCA5LjM1MjEtMC44NDUxNiAyLjMzODgtMy44MjYgOC4xMzIzLTUuMzEyMyA2Ljc3OTQtMC43MzA5NC01LjQwODcgMC40MjI3Mi0xMS4xMyA0LjM4MjgtMTUuMDUyIDMuMTU1Ni0zLjExMzkgNy42MjY0LTUuNDAxOCA3LjczMjUtMTAuNDc4IDAuODU1ODUtNS44NDI0IDAuMjQxMTktMTIuODU3IDUuMTY3OS0xNy4wNTQgMS4yMzI0LTEuNjI3OCA0LjgzOTItMS43MzY1IDUuMzMzMy0yLjU2LTIuMzc0MS0xLjQ1NDMtNS42NjI1LTIuMjY0OS04LjUzMzMtMS4yOC00Ljc0OTIgMS41MzMtOC4yMzE1IDYuNzcyNy04Ljg2MzkgMTEuNzc0LTAuMTUgMi40NTI0LTMuMzE0OSA5LjU5MS00LjY1NjMgNy41ODMgMC4wOTMxLTcuODU5MiAwLjc0MTkyLTE2LjY3NSA2LjU4NjktMjIuNTQ5IDMuNjQ3LTQuMjU3MyA0LjY4MDItMTEuMDMyIDIuMTMzMy0xNi4wMDgtMy4yMjIxLTUuNDE3Mi0yLjg5NDMtMTIuNjczLTAuMTAzNTctMTguMzUzIDAuMzM4OTYtMS44MDExLTMuNzI4MiAwLjM0MjI1LTQuODQ2NSAxLjE0OTQtNC42MTI1IDMuNTU1My0yLjYwMzYgOS43ODU3LTIuNjM4MSAxNC42ODQtMC4yNjAyMyA0LjQ0NzUtMi4zMTU4IDkuNDgwOS02LjcwNDkgMTEuMTE1LTEuODg5MiAwLjMyMTU4LTAuNzA5MDQgMi43OTY4LTEuMDAzNiA0LjMzMzUgMC40NzYxMSAzNS4wNDMgMC4yNTMxNyA3MC4wOTEgMC45NzE1MiAxMDUuMTMgMC4wNzcxIDIuNTg0NyAwLjA3NyAxLjA2MTYgMC44MDAyMy0wLjA5OTd6IiBmaWxsPSIjYmExMjJiIiBzdHJva2Utd2lkdGg9Ii4yMTMzMyIvPgo8cGF0aCBkPSJtMTIyLjg3IDg1LjkyNy0wLjE3NzczIDAuMzEyNS0zLjg3MTEgOC4xOTkyLTEuNjk3MyAxNTIuNTFjMy44MDE1IDAuNjc4NCA3Ljc3NTUgMC43ODYyIDExLjU4NCAwLjE0ODQ0bC0xLjM5MDYtMTUyLjQ0eiIgZmlsbD0iI2ZmZiIgc3Ryb2tlLXdpZHRoPSIuMjEzMzMiLz4KPHBhdGggZD0ibTg5LjEyNiAyMzcuNThjLTEuODcxNyAwLjAzMzQtMy45MzIyIDAuNTg3MTYtNS4wNzQyIDEuNDI3Ny0xLjM2NjQgMS4wMDU3LTIuNTA4IDMuNzg1MS0xIDQuNTYyNSAyMC40NzUgMTAuNTU2IDMzLjcwMSA5LjYxOTEgMzMuNzAxIDkuNjE5MWwtMC45NTExNyAzMy4xMzFzMC4yNzY4OCAzLjExMDkgNi4yNSAzLjI1YzguNjIzIDAuMjAwOCA4LjEyNS0zLjg3NSA4LjEyNS0zLjg3NWwtMC42NDg0NC0zMi41MDZjMi4yOTYgMC4wNTc3IDE0Ljc2MiAwLjA4MDQgMzMuMjIxLTkuNDM1NiAxLjUwOC0wLjc3NzQzIDAuMzY2MzktMy41NTY4LTEtNC41NjI1LTEuODI3Mi0xLjM0NDktNi4wMDU4LTEuOTU3MS04LTAuODc1LTEzLjI0NyA3LjE4ODItMTUuOTk5IDcuNjA4NS0yNS4wMjkgOS4yMjI3LTRlLTMgLTAuMDI1OSA5ZS01IC04LjllLTQgLTRlLTMgLTAuMDI3NC0zLjgxNDEgMC42Mzk0OC03Ljc5NDYgMC41MzAyMS0xMS42MDItMC4xNTAzOS05LjA1ODgtMS42MTk1LTExLjc5OC0yLjAzMDgtMjUuMDYyLTkuMjI4NS0wLjc0NzgxLTAuNDA1NzgtMS44MDI4LTAuNTcyNzYtMi45MjU4LTAuNTUyNzR6IiBmaWxsPSIjZmZjNjFkIi8+CjxwYXRoIGQ9Im0xMjQuMTYgMTMuMTk4Yy01Mi43OS0wLjY4NzcyLTEwOC4zMiAzMC40NjMtMTA5Ljg5IDMxLjM1IDEuMDAzNSAxNC4xMzEgMS44NDg0IDI4LjIzMyAzLjA0MyA0Mi4yODEgNi4xNDY3LTUuNTA2NiAxNC43ODItMTIuNTM5IDI1LjkxMi0xOS4yNDQgMTkuMzk3LTExLjY4NSA0Ni40MDgtMjIuNDQ2IDgwLjg5NS0yMi42OTloMC4wNDNjMzQuNDg2IDAuMjUyOTkgNjEuNDk4IDExLjAxNCA4MC44OTUgMjIuNjk5IDEwLjM1IDYuMjM1NCAxOC41MDUgMTIuNzMxIDI0LjU1MSAxOC4wNDUgMS4wNTk4LTEzLjc2MyAyLjAwNjQtMjguMTggMi42MTUyLTQwLjg1LTEuNTI0Mi0wLjg3OTg3LTUzLjgyNS0zMC44NzUtMTA4LjA2LTMxLjU4MnptLTAuMDE3NiAzNy42ODhjLTMzLjI1MyAwLjI0ODQyLTU5LjEzOSAxMC41ODUtNzcuODIgMjEuODQtMTMuMDA2IDcuODM1NS0yMi4zMDcgMTUuOTU0LTI4LjMyOCAyMS42MTcgMC4wMzc2MSAwLjM5NDIyIDAuMDY5MDkgMC43ODk0NiAwLjEwNzQyIDEuMTgzNmwxMDUuMjItNDIuMDYyIDEwNS4yMSA0NS41MTZjMC4xNjIwMS0xLjg5NTQgMC4zMjExNi0zLjg2OTUgMC40ODA0Ny01LjgyMDMtNi4wMzQ1LTUuNTgzOC0xNC45MDYtMTMuMTE5LTI3LjA0OS0yMC40MzQtMTguNjgxLTExLjI1NC00NC41NjctMjEuNTkxLTc3LjgyLTIxLjg0eiIgZmlsbD0iIzhjOTlhMiIvPgo8cGF0aCBkPSJtMTI0LjEyIDQ0Ljg4NmMtMzQuNDg2IDAuMjUyOTktNjEuNDk4IDExLjAxNC04MC44OTUgMjIuNjk5LTExLjEzMiA2LjcwNjItMTkuNzYxIDEzLjczNC0yNS45MTIgMTkuMjQ0IDAuMjEzMTIgMi41MDYzIDAuNDQwOTQgNS4wMTExIDAuNjc5NjkgNy41MTM3IDYuMDI0OC01LjY2NTUgMTUuMzIzLTEzLjc4MyAyOC4zMjgtMjEuNjE3IDE4LjY4MS0xMS4yNTQgNDQuNTY3LTIxLjU5MSA3Ny44Mi0yMS44NCAzMy4yNTMgMC4yNDg0MiA1OS4xMzkgMTAuNTg1IDc3LjgyIDIxLjg0IDEyLjA5NyA3LjI4NzggMjEuMDA4IDE0LjgzNyAyNy4wNDkgMjAuNDIgMC4yMDMwNC0yLjQ4NjYgMC40MDE0Mi00Ljk3NjggMC41OTc2Ni03LjUyNTQtNi4wNDk3LTUuMzEyMi0xNC4yMjYtMTEuODE1LTI0LjU1MS0xOC4wMzUtMTkuMzk3LTExLjY4NS00Ni40MDgtMjIuNDQ2LTgwLjg5NS0yMi42OTloLTAuMDIxNXoiIGZpbGw9IiNiYTEyMmIiLz4KPHBhdGggZD0ibTEyNC4xMSA2Mi43OTJ2MmUtM2MtNTYuNDkyIDAuMDI0Ny05MS43NDcgMzIuNTg2LTEwNC40NiA0Ni43OTEgMC4zMjg5MiAyLjY1MzcgMC42NzgxNiA1LjMwNDcgMS4wNTY2IDcuOTUzMSA3LjU0ODgtOS40NzA4IDQyLjUwOC00OC43MyAxMDMuNDQtNDguNzQ0IDU5LjM2OCAwLjAxMzUxIDk0LjAyMSAzNy4yMzUgMTAyLjc0IDQ3LjkwNiAwLjI2MzE5LTIuNjA0OSAwLjUyODI5LTUuMzAzOCAwLjc5NDkyLTguMTc3Ny0xMy40OTUtMTQuNzE1LTQ4LjQyLTQ1LjcwNC0xMDMuNTEtNDUuNzI5di0yZS0zeiIgZmlsbD0iIzE0NGQyYSIvPgo8cGF0aCBkPSJtMTI0LjExIDU2Ljc2MXYyZS0zYy01Ni43MTQgMC4wMjQ0LTkzLjI4IDMyLjM3NC0xMDUuMzYgNDQuOTQ1IDAuMjg0NjUgMi42MzczIDAuNTcxOTggNS4yNzM4IDAuODk4NDQgNy45MDYyIDQuOTQ5OS01Ljg2NzMgNDEuNzUxLTQ2LjgzOCAxMDQuNDktNDYuODUyIDU5LjY3IDAuMDEzMzMgOTUuODc4IDM3LjA3NyAxMDMuNTQgNDUuNzU0IDAuMjM4MjYtMi41NjgzIDAuNDc2MTctNS4yMjEyIDAuNzEyODktNy45NTUxLTEzLjA2NS0xMy4yNTUtNDkuMDg4LTQzLjc3NS0xMDQuMjItNDMuNzk5di0yZS0zeiIgZmlsbD0iI2ZjYzkxNiIvPgo8cGF0aCBkPSJtMTI0LjExIDUwLjg4NnYwLjAwMzljLTU0LjEyMi0wLjA2NTQ2LTkwLjcwOSAyOC4zNTUtMTA2LjEzIDQzLjIwMSAwLjI0Mjc4IDIuNTU1MiAwLjUxMTU5IDUuMTA3MiAwLjc4NzExIDcuNjU4MiAxMS45ODktMTIuNTE2IDQ4LjUzNC00NC45NDggMTA1LjM4LTQ0Ljg2MSA1NS4yNjQtMC4wODQ1IDkxLjI2MyAzMC41MDUgMTA0LjI1IDQzLjcxMyAwLjIxNzg1LTIuNTE1MSAwLjQzMTI0LTUuMTE0NyAwLjY0NDUzLTcuNzMyNC0xNi4xMjItMTUuMTMxLTUyLjIwMi00Mi4wNDItMTA0Ljg2LTQxLjk3OXYtMC4wMDM5Yy0yZS0zIC00ZS02IC00ZS0zIDNlLTYgLTZlLTMgMGgtMC4wNjI1Yy0yZS0zIDNlLTYgLTRlLTMgLTRlLTYgLTZlLTMgMHoiIGZpbGw9IiNmYTllMGQiLz4KPHBhdGggZD0ibTIyNi44IDEyNi44OWMyLjI4My0xOS40MzQgNS4xNjc0LTU1LjMyMyA2LjQ2NTktODIuNjkxIDAgMC01My42ODMtMzEuMjc4LTEwOS4wOS0zMi01My45NTYtMC43MDI5MS0xMTAuOTUgMzEuNzY2LTExMC45NSAzMS43NjYgMS45ODI0IDI3Ljc3IDMuMjk0OCA1NS40ODQgNy45MTQ2IDgyLjkyNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMjUyNTQxIiBzdHJva2Utd2lkdGg9IjIiLz4KPC9zdmc+Cg=="
)
INSIGNIA_IMG = f'<img src="data:image/svg+xml;base64,{_INSIGNIA_B64}" {{0}} />'

# ---------------------------------------------------------------------------
# Plotly color sequences matching the brand
# ---------------------------------------------------------------------------
PLOTLY_NAVY_SEQ = [NAVY, NAVY_MID, NAVY_LIGHT, "#2563a8", "#3b7dd8", "#6ba0e8"]
PLOTLY_GOLD_SEQ = [GOLD_DARK, GOLD, GOLD_LIGHT, "#e8c850", "#f0d870"]
PLOTLY_MIXED_SEQ = [NAVY, GOLD, NAVY_MID, GOLD_DARK, NAVY_LIGHT, CAUTION_AMBER]
PLOTLY_RAG = [RAG_RED, RAG_AMBER, RAG_GREEN]
PLOTLY_STATUS = [NAVY, GREEN_OK, GOLD, WARNING_RED, GRAY_400]

# Colorscale for heatmaps (red → amber → green)
RAG_COLORSCALE = [
    [0.0, RAG_RED],
    [0.5, CAUTION_AMBER],
    [0.8, RAG_GREEN],
    [1.0, "#145020"],
]

# Colorscale for intensity (navy pale → navy dark)
NAVY_COLORSCALE = [
    [0.0, NAVY_PALE],
    [0.3, "#a0b8d8"],
    [0.6, NAVY_MID],
    [1.0, NAVY_DARK],
]

# ---------------------------------------------------------------------------
# Plotly layout defaults
# ---------------------------------------------------------------------------
PLOTLY_LAYOUT = dict(
    font=dict(family="Inter, Arial, Helvetica, sans-serif", color=GRAY_700),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=40, b=10),
    title_font=dict(size=14, color=NAVY, family="Arial, Helvetica, sans-serif"),
    xaxis=dict(gridcolor=GRAY_100, zerolinecolor=GRAY_200),
    yaxis=dict(gridcolor=GRAY_100, zerolinecolor=GRAY_200),
)


def apply_plotly_theme(fig):
    """Apply USAREUR-AF branding to a Plotly figure."""
    fig.update_layout(**PLOTLY_LAYOUT)
    return fig


# ---------------------------------------------------------------------------
# Streamlit CSS injection — matches MSS Training Hub styling
# ---------------------------------------------------------------------------
_CSS = f"""
<style>
/* === GLOBAL OVERRIDES === */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: Inter, system-ui, -apple-system, Arial, Helvetica, sans-serif;
}}

/* === HEADER BAR === */
header[data-testid="stHeader"] {{
    background: linear-gradient(155deg, {NAVY_DARK} 0%, {NAVY} 50%, {NAVY_LIGHT} 100%);
    border-bottom: 3px solid {GOLD};
}}

/* === SIDEBAR === */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {NAVY_DARK} 0%, {NAVY} 100%);
    border-right: 2px solid {GOLD_DARK};
}}

section[data-testid="stSidebar"] .stRadio label,
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div {{
    color: {WHITE} !important;
}}

/* Sidebar title styling */
section[data-testid="stSidebar"] h1 {{
    font-family: Arial, Helvetica, sans-serif !important;
    font-size: 20px !important;
    font-weight: bold !important;
    letter-spacing: 0.5px;
    border-bottom: 2px solid {GOLD_DARK};
    padding-bottom: 10px;
}}

/* Sidebar caption */
section[data-testid="stSidebar"] .stCaption span {{
    color: {GOLD_LIGHT} !important;
    font-size: 11px !important;
    letter-spacing: 1px;
    text-transform: uppercase;
}}

/* Sidebar radio buttons — active state */
section[data-testid="stSidebar"] .stRadio [data-checked="true"] {{
    border-left: 3px solid {GOLD} !important;
    background: rgba(255,255,255,0.07) !important;
}}

/* === MAIN CONTENT === */
.main .block-container {{
    max-width: 1280px;
    padding-top: 1.5rem;
}}

/* Page titles */
h1 {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {NAVY} !important;
    font-weight: bold !important;
    letter-spacing: 0.3px;
    border-bottom: 2px solid {GOLD_DARK};
    padding-bottom: 8px;
}}

h2, h3 {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {NAVY} !important;
    font-weight: bold !important;
}}

/* Captions */
.stCaption span {{
    color: {GRAY_400} !important;
    letter-spacing: 0.5px;
}}

/* === METRICS === */
div[data-testid="stMetric"] {{
    background: {WHITE};
    border: 1px solid {GRAY_100};
    border-top: 4px solid {NAVY};
    border-radius: 3px;
    padding: 12px 16px;
    box-shadow: 0 1px 5px rgba(0,0,0,0.08);
}}

div[data-testid="stMetric"]:hover {{
    border-top-color: {GOLD};
    box-shadow: 0 4px 12px rgba(12,35,64,0.12);
    transform: translateY(-1px);
    transition: all 0.2s ease;
}}

div[data-testid="stMetric"] label {{
    font-family: Arial, Helvetica, sans-serif !important;
    font-size: 11px !important;
    font-weight: bold !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: {GRAY_400} !important;
}}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {{
    font-family: Arial, Helvetica, sans-serif !important;
    color: {NAVY} !important;
    font-weight: bold !important;
}}

/* === DATAFRAMES === */
.stDataFrame {{
    border: 1px solid {GRAY_100};
    border-radius: 3px;
    overflow: hidden;
}}

/* === BUTTONS === */
.stButton > button {{
    background: {NAVY};
    color: {WHITE};
    border: 1px solid {NAVY_LIGHT};
    border-radius: 3px;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    padding: 8px 20px;
}}

.stButton > button:hover {{
    background: {NAVY_LIGHT};
    border-color: {GOLD};
    color: {GOLD_LIGHT};
}}

.stLinkButton > a {{
    background: {NAVY} !important;
    color: {WHITE} !important;
    border: 1px solid {NAVY_LIGHT} !important;
    border-radius: 3px !important;
    font-family: Arial, Helvetica, sans-serif !important;
    font-weight: bold !important;
    letter-spacing: 0.5px !important;
}}

.stLinkButton > a:hover {{
    background: {NAVY_LIGHT} !important;
    border-color: {GOLD} !important;
}}

/* === EXPANDERS === */
.streamlit-expanderHeader {{
    font-family: Arial, Helvetica, sans-serif;
    font-weight: bold;
    color: {NAVY};
    background: {GRAY_50};
    border-left: 4px solid {NAVY};
    border-radius: 0 3px 3px 0;
}}

/* === SELECTBOX === */
.stSelectbox label {{
    font-family: Arial, Helvetica, sans-serif !important;
    font-size: 12px !important;
    font-weight: bold !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: {GRAY_600} !important;
}}

/* === TABS (if used) === */
.stTabs [data-baseweb="tab-list"] {{
    background: {NAVY_DARK};
    border-bottom: 2px solid {GOLD_DARK};
}}

.stTabs [data-baseweb="tab"] {{
    color: rgba(255,255,255,0.6);
    font-family: Arial, Helvetica, sans-serif;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 1px;
    text-transform: uppercase;
}}

.stTabs [aria-selected="true"] {{
    color: {GOLD} !important;
    border-bottom: 3px solid {GOLD} !important;
}}

/* === ALERTS === */
.stAlert {{
    border-radius: 0 3px 3px 0;
}}

/* Success */
div[data-testid="stAlert"][data-type="success"] {{
    border-left: 5px solid {GREEN_OK};
    background: #f0f9f1;
}}

/* Warning */
div[data-testid="stAlert"][data-type="warning"] {{
    border-left: 5px solid {CAUTION_AMBER};
    background: {GOLD_PALE};
}}

/* Error */
div[data-testid="stAlert"][data-type="error"] {{
    border-left: 5px solid {WARNING_RED};
    background: #fdf0f0;
}}

/* Info */
div[data-testid="stAlert"][data-type="info"] {{
    border-left: 5px solid {NAVY_MID};
    background: {NAVY_PALE};
}}

/* === DIVIDERS === */
hr {{
    border-color: {GRAY_100} !important;
}}

/* === CLASSIFICATION BANNER (injected separately) === */
.clf-banner {{
    background: {CUI_PURPLE};
    color: {WHITE};
    font-family: Arial, Helvetica, sans-serif;
    font-size: 11px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 4px;
    text-align: center;
    padding: 5px 0;
    margin: -1rem -1rem 1rem -1rem;
    width: calc(100% + 2rem);
}}

/* === SIDEBAR INSIGNIA === */
.sidebar-insignia {{
    text-align: center;
    padding: 20px 10px 10px 10px;
}}

.sidebar-insignia img {{
    width: 80px;
    height: auto;
    filter: drop-shadow(0 2px 8px rgba(0,0,0,0.3));
    margin-bottom: 8px;
}}

.sidebar-cmd-text {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 9px;
    font-weight: bold;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: {GOLD};
    text-align: center;
    line-height: 1.4;
    margin-bottom: 4px;
}}

/* === PROGRESS BAR === */
.stProgress > div > div {{
    background: {NAVY} !important;
}}

/* === MULTISELECT CHIPS === */
span[data-baseweb="tag"] {{
    background: {NAVY} !important;
    color: {WHITE} !important;
}}

/* === HIDE STREAMLIT DEPLOY BUTTON === */
.stDeployButton, [data-testid="stToolbar"] {{
    display: none !important;
}}

/* === FOOTER === */
.app-footer {{
    text-align: center;
    color: {GRAY_400};
    font-size: 10px;
    font-family: Arial, Helvetica, sans-serif;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 20px 0;
    border-top: 1px solid {GRAY_100};
    margin-top: 40px;
}}
</style>
"""


def inject_branding(
    title: str,
    subtitle: str = "USAREUR-AF Operational Data Team",
    show_classification: bool = True,
):
    """Inject USAREUR-AF branding CSS and optional classification banner.

    Call this once at the top of each dashboard, right after st.set_page_config().
    """
    st.markdown(_CSS, unsafe_allow_html=True)

    if show_classification:
        st.markdown(
            '<div class="clf-banner">CUI // FOUO</div>',
            unsafe_allow_html=True,
        )

    # Sidebar: USAREUR-AF insignia + command identification
    with st.sidebar:
        _insignia_html = INSIGNIA_IMG.format(
            'style="width:80px; height:auto;"'
        )
        st.markdown(f"""
        <div class="sidebar-insignia">
            {_insignia_html}
            <div class="sidebar-cmd-text">
                United States Army<br>Europe and Africa
            </div>
        </div>
        """, unsafe_allow_html=True)
