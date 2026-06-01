# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/571?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/571
- Title: ____ Act
- Congress: 119
- Bill type: HR
- Bill number: 571
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2025-06-04T18:35:57Z
- Update date including text: 2025-06-04T18:35:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/571",
    "number": "571",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "G000568",
        "district": "9",
        "firstName": "H.",
        "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
        "lastName": "Griffith",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "____ Act",
    "type": "HR",
    "updateDate": "2025-06-04T18:35:57Z",
    "updateDateIncludingText": "2025-06-04T18:35:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:00:25Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr571ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 571\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Mr. Griffith introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title II of the Social Security Act to means-test certain child\u2019s insurance benefits.\n#### 1. Short title\nThis Act may be cited as the ____ Act .\n#### 2. Means-testing child\u2019s insurance benefits\n##### (a) In general\nSection 202(d)(7) of the Social Security Act ( 42 U.S.C. 407(d) ) is amended by adding at the end the following:\n(E) No child aged 18 years or older shall be considered a full-time elementary or secondary school student for any month of a taxable year if being so considered would entitle such child to a benefit under this subsection on the basis of the wages and self-employment income of an individual who\u2014 (i) is entitled to old-age or disability insurance benefits, (ii) is 67 years of age or older, and (iii) has more than $125,000 of earnings for such taxable year as computed under section 203(f)(5)(A). .\n##### (b) Effective date\nThe amendment made by this Act shall apply to with respect to benefits paid for any month beginning after the date of enactment of this Act.",
      "versionDate": "2025-01-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability assistance",
            "updateDate": "2025-04-04T16:00:40Z"
          },
          {
            "name": "Social security and elderly assistance",
            "updateDate": "2025-04-04T16:00:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-03-31T15:13:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr571",
          "measure-number": "571",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2025-06-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr571v00",
            "update-date": "2025-06-04"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill implements a means test for certain elementary and secondary school students aged 18 or older to collect Social Security child\u2019s benefits.\u00a0</p><p>Specifically, a child beneficiary aged 18 years or older may not be eligible for Social Security child\u2019s benefits based on their status as a full-time elementary or secondary school student if the individual on whose wages and income the benefit is based (e.g., the child\u2019s parent or guardian) (1) is entitled to Social Security benefits, (2) is 67 years of age or older, and (3) has more than $125,000 of annual earnings for the taxable year.\u00a0</p>"
        },
        "title": "____ Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr571.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill implements a means test for certain elementary and secondary school students aged 18 or older to collect Social Security child\u2019s benefits.\u00a0</p><p>Specifically, a child beneficiary aged 18 years or older may not be eligible for Social Security child\u2019s benefits based on their status as a full-time elementary or secondary school student if the individual on whose wages and income the benefit is based (e.g., the child\u2019s parent or guardian) (1) is entitled to Social Security benefits, (2) is 67 years of age or older, and (3) has more than $125,000 of annual earnings for the taxable year.\u00a0</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119hr571"
    },
    "title": "____ Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill implements a means test for certain elementary and secondary school students aged 18 or older to collect Social Security child\u2019s benefits.\u00a0</p><p>Specifically, a child beneficiary aged 18 years or older may not be eligible for Social Security child\u2019s benefits based on their status as a full-time elementary or secondary school student if the individual on whose wages and income the benefit is based (e.g., the child\u2019s parent or guardian) (1) is entitled to Social Security benefits, (2) is 67 years of age or older, and (3) has more than $125,000 of annual earnings for the taxable year.\u00a0</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119hr571"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr571ih.xml"
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
      "title": "____ Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "____ Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to means-test certain child's insurance benefits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:11Z"
    }
  ]
}
```
