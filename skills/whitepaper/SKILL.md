---
name: whitepaper
description: Plan, research, write, fact-check, design, and repurpose credible B2B white papers using AI. Use for industrial AI, manufacturing, enterprise technology, thought leadership, lead generation, investor education, and policy papers.
---

# AI White Paper Skill

## Mission

Produce a decision-useful, evidence-led white paper—not a long blog post or a disguised sales brochure. Use AI to accelerate planning, research synthesis, outlining, drafting, editing, and repurposing. Keep humans responsible for strategic judgment, source verification, original analysis, claims, and final approval.

Reference inspiration: Skill Arbitrage, “How to use AI to write a white paper: a step-by-step guide for content writers” (19 June 2025): https://skillarbitra.ge/blog/how-to-use-ai-to-write-a-white-paper/

## When to use

- B2B thought leadership and lead-generation papers
- Industrial AI, manufacturing, operations, safety, energy, quality, predictive maintenance, edge AI, and digital transformation
- Technical or solution-framework papers for executives and practitioners
- Investor education, policy advocacy, and market education

## Required inputs

Start with what is available. Ask only for missing details that materially change the paper.

- Organisation/product and approved positioning
- Topic, target industry, geography, and time period
- Primary reader and their decision or problem
- Business purpose: thought leadership, qualified leads, investor education, policy influence, or technical education
- Desired action after reading
- Target length, deadline, language, brand voice, and design requirements
- Approved internal documents, customer interviews, case studies, product facts, and restrictions

Never invent product capabilities, customer results, quotations, deployments, certifications, ROI, or company claims. If details are unknown, mark them as questions or evidence gaps.

## Workflow

### Stage 1 — Define the strategic brief

1. Identify the reader, their high-value problem, business impact, decision criteria, and likely objections.
2. Define one central thesis: what the reader should understand or do differently after reading.
3. Select the paper's purpose and primary CTA.
4. Propose three possible angles and explain the differentiation, audience relevance, and evidence needed for each.
5. Agree the brief before drafting.

**Prompt**
> Act as a senior B2B research strategist. Develop a white-paper brief on [topic] for [audience] in [industry/geography]. Business goal: [goal]. Reader problem: [problem]. Approved company/product context: [context]. Propose three differentiated angles. For each, specify the thesis, audience value, evidence required, likely objections, business relevance, and CTA. Do not draft the paper yet. Identify missing information and unsupported assumptions.

### Stage 2 — Develop the title and promise

Generate 6–10 title/subtitle combinations. Prefer specific outcomes, questions, trade-offs, frameworks, or evidence-backed claims. Avoid sensational numbers, unsupported percentages, and promises the paper cannot prove.

**Prompt**
> Generate 8 credible white-paper title and subtitle options for [audience] about [topic]. Make each specific, decision-relevant, and distinct. For each, state the reader promise and the evidence needed to support it. Do not use statistics or superlatives unless supplied and verifiable.

### Stage 3 — Research the evidence base

Research in four passes:

1. **Landscape:** industry structure, operating context, technology maturity, regulations, and current developments.
2. **Problem:** recurring pain points, causes, consequences, existing workarounds, and who owns the decision.
3. **Solutions:** technical approaches, implementation patterns, constraints, risks, and success measures.
4. **Differentiation:** what existing papers cover, where evidence is weak, what remains unresolved, and what original perspective this paper can add.

Prioritise primary sources: government and regulator publications, standards bodies, peer-reviewed research, official datasets, company technical documentation, audited reports, and directly attributable case studies. Use reputable industry reports and journalism for context, not as substitutes for original evidence.

For every important claim, record:
- Claim ID and exact proposed claim
- Source title, publisher, URL, publication date, and access date
- Exact supporting passage, table, or page number
- Geography, population, sample, timeframe, and methodology where relevant
- Whether the source is primary or secondary
- Confidence: verified, partial, disputed, or unverified
- Planned location in the paper

Never cite a source you have not opened and checked. Search snippets and AI-generated references are leads, not proof. If browsing or source access is unavailable, disclose that limitation and create a research checklist rather than pretending verification is complete.

**Research prompts**
> Map the current evidence on [problem] in [industry/geography] for [time period]. Return a source table with claim, finding, source URL, publication date, source type, methodology/sample if stated, limitations, and relevance to [audience]. Separate measured evidence from opinions and vendor claims. Flag conflicts and gaps. Do not fabricate citations.

