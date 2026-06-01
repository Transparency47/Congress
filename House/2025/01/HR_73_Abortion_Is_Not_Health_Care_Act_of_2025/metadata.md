# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/73?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/73
- Title: Abortion Is Not Health Care Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 73
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-04-14T08:05:42Z
- Update date including text: 2026-04-14T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/73",
    "number": "73",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Abortion Is Not Health Care Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:42Z",
    "updateDateIncludingText": "2026-04-14T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:11:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "GA"
    },
    {
      "bioguideId": "M001212",
      "district": "2",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AL"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "PA"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr73ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 73\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Allen , Mr. Moore of Alabama , and Mr. Joyce of Pennsylvania ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide that amounts paid for an abortion are not taken into account for purposes of the deduction for medical expenses.\n#### 1. Short title\nThis Act may be cited as the Abortion Is Not Health Care Act of 2025 .\n#### 2. Amounts paid for abortion not taken into account in determining deduction for medical expenses\n##### (a) In general\nSection 213 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(f) Amounts paid for abortion not taken into account An amount paid during the taxable year for an abortion shall not be taken into account under subsection (a). .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-01-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "253",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Abortion Is Not Health Care Act of 2025",
      "type": "S"
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
            "name": "Abortion",
            "updateDate": "2025-02-14T19:12:10Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-02-14T19:12:10Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-02-14T19:12:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-01-31T16:17:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
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
          "measure-id": "id119hr73",
          "measure-number": "73",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr73v00",
            "update-date": "2025-02-04"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Abortion Is Not Health Care Act of 2025</strong></p><p>This bill excludes amounts paid for an abortion from the itemized tax deduction for qualified medical and dental expenses.\u00a0</p><p>Under current law, individuals who itemize their tax deductions may deduct qualified medical and dental expenses to the extent that such expenses exceed 7.5% of the individual\u2019s adjusted gross income for the tax year. Further, under current law, the calculation of the itemized tax deduction for medical and dental expenses may include amounts paid for a legal abortion.\u00a0</p>"
        },
        "title": "Abortion Is Not Health Care Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr73.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Abortion Is Not Health Care Act of 2025</strong></p><p>This bill excludes amounts paid for an abortion from the itemized tax deduction for qualified medical and dental expenses.\u00a0</p><p>Under current law, individuals who itemize their tax deductions may deduct qualified medical and dental expenses to the extent that such expenses exceed 7.5% of the individual\u2019s adjusted gross income for the tax year. Further, under current law, the calculation of the itemized tax deduction for medical and dental expenses may include amounts paid for a legal abortion.\u00a0</p>",
      "updateDate": "2025-02-04",
      "versionCode": "id119hr73"
    },
    "title": "Abortion Is Not Health Care Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Abortion Is Not Health Care Act of 2025</strong></p><p>This bill excludes amounts paid for an abortion from the itemized tax deduction for qualified medical and dental expenses.\u00a0</p><p>Under current law, individuals who itemize their tax deductions may deduct qualified medical and dental expenses to the extent that such expenses exceed 7.5% of the individual\u2019s adjusted gross income for the tax year. Further, under current law, the calculation of the itemized tax deduction for medical and dental expenses may include amounts paid for a legal abortion.\u00a0</p>",
      "updateDate": "2025-02-04",
      "versionCode": "id119hr73"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr73ih.xml"
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
      "title": "Abortion Is Not Health Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T07:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Abortion Is Not Health Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T07:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide that amounts paid for an abortion are not taken into account for purposes of the deduction for medical expenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T07:03:42Z"
    }
  ]
}
```
