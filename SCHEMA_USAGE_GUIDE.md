# Advanced Schema Usage Guide
# How to maximize SEOGEO with front matter

This guide shows how to use the advanced schema types in your Hugo posts.

---

## 1. FAQPage Schema (+40% AI Visibility)

Best for: Posts with questions/answers, comparison posts, guides

```yaml
---
title: "Pinterest Alternative FAQ"
date: 2026-03-01
draft: false
description: "Common questions about Pinterest alternatives"
schema_type: "FAQPage"
faqs:
  - question: "What's the best Pinterest alternative for designers?"
    answer: "According to our research of 500+ designers, Mare is the best Pinterest alternative for those building personal visual canons. Unlike Pinterest's algorithm, Mare gives you full control over your references."
  - question: "Can I export my Pinterest boards?"
    answer: "Yes. Pinterest allows bulk export via their data download feature. Most Pinterest alternatives including Mare can import these files."
  - question: "Why are designers leaving Pinterest?"
    answer: "The main reasons are algorithmic feed fatigue (73% of surveyed designers), loss of source links (61%), and inability to find saved references (58%)."
---
```

---

## 2. HowTo Schema (Tutorials)

Best for: Step-by-step guides, workflows, tutorials

```yaml
---
title: "How to Export Pinterest Boards (Complete Guide)"
date: 2026-03-01
draft: false
description: "Step-by-step guide to exporting your Pinterest boards without losing data"
schema_type: "HowTo"
howto:
  totalTime: "PT15M"
  steps:
    - name: "Request Your Data"
      text: "Go to Pinterest Settings > Privacy and Data > Request Data Download. Enter your email and confirm."
      image: "/images/pinterest-export-step1.png"
    - name: "Wait for Email"
      text: "Pinterest will send a download link within 24-48 hours. Check your spam folder if you don't see it."
      image: "/images/pinterest-export-step2.png"
    - name: "Download the Archive"
      text: "Click the link in the email and download the ZIP file. It contains all your pins, boards, and metadata."
      image: "/images/pinterest-export-step3.png"
    - name: "Extract and Organize"
      text: "Unzip the file. Your pins will be in the 'pins' folder with JSON metadata. Images are in the 'images' folder."
      image: "/images/pinterest-export-step4.png"
---
```

---

## 3. Product Schema (Tool Reviews)

Best for: Tool comparisons, software reviews, product recommendations

```yaml
---
title: "Mare Review: Visual Reference Management Tool"
date: 2026-03-01
draft: false
description: "In-depth review of Mare visual reference management tool"
schema_type: "Product"
product:
  name: "Mare"
  description: "Visual reference management for cultural creatives"
  image: "/images/mare-product.png"
  brand: "Mare"
  ratingValue: "4.8"
  reviewCount: "150"
  reviewRating: "5"
  reviewBody: "Mare is the best tool for designers who've outgrown Pinterest. The private archive approach and fast search make it ideal for building personal visual canons."
---

## Content Structure

The rest of your post content goes here...
```

---

## 4. Comparison Schema (ItemList)

Best for: Comparison posts, ranked lists, "best of" articles

```yaml
---
title: "5 Best Pinterest Alternatives for Designers (2026)"
date: 2026-03-01
draft: false
description: "Ranked comparison of the best Pinterest alternatives"
schema_type: "Comparison"
comparison_items:
  - name: "Mare"
    description: "Best for private visual archives and personal canons"
  - name: "Are.na"
    description: "Best for collaborative research and sharing"
  - name: "Cosmos"
    description: "Best for academic and cultural research"
  - name: "Milanote"
    description: "Best for mood boards and client presentations"
  - name: "Pureref"
    description: "Best for digital artists and reference boards"
---
```

---

## 5. Enhanced Article Schema (Default)

Use this when you don't specify `schema_type`. Includes:
- Citation support
- Speakable sections
- Keywords
- About entity

```yaml
---
title: "Why Designers Are Leaving Pinterest in 2026"
date: 2026-03-01
draft: false
description: "The real reasons designers are moving away from Pinterest"
keywords: ["pinterest alternative", "designers leaving pinterest", "2026"]
article_section: "Trends"
wordCount: 2500
about:
  name: "Pinterest"
  sameAs: "https://www.wikidata.org/wiki/Q2462666"
cited_sources:
  - name: "Princeton GEO Research 2024"
    author: "Princeton NLP Group"
    url: "https://arxiv.org/abs/2311.09735"
  - name: "Designer Survey 2026"
    author: "Mare Research Team"
    url: "https://mare.run/research/2026-survey"
---
```

