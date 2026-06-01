# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1440?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1440
- Title: Discriminatory Gaming Tax Repeal Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1440
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-05-06T13:57:53Z
- Update date including text: 2026-05-06T13:57:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1440",
    "number": "1440",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Discriminatory Gaming Tax Repeal Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-06T13:57:53Z",
    "updateDateIncludingText": "2026-05-06T13:57:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:00:20Z",
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
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "PA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "PA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NV"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "NV"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1440ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1440\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Ms. Titus (for herself, Mr. Reschenthaler , Mr. Kelly of Pennsylvania , Mr. Horsford , and Mr. Amodei of Nevada ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the excise taxes on wagering.\n#### 1. Short title\nThis Act may be cited as the Discriminatory Gaming Tax Repeal Act of 2025 .\n#### 2. Repeal of excise taxes on wagering\n##### (a) In general\nChapter 35 of the Internal Revenue Code of 1986 (relating to taxes on wagering) is repealed.\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-02-18",
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
        "name": "Taxation",
        "updateDate": "2025-05-07T12:35:55Z"
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
          "measure-id": "id119hr1440",
          "measure-number": "1440",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2026-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1440v00",
            "update-date": "2026-05-06"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Discriminatory Gaming Tax Repeal Act of 2025</strong></p><p>This bill repeals the excise tax imposed on wagers (also known as the handle tax) and the occupational tax imposed on businesses receiving taxable wagers.</p><p>As background, an excise tax on wagers is imposed on businesses that accept wagers, persons conducting a wagering pool or lottery, and certain persons accepting wagers on behalf of another person. Under current law, the amount of the excise tax is (1) 0.25% of the amount wagered (also known as the handle) for wagers authorized by the state, or (2) 2% of the amount wagered for wagers not authorized by the state. (Some exceptions apply.)</p><p>Further, under current law, an annual occupational tax is imposed in the amount of (1) $50 for persons in the business of accepting taxable wagers (or persons accepting taxable wagers on such persons\u2019 behalf) in a state where the wagers are authorized, or (2) $500 for such persons in states where the wagers are not authorized. (Some exceptions apply.)</p>"
        },
        "title": "Discriminatory Gaming Tax Repeal Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1440.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Discriminatory Gaming Tax Repeal Act of 2025</strong></p><p>This bill repeals the excise tax imposed on wagers (also known as the handle tax) and the occupational tax imposed on businesses receiving taxable wagers.</p><p>As background, an excise tax on wagers is imposed on businesses that accept wagers, persons conducting a wagering pool or lottery, and certain persons accepting wagers on behalf of another person. Under current law, the amount of the excise tax is (1) 0.25% of the amount wagered (also known as the handle) for wagers authorized by the state, or (2) 2% of the amount wagered for wagers not authorized by the state. (Some exceptions apply.)</p><p>Further, under current law, an annual occupational tax is imposed in the amount of (1) $50 for persons in the business of accepting taxable wagers (or persons accepting taxable wagers on such persons\u2019 behalf) in a state where the wagers are authorized, or (2) $500 for such persons in states where the wagers are not authorized. (Some exceptions apply.)</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr1440"
    },
    "title": "Discriminatory Gaming Tax Repeal Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Discriminatory Gaming Tax Repeal Act of 2025</strong></p><p>This bill repeals the excise tax imposed on wagers (also known as the handle tax) and the occupational tax imposed on businesses receiving taxable wagers.</p><p>As background, an excise tax on wagers is imposed on businesses that accept wagers, persons conducting a wagering pool or lottery, and certain persons accepting wagers on behalf of another person. Under current law, the amount of the excise tax is (1) 0.25% of the amount wagered (also known as the handle) for wagers authorized by the state, or (2) 2% of the amount wagered for wagers not authorized by the state. (Some exceptions apply.)</p><p>Further, under current law, an annual occupational tax is imposed in the amount of (1) $50 for persons in the business of accepting taxable wagers (or persons accepting taxable wagers on such persons\u2019 behalf) in a state where the wagers are authorized, or (2) $500 for such persons in states where the wagers are not authorized. (Some exceptions apply.)</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr1440"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1440ih.xml"
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
      "title": "Discriminatory Gaming Tax Repeal Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T11:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Discriminatory Gaming Tax Repeal Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T11:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to repeal the excise taxes on wagering.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T11:03:24Z"
    }
  ]
}
```
