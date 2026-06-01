# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2826?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2826
- Title: 988 LGBTQ+ Youth Access Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2826
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-04-16T19:12:57Z
- Update date including text: 2026-04-16T19:12:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2826",
    "number": "2826",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "988 LGBTQ+ Youth Access Act of 2025",
    "type": "S",
    "updateDate": "2026-04-16T19:12:57Z",
    "updateDateIncludingText": "2026-04-16T19:12:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
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
            "date": "2026-03-19T14:00:48Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-09-17T15:38:13Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2826is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2826\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Ms. Baldwin (for herself and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo direct the Secretary of Health and Human Services to dedicate sufficient resources for the support of LGBTQ+ youth seeking help from the 9\u20138\u20138 suicide prevention hotline, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 988 LGBTQ+ Youth Access Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\naccording to the Centers for Disease Control and Prevention, 45 percent of high school students who seriously considered attempting suicide in 2021 identified as LGBTQ+;\n**(2)**\nsince its launch, the Specialized Services for LGBTQ+ youth within the 988 Suicide Prevention and Crisis Lifeline have received nearly 1,500,000 calls, texts, and chats, with an average of 2,200 contacts per day as of May 2025; and\n**(3)**\ngiven that LGBTQ+ youth are four times more likely to attempt suicide as compared to their peers, the Specialized Services for LGBTQ+ youth are equipped with crucial training addressing LGBTQ+ specific challenges and needs.\n#### 3. Suicide prevention hotline services for LGBTQ+ youth\n##### (a) In general\nSection 520E\u20133(b) of the Public Health Service Act (42 U.S.C. 290bb\u201336c(b)) is amended\u2014\n**(1)**\nin paragraph (4), by striking and at the end;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(6) dedicating sufficient resources, including establishing, re-establishing, operating, and maintaining specialized services (known as the Press 3 option or Integrated Voice Response (IVR)), for the support of youth who are lesbian, gay, bisexual, transgender, queer, or questioning (LGBTQ+) seeking help from the suicide prevention hotline. .\n##### (b) Funding\nSection 520E\u20133(f) of the Public Health Service Act (42 U.S.C. 290bb\u201336c(f)) is amended by adding at the end the following: Of the amounts appropriated under this subsection for a fiscal year, the Secretary shall reserve not less than 9 percent for carrying out subsection (b)(6). .",
      "versionDate": "2025-09-17",
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
        "actionDate": "2025-09-17",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "5434",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "988 LGBTQ+ Youth Access Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Emergency communications systems",
            "updateDate": "2026-04-16T19:12:47Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-04-16T19:12:51Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2026-04-16T19:12:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-11-17T18:42:13Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2826is.xml"
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
      "title": "988 LGBTQ+ Youth Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "988 LGBTQ+ Youth Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Health and Human Services to dedicate sufficient resources for the support of LGBTQ+ youth seeking help from the 9-8-8 suicide prevention hotline, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:17Z"
    }
  ]
}
```
