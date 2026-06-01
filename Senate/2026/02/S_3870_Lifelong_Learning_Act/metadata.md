# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3870?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3870
- Title: Lifelong Learning Act
- Congress: 119
- Bill type: S
- Bill number: 3870
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-02-27T17:00:09Z
- Update date including text: 2026-02-27T17:00:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3870",
    "number": "3870",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Lifelong Learning Act",
    "type": "S",
    "updateDate": "2026-02-27T17:00:09Z",
    "updateDateIncludingText": "2026-02-27T17:00:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T19:32:24Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3870is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3870\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Peters (for himself, Mr. Budd , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to permit greater flexibility in carrying out incumbent worker training programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lifelong Learning Act .\n#### 2. Incumbent worker training and transitional jobs standard reservation of funds\nSection 134(d) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3174(d) ) is amended\u2014\n**(1)**\nin paragraph (4)(A)(i), by striking 20 and inserting 30 ; and\n**(2)**\nin paragraph (5), in the matter preceding subparagraph (A), by striking 10 and inserting 15 .\n#### 3. Reporting incumbent worker training outcomes\nSection 116(d)(2)(A) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3141(d)(2)(A) ) is amended\u2014\n**(1)**\nby striking (A) information and inserting (A)(i) information ;\n**(2)**\nin clause (i), as so designated, by adding and at the end; and\n**(3)**\nby adding at the end the following:\n(ii) in the case of a State in which local areas are implementing incumbent worker training programs under section 134(d)(4), information on the levels of performance achieved for those programs with respect to the primary indicators of performance described in subsection (b)(2)(A), which information shall be used by the State and the Secretary of Labor in conjunction with the Secretary of Education to adapt the State adjusted levels of performance with respect to such indicators for the adult program and for the dislocated worker program authorized under chapter 3 of subtitle B. .\n#### 4. Expanding the flexibility of one-stop operators\nSection 121(d)(2) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3151(d)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking ; and and inserting a semicolon;\n**(2)**\nin subparagraph (B)(vi), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(C) subject to approval from the chief elected official and Governor and in accordance with any other eligibility criteria established by the State, and notwithstanding subparagraph (B), may be a local board, if the local board\u2014 (i) enters into a written agreement with the chief elected official and clarifies how the local board will carry out the functions and responsibilities of a one-stop operator in a manner that complies with appropriate internal controls to prevent any conflicts of interest, which shall include how the local board, while serving as a one-stop operator, will comply with\u2014 (I) the relevant Office of Management and Budget circulars relating to conflicts of interest; and (II) any applicable State conflict of interest policy; and (ii) complies with the other applicable requirements of this subsection. .",
      "versionDate": "2026-02-12",
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
        "name": "Labor and Employment",
        "updateDate": "2026-02-27T17:00:09Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3870is.xml"
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
      "title": "Lifelong Learning Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T06:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lifelong Learning Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Workforce Innovation and Opportunity Act to permit greater flexibility in carrying out incumbent worker training programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T06:18:26Z"
    }
  ]
}
```
