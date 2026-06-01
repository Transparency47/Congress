# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4615?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4615
- Title: Small Business Payment for Performance Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4615
- Origin chamber: House
- Introduced date: 2025-07-22
- Update date: 2026-04-21T08:06:00Z
- Update date including text: 2026-04-21T08:06:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-22: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-07-22: Introduced in House

## Actions

- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Introduced in House
- 2025-07-22 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4615",
    "number": "4615",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Small Business Payment for Performance Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:00Z",
    "updateDateIncludingText": "2026-04-21T08:06:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T14:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "PA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NJ"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "IL"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "HI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "KS"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-02",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NC"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4615ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4615\nIN THE HOUSE OF REPRESENTATIVES\nJuly 22, 2025 Mr. Stauber (for himself, Mr. Veasey , Mr. Fitzpatrick , and Mr. Norcross ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to provide interim partial payment to small business contractors that request an equitable adjustment due to a change in the terms of a construction contract, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Payment for Performance Act of 2025 .\n#### 2. Equitable adjustments to construction contracts\n##### (a) In general\nSection 15 of the Small Business Act ( 15 U.S.C. 644 ) is amended\u2014\n**(1)**\nby redesignating subsections (x) and (y) as subsections (y) and (z), respectively; and\n**(2)**\nby inserting after subsection (w) the following new subsection:\n(x) Interim partial payments for equitable adjustments to construction contracts (1) Request for an equitable adjustment A small business concern that was awarded a construction contract by an agency may submit a request for an equitable adjustment to the contracting officer of such agency if the contracting officer directs a change in the terms of the contract performance without the agreement of the small business concern. Such request shall\u2014 (A) be timely made pursuant to the terms of the contract; and (B) specify the estimated amount required to cover additional costs resulting from such change in the terms. (2) Amount Upon receipt of a request for equitable adjustment from a small business concern under paragraph (1), the agency shall provide to such concern an interim partial payment in an amount equal to not less than 50 percent of the estimated amount under paragraph (1)(B). (3) Limitation Any interim partial payment made under this section may not be deemed to be an action to definitize the request for an equitable adjustment. (4) Flow-down of interim partial payment amounts A small business concern that receives an equitable adjustment under this subsection shall pay to a first tier subcontractor of such concern the portion of each interim partial payment received that is attributable to the increased costs of performance incurred by such subcontractor due to the change in the terms of the contract performance described in paragraph (1). A first tier subcontractor that receives a portion of an interim partial payment under this section shall pay to a subcontractor (at any tier) the appropriate portion of such payment. .\n##### (b) Implementation\nThe Administrator of the Small Business Administration shall implement the requirements of this section not later than the earlier of the following dates:\n**(1)**\nThe first day of the first full fiscal year beginning after the date of the enactment of this Act.\n**(2)**\nOctober 1, 2027.",
      "versionDate": "2025-07-22",
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
        "name": "Commerce",
        "updateDate": "2025-09-11T13:39:21Z"
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
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4615ih.xml"
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
      "title": "Small Business Payment for Performance Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T09:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Business Payment for Performance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T09:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to provide interim partial payment to small business contractors that request an equitable adjustment due to a change in the terms of a construction contract, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T09:33:17Z"
    }
  ]
}
```
