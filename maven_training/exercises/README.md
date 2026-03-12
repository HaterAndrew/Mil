# MSS Training Exercises

**Version 1.1 | March 2026**

This directory contains practical exercise packages and written assessments for each level of the MSS training curriculum. Exercise packages define the scenario, tasks, and Go/No-Go criteria. **Exercise data files and MSS environment access must be arranged separately** — see notes in each package.

---

## Baseline Assessments (Pre-Test / Post-Test)

Written exams for all 15 courses are in [exams/](exams/). Each course has two forms:

| File Pattern | Purpose | Scoring |
|---|---|---|
| `EXAM_[ID]_PRE.md` | Diagnostic — administered before training | No passing score; instructor use only |
| `EXAM_[ID]_POST.md` | Mastery assessment — administered after training | 70% required (42/60 pts) |

| Pre/Post Exams | Course | Audience |
|---|---|---|
| [TM-10](exams/EXAM_TM10_PRE.md) / [POST](exams/EXAM_TM10_POST.md) | Maven User | All personnel |
| [TM-20](exams/EXAM_TM20_PRE.md) / [POST](exams/EXAM_TM20_POST.md) | Builder | All staff |
| [TM-30](exams/EXAM_TM30_PRE.md) / [POST](exams/EXAM_TM30_POST.md) | Advanced Builder | Data-adjacent specialists |
| [TM-40A](exams/EXAM_TM40A_PRE.md) / [POST](exams/EXAM_TM40A_POST.md) | ORSA | FA49 / ORSA analysts |
| [TM-40B](exams/EXAM_TM40B_PRE.md) / [POST](exams/EXAM_TM40B_POST.md) | AI Engineer | AI/ML specialists |
| [TM-40C](exams/EXAM_TM40C_PRE.md) / [POST](exams/EXAM_TM40C_POST.md) | ML Engineer | ML engineers / data scientists |
| [TM-40D](exams/EXAM_TM40D_PRE.md) / [POST](exams/EXAM_TM40D_POST.md) | Program Manager | PMs / G8-S8 / resource managers |
| [TM-40E](exams/EXAM_TM40E_PRE.md) / [POST](exams/EXAM_TM40E_POST.md) | Knowledge Manager | KMOs / 37F / knowledge officers |
| [TM-40F](exams/EXAM_TM40F_PRE.md) / [POST](exams/EXAM_TM40F_POST.md) | Software Engineer | SWEs |
| [TM-50A](exams/EXAM_TM50A_PRE.md) / [POST](exams/EXAM_TM50A_POST.md) | Advanced ORSA | Senior FA49 / ORSA section chiefs |
| [TM-50B](exams/EXAM_TM50B_PRE.md) / [POST](exams/EXAM_TM50B_POST.md) | Advanced AI Engineer | AI architects / capability leads |
| [TM-50C](exams/EXAM_TM50C_PRE.md) / [POST](exams/EXAM_TM50C_POST.md) | Advanced ML Engineer | Senior MLEs / platform engineers |
| [TM-50D](exams/EXAM_TM50D_PRE.md) / [POST](exams/EXAM_TM50D_POST.md) | Advanced Program Manager | Senior technical PMs |
| [TM-50E](exams/EXAM_TM50E_PRE.md) / [POST](exams/EXAM_TM50E_POST.md) | Advanced Knowledge Manager | Corps/Theater KM architects |
| [TM-50F](exams/EXAM_TM50F_PRE.md) / [POST](exams/EXAM_TM50F_POST.md) | Advanced Software Engineer | Senior SWEs / platform leads |

Each exam: 15 MCQ (2 pts) + 5 short answer (6 pts) = 60 pts total. Instructor answer key included in every file.

---

## Practical Exercise Packages

| Package | Corresponds To | Audience | Status |
|---------|---------------|----------|--------|
| [EX-10_operator_basics/](EX-10_operator_basics/) | TM-10 | All personnel | Stub — needs data |
| [EX-20_no_code_builder/](EX-20_no_code_builder/) | TM-20 | All staff | Stub — needs data |
| [EX-30_advanced_builder/](EX-30_advanced_builder/) | TM-30 | Data-adjacent specialists | Stub — needs data |
| [EX-40A_orsa/](EX-40A_orsa/) | TM-40A | ORSA | Stub — needs data |
| [EX-40B_ai_engineer/](EX-40B_ai_engineer/) | TM-40B | AI Engineers | Stub — needs data |
| [EX-40C_ml_engineer/](EX-40C_ml_engineer/) | TM-40C | ML Engineers | Stub — needs data |
| [EX-40D_program_manager/](EX-40D_program_manager/) | TM-40D | Technical PMs | Stub — needs data |
| [EX-40E_knowledge_manager/](EX-40E_knowledge_manager/) | TM-40E | Knowledge Managers | Stub — needs data |
| [EX-40F_software_engineer/](EX-40F_software_engineer/) | TM-40F | Software Engineers | Stub — needs data |

---

## What "Stub — Needs Data" Means

Each exercise package contains:
- Scenario framing (OPORD-style context)
- Task list with Go/No-Go criteria
- Evaluator notes
- **Placeholder** for the exercise dataset or MSS environment setup instructions

To make an exercise operational, an instructor must:
1. Obtain or create a synthetic dataset appropriate to the scenario
2. Load it into an MSS sandbox or training environment
3. Fill in the `ENVIRONMENT_SETUP.md` within the exercise package
4. Conduct a dry run and update the evaluator notes accordingly

---

## Data Sourcing Guidance

Exercise data must be:
- **Unclassified** — training environments are not accredited for classified data
- **Synthetic or sanitized** — no real operational data in training exercises
- **Scenario-appropriate** — USAREUR-AF context preferred (unit designators, European locations, LOGSTAT-type structures)

Contact the unit data steward or OPDATA team to request synthetic dataset generation.
