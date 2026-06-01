# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3431?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3431
- Title: Improving Measurements for Loneliness and Isolation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3431
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-03-31T19:28:46Z
- Update date including text: 2026-03-31T19:28:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3431",
    "number": "3431",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Improving Measurements for Loneliness and Isolation Act of 2025",
    "type": "S",
    "updateDate": "2026-03-31T19:28:46Z",
    "updateDateIncludingText": "2026-03-31T19:28:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-12-11T15:36:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NH"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3431is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3431\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Ricketts (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo direct the Secretary of Health and Human Services to establish a working group to formulate recommendations for standardizing the measurements of loneliness and isolation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Measurements for Loneliness and Isolation Act of 2025 .\n#### 2. Working Group on Unifying Loneliness Research\n##### (a) Definitions\nIn this section:\n**(1)**\nThe term isolation means the objective lack of social relationships or limited social contact with others.\n**(2)**\nThe term loneliness means a subjective feeling of being isolated.\n##### (b) Establishment\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall establish a national working group, to be known as the Working Group on Unifying Loneliness Research (in this section referred to as the Working Group ), to formulate recommendations for standardizing the measurements of loneliness and isolation.\n##### (c) Goals\nThe goals of the recommendations under subsection (b) shall be the following:\n**(1)**\nCollaboration, cooperation, and consultation among Federal departments and agencies with respect to developing standardized measurements of loneliness and isolation for the purposes of\u2014\n**(A)**\nhaving standardized measurements for use in public and private research, including surveys across varying populations, with the ability to capture the level of granularity needed to guide strategic decisionmaking, planning, and evaluation of strategies to combat loneliness and isolation; and\n**(B)**\nproviding reliable, consistent measurement tools for use across fields and industries in health care.\n**(2)**\nCollaboration, cooperation, and consultation among Federal departments and agencies with respect to developing standardized definitions of loneliness, isolation, and relevant terms associated with loneliness and isolation for the purposes of education, awareness, and understanding of the terms for the general public.\n**(3)**\nAssessment of the alignment of previous methods of measuring loneliness and isolation in the public and private sectors.\n##### (d) Composition\nThe Working Group shall be composed of\u2014\n**(1)**\nsenior-level representatives of\u2014\n**(A)**\nthe Department of Health and Human Services;\n**(B)**\nthe Centers for Medicare & Medicaid Services;\n**(C)**\nthe Centers for Disease Control and Prevention;\n**(D)**\nthe Administration for Community Living;\n**(E)**\nthe National Institutes of Health;\n**(F)**\nthe Substance Abuse and Mental Health Services Administration;\n**(G)**\nthe Health Resources and Services Administration;\n**(H)**\nthe Agency for Healthcare Research and Quality; and\n**(I)**\nother agencies, groups, subject matter experts, or researchers the Secretary deems beneficial to be represented in the Working Group consistent with the goals specified in subsection (c);\n**(2)**\n1 representative of each of the three States with the highest numbers of practitioners needed to remove the designations of all mental health care health professional shortage areas in the respective State (as reflected in the report of the Health Resources and Services Administration titled Designated Health Professional Shortage Areas Statistics (June 30, 2023)), with each such representative designated by the Governor of the respective State; and\n**(3)**\n1 representative of the each of the three States with the lowest numbers of practitioners needed to remove such designations, with each such representative designated by the Governor of the respective State.\n##### (e) Report to Congress\n**(1) In general**\nNot later than one year after the date of enactment of this Act, the Working Group shall\u2014\n**(A)**\nsubmit to the committees listed in paragraph (3) a report describing the work and recommendations of the Working Group; and\n**(B)**\nmake such report publicly available on the internet.\n**(2) Meetings**\nThe Working Group shall meet not less than 3 times in the course of developing its report.\n**(3) Committees**\nThe committees referred to in paragraph (1)(A) are the following:\n**(A)**\nThe Committee on Education and Workforce of the House of Representatives.\n**(B)**\nThe Committee on Energy and Commerce of the House of Representatives.\n**(C)**\nThe Committee on Ways and Means of the House of Representatives.\n**(D)**\nThe Committee on Finance of the Senate.\n**(E)**\nThe Committee on Health, Education, Labor, and Pensions of the Senate.\n##### (f) Definition\nIn this section, the term State means each of the 50 States.\n##### (g) Sunset\nThis section shall cease to be effective at the end of calendar year 2027.",
      "versionDate": "2025-12-11",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-13",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1305",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Improving Measurements for Loneliness and Isolation Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-01-08T19:44:39Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3431is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Improving Measurements for Loneliness and Isolation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Measurements for Loneliness and Isolation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Health and Human Services to establish a working group to formulate recommendations for standardizing the measurements of loneliness and isolation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:26Z"
    }
  ]
}
```
