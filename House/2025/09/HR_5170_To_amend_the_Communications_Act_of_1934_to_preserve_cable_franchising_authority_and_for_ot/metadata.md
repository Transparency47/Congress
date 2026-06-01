# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5170?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5170
- Title: CABLE Leadership Act
- Congress: 119
- Bill type: HR
- Bill number: 5170
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2025-09-23T17:47:00Z
- Update date including text: 2025-09-23T17:47:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5170",
    "number": "5170",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001306",
        "district": "12",
        "firstName": "Troy",
        "fullName": "Rep. Balderson, Troy [R-OH-12]",
        "lastName": "Balderson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "CABLE Leadership Act",
    "type": "HR",
    "updateDate": "2025-09-23T17:47:00Z",
    "updateDateIncludingText": "2025-09-23T17:47:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-09-08T16:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5170ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5170\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Mr. Balderson introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Communications Act of 1934 to preserve cable franchising authority, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cable Access for Broadband and Local Economic Leadership Act or the CABLE Leadership Act .\n#### 2. Request for new franchise\nSection 621 of the Communications Act of 1934 ( 47 U.S.C. 541 ) is amended by adding at the end the following:\n(g) Timing of decision on request for franchise (1) In general Not later than 120 days after the date on which a franchising authority receives a complete request for the grant of a franchise (other than a renewal thereof), the franchising authority shall approve or deny such request. (2) Deemed grant of new franchise If the franchising authority does not approve or deny a request under paragraph (1) by the day after the date on which the time period ends under such paragraph, such request shall be deemed granted on such day. (3) Applicability Notwithstanding any provision of this title, the timeframe under paragraph (1) shall apply collectively to all proceedings required by a franchising authority for the approval of the request. (4) No tolling The timeframe under paragraph (1) may not be tolled by any moratorium, whether express or de facto, imposed by a franchising authority on the consideration of any request for a franchise. (5) Written decision and record Any decision by a franchising authority to deny a complete request for a franchise shall be\u2014 (A) in writing; (B) supported by substantial evidence contained in a written record; and (C) publicly released, and provided to the requesting party, on the same day such decision is made. (6) When request considered complete; received (A) When request considered complete (i) In general For the purposes of this subsection, a request to a franchising authority shall be considered complete if the requesting party\u2014 (I) has taken the first procedural step within the control of the requesting party that the franchising authority requires as part of the process of the franchising authority for reviewing requests related to franchises; and (II) has not received a written notice from the franchising authority within 30 days after the date on which the request is received by the franchising authority\u2014 (aa) stating that all the information (including any form or other document) required by the franchising authority to be submitted for the request to be considered complete, has not been submitted; (bb) identifying the information required to be submitted that was not submitted; and (cc) that includes a citation to a specific provision of a publicly available rule, regulation, or standard issued by the franchising authority requiring that the information be submitted with such a request. (ii) Definition In this subparagraph, the term the date on which the request is received by the franchising authority means\u2014 (I) in the case of a request submitted electronically, the date on which the request is transmitted; (II) in the case of a request submitted in person, the date on which the request is delivered to the individual or at the location specified by franchising authority for in-person submission; and (III) in the case of a request submitted in any other manner, the date determined under regulations promulgated by the Commission for the manner in which the request is submitted. (B) When complete request considered received For the purposes of this subsection, a complete request shall be considered received\u2014 (i) except as provided in clause (ii), on the date on which the requesting party submits to the franchising authority all information (including any form or other document) required by the franchising authority to be submitted for the request to be considered complete; or (ii) in the case of a request with respect to which all such information is not submitted and that is considered complete under subparagraph (A)(i) because the requesting party has not received a written notice from the franchising authority within the period described in such subparagraph, on the day after the last day of such period. .",
      "versionDate": "2025-09-08",
      "versionType": "Introduced in House"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-23T17:47:00Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5170ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "CABLE Leadership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CABLE Leadership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cable Access for Broadband and Local Economic Leadership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Communications Act of 1934 to preserve cable franchising authority, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:38Z"
    }
  ]
}
```
