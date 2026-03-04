#!/usr/bin/env python3
"""Test Content Gap Analysis for Hugo blog"""

import json
import os
from pathlib import Path
from datetime import datetime

BLOG_DIR = Path("/home/felipe/.openclaw/workspace/blog-mare/content/posts")
DATA_DIR = Path("/home/felipe/shared/openclaw_data")

def get_posts():
    """Get all posts with their frontmatter"""
    posts = []
    for md in BLOG_DIR.glob("*.md"):
        content = md.read_text()
        title = None
        tags = []
        categories = []
        description = None

        for line in content.split('\n'):
            if line.startswith('title:'):
                title = line.split(':', 1)[1].strip().strip('"')
            elif line.startswith('tags:'):
                tags = [t.strip().strip('"') for t in line.split('[', 1)[1].split(']')[0].split(',')]
            elif line.startswith('categories:'):
                categories = [t.strip().strip('"') for t in line.split('[', 1)[1].split(']')[0].split(',')]
            elif line.startswith('description:'):
                description = line.split(':', 1)[1].strip().strip('"')

        posts.append({
            'file': md.name,
            'title': title,
            'tags': tags,
            'categories': categories,
            'description': description
        })
    return posts

def get_keywords():
    """Get keyword research data if exists"""
    kw_file = DATA_DIR / "keywords.json"
    if kw_file.exists():
        return json.loads(kw_file.read_text())
    return {}

def get_competitors():
    """Get competitor data"""
    comp_file = DATA_DIR / "competitors.json"
    if comp_file.exists():
        return json.loads(comp_file.read_text())
    return {}

def analyze_gaps(posts, keywords, competitors):
    """Analyze content gaps"""
    existing_topics = set()
    for p in posts:
        existing_topics.update(p.get('tags', []))
        existing_topics.update(p.get('categories', []))
        if p.get('title'):
            existing_topics.add(p['title'].lower())

    gaps = []

    # Gap 1: Pinterest addiction alternatives (high volume)
    if 'pinterest' not in existing_topics and 'pinterest addiction' not in str(existing_topics):
        gaps.append({
            'topic': 'Pinterest addiction recovery',
            'reason': 'High search volume, competitors rank well',
            'priority': 1
        })

    # Gap 2: Visual reference management
    if 'reference management' not in str(existing_topics):
        gaps.append({
            'topic': 'Visual reference management',
            'reason': 'Core keyword for Mare positioning',
            'priority': 1
        })

    # Gap 3: Design inspiration tools comparison
    if 'comparison' not in str(existing_topics):
        gaps.append({
            'topic': 'Design inspiration tools comparison',
            'reason': 'Intentional search queries, high conversion',
            'priority': 2
        })

    # Gap 4: Creative workflow organization
    if 'workflow' not in str(existing_topics):
        gaps.append({
            'topic': 'Creative workflow organization',
            'reason': 'Related to existing design-workflow tag',
            'priority': 2
        })

    # Gap 5: Offline inspiration capture
    if 'offline' not in str(existing_topics):
        gaps.append({
            'topic': 'Offline inspiration capture methods',
            'reason': 'Pain point mentioned by competitors users',
            'priority': 3
        })

    return gaps

def main():
    print("=== Content Gap Analysis Test ===\n")

    posts = get_posts()
    print(f"Posts found: {len(posts)}")
    for p in posts:
        print(f"  - {p['title']} [{', '.join(p['tags'][:3])}]")

    keywords = get_keywords()
    competitors = get_competitors()

    gaps = analyze_gaps(posts, keywords, competitors)

    print(f"\n=== Content Gaps Identified: {len(gaps)} ===\n")

    for i, gap in enumerate(gaps, 1):
        print(f"{i}. {gap['topic']}")
        print(f"   Priority: {gap['priority']}")
        print(f"   Reason: {gap['reason']}")
        print()

    print("=== Recommendations ===")
    print("- Priority 1: High volume, low competition topics")
    print("- Priority 2: Competitor weaknesses we can exploit")
    print("- Priority 3: Emerging trends from Reddit/Google Trends")

    print("\n=== Output for Cron ===")
    print(json.dumps({'gaps': gaps, 'count': len(gaps)}, indent=2))

if __name__ == "__main__":
    main()