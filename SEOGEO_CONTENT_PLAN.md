# SEOGEO Content Plan for blog.mare.run
## March 2026

---

## Executive Summary

**Goal:** Dominate both traditional SEO (Google/Bing) and GEO (AI search citations) for visual reference management keywords.

**Strategy:** 
- **GEO Focus:** Answer-first format, statistics, citations, FAQPage schema
- **SEO Focus:** Long-tail keywords, topic clusters, internal linking
- **Content Cadence:** 2 posts/week (1 pillar, 1 supporting)

---

## Current Status Audit

### ✅ What's Working
- Hugo site with PaperMod theme (fast, mobile-friendly)
- Good meta tags and Open Graph
- Organization schema in place
- 4 core comparison posts live

### ❌ What's Missing
- No FAQPage schema (critical for GEO)
- No Article schema on posts
- Missing `robots.txt` optimization for AI bots
- No `llms.txt` file for AI context
- Limited content depth (4 posts only)
- No content clustering strategy

---

## Phase 1: Foundation (Week 1-2)

### Technical Setup

**1. Create `/static/robots.txt`**
```
User-agent: *
Allow: /

# AI Search Engine Bots (GEO Critical)
User-agent: PerplexityBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

Sitemap: https://blog.mare.run/sitemap.xml
```

**2. Create `/static/llms.txt`**
```
# llms.txt for blog.mare.run
# Last updated: 2026-03-01

## About Mare
Mare is a visual reference management tool for cultural creatives—designers, researchers, and artists who need more than Pinterest or Are.na. Unlike algorithm-driven platforms, Mare is built for curation, not consumption.

## Core Topics
- Visual reference management workflows
- Pinterest alternatives for designers
- Are.na vs private archives
- Design inspiration organization
- Creative research methods

## Key Resources
- Homepage: https://blog.mare.run/
- All posts: https://blog.mare.run/posts/
- Tags: https://blog.mare.run/tags/

## Contact
- Website: https://mare.run
- Twitter: https://twitter.com/marevisual
```

**3. Add Schema Templates to Hugo**

Create `/layouts/partials/schema.html`:
```html
{{ if .IsPage }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{{ .Title }}",
  "description": "{{ .Description }}",
  "author": {
    "@type": "Organization",
    "name": "Mare"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Mare",
    "logo": {
      "@type": "ImageObject",
      "url": "https://blog.mare.run/favicon.ico"
    }
  },
  "datePublished": "{{ .Date.Format "2006-01-02" }}",
  "dateModified": "{{ .Lastmod.Format "2006-01-02" }}",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{ .Permalink }}"
  }
}
</script>
{{ end }}
```

---

## Phase 2: Content Clusters (Week 3-8)

### Cluster 1: Pinterest Alternative (High Volume, High Competition)

**Pillar Post (3000+ words):**
- **Title:** "The Complete Guide to Pinterest Alternatives for Designers (2026)"
- **URL:** `/complete-guide-pinterest-alternatives-2026/`
- **Target Keywords:** 
  - Primary: "pinterest alternatives 2026" (2,400/mo, KD: 45)
  - Secondary: "pinterest alternative for designers" (880/mo, KD: 32)
  - Long-tail: "best pinterest alternative without algorithm" (140/mo, KD: 18)

**GEO Optimization:**
- FAQ section with 10 questions
- Statistics: "According to [source], 73% of designers struggle with..."
- Cite 5+ authoritative sources
- Answer-first structure

**Supporting Posts (1500+ words each):**
1. "Why Designers Are Leaving Pinterest in 2026: The Algorithm Problem"
   - URL: `/why-designers-leaving-pinterest-2026/`
   - Target: "why designers hate pinterest" (320/mo)

2. "Pinterest vs Are.na vs Mare: Which Tool Fits Your Workflow?"
   - URL: `/pinterest-vs-arena-vs-mare/`
   - Target: "pinterest vs arena" (590/mo)

3. "How to Export Your Pinterest Boards (Without Losing Your Work)"
   - URL: `/export-pinterest-boards-guide/`
   - Target: "export pinterest boards" (720/mo)

4. "Building a Visual Archive You Own (Not Renting from Platforms)"
   - URL: `/own-your-visual-archive/`
   - Target: "own your visual data" (210/mo)

---

### Cluster 2: Visual Reference Management (Medium Volume, Low Competition)

**Pillar Post (2500+ words):**
- **Title:** "Visual Reference Management: The Complete Workflow Guide (2026)"
- **URL:** `/visual-reference-management-guide/`
- **Target Keywords:**
  - Primary: "visual reference management" (480/mo, KD: 28)
  - Secondary: "design reference workflow" (260/mo, KD: 22)
  - Long-tail: "how to organize design references" (170/mo, KD: 15)