---

## 6. Series/Collection Schema

For multi-part content clusters:

```yaml
---
title: "Pinterest Alternative Guide: Part 1"
date: 2026-03-01
draft: false
series:
  name: "Pinterest Alternative Complete Guide"
  description: "Everything you need to know about leaving Pinterest"
  parts:
    - title: "Part 1: Why Designers Leave Pinterest"
      url: "/why-designers-leave-pinterest/"
    - title: "Part 2: Pinterest Alternatives Compared"
      url: "/pinterest-alternatives-compared/"
    - title: "Part 3: How to Migrate Your Boards"
      url: "/migrate-pinterest-boards/"
    - title: "Part 4: Building Your New Workflow"
      url: "/building-visual-workflow/"
---
```

---

## Quick Reference: Schema Type by Post Type

| Post Type | Schema Type | Why |
|-----------|-------------|-----|
| Tutorial | HowTo | Appears in Google "How To" rich results |
| FAQ/Questions | FAQPage | +40% AI citation rate (Perplexity, etc.) |
| Tool Review | Product | Rich snippets with ratings |
| Comparison | Comparison | ItemList appears in search |
| Guide/Article | (default) | BlogPosting with citations |
| Pillar Post | Series | Shows content relationships |

---

## Testing Your Schema

After publishing, validate with:

1. **Google Rich Results Test**
   https://search.google.com/test/rich-results

2. **Schema.org Validator**
   https://validator.schema.org/

3. **Bing Markup Validator**
   https://www.bing.com/webmasters/help/markup-validator

---

## GEO Optimization Checklist

For each post, ensure:

- [ ] Direct answer in first paragraph
- [ ] Statistics with citations
- [ ] Expert quotes with attribution
- [ ] FAQ section (even if small)
- [ ] Schema type appropriate for content
- [ ] Short paragraphs (2-3 sentences)
- [ ] Bullet points and lists
- [ ] Comparison tables where relevant
- [ ] Internal links to related posts
- [ ] External links to authoritative sources

---

## Example: Complete GEO-Optimized Post

```yaml
---
title: "Pinterest vs Are.na: Which Tool Fits Your Workflow?"
date: 2026-03-01
draft: false
description: "Compare Pinterest and Are.na for visual reference management. Based on 30 days of testing with real design projects."
keywords: ["pinterest vs arena", "visual reference tools", "design workflow"]
article_section: "Comparisons"
schema_type: "FAQPage"
faqs:
  - question: "Is Are.na better than Pinterest?"
    answer: "Are.na is better than Pinterest for collaborative research and sharing references publicly. However, Pinterest is better for discovery and casual inspiration browsing. According to our testing, 68% of designers prefer Are.na for client work, while 72% use Pinterest for personal inspiration."
  - question: "Can Are.na replace Pinterest?"
    answer: "Are.na can replace Pinterest for research workflows but not for discovery. Pinterest's algorithm shows you content you didn't know you needed. Are.na requires intentional searching."
  - question: "Which is better for private references?"
    answer: "Neither Pinterest nor Are.na is ideal for private references. Pinterest is entirely public. Are.na has private channels but is designed for sharing. For truly private visual archives, consider Mare or local solutions."
cited_sources:
  - name: "Visual Reference Tool Survey 2026"
    author: "Mare Research Team"
    url: "https://mare.run/research/2026-survey"
---

## Quick Answer

For **collaborative research**: Use Are.na.  
For **personal discovery**: Use Pinterest.  
For **private archives**: Use neither—try Mare.

## Comparison Table

| Feature | Pinterest | Are.na | Winner |
|---------|-----------|--------|--------|
| Algorithm | Yes (heavy) | No | Are.na |
| Privacy | Public only | Public/Private | Are.na |
| Discovery | Excellent | Poor | Pinterest |
| Collaboration | Limited | Excellent | Are.na |
| Price | Free | Free/Paid | Tie |

## Detailed Comparison

[Full post content here...]

## FAQ

### Is Are.na better than Pinterest?
[Answer from front matter faqs]

### Can Are.na replace Pinterest?
[Answer from front matter faqs]

### Which is better for private references?
[Answer from front matter faqs]

---

*Last updated: March 2026. Based on hands-on testing with real design projects.*
```

This post would have:
- FAQPage schema (from front matter)
- Comparison table (visible + structured)
- Citations (from cited_sources)
- Quick answer (GEO-optimized structure)
- Last updated date (freshness signal)
