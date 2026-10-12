---
name: industrial-pain-point-research
description: Research and validate real industrial and manufacturing pain points using credible evidence, operational context, data requirements, measurable KPIs, and potential AI opportunities.
---

# Industrial Pain-Point Research Skill

## Purpose
Find specific, decision-relevant operational problems—not generic claims that AI improves everything. Turn verified research into an opportunity map for industrial AI products, thought leadership, and customer discovery.

## Inputs
Industry/subsector, process or asset, geography, time period, target role, research purpose, approved product context, and available internal documents. Ask only for missing details that materially affect the research.

## Research workflow
1. Scope the operating context: industry, plant type, process, asset, operating conditions, stakeholders.
2. Discover pain signals from regulators, public tenders, standards, peer-reviewed research, engineering papers, annual reports, incident reports, case studies, and practitioner interviews.
3. Prioritise primary sources. Treat vendor content and search snippets as leads, not independent proof.
4. Explain the mechanism: what happens, where, why current controls fail, and who bears the consequence.
5. Check data feasibility: PLC/SCADA, MES, CMMS, historian, ERP, CCTV, inspection logs, laboratory data, sensors, and manual records.
6. Compare interventions: process redesign, rules, conventional analytics, vision, forecasting, optimisation, AI agents—or no AI where unjustified.
7. Define a measurable baseline and KPIs. Never invent loss figures, incident rates, or ROI.
8. Record validation questions for interviews, site visits, data samples, and pilots.

## Opportunity record
For each problem capture:
- Industry and sub-industry
- Process, asset, or operating zone
- Observable problem statement and affected role
- Root-cause hypotheses versus confirmed causes
- Operational, safety, quality, energy, compliance, or financial consequence
- Evidence, source URL, publisher, and date
- Evidence strength: strong, moderate, weak, or hypothesis
- Existing controls and workarounds
- Data inputs, likely availability, quality, and access
- Candidate analytical/AI approach and rationale
- Detection, prediction, decision, and action
- Human responsibility, override, and escalation
- Baseline, KPI definitions, and evaluation window
- Integration, cybersecurity, safety, and deployment constraints
- Pilot scenario, acceptance criteria, approved product mapping, and next action

## Research prompt
> Research real operational pain points in [industry/subsector] in [geography] during [period], for [target role]. Find specific workflows, assets, failure modes, workarounds, consequences, and evidence. Prefer primary sources and provide URL, publisher, date, exact supporting passage/page, methodology, limitations, and relevance. Separate verified findings from vendor claims and hypotheses. Do not invent incident rates, costs, or citations. Return a ranked opportunity table and validation questions.

## Ranking
Score 1–5 for business impact, evidence strength, urgency/frequency, data readiness, technical feasibility, integration ease, buyer ownership, and repeatability. Keep weights visible. High impact with weak evidence is a validation priority, not a proven market claim. Treat high safety sensitivity as a need for stronger controls, not automatically as a higher opportunity score.

## Interview questions
- Walk me through the last time this problem occurred.
- What triggered it and how was it detected?
- What did the team do next, and how long did each step take?
- What logs or data exist, and who owns them?
- How is the baseline measured?
- What happens when existing controls miss the issue?
- What would make a pilot credible or unacceptable?
- Who owns budget, deployment, safety approval, and the decision?

## Industry.AI mapping
Industry → Problem → Asset/Process → Data Inputs → AI/Analytics → Detection/Prediction → Insight → Action → Human/AI Role → Business Outcome → KPIs → Approved Product Mapping → Demo Scenario → Website Solution Mapping.

## Rules
Cite material external claims. Never treat a possible AI solution as a validated product capability. Distinguish detection, prediction, recommendation, and autonomous control. For safety-critical workflows, include fail-safe design, human oversight, integration, and engineering validation. End with evidence gaps and the next concrete validation step.
