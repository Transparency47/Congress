# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2924?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2924
- Title: Small Entity Update Act
- Congress: 119
- Bill type: S
- Bill number: 2924
- Origin chamber: Senate
- Introduced date: 2025-09-29
- Update date: 2026-04-21T11:03:28Z
- Update date including text: 2026-04-21T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-29: Introduced in Senate
- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-29: Introduced in Senate

## Actions

- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-29",
    "latestAction": {
      "actionDate": "2025-09-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2924",
    "number": "2924",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Small Entity Update Act",
    "type": "S",
    "updateDate": "2026-04-21T11:03:28Z",
    "updateDateIncludingText": "2026-04-21T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-29",
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
        "item": [
          {
            "date": "2025-09-29T19:51:52Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-29T19:51:52Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MD"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2924is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2924\nIN THE SENATE OF THE UNITED STATES\nSeptember 29, 2025 Mrs. Britt (for herself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Securities and Exchange Commission to carry out a study and rulemaking on the definition of the term small entity under the securities laws for purposes of chapter 6 of title 5, United States Code, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Entity Update Act .\n#### 2. Studies, reports, and rules regarding small entities\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term Commission means the Securities and Exchange Commission; and\n**(2)**\nthe term small entity \u2014\n**(A)**\nhas the meaning given the term in section 601 of title 5, United States Code, with respect to the activities of the Commission; and\n**(B)**\nincludes any definition established by the Commission of the term small business , small organization , small governmental jurisdiction , or small entity under paragraph (3), (4), (5), or (6), respectively, of section 601 of title 5, United States Code, with respect to the activities of the Commission.\n##### (b) Studies and reports\nNot later than 1 year after the date of enactment of this Act, and again 5 years thereafter, the Commission shall\u2014\n**(1)**\nconduct a study of the definition of the term small entity with respect to the activities of the Commission for the purposes of chapter 6 of title 5, United States Code, which shall consider\u2014\n**(A)**\nthe extent to which the definition of the term small entity , as in effect during the period in which the study is conducted, aligns with the findings and declarations made under section 2(a) of the Regulatory Flexibility Act ( 5 U.S.C. 601 note);\n**(B)**\nthe amount by which financial markets in the United States have grown since the last time the Commission amended the definition of the term small entity , if applicable; and\n**(C)**\nhow the Commission should define the term small entity to ensure that a meaningful number of entities would fall under that definition; and\n**(2)**\nsubmit to Congress a report that includes\u2014\n**(A)**\nthe results of the applicable study conducted under paragraph (1); and\n**(B)**\nspecific and detailed recommendations on the ways in which the Commission could amend the definition of the term small entity to\u2014\n**(i)**\nbe consistent with the results described in subparagraph (A); and\n**(ii)**\nexpand the number of entities covered by such definition.\n##### (c) Rulemaking\nConcurrently with, or after the completion of, each study required under subsection (b), the Commission shall, subject to public notice and comment, revise the rules of the Commission consistent with the results of such study.\n##### (d) Inflation adjustments\nAfter the Commission issued the final rule revisions required under subsection (c), and every 5 years thereafter, the Commission shall adjust any dollar figures under the definition of small entity established by the Commission to reflect the change in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor.",
      "versionDate": "2025-09-29",
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
        "actionDate": "2025-07-22",
        "text": "Received in the Senate and Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3382",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Small Entity Update Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-16T17:58:13Z"
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
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2924is.xml"
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
      "title": "Small Entity Update Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Entity Update Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-09T04:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Securities and Exchange Commission to carry out a study and rulemaking on the definition of the term \"small entity\" under the securities laws for purposes of chapter 6 of title 5, United States Code, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-09T04:48:16Z"
    }
  ]
}
```
