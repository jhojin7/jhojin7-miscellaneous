# queries.py
# Module for GraphQL queries text

QUERY_SUBMISSIONS = \
"""
{
    "operationName": "Submissions",
    "variables": {
        "offset": 0,
        "limit": 20,
        "lastKey": null,
        "questionSlug": "%s"
    },
    "query": "query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {
        submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
            lastKey
            hasNext
            submissions {
            id
            statusDisplay
            lang
            runtime
            timestamp
            url
            isPending
            memory
            __typename
            }
            __typename
        }
    }"
}
"""
QUERY_DAILYCODINGCHALLENGE = \
"""
query {    
    dailyCodingChallengeV2(year: %s, month: %s) {
        challenges {
            date
            userStatus
            link
            question {
                questionFrontendId
                title
                titleSlug
            }
        }
        weeklyChallenges {
            date
            userStatus
            link
            question {
                questionFrontendId
                title
                titleSlug
            }
        }
    }
}
"""

print("success queries.py")

import requests
url = 'https://leetcode.com'
session_id = ''
cookie = {'LEETCODE_SESSION': session_id}
resp = requests.get(url, cookies=cookie)