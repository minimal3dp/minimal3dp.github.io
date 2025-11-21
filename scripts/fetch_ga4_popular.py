#!/usr/bin/env python3
"""
Fetch top pages from GA4 using the Google Analytics Data API.
Writes to static/data/popular.json

Requires: GOOGLE_APPLICATION_CREDENTIALS pointing to service account json.
Repo secrets: GA4_SERVICE_ACCOUNT (base64) and GA4_PROPERTY_ID
"""
import json
import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest

PROPERTY_ID = os.getenv('GA4_PROPERTY_ID')
OUTPUT = os.getenv('OUTPUT_PATH','static/data/popular.json')
MAX = int(os.getenv('MAX',5))
SECTIONS = os.getenv('SECTIONS','/blog/,/tools/,/projects/')

if not PROPERTY_ID:
    raise SystemExit('GA4_PROPERTY_ID not provided')

client = BetaAnalyticsDataClient()
request = RunReportRequest(
    property=f"properties/{PROPERTY_ID}",
    date_ranges=[DateRange(start_date='30daysAgo', end_date='today')],
    dimensions=[Dimension(name='pagePath'), Dimension(name='pageTitle')],
    metrics=[Metric(name='screenPageViews')],
    limit=50,
)

response = client.run_report(request)
results = []
for row in response.rows:
    path = row.dimension_values[0].value
    title = row.dimension_values[1].value
    views = int(row.metric_values[0].value)
    # convert pagePath to full url for site
    url = path if path.startswith('http') else path
    results.append({'title': title,'url': url,'views': views})

# sort and pick top
results.sort(key=lambda x: x['views'], reverse=True)
# Build a top-level map: global + keyed sections (by path prefix)
sections = [s.strip() for s in SECTIONS.split(',') if s.strip()]
output = {}
results.sort(key=lambda x: x['views'], reverse=True)
output['global'] = results[:MAX]
for prefix in sections:
    filtered = [r for r in results if r['url'].startswith(prefix)]
    output_key = prefix.strip('/').replace('/','-') or 'section'
    output[output_key] = filtered[:MAX]

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT,'w') as f:
    json.dump(output,f,indent=2)

print('Wrote', OUTPUT)
