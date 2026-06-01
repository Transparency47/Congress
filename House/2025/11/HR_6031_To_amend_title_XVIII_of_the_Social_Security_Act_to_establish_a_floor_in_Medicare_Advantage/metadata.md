# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6031?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6031
- Title: Medicare Advantage Integrity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6031
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2026-01-23T15:40:15Z
- Update date including text: 2026-01-23T15:40:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-12 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-12 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6031",
    "number": "6031",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001103",
        "district": "",
        "firstName": "Pablo",
        "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
        "lastName": "Hern\u00e1ndez",
        "party": "D",
        "state": "PR"
      }
    ],
    "title": "Medicare Advantage Integrity Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-23T15:40:15Z",
    "updateDateIncludingText": "2026-01-23T15:40:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-12T17:01:50Z",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6031ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6031\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Hern\u00e1ndez (for himself, Ms. Salazar , and Mr. Soto ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to establish a floor in Medicare Advantage benchmark rates for regions with low Medicare fee-for-service penetration.\n#### 1. Short title\nThis Act may be cited as the Medicare Advantage Integrity Act of 2025 .\n#### 2. Addressing disparities in Medicare Advantage benchmark levels based on penetration\n##### (a) In general\nSection 1853(n) of the Social Security Act ( 42 U.S.C. 1395w\u201323(n) ) is amended\u2014\n**(1)**\nin paragraph (1)(B), by striking subsequent year and inserting subsequent year, subject to paragraph (6), ; and\n**(2)**\nby adding at the end the following new paragraph:\n(6) Average geographic adjustment floor For 2026 and subsequent years, when calculating the adjusted average per capita cost under section 1876(a)(4) for the purposes of establishing the base payment amount specified in paragraph (2)(E), the average geographic adjustment shall not be less than 0.70 for any area. For the purposes of the previous sentence, the Secretary may define the term average geographic adjustment under subparagraph (A) by program instruction or otherwise. .\n##### (b) Ensuring plan payments flow to providers and patients\nSection 1854(a)(6) of the Social Security Act ( 42 U.S.C. 1395w\u201324(a)(6) ) is amended by adding at the end the following new subparagraph:\n(C) Ensuring increased payments support care With respect to the increase in blended benchmark amount attributable to the application of section 1853(n)(6), no less than 50 percent shall be directed toward payment for basic benefits as defined in section 1852(a)(1)(B). .",
      "versionDate": "2025-11-12",
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
        "name": "Health",
        "updateDate": "2025-11-19T13:14:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-12",
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
          "measure-id": "id119hr6031",
          "measure-number": "6031",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-12",
          "originChamber": "HOUSE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6031v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-11-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medicare Advantage Integrity Act of 2025</strong></p><p>This bill temporarily establishes geographic adjustments for certain Medicare Advantage payment formulations, and specifies that a certain percentage of corresponding payment increases must be directed toward payments for basic benefits.</p>"
        },
        "title": "Medicare Advantage Integrity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6031.xml",
    "summary": {
      "actionDate": "2025-11-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicare Advantage Integrity Act of 2025</strong></p><p>This bill temporarily establishes geographic adjustments for certain Medicare Advantage payment formulations, and specifies that a certain percentage of corresponding payment increases must be directed toward payments for basic benefits.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr6031"
    },
    "title": "Medicare Advantage Integrity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medicare Advantage Integrity Act of 2025</strong></p><p>This bill temporarily establishes geographic adjustments for certain Medicare Advantage payment formulations, and specifies that a certain percentage of corresponding payment increases must be directed toward payments for basic benefits.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr6031"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6031ih.xml"
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
      "title": "Medicare Advantage Integrity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicare Advantage Integrity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T10:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to establish a floor in Medicare Advantage benchmark rates for regions with low Medicare fee-for-service penetration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T10:18:26Z"
    }
  ]
}
```
