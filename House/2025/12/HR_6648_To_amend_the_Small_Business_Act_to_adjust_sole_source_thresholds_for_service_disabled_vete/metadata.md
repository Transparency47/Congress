# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6648?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6648
- Title: FAIR Vets Act
- Congress: 119
- Bill type: HR
- Bill number: 6648
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-03-10T08:05:46Z
- Update date including text: 2026-03-10T08:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6648",
    "number": "6648",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "FAIR Vets Act",
    "type": "HR",
    "updateDate": "2026-03-10T08:05:46Z",
    "updateDateIncludingText": "2026-03-10T08:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:01:10Z",
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CO"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NE"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "IA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NC"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6648ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6648\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mrs. Kiggans of Virginia (for herself, Mr. Neguse , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act to adjust sole-source thresholds for service-disabled veteran-owned small business concerns, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Acquisition Improvement and Reform Vets Act or the FAIR Vets Act .\n#### 2. Modernization of sole-source thresholds for service-disabled veteran-owned small business concerns\n##### (a) Amendments\nSection 36 of the Small Business Act ( 15 U.S.C. 657f ) is amended\u2014\n**(1)**\nin subsection (c)(2), by striking (including options) ;\n**(2)**\nin subsection (c)(2)(A), by striking $7,000,000 and inserting $10,000,000 ; and\n**(3)**\nin subsection (c)(2)(B), by striking $3,000,000 and inserting $8,000,000 .\n##### (b) Implementation\nNot later than 180 days after the date of enactment of this Act, the Federal Acquisition Regulatory Council shall amend the Federal Acquisition Regulation (including FAR 19.1406) and the Secretary of Defense shall amend the Defense Federal Acquisition Regulation Supplement to implement the amendments made by subsection (a).\n##### (c) Application\nThe amendments made by this section shall apply to solicitations issued on or after the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-12-11",
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
        "updateDate": "2026-01-08T14:39:09Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6648ih.xml"
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
      "title": "FAIR Vets Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T07:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR Vets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Acquisition Improvement and Reform Vets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act to adjust sole-source thresholds for service-disabled veteran-owned small business concerns, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T07:33:27Z"
    }
  ]
}
```
