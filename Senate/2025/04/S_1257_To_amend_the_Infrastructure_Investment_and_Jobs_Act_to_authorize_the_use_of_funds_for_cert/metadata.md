# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1257
- Title: A bill to amend the Infrastructure Investment and Jobs Act to authorize the use of funds for certain additional Carey Act projects, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 1257
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1257",
    "number": "1257",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A bill to amend the Infrastructure Investment and Jobs Act to authorize the use of funds for certain additional Carey Act projects, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T18:20:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1257is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1257\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Risch (for himself and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to authorize the use of funds for certain additional Carey Act projects, and for other purposes.\n#### 1. Eligibility under the Infrastructure Investment and Jobs Act of additional Carey Act projects for certain funds\nSection 40904(b) of the Infrastructure Investment and Jobs Act ( 43 U.S.C. 3204(b) ) is amended\u2014\n**(1)**\nin paragraph (3), by redesignating subparagraphs (A) through (C) as clauses (i) through (iii), respectively, and indenting appropriately;\n**(2)**\nby redesignating paragraphs (1) through (4) as subparagraphs (A) through (D), respectively, and indenting appropriately;\n**(3)**\nin the matter preceding subparagraph (A) (as so redesignated), by striking The Secretary and inserting the following:\n(1) In general The Secretary ; and\n**(4)**\nby adding at the end the following:\n(2) Additional projects (A) In general On making the affirmative determinations described in subparagraph (B), the Secretary shall use amounts made available under section 40901(2)(B) to fund the rehabilitation, reconstruction, or replacement of any dams that were developed pursuant to, and continue to operate as dams under, section 4 of the Act of August 18, 1894 (commonly known as the Carey Act ) ( 43 U.S.C. 641 ; 28 Stat. 422, chapter 301). (B) Determinations described The determinations referred to in subparagraph (A) are\u2014 (i) a determination by the Secretary that any dams that meet the criteria described in paragraph (1) have received the necessary funding to complete rehabilitation, reconstruction, or replacement activities under this subsection; and (ii) a determination by the Secretary that amounts made available under section 40901(2)(B) remain available. .",
      "versionDate": "2025-04-02",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-05-14T16:20:11Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1257is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Infrastructure Investment and Jobs Act to authorize the use of funds for certain additional Carey Act projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:16Z"
    },
    {
      "title": "A bill to amend the Infrastructure Investment and Jobs Act to authorize the use of funds for certain additional Carey Act projects, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:08:56Z"
    }
  ]
}
```
