# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2358?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2358
- Title: IRS Accountability and Taxpayer Protection Act
- Congress: 119
- Bill type: S
- Bill number: 2358
- Origin chamber: Senate
- Introduced date: 2025-07-21
- Update date: 2025-08-06T18:15:30Z
- Update date including text: 2025-08-06T18:15:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in Senate
- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-21: Introduced in Senate

## Actions

- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2358",
    "number": "2358",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "IRS Accountability and Taxpayer Protection Act",
    "type": "S",
    "updateDate": "2025-08-06T18:15:30Z",
    "updateDateIncludingText": "2025-08-06T18:15:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-21",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T19:41:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "WY"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "IA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "WY"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "ID"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2358is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2358\nIN THE SENATE OF THE UNITED STATES\nJuly 21, 2025 Mr. Scott of South Carolina (for himself, Ms. Lummis , Mr. Tillis , Mr. Grassley , Mr. Barrasso , Mr. Crapo , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the procedural rules for penalties.\n#### 1. Short title\nThis Act may be cited as the IRS Accountability and Taxpayer Protection Act .\n#### 2. Modification of procedural requirements for penalties and disallowance periods\n##### (a) In general\nSection 6751(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking paragraph (1) and inserting the following:\n(1) In general No penalty under this title shall be assessed, and no disallowance period shall take effect, unless\u2014 (A) the initial determination to apply such penalty or disallowance period, as applicable, is personally approved (in writing) by the immediate supervisor of the individual making such determination, and (B) the approval described in subparagraph (A) is obtained on or before the date any notice is sent to the taxpayer regarding the application of such penalty or disallowance period. , and\n**(2)**\nby adding at the end the following:\n(3) Initial determination (A) In general For purposes of this subsection, the term initial determination means the first determination, provided in a written notice to a taxpayer, that, based on specific facts and circumstances with respect to such taxpayer\u2014 (i) a specific penalty applies to such taxpayer for a specific amount, or (ii) a disallowance period applies to such taxpayer for a specific period. (B) Requests or inquiries No request or inquiry made by the Secretary shall be deemed to be an initial determination unless such request or inquiry provides the taxpayer with an offer to agree to a specific penalty for a specific amount (with the exception of any penalty offered under a settlement initiative to a class of taxpayers) or a disallowance period for a specific period. .\n##### (b) Disallowance period\nSection 6751 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(d) Disallowance period (1) In general For purposes of this section, the term disallowance period means\u2014 (A) with respect to any credit under section 24, the period determined under section 24(g)(1), (B) with respect to any credit under section 25A, the period determined under section 25A(b)(4)(A), and (C) with respect to any credit under section 32, the period determined under section 32(k)(1). (2) Approval required for disallowance period automatically calculated through electronic means With respect to the application of any disallowance period, subsection (b)(2)(B) shall not apply. .\n##### (c) Effective date\nThe amendments made by this section shall apply to notices sent after the date of the enactment of this Act.\n##### (d) Report\nNot later than 24 months after the date of enactment of this Act, and annually thereafter, the Secretary of the Treasury (or the Secretary's delegate) shall make publicly available a report regarding all penalties assessed by the Internal Revenue Service pursuant to the Internal Revenue Code of 1986 during the preceding calendar year, with all relevant data regarding such penalties to be collected and reported with respect to\u2014\n**(1)**\nevery organizational unit of the Internal Revenue Service that has power to assess, abate, or otherwise enforce any penalty imposed by the Internal Revenue Service under the Internal Revenue Code of 1986, and\n**(2)**\nthe progression of such penalties at each step of the determination, assessment, and review processes, as well as the final result with respect to such penalties.",
      "versionDate": "2025-07-21",
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
        "name": "Taxation",
        "updateDate": "2025-08-06T18:15:30Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2358is.xml"
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
      "title": "IRS Accountability and Taxpayer Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "IRS Accountability and Taxpayer Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modify the procedural rules for penalties.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:30Z"
    }
  ]
}
```
