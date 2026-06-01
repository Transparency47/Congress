# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4238
- Title: Endless Mountains National Heritage Area Act
- Congress: 119
- Bill type: S
- Bill number: 4238
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-15T01:31:57Z
- Update date including text: 2026-04-15T01:31:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4238",
    "number": "4238",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Endless Mountains National Heritage Area Act",
    "type": "S",
    "updateDate": "2026-04-15T01:31:57Z",
    "updateDateIncludingText": "2026-04-15T01:31:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T18:50:41Z",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4238is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4238\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. McCormick (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to designate as a component of the National Heritage Area System the Endless Mountains National Heritage Area in the State of Pennsylvania, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Endless Mountains National Heritage Area Act .\n#### 2. Designation of Endless Mountains National Heritage Area\n##### (a) Designation\nSection 6001(a) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 768; 136 Stat. 6163) is amended by adding at the end the following:\n(14) Endless Mountains National Heritage Area (A) In general There is established as a component of the National Heritage Area System the Endless Mountains National Heritage Area in the State of Pennsylvania, to consist of Bradford, Sullivan, Susquehanna, and Wyoming Counties, Pennsylvania, and any portions of other counties in the State of Pennsylvania identified in the feasibility study for the Endless Mountains National Heritage Area, the specific boundaries of which shall be established by the Secretary based on that feasibility study. (B) Local coordinating entity The Endless Mountains Heritage Region, Inc., shall be the local coordinating entity for the National Heritage Area designated by subparagraph (A). .\n##### (b) Management plan\nFor the purposes of section 6001(c) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 772; 136 Stat. 6173), the local coordinating entity for the Endless Mountains National Heritage Area designated under the amendment made by subsection (a) shall submit to the Secretary of the Interior for approval a proposed management plan for the Endless Mountains National Heritage Area not later than 3 years after the date of enactment of this Act.\n##### (c) Termination of authority\nFor the purposes of subsection (g)(4) of section 6001 of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 776), the authority of the Secretary of the Interior to provide assistance under that section for the Endless Mountains National Heritage Area designated under the amendment made by subsection (a) shall terminate on the date that is 15 years after the date of enactment of this Act.",
      "versionDate": "2026-03-26",
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
        "actionDate": "2026-03-26",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "8114",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Endless Mountains National Heritage Area Act",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-04-15T01:31:57Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4238is.xml"
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
      "title": "Endless Mountains National Heritage Area Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Endless Mountains National Heritage Area Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the John D. Dingell, Jr. Conservation, Management, and Recreation Act to designate as a component of the National Heritage Area System the Endless Mountains National Heritage Area in the State of Pennsylvania, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:30Z"
    }
  ]
}
```
