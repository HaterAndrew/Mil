// MSS Training Hub — Media Set URLs
// Media Set RID: ri.mio.main.media-set.9c297238-56bf-46d4-881a-db21-dcee1c
// All PDFs require CAC/MSS authentication at mss.data.mil

const BASE = 'https://mss.data.mil/mio/api/mediaSet/ri.mio.main.media-set.9c297238-56bf-46d4-881a-db21-dcee1c/file'

export const URLS = {
  // Quick References
  QUICK_START:               `${BASE}/QUICK_START.pdf`,
  CHEATSHEET:                `${BASE}/CHEATSHEET.pdf`,
  GLOSSARY:                  `${BASE}/GLOSSARY_data_foundry.pdf`,

  // Doctrine / Data Literacy
  DATA_LITERACY_SL:          `${BASE}/DATA_LITERACY_senior_leaders.pdf`,
  DATA_LITERACY_TECH:        `${BASE}/DATA_LITERACY_technical_reference.pdf`,

  // Senior Leader Executive Course (TM-EXEC)
  TM_EXEC:                   `${BASE}/TM_EXEC_SENIOR_LEADER.pdf`,
  CG_TM_EXEC:                `${BASE}/CONCEPTS_GUIDE_TM_EXEC_SENIOR_LEADER.pdf`,
  SYL_TM_EXEC:               `${BASE}/SYLLABUS_TM_EXEC.pdf`,

  // Foundation Courses
  SL1:                       `${BASE}/TM_10_MAVEN_USER.pdf`,
  SL2:                       `${BASE}/TM_20_BUILDER.pdf`,
  SL3:                       `${BASE}/TM_30_ADVANCED_BUILDER.pdf`,

  // SL 4 Specialist Tracks
  SL4G:                      `${BASE}/TM_40G_ORSA.pdf`,
  SL4H:                      `${BASE}/TM_40H_AI_ENGINEER.pdf`,
  SL4M:                      `${BASE}/TM_40M_ML_ENGINEER.pdf`,
  SL4J:                      `${BASE}/TM_40J_PROGRAM_MANAGER.pdf`,
  SL4K:                      `${BASE}/TM_40K_KNOWLEDGE_MANAGER.pdf`,
  SL4L:                      `${BASE}/TM_40L_SOFTWARE_ENGINEER.pdf`,
  SL4N:                      `${BASE}/TM_40N_UX_DESIGNER.pdf`,
  SL4O:                      `${BASE}/TM_40O_PLATFORM_ENGINEER.pdf`,

  // SL 4 WFF Tracks
  SL4A:                      `${BASE}/TM_40A_INTELLIGENCE.pdf`,
  SL4B:                      `${BASE}/TM_40B_FIRES.pdf`,
  SL4C:                      `${BASE}/TM_40C_MOVEMENT_MANEUVER.pdf`,
  SL4D:                      `${BASE}/TM_40D_SUSTAINMENT.pdf`,
  SL4E:                      `${BASE}/TM_40E_PROTECTION.pdf`,
  SL4F:                      `${BASE}/TM_40F_MISSION_COMMAND.pdf`,

  // SL 5 Advanced Tracks
  SL5G:                      `${BASE}/TM_50G_ORSA_ADVANCED.pdf`,
  SL5H:                      `${BASE}/TM_50H_AI_ENGINEER_ADVANCED.pdf`,
  SL5M:                      `${BASE}/TM_50M_ML_ENGINEER_ADVANCED.pdf`,
  SL5J:                      `${BASE}/TM_50J_PROGRAM_MANAGER_ADVANCED.pdf`,
  SL5K:                      `${BASE}/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.pdf`,
  SL5L:                      `${BASE}/TM_50L_SOFTWARE_ENGINEER_ADVANCED.pdf`,
  SL5N:                      `${BASE}/TM_50N_UX_DESIGNER_ADVANCED.pdf`,
  SL5O:                      `${BASE}/TM_50O_PLATFORM_ENGINEER_ADVANCED.pdf`,

  // Syllabi — Foundation
  SYL_SL1:                   `${BASE}/SYLLABUS_TM10.pdf`,
  SYL_SL2:                   `${BASE}/SYLLABUS_TM20.pdf`,
  SYL_SL3:                   `${BASE}/SYLLABUS_TM30.pdf`,

  // Syllabi — Specialist
  SYL_SL4G:                  `${BASE}/SYLLABUS_TM40G.pdf`,
  SYL_SL4H:                  `${BASE}/SYLLABUS_TM40H.pdf`,
  SYL_SL4M:                  `${BASE}/SYLLABUS_TM40M.pdf`,
  SYL_SL4J:                  `${BASE}/SYLLABUS_TM40J.pdf`,
  SYL_SL4K:                  `${BASE}/SYLLABUS_TM40K.pdf`,
  SYL_SL4L:                  `${BASE}/SYLLABUS_TM40L.pdf`,

  // Syllabi — WFF
  SYL_SL4A:                  `${BASE}/SYLLABUS_TM40A.pdf`,
  SYL_SL4B:                  `${BASE}/SYLLABUS_TM40B.pdf`,
  SYL_SL4C:                  `${BASE}/SYLLABUS_TM40C.pdf`,
  SYL_SL4D:                  `${BASE}/SYLLABUS_TM40D.pdf`,
  SYL_SL4E:                  `${BASE}/SYLLABUS_TM40E.pdf`,
  SYL_SL4F:                  `${BASE}/SYLLABUS_TM40F.pdf`,

  // Concepts Guides — WFF
  CG_SL4A:                   `${BASE}/CONCEPTS_GUIDE_TM40A_INTELLIGENCE.pdf`,
  CG_SL4B:                   `${BASE}/CONCEPTS_GUIDE_TM40B_FIRES.pdf`,
  CG_SL4C:                   `${BASE}/CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.pdf`,
  CG_SL4D:                   `${BASE}/CONCEPTS_GUIDE_TM40D_SUSTAINMENT.pdf`,
  CG_SL4E:                   `${BASE}/CONCEPTS_GUIDE_TM40E_PROTECTION.pdf`,
  CG_SL4F:                   `${BASE}/CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.pdf`,

  // Concepts Guides — Specialist
  CG_SL4G:                   `${BASE}/CONCEPTS_GUIDE_TM40G_ORSA.pdf`,
  CG_SL4H:                   `${BASE}/CONCEPTS_GUIDE_TM40H_AI_ENGINEER.pdf`,
  CG_SL4M:                   `${BASE}/CONCEPTS_GUIDE_TM40M_ML_ENGINEER.pdf`,
  CG_SL4J:                   `${BASE}/CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER.pdf`,
  CG_SL4K:                   `${BASE}/CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.pdf`,
  CG_SL4L:                   `${BASE}/CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER.pdf`,

  // Concepts Guides — Advanced
  CG_SL5G:                   `${BASE}/CONCEPTS_GUIDE_TM50G_ORSA_ADVANCED.pdf`,
  CG_SL5H:                   `${BASE}/CONCEPTS_GUIDE_TM50H_AI_ENGINEER_ADVANCED.pdf`,
  CG_SL5M:                   `${BASE}/CONCEPTS_GUIDE_TM50M_ML_ENGINEER_ADVANCED.pdf`,
  CG_SL5J:                   `${BASE}/CONCEPTS_GUIDE_TM50J_PROGRAM_MANAGER_ADVANCED.pdf`,
  CG_SL5K:                   `${BASE}/CONCEPTS_GUIDE_TM50K_KNOWLEDGE_MANAGER_ADVANCED.pdf`,
  CG_SL5L:                   `${BASE}/CONCEPTS_GUIDE_TM50L_SOFTWARE_ENGINEER_ADVANCED.pdf`,

  // Exercises — Foundation
  EX_SL1:                    `${BASE}/EX_10_OPERATOR_BASICS.pdf`,
  EX_SL2:                    `${BASE}/EX_20_NO_CODE_BUILDER.pdf`,
  EX_SL3:                    `${BASE}/EX_30_ADVANCED_BUILDER.pdf`,

  // Exercises — Specialist
  EX_SL4G:                   `${BASE}/EX_40G_ORSA.pdf`,
  EX_SL4H:                   `${BASE}/EX_40H_AI_ENGINEER.pdf`,
  EX_SL4M:                   `${BASE}/EX_40M_ML_ENGINEER.pdf`,
  EX_SL4J:                   `${BASE}/EX_40J_PROGRAM_MANAGER.pdf`,
  EX_SL4K:                   `${BASE}/EX_40K_KNOWLEDGE_MANAGER.pdf`,
  EX_SL4L:                   `${BASE}/EX_40L_SOFTWARE_ENGINEER.pdf`,

  // Foundry Bootcamp Program (FBC)
  FBC_GUIDE:                 `${BASE}/FBC_GUIDE.pdf`,
  FBC_SPRINT_PACKAGE:        `${BASE}/FBC_SPRINT_PACKAGE.pdf`,
  FBC_ENVIRONMENT_SETUP:     `${BASE}/FBC_ENVIRONMENT_SETUP.pdf`,
  FOUNDRY_BOOTCAMP_SOP:        `${BASE}/FOUNDRY_BOOTCAMP_SOP.pdf`,

  // Governance
  NAMING_STANDARDS:          `${BASE}/NAMING_AND_GOVERNANCE_STANDARDS.pdf`,

  // Training Management
  MTP:                       `${BASE}/MTP_MSS.pdf`,
  POI:                       `${BASE}/POI_MSS.pdf`,
  TEO:                       `${BASE}/TEO_MSS.pdf`,
  ENROLLMENT_SOP:            `${BASE}/ENROLLMENT_SOP.pdf`,
  CURRICULUM_SOP:            `${BASE}/CURRICULUM_MAINTENANCE_SOP.pdf`,
  ANNUAL_SCHEDULE:           `${BASE}/ANNUAL_TRAINING_SCHEDULE.pdf`,
  POLICY_LETTER:             `${BASE}/POLICY_LETTER.pdf`,
  COMPLETION_CERT:           `${BASE}/COMPLETION_CERTIFICATE.pdf`,
  AAR_TEMPLATE:              `${BASE}/AAR_TEMPLATE.pdf`,
  FACULTY_DEV_PLAN:          `${BASE}/FACULTY_DEVELOPMENT_PLAN.pdf`,
  CAD:                       `${BASE}/CAD_MSS.pdf`,

  // Train-the-Trainer (T3)
  T3I:                       `${BASE}/T3_I_INSTRUCTOR_CERTIFICATION.pdf`,
  T3F:                       `${BASE}/T3_F_MSC_FORCE_MULTIPLIER.pdf`,
  CG_T3I:                    `${BASE}/CONCEPTS_GUIDE_T3I_INSTRUCTOR_CERTIFICATION.pdf`,
  CG_T3F:                    `${BASE}/CONCEPTS_GUIDE_T3F_MSC_FORCE_MULTIPLIER.pdf`,
  SYL_T3I:                   `${BASE}/SYLLABUS_T3I.pdf`,
  SYL_T3F:                   `${BASE}/SYLLABUS_T3F.pdf`,
  EX_T3I:                    `${BASE}/EX_T3I_INSTRUCTOR_CERTIFICATION.pdf`,
  EX_T3F:                    `${BASE}/EX_T3F_FORCE_MULTIPLIER.pdf`,
  LP_T3I:                    `${BASE}/T3I_LESSON_PLAN_OUTLINES.pdf`,
  LP_T3F:                    `${BASE}/T3F_LESSON_PLAN_OUTLINES.pdf`,
  INSTRUCTOR_TIERS:          `${BASE}/INSTRUCTOR_TIER_DEFINITIONS.pdf`,
  SME_RUBRIC:                `${BASE}/C2DAO_SME_DESIGNATION_RUBRIC.pdf`,
  UDT_SOP:                   `${BASE}/UNIT_DATA_TRAINER_SOP.pdf`,
  MTT_SOP:                   `${BASE}/MTT_OPERATIONS_SOP.pdf`,
  SUCCESSOR_GUIDE:           `${BASE}/SUCCESSOR_PLANNING_GUIDE.pdf`,

  // Lesson Plans
  LP_SL1:                    `${BASE}/TM10_LESSON_PLANS.pdf`,
  LP_SL2:                    `${BASE}/TM20_LESSON_PLAN_OUTLINES.pdf`,
  LP_SL3:                    `${BASE}/TM30_LESSON_PLAN_OUTLINES.pdf`,
  LP_SL4_SPECIALIST:         `${BASE}/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.pdf`,
  LP_TEMPLATE:               `${BASE}/LP_TEMPLATE.pdf`,
} as const
