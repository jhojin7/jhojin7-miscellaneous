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

QUERY_ACTIVECODINGCHALLENGE = """
{"query":"\n    query questionOfToday {\n  activeDailyCodingChallengeQuestion {\n    date\n    userStatus\n    link\n    question {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      hasVideoSolution\n      hasSolution\n      topicTags {\n        name\n        id\n        slug\n      }\n    }\n  }\n}\n    ","variables":{}}
"""


print("success queries.py")

# import requests
# url = 'https://leetcode.com'
# # cookie = {'LEETCODE_SESSION': session_id}
# resp = requests.get(url, cookies=COOKIE)
# print(resp.text)