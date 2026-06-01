# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/605
- Title: CHAMPVA Children's Care Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 605
- Origin chamber: Senate
- Introduced date: 2025-02-18
- Update date: 2026-03-19T11:03:25Z
- Update date including text: 2026-03-19T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in Senate
- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- Latest action: 2025-02-18: Introduced in Senate

## Actions

- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/605",
    "number": "605",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "CHAMPVA Children's Care Protection Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:25Z",
    "updateDateIncludingText": "2026-03-19T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-18",
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
      "actionDate": "2025-02-18",
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
            "date": "2025-05-21T20:00:10Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:10Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-18T21:12:54Z",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NY"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NV"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-18",
      "state": "VT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "WA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "IL"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "RI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "RI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s605is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 605\nIN THE SENATE OF THE UNITED STATES\nFebruary 18, 2025 Mr. Blumenthal (for himself, Mrs. Gillibrand , Ms. Rosen , Mr. Padilla , Mr. Sanders , Mrs. Murray , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to increase the maximum age for children eligible for medical care under the CHAMPVA program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the CHAMPVA Children's Care Protection Act of 2025 .\n#### 2. Increase of maximum age for children eligible for medical care under champva program\n##### (a) Increase\nSubsection (c) of section 1781 of title 38, United States Code, is amended to read as follows:\n(c) (1) Notwithstanding clauses (i) and (iii) of section 101(4)(A) of this title and except as provided in paragraph (2), for purposes of this section, a child is eligible for benefits under subsection (a) until the child's 26th birthday, regardless of the child's marital status. (2) This subsection shall not be construed to limit eligibility for benefits under subsection (a) of a child described in section 101(4)(A)(ii) of this title. .\n##### (b) Effective date\nSubsection (c) of such section, as amended by subsection (a), shall apply with respect to medical care provided under such section on or after the date of the enactment of this Act.",
      "versionDate": "2025-02-18",
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
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "1404",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CHAMPVA Children\u2019s Care Protection Act of 2025",
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
            "name": "Child health",
            "updateDate": "2025-06-03T16:01:07Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-03T16:01:07Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-03T16:01:07Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-06-03T16:01:07Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-03T16:01:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T17:26:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s605",
          "measure-number": "605",
          "measure-type": "s",
          "orig-publish-date": "2025-02-18",
          "originChamber": "SENATE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s605v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>CHAMPVA Children's Care Protection Act of 2025</strong></p><p>This bill provides that a child shall be eligible for medical care under the Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) until the child's 26th birthday, regardless of the child's marital status.</p>"
        },
        "title": "CHAMPVA Children's Care Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s605.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>CHAMPVA Children's Care Protection Act of 2025</strong></p><p>This bill provides that a child shall be eligible for medical care under the Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) until the child's 26th birthday, regardless of the child's marital status.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s605"
    },
    "title": "CHAMPVA Children's Care Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>CHAMPVA Children's Care Protection Act of 2025</strong></p><p>This bill provides that a child shall be eligible for medical care under the Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) until the child's 26th birthday, regardless of the child's marital status.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s605"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s605is.xml"
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
      "title": "CHAMPVA Children's Care Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CHAMPVA Children's Care Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to increase the maximum age for children eligible for medical care under the CHAMPVA program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:24Z"
    }
  ]
}
```
