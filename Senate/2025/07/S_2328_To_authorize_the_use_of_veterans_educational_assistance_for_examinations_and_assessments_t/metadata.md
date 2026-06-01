# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2328?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2328
- Title: Military Learning for Credit Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2328
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-04-02T20:35:24Z
- Update date including text: 2026-04-02T20:35:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2328",
    "number": "2328",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Military Learning for Credit Act of 2025",
    "type": "S",
    "updateDate": "2026-04-02T20:35:24Z",
    "updateDateIncludingText": "2026-04-02T20:35:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
            "date": "2026-03-18T20:00:20Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:24Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-07-17T17:20:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2328is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2328\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Coons (for himself and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo authorize the use of veterans educational assistance for examinations and assessments to receive credit toward degrees awarded by institutions of higher learning, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military Learning for Credit Act of 2025 .\n#### 2. Authority for use of veterans educational assistance for examinations and assessments to receive credit toward degrees awarded by institutions of higher learning\n##### (a) In general\nAn individual who is entitled to veterans educational assistance may use such assistance to cover the costs of covered examinations and assessments to receive credit toward degrees awarded by institutions of higher learning for approved programs of education.\n##### (b) Veterans educational assistance\nFor purposes of this section, veterans educational assistance is educational assistance available to veterans and other eligible individuals under the provisions of law as follows:\n**(1)**\nChapters 30, 32, 33, 34, and 35 of title 38, United States Code.\n**(2)**\nAny other provision of law providing educational assistance to a veteran, or to another individual in connection with the service of a veteran in the Armed Forces.\n##### (c) Limitation on amount usable\nThe total amount of veterans educational assistance that may be used for the costs of a covered examination or assessment under subsection (a) may not exceed the lesser of\u2014\n**(1)**\nthe amount charged for the examination or assessment by the entity administering the examination or assessment; or\n**(2)**\n$500.\n##### (d) Charge against entitlement\n**(1) In general**\nThe number of months (or fraction thereof) of entitlement charged an individual under the applicable provision of law specified in subsection (b) for use of veterans educational assistance for costs of covered examinations and assessments under this section shall be equal to the quotient obtained by dividing\u2014\n**(A)**\nthe cost of the examination or assessment (as determined pursuant to subsection (c)); by\n**(B)**\nthe monthly rate of veterans educational assistance to which the individual is entitled under such provision of law at the time of the examination or assessment.\n**(2) Rule of construction**\nA charge against entitlement to educational assistance under a law administered by the Secretary of Veterans Affairs in order to receive assistance under this section shall not be construed to affect entitlement to educational assistance under a law administered by the Secretary of Defense, including entitlement to educational assistance under the Department of Defense Tuition Assistance Program.\n##### (e) Definitions\nIn this section:\n**(1)**\nThe term approved program of education means a program of education approved for use of veterans educational assistance pursuant to chapter 35 or 36 of title 38, United States Code, or another applicable provision of law.\n**(2)**\nThe term covered examinations and assessments means the following:\n**(A)**\nA DANTES Subject Standardized Test Program (DSST) examination.\n**(B)**\nA College Level Examination Program (CLEP) examination.\n**(C)**\nThe National Career Readiness Certificate examination.\n**(D)**\nAny other examination of a similar nature to an exam specified in subparagraph (A), (B), or (C) specified by the Secretary of Veterans Affairs for purposes of this section.\n**(E)**\nAn assessment by an institution of higher learning of a portfolio or written narrative by a student with supporting documentation that demonstrates prior military training or learning.\n**(3)**\nThe term institution of higher learning has the meaning given such term in section 3452(f) of title 38, United States Code.",
      "versionDate": "2025-07-17",
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
        "actionDate": "2025-12-19",
        "text": "Referred to the Subcommittee on Economic Opportunity."
      },
      "number": "4594",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Military Learning for Credit Act of 2025",
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
            "name": "Higher education",
            "updateDate": "2026-01-09T16:22:08Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2026-01-09T16:22:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-08-01T15:15:43Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2328is.xml"
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
      "title": "Military Learning for Credit Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Military Learning for Credit Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the use of veterans educational assistance for examinations and assessments to receive credit toward degrees awarded by institutions of higher learning, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:28Z"
    }
  ]
}
```