> Identify the 5 most consequential operational challenges faced by [target role] in [industry]. For each, explain the mechanism, business consequence, existing workaround, evidence available, and unresolved question. Distinguish validated findings from hypotheses.

> Compare [approach A], [approach B], and [approach C] using implementation complexity, data requirements, integration, latency, reliability, security, cost drivers, human oversight, limitations, and measurable outcomes. Cite evidence for each material comparison and mark unknowns explicitly.

### Stage 4 — Build the argument and outline

Create a claim-evidence matrix before writing. Every major section should advance the thesis, answer a reader question, and rely on identified evidence. Separate:
- Established facts
- Source-reported findings
- Analysis or interpretation
- Illustrative examples
- Hypotheses requiring validation
- Company/product statements

**Standard outline**
1. Cover: title, subtitle, author/organisation, date, version
2. Executive summary (usually 150–250 words)
3. The decision context and why the issue matters now
4. Problem definition: workflow, root causes, operational/business consequences
5. Evidence and current-state landscape
6. Why existing approaches are insufficient or difficult
7. Proposed framework or solution approach
8. Implementation roadmap and prerequisites
9. Measurement framework: baseline, KPIs, evaluation method
10. Risks, limitations, governance, security, and human oversight
11. Illustrative use case or verified case study
12. Recommendations and conclusion
13. Specific CTA
14. References, methodology, definitions, and appendices as needed

Adapt the outline to the paper's purpose. Do not force every section into a short paper.

### Stage 5 — Draft section by section

Draft only after the brief, outline, and evidence table are approved. Write for the intended reader, not for search engines or AI detectors. Use a clear argument, concrete examples, informative headings, and concise paragraphs. Define acronyms on first use. Avoid generic openings, repeated conclusions, unsupported certainty, and sales-heavy language.

**Executive summary prompt**
> Draft a [150–250]-word executive summary for [audience]. In order: state the decision/problem, why it matters, the most important evidence-backed insight, the recommended framework or approach, major caveat, and reader benefit. Use only claims in the approved evidence table. Do not introduce new facts or citations.

**Problem-definition prompt**
> Explain [problem] for [reader role] using the verified evidence. Describe the real workflow, root causes, operational consequences, current workarounds, and why the issue persists. Separate quantified evidence from qualitative observations. Do not invent a company story, loss amount, or statistic.

**Framework prompt**
> Present [approach] as a practical framework with 3–5 components. For each, explain purpose, prerequisites, process, accountable role, risks, and measurable success criteria. Include dependencies and realistic implementation stages. Distinguish generally applicable guidance from claims specific to [organisation/product].

**Case-study prompt**
> Use only the supplied and approved case-study material. Structure it as context → challenge → intervention → measured result → limitations → lesson. Preserve exact metrics and timeframe. If evidence is missing, insert [EVIDENCE REQUIRED] rather than filling the gap.

### Stage 6 — Add useful visual storytelling

Recommend visuals only when they clarify evidence, systems, comparisons, or decisions. Potential assets:
- Problem-to-impact causal diagram
- Current-state versus future-state workflow
- Reference architecture or data-flow diagram
- Implementation roadmap
- Comparison matrix
- KPI tree or measurement model
- Evidence chart with source and date
- Risk/control matrix
- Clearly labelled illustrative scenario

Every chart must have a traceable source, units, timeframe, definitions, and a note on whether values are measured, estimated, or illustrative. Never fabricate chart data. Label conceptual diagrams as conceptual and product architectures as proposed unless implementation is verified.

**Prompt**
> Review the approved outline and evidence table. Recommend up to 6 visuals that materially improve understanding. For each, specify the reader question, visual type, exact inputs needed, source/caption requirements, and whether it is evidence-based or conceptual. Do not create unsupported data.

### Stage 7 — Edit in separate passes

Run separate reviews instead of asking for a vague “polish”:

