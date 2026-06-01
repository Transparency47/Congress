# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1504?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1504
- Title: Claiming Age Clarity Act
- Congress: 119
- Bill type: S
- Bill number: 1504
- Origin chamber: Senate
- Introduced date: 2025-04-29
- Update date: 2026-04-28T11:03:22Z
- Update date including text: 2026-04-28T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-29: Introduced in Senate
- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-29: Introduced in Senate

## Actions

- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1504",
    "number": "1504",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Claiming Age Clarity Act",
    "type": "S",
    "updateDate": "2026-04-28T11:03:22Z",
    "updateDateIncludingText": "2026-04-28T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
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
            "date": "2025-04-29T15:54:09Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-29T15:54:09Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "DE"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "ME"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-05-14",
      "state": "VT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-12-08",
      "state": "NC"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "UT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "IN"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NH"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "VA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "OH"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1504is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1504\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2025 Mr. Cassidy (for himself, Mr. Coons , Ms. Collins , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the Social Security Administration to make changes to the social security terminology used in the rules, regulation, guidance, or other materials of the Administration.\n#### 1. Short title\nThis Act may be cited as the Claiming Age Clarity Act .\n#### 2. Changes to social security terminology\nNot later than January 1, 2027, the Commissioner of Social Security shall ensure that, in any rules, regulation, guidance, or other materials of the Social Security Administration, whether online or in print\u2014\n**(1)**\nthe term early eligibility age is replaced with the term minimum monthly benefit age ;\n**(2)**\nthe terms full retirement age and normal retirement age are replaced with the term standard monthly benefit age ; and\n**(3)**\nthe term delayed retirement credit shall not be used and any reference to age 70 as the maximum age up to which delayed retirement credits can be received shall be replaced with the term maximum monthly benefit age .",
      "versionDate": "2025-04-29",
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
        "actionDate": "2025-12-02",
        "text": "Received in the Senate and Read twice and referred to the Committee on Finance."
      },
      "number": "5284",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Claiming Age Clarity Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-09-24T20:19:03Z"
          },
          {
            "name": "Aging",
            "updateDate": "2025-09-24T20:19:03Z"
          },
          {
            "name": "Social Security Administration",
            "updateDate": "2025-09-24T20:19:03Z"
          },
          {
            "name": "Social security and elderly assistance",
            "updateDate": "2025-09-24T20:19:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-05-22T15:32:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-29",
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
          "measure-id": "id119s1504",
          "measure-number": "1504",
          "measure-type": "s",
          "orig-publish-date": "2025-04-29",
          "originChamber": "SENATE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1504v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2025-04-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Claiming Age Clarity Act</strong></p><p>This bill changes certain terms that are used by the Social Security Administration (SSA) to describe the ages at which a worker may claim Social Security retirement benefits.</p><p>First, the SSA must use <em>minimum monthly benefit age</em> instead of <em>early eligibility age</em>. This refers to the earliest age (62 under current law) at which a worker may claim benefits. (Currently, the benefit amount of a worker who claims benefits early is reduced to account for the longer period during which the worker is expected to receive benefits.)</p><p>Second, the SSA must use <em>standard monthly benefit age </em>instead of <em>full retirement age</em> and <em>normal retirement age</em>. These terms refer to the age at which a worker may claim benefits without a reduction in the benefit amount. (Currently, this age ranges from 65 to 67, depending on the worker's year of birth.)</p><p>Finally, the SSA must use the term <em>maximum monthly benefit age</em> for any reference to age 70 as the maximum age at which a worker may receive delayed retirement credits. The SSA may not use the term <em>delayed retirement credit. </em>These terms refer to the mechanism that increases the benefit amount of a worker who delays claiming benefits after reaching the full retirement age. (Currently, a worker receives a credit for each month between the full retirement age and age 70 that the worker delays claiming benefits. Each credit increases the benefit amount that the worker will receive after claiming benefits by a specified percentage.)</p>"
        },
        "title": "Claiming Age Clarity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1504.xml",
    "summary": {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Claiming Age Clarity Act</strong></p><p>This bill changes certain terms that are used by the Social Security Administration (SSA) to describe the ages at which a worker may claim Social Security retirement benefits.</p><p>First, the SSA must use <em>minimum monthly benefit age</em> instead of <em>early eligibility age</em>. This refers to the earliest age (62 under current law) at which a worker may claim benefits. (Currently, the benefit amount of a worker who claims benefits early is reduced to account for the longer period during which the worker is expected to receive benefits.)</p><p>Second, the SSA must use <em>standard monthly benefit age </em>instead of <em>full retirement age</em> and <em>normal retirement age</em>. These terms refer to the age at which a worker may claim benefits without a reduction in the benefit amount. (Currently, this age ranges from 65 to 67, depending on the worker's year of birth.)</p><p>Finally, the SSA must use the term <em>maximum monthly benefit age</em> for any reference to age 70 as the maximum age at which a worker may receive delayed retirement credits. The SSA may not use the term <em>delayed retirement credit. </em>These terms refer to the mechanism that increases the benefit amount of a worker who delays claiming benefits after reaching the full retirement age. (Currently, a worker receives a credit for each month between the full retirement age and age 70 that the worker delays claiming benefits. Each credit increases the benefit amount that the worker will receive after claiming benefits by a specified percentage.)</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119s1504"
    },
    "title": "Claiming Age Clarity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Claiming Age Clarity Act</strong></p><p>This bill changes certain terms that are used by the Social Security Administration (SSA) to describe the ages at which a worker may claim Social Security retirement benefits.</p><p>First, the SSA must use <em>minimum monthly benefit age</em> instead of <em>early eligibility age</em>. This refers to the earliest age (62 under current law) at which a worker may claim benefits. (Currently, the benefit amount of a worker who claims benefits early is reduced to account for the longer period during which the worker is expected to receive benefits.)</p><p>Second, the SSA must use <em>standard monthly benefit age </em>instead of <em>full retirement age</em> and <em>normal retirement age</em>. These terms refer to the age at which a worker may claim benefits without a reduction in the benefit amount. (Currently, this age ranges from 65 to 67, depending on the worker's year of birth.)</p><p>Finally, the SSA must use the term <em>maximum monthly benefit age</em> for any reference to age 70 as the maximum age at which a worker may receive delayed retirement credits. The SSA may not use the term <em>delayed retirement credit. </em>These terms refer to the mechanism that increases the benefit amount of a worker who delays claiming benefits after reaching the full retirement age. (Currently, a worker receives a credit for each month between the full retirement age and age 70 that the worker delays claiming benefits. Each credit increases the benefit amount that the worker will receive after claiming benefits by a specified percentage.)</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119s1504"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1504is.xml"
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
      "title": "Claiming Age Clarity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Claiming Age Clarity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Social Security Administration to make changes to the social security terminology used in the rules, regulation, guidance, or other materials of the Administration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:48:23Z"
    }
  ]
}
```
