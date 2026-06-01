# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3407?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3407
- Title: Western Refined Fuel Reserve Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3407
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-04-17T19:51:02Z
- Update date including text: 2026-04-17T19:51:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3407",
    "number": "3407",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Western Refined Fuel Reserve Act of 2025",
    "type": "S",
    "updateDate": "2026-04-17T19:51:02Z",
    "updateDateIncludingText": "2026-04-17T19:51:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-09",
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
            "date": "2025-12-09T21:59:33Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-09T21:59:33Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3407is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3407\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Curtis introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of Energy to establish a Western Refined Fuel Storage Reserve as part of the Strategic Petroleum Reserve, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Western Refined Fuel Reserve Act of 2025 .\n#### 2. Western Refined Fuel Storage Reserve\nThe Energy Policy and Conservation Act is amended by inserting after section 163 ( 42 U.S.C. 6243 ) the following:\n164. Western Refined Fuel Storage Reserve (a) Definitions In this section: (1) Refined Fuel Storage Reserve The term Refined Fuel Storage Reserve means a storage facility that\u2014 (A) is a salt cavern formation; and (B) is capable of storing refined petroleum products. (2) Refined petroleum product The term refined petroleum product means gasoline, diesel, and jet fuel. (3) Western State The term Western State means the States of Arizona, California, Idaho, Montana, Nevada, Oregon, Utah, and Washington. (b) Establishment (1) In general Not later than 6 months after the date of enactment of the Western Refined Fuel Reserve Act of 2025 , the Secretary shall establish a Refined Fuel Storage Reserve for the storage of refined petroleum products as part of the Strategic Petroleum Reserve, pursuant to\u2014 (A) the authority of the Secretary under section 159(f) to address energy supply and transportation vulnerabilities in Western States, in accordance with Executive Order 14156 (90 Fed. Reg. 8433; relating to declaring a national energy emergency); and (B) this Act. (2) Requirements (A) Identification and selection In carrying out paragraph (1), the Secretary shall\u2014 (i) identify existing or potential storage locations in Western States suitable to establish a Refined Fuel Storage Reserve, taking into account\u2014 (I) the proximity of existing distribution systems; (II) areas of the United States\u2014 (aa) most dependent on imported petroleum products; and (bb) areas of the United States most likely to experience shortages of refined petroleum products; (III) the capability for expeditious distribution of refined petroleum products from the Refined Fuel Storage Reserve to areas of the United States described in subclause (II); and (IV) the cost of establishing the Refined Fuel Storage Reserve\u2014 (aa) in the applicable Western State; and (bb) at the applicable storage location; and (ii) select 1 storage location. (B) Existing locations In carrying out subparagraph (A), the Secretary shall, to the maximum extent practicable\u2014 (i) identify locations suitable for the Refined Fuel Storage Reserve in Western States; and (ii) enter into a contractual arrangement with a public or private entity for the use and operation of a public or private storage location. (c) Fill and maintenance (1) Requirements During the 5 fiscal years following the date of establishment of the Refined Fuel Storage Reserve under subsection (b)(1), the Secretary shall, in accordance with paragraph (2), fill and maintain the Refined Fuel Storage Reserve at not less than 75 percent of the minimum capacity for each refined petroleum product on an adjusted annual basis using\u2014 (A) amounts appropriated by Congress for acquisition, by purchase, of petroleum products for storage in the Strategic Petroleum Reserve; and (B) revenues from emergency or test sales carried out pursuant to section 161. (2) Minimum capacity The minimum capacity of the Refined Fuel Storage Reserve is\u2014 (A) 5,000,000 barrels of gasoline; (B) 3,000,000 barrels of diesel; and (C) 2,000,000 barrels of jet fuel. (d) Drawdown The Secretary may withdraw refined petroleum products stored in the Refined Fuel Storage Reserve to respond to emergencies, supply disruptions, or any other circumstances consistent with the intent of the Strategic Petroleum Reserve or the needs of Western States. (e) State and local government storage The Secretary shall, as the Secretary determines appropriate, pursue agreements with applicable Western State governments and local governments for storage of non-Federal petroleum products within the Refined Fuel Storage Reserve. (f) Report Not later than 1 year after the date of enactment of the Western Refined Fuel Reserve Act of 2025 , and annually thereafter, the Secretary shall submit to Congress a report on the establishment and operations of the Refined Fuel Storage Reserve, which shall include\u2014 (1) an evaluation of\u2014 (A) the mechanisms used to carry out the requirements of this section; and (B) other potential mechanisms that could be used in the future to carry out the requirements of this section; (2) the process for purchase or leasing of storage facilities required for the Refined Fuel Storage Reserve, as applicable; and (3) recommendations for future storage of refined petroleum products in the Refined Fuel Storage Reserve, including any administrative actions and legislation necessary to implement the recommendations, as the Secretary determines appropriate. .",
      "versionDate": "2025-12-09",
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
        "actionDate": "2026-04-06",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8204",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Western Refined Fuel Reserve Act of 2026",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-01-08T19:29:38Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3407is.xml"
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
      "title": "Western Refined Fuel Reserve Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Western Refined Fuel Reserve Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Energy to establish a Western Refined Fuel Storage Reserve as part of the Strategic Petroleum Reserve, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:35Z"
    }
  ]
}
```