**Supporting Posts:**
1. "The 5-Step Visual Research Workflow That Actually Works"
2. "How to Find That One Reference You Saved 3 Months Ago"
3. "Organizing References by Project vs. by Topic: Which Works Better?"
4. "From Discovery to Deliverable: A Designer's Reference Pipeline"

---

### Cluster 3: Are.na Alternative (Niche, Low Competition)

**Pillar Post (2000+ words):**
- **Title:** "Are.na Alternative: When to Keep References Private"
- **URL:** `/are-na-alternative-private-references/`
- **Target Keywords:**
  - Primary: "are.na alternative" (390/mo, KD: 19)
  - Secondary: "private visual archive" (110/mo, KD: 12)

**Supporting Posts:**
1. "Are.na vs Private Archives: The Social Cost of Sharing Too Early"
2. "Building a Personal Canon vs. a Public Feed"

---

### Cluster 4: Creative Workflows (Emerging, Low Competition)

**Pillar Post (2500+ words):**
- **Title:** "The Modern Creative's Visual Workflow: From Inspiration to Archive"
- **URL:** `/creative-visual-workflow-2026/`
- **Target Keywords:**
  - Primary: "creative workflow 2026" (140/mo, KD: 15)
  - Secondary: "designer workflow tools" (220/mo, KD: 28)

**Supporting Posts:**
1. "Mood Boards Are Dead: What's Replacing Them in 2026"
2. "The 30-Second Reference Retrieval Challenge"
3. "Why Your Inspiration System Isn't Working (And How to Fix It)"

---

## Phase 3: GEO-Optimized Content Templates

### Template: Comparison Post (High GEO Potential)

```markdown
---
title: "[Tool A] vs [Tool B]: Which Fits Your [Use Case]?"
date: 2026-03-XX
draft: false
description: "Compare [Tool A] and [Tool B] for [use case]. 
Based on [X] hours of testing and [Y] designer workflows."
tags: ["tools", "comparison", "workflow"]
categories: ["guides"]
---

## Quick Answer

For [specific use case], **[Winner]** is better because [one-sentence reason]. 
However, choose **[Alternative]** if [specific condition].

| Feature | [Tool A] | [Tool B] | Winner |
|---------|----------|----------|--------|
| [Feature 1] | [Detail] | [Detail] | [Winner] |
| [Feature 2] | [Detail] | [Detail] | [Winner] |

---

## Why This Comparison Matters

[Problem statement with statistics]
According to [Source], [X]% of [audience] struggle with [problem].

---

## [Tool A] Overview

### What [Tool A] Does Best
- [Point 1 with specific example]
- [Point 2 with specific example]
- [Point 3 with specific example]

### Where [Tool A] Falls Short
- [Limitation 1]
- [Limitation 2]

### Best For
- [Persona 1]
- [Persona 2]

---

## [Tool B] Overview

### What [Tool B] Does Best
...

### Where [Tool B] Falls Short
...

### Best For
...

---

## Side-by-Side Comparison

[Detailed comparison table or sections]

---

## FAQ

### Which is better for [specific use case]?
[Direct answer with reasoning]

### Can I use both tools together?
[Answer with workflow suggestion]

### Is there a free alternative?
[Answer with options]

### What do designers on Reddit say?
[Quote from r/graphic_design or similar]

---

## Bottom Line

Choose **[Tool A]** if: [conditions]
Choose **[Tool B]** if: [conditions]

Neither fits? Try [Mare/Alternative] for [specific advantage].

*[This guide was last updated March 2026 based on hands-on testing 
with real design projects.]*
```

### Template: Tutorial Post (High SEO + Medium GEO)

```markdown
---
title: "How to [Achieve Result] in [Timeframe]: Complete Guide"
date: 2026-03-XX
draft: false
description: "Learn how to [achieve result] step by step. 
Based on [X] hours of research and real-world testing."
tags: ["tutorial", "workflow", "how-to"]
categories: ["tutorials"]
---

## What You'll Learn

By the end of this guide, you'll be able to [specific outcome]. 
This process takes approximately [time] and requires [tools/prerequisites].

---

## Quick Overview

1. [Step 1] → [Result]
2. [Step 2] → [Result]
3. [Step 3] → [Result]
4. [Step 4] → [Final result]

---

## Before You Start

### What You Need
- [Tool/Requirement 1]
- [Tool/Requirement 2]
- [Tool/Requirement 3]

### Expected Time
- Setup: [X] minutes
- Execution: [Y] minutes
- Total: [Z] minutes

---

## Step 1: [Action]

[Detailed instructions with screenshots if applicable]

**Pro tip:** [Expert advice]

**Common mistake:** [What to avoid]

---

## Step 2: [Action]

...

---

## FAQ

### What if [common problem]?
[Solution]

### Can I do this with [alternative tool]?
[Answer with caveats]

### How long does this take for [specific use case]?
[Time estimate]

---

## Next Steps

Now that you've [achieved result], consider:
- [Related article 1]
- [Related article 2]
- [Tool/Resource recommendation]
```