1. **Argument:** Does each section support the thesis? Are counterarguments addressed?
2. **Evidence:** Does every factual, numerical, comparative, technical, regulatory, and customer claim have adequate support?
3. **Technical review:** Are mechanisms, assumptions, dependencies, risks, and limitations accurate?
4. **Audience clarity:** Can the intended reader understand it without unnecessary jargon?
5. **Flow:** Are section order and transitions logical? Is there repetition?
6. **Tone:** Is it authoritative, balanced, precise, and accessible?
7. **Commercial integrity:** Are product claims approved and proportionate? Is the CTA relevant?
8. **Copyedit:** Grammar, terminology, acronym consistency, units, tables, references, and formatting.

**Editing prompt**
> Review this draft as (1) a domain expert, (2) a skeptical executive reader, and (3) a fact-checking editor. Return a table with issue, location, severity, reason, evidence needed, and recommended correction. Do not silently rewrite factual claims. Preserve supported meaning and flag any statement that exceeds its evidence.

### Stage 8 — Fact-check and release gate

Before publication, build a claim ledger and confirm:
- All numbers, dates, quotations, citations, and named examples are checked against source material.
- Sources actually support the sentence they are attached to.
- Comparisons use comparable definitions, time periods, populations, and units.
- Customer names, logos, testimonials, internal data, and case studies are authorised for publication.
- Product, security, performance, integration, compliance, and ROI claims are approved by the relevant owner.
- Limitations, assumptions, and conflicts of interest are disclosed where relevant.
- No confidential, personal, or restricted information is exposed.
- Images, charts, and excerpts have appropriate usage rights.
- Version, publication date, owner, and review status are recorded.

Remove or qualify any unverified claim. Never fabricate a source or imply that a pilot, result, certification, or capability exists when it does not. Obtain domain-expert, legal, security, or compliance review where the subject requires it.

### Stage 9 — Design and conversion

Use a consistent document system: clear H1/H2/H3 hierarchy, readable typography, ample whitespace, restrained colour, accessible contrast, page numbers, running headers/footers, captions, and a table of contents for longer documents. Keep the cover promise aligned with the paper's actual contents.

The CTA should be a logical next step for this reader, such as a technical consultation, assessment, benchmark discussion, demo, or implementation workshop. State what the reader receives and what happens next; avoid fake urgency.

### Stage 10 — Repurpose and measure

After approval, derive content from the final paper without changing the meaning of its claims:
- 1 executive LinkedIn article
- 4–6 short social posts
- 3 evidence-backed quote cards
- 1 email summary
- 1 landing-page summary
- 1 webinar or presentation outline
- 1 sales enablement brief
- 1 FAQ for the relevant audience

Link derived claims back to the approved paper and source ledger. Measure qualified downloads, target-account engagement, CTA conversion, meetings influenced, sales-team usage, and feedback—not downloads alone.

## Industry.AI adaptation

For industrial AI and manufacturing papers, analyse the full chain:

**Industry → Problem → Asset/Process → Data Inputs → AI/Analytics → Detection/Prediction → Insight → Action → Human/AI Role → Business Outcome → KPIs → Industry.AI Technology/Product → Demo Scenario → Website Solution Mapping**

For each use case, document operating context, failure or inefficiency mode, available signals, data quality, system integration, latency, edge/cloud constraints, safety implications, human override, baseline, evaluation window, and success criteria. Treat YodaEdge, Orion, and other product capabilities only as supplied/approved facts. Do not promise autonomous control, predictive accuracy, savings, or deployment readiness without evidence and engineering approval.

## Final output package

Unless the user asks for a different deliverable, provide:
1. Strategic brief and audience
2. Recommended title/subtitle
3. Approved outline
4. Research and claim-evidence ledger
5. Full white-paper draft with citations
6. Visual plan and captions
7. Fact-check and review checklist
8. CTA and landing-page summary
9. Repurposing plan
10. Open questions, assumptions, and items needing human approval

## Operating rules

- Work stage by stage; do not leap straight from a broad topic to a polished paper.
- If the topic is underspecified, ask one concise question or propose clearly labelled assumptions.
- Do not claim that research is complete until sources have been checked.
- Never fabricate citations, data, customer stories, quotations, or outcomes.
- Make uncertainty visible. Prefer “the available evidence suggests” to unwarranted certainty.
- Preserve original analysis and add audience-specific insight; avoid paraphrasing competitors into a derivative paper.
- Treat the linked article as workflow inspiration, not as proof of its performance or conversion statistics.
