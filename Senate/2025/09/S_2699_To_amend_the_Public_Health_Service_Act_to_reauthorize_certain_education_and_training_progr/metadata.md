# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2699?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2699
- Title: Geriatrics Workforce Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 2699
- Origin chamber: Senate
- Introduced date: 2025-09-03
- Update date: 2026-04-16T19:09:59Z
- Update date including text: 2026-04-16T19:09:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in Senate
- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S6010-6011)
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-09-03: Introduced in Senate

## Actions

- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S6010-6011)
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2699",
    "number": "2699",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "Geriatrics Workforce Improvement Act",
    "type": "S",
    "updateDate": "2026-04-16T19:09:59Z",
    "updateDateIncludingText": "2026-04-16T19:09:59Z"
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
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S6010-6011)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-03",
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
            "date": "2026-03-19T14:00:44Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-09-03T20:14:20Z",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2699is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2699\nIN THE SENATE OF THE UNITED STATES\nSeptember 3, 2025 Ms. Collins (for herself and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to reauthorize certain education and training programs relating to geriatrics, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Geriatrics Workforce Improvement Act .\n#### 2. Education and training relating to geriatrics\nSection 753(d) of the Public Health Service Act ( 42 U.S.C. 294c(d) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated $48,245,000 for each of fiscal years 2026 through 2030 for purposes of carrying out this section. .",
      "versionDate": "2025-09-03",
      "versionType": "Introduced in Senate"
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
            "name": "Aging",
            "updateDate": "2026-04-16T19:09:54Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-04-16T19:09:39Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-04-16T19:09:44Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2026-04-16T19:09:24Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2026-04-16T19:09:59Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-04-16T19:09:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-22T14:49:18Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2699is.xml"
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
      "title": "Geriatrics Workforce Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Geriatrics Workforce Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to reauthorize certain education and training programs relating to geriatrics, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:31Z"
    }
  ]
}
```