---

## Phase 4: Publishing Schedule

### March 2026

| Week | Pillar Post | Supporting Post 1 | Supporting Post 2 |
|------|-------------|-------------------|-------------------|
| W1 | Technical setup + robots.txt | — | — |
| W2 | Pinterest Complete Guide | Why Designers Leaving Pinterest | — |
| W3 | Visual Reference Management Guide | 5-Step Workflow | How to Find Old References |
| W4 | Are.na Alternative | Private vs Public Archives | — |

### April 2026

| Week | Pillar Post | Supporting Post 1 | Supporting Post 2 |
|------|-------------|-------------------|-------------------|
| W1 | Creative Workflow 2026 | Mood Boards Are Dead | 30-Second Retrieval |
| W2 | Pinterest vs Are.na vs Mare | — | — |
| W3 | Export Pinterest Guide | — | — |
| W4 | Own Your Archive | — | — |

### May 2026

- Update existing posts with new data
- Create content upgrades (templates, checklists)
- Build email course from post series
- Repurpose into Twitter/LinkedIn threads

---

## Phase 5: GEO Optimization Checklist

### Per Post Requirements

**Answer-First Structure:**
- [ ] H1 is a question or clear statement
- [ ] First paragraph answers the question directly
- [ ] No fluff before the answer

**Statistics & Citations:**
- [ ] 3+ statistics with sources
- [ ] 2+ expert quotes with attribution
- [ ] 1+ study/research reference

**Schema Markup:**
- [ ] Article schema present
- [ ] FAQPage schema (if FAQ section exists)
- [ ] HowTo schema (if tutorial)
- [ ] BreadcrumbList schema

**Content Format:**
- [ ] Comparison table (if comparing)
- [ ] Numbered lists for steps
- [ ] Bullet points for features
- [ ] Short paragraphs (2-3 sentences)

**Technical:**
- [ ] Page loads in <3 seconds
- [ ] Mobile-friendly
- [ ] Proper heading hierarchy (H1 > H2 > H3)
- [ ] Internal links to related posts
- [ ] External links to authoritative sources

---

## Phase 6: Monitoring & Iteration

### Track Weekly
- Google Search Console: Impressions, CTR, avg position
- Google Analytics: Organic traffic, bounce rate, time on page
- Bing Webmaster Tools: Indexing status

### Track Monthly
- AI search citations (manual check: ChatGPT, Perplexity, Claude)
- Keyword rankings (manual spot checks)
- Backlinks earned
- Social shares

### Update Quarterly
- Refresh statistics with 2026 data
- Add new FAQ based on user questions
- Update comparison posts with new features
- Check and fix broken links

---

## Target Metrics (90 Days)

| Metric | Baseline | Target |
|--------|----------|--------|
| Total posts | 4 | 16 |
| Organic sessions | ~0 | 500/mo |
| Avg position (tracked keywords) | — | Top 20 |
| AI search citations | 0 | 5+ |
| Featured snippets | 0 | 2+ |

---

## Priority Keywords (Track These)

### Tier 1 (Immediate Focus)
1. "pinterest alternative 2026" — 2,400/mo
2. "pinterest alternative for designers" — 880/mo
3. "visual reference management" — 480/mo
4. "are.na alternative" — 390/mo

### Tier 2 (Month 2-3)
5. "export pinterest boards" — 720/mo
6. "pinterest vs arena" — 590/mo
7. "design reference workflow" — 260/mo
8. "why designers hate pinterest" — 320/mo

### Tier 3 (Long Tail)
9. "own your visual data" — 210/mo
10. "how to organize design references" — 170/mo
11. "best pinterest alternative without algorithm" — 140/mo
12. "creative workflow 2026" — 140/mo

---

## Next Actions

**This Week:**
1. [ ] Create robots.txt with AI bot permissions
2. [ ] Create llms.txt file
3. [ ] Add Article schema to Hugo theme
4. [ ] Write "Complete Pinterest Alternatives Guide" pillar post

**Next Week:**
1. [ ] Publish pillar post
2. [ ] Write "Why Designers Are Leaving Pinterest" supporting post
3. [ ] Submit sitemap to Google Search Console
4. [ ] Set up Bing Webmaster Tools

Ready to start?