#!/usr/bin/env python3
"""Test SEO Report for Hugo blog"""

import json
from pathlib import Path
from datetime import datetime, timedelta

BLOG_DIR = Path("/home/felipe/.openclaw/workspace/blog-mare")
DATA_DIR = Path("/home/felipe/shared/openclaw_data")

def get_posts():
    """Get all posts with their metadata"""
    posts_dir = BLOG_DIR / "content/posts"
    posts = []
    for md in posts_dir.glob("*.md"):
        content = md.read_text()
        title = None
        date = None
        tags = []
        description = None

        for line in content.split('\n'):
            if line.startswith('title:'):
                title = line.split(':', 1)[1].strip().strip('"')
            elif line.startswith('date:'):
                date = line.split(':', 1)[1].strip()
            elif line.startswith('tags:'):
                tags = [t.strip().strip('"') for t in line.split('[', 1)[1].split(']')[0].split(',') if t.strip()]
            elif line.startswith('description:'):
                description = line.split(':', 1)[1].strip().strip('"')

        posts.append({
            'file': md.name,
            'title': title,
            'date': date,
            'tags': tags,
            'description': description
        })
    return posts

def check_seo_health():
    """Check technical SEO health"""
    issues = []
    posts = get_posts()

    # Check for posts without descriptions
    missing_desc = [p for p in posts if not p.get('description')]
    if missing_desc:
        issues.append({
            'type': 'meta_description',
            'count': len(missing_desc),
            'files': [p['file'] for p in missing_desc]
        })

    # Check for posts without tags
    missing_tags = [p for p in posts if not p.get('tags')]
    if missing_tags:
        issues.append({
            'type': 'tags',
            'count': len(missing_tags),
            'files': [p['file'] for p in missing_tags]
        })

    # Check sitemap
    sitemap = BLOG_DIR / "public/sitemap.xml"
    if sitemap.exists():
        sitemap_content = sitemap.read_text()
        url_count = sitemap_content.count('<url>') - 1  # Subtract 1 for urlset
        issues.append({
            'type': 'sitemap',
            'status': 'ok',
            'urls': url_count
        })
    else:
        issues.append({
            'type': 'sitemap',
            'status': 'missing'
        })

    return issues

def get_content_performance():
    """Get content performance summary"""
    posts = get_posts()

    # Count by tags
    tag_counts = {}
    for p in posts:
        for tag in p.get('tags', []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    # Top categories
    categories = {}
    for p in posts:
        # Extract category from file or tags
        if 'alternative' in str(p.get('tags', [])).lower():
            categories['Alternatives'] = categories.get('Alternatives', 0) + 1
        if 'pinterest' in str(p.get('tags', [])).lower():
            categories['Pinterest'] = categories.get('Pinterest', 0) + 1
        if 'design workflow' in str(p.get('tags', [])).lower():
            categories['Workflow'] = categories.get('Workflow', 0) + 1

    return {
        'total_posts': len(posts),
        'tag_distribution': tag_counts,
        'category_breakdown': categories,
        'top_tags': sorted(tag_counts.items(), key=lambda x: -x[1])[:5]
    }

def main():
    print("=== SEO Report Test ===\n")

    # 1. Content Overview
    posts = get_posts()
    print(f"Total Posts: {len(posts)}")
    print("\nPosts:")
    for p in posts:
        print(f"  - {p['title']} ({p['date']})")

    # 2. Content Performance
    perf = get_content_performance()
    print(f"\n=== Content Performance ===")
    print(f"Total posts: {perf['total_posts']}")
    print(f"\nTag distribution:")
    for tag, count in perf['top_tags']:
        print(f"  {tag}: {count}")

    # 3. Technical SEO Health
    print(f"\n=== Technical SEO Health ===")
    health = check_seo_health()
    for issue in health:
        if issue['type'] == 'sitemap':
            print(f"  Sitemap: {issue.get('status', 'unknown')} ({issue.get('urls', 0)} URLs)")
        else:
            print(f"  {issue['type']}: {issue['count']} issues")

    # 4. Action Items
    print(f"\n=== Action Items ===")
    action_items = []

    if len(posts) < 10:
        action_items.append(f"Add more content ({10 - len(posts)} more posts recommended)")

    health_issues = [i for i in health if i['type'] != 'sitemap']
    if health_issues:
        action_items.append(f"Fix {len(health_issues)} technical SEO issues")

    for item in action_items:
        print(f"  - {item}")

    # 5. Output for cron
    print(f"\n=== Cron Output ===")
    output = {
        'total_posts': len(posts),
        'posts': posts,
        'technical_health': health,
        'performance': perf,
        'action_items': action_items
    }
    print(json.dumps(output, indent=2, default=str))

if __name__ == "__main__":
    main()