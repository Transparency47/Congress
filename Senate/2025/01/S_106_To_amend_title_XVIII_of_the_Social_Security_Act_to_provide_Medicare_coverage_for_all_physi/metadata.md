# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/106?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/106
- Title: A bill to amend title XVIII of the Social Security Act to provide Medicare coverage for all physicians' services furnished by doctors of chiropractic within the scope of their license, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 106
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-03-06T11:57:02Z
- Update date including text: 2026-03-06T11:57:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/106",
    "number": "106",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "A bill to amend title XVIII of the Social Security Act to provide Medicare coverage for all physicians' services furnished by doctors of chiropractic within the scope of their license, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-06T11:57:02Z",
    "updateDateIncludingText": "2026-03-06T11:57:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
            "date": "2025-01-16T17:32:27Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-16T17:32:27Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CT"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "KS"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NH"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SD"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MN"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NM"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ND"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "DE"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WY"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "MS"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "DE"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NM"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s106is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 106\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Cramer (for himself, Mr. Blumenthal , Mr. Daines , Ms. Baldwin , Mr. Moran , Mrs. Shaheen , Mr. Rounds , Ms. Klobuchar , Mr. Heinrich , Mr. Hoeven , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide Medicare coverage for all physicians\u2019 services furnished by doctors of chiropractic within the scope of their license, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chiropractic Medicare Coverage Modernization Act of 2025 .\n#### 2. Findings; Statement of purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nIn 1972, coverage was established under the Medicare program for beneficiaries to receive chiropractic care.\n**(2)**\nUnfortunately, the antiquated statute restricts beneficiaries to one service in a chiropractic clinic and Medicare chiropractic coverage has not kept up with private sector coverage and other Federal health delivery systems.\n**(3)**\nToday, due to positive evidence-based outcomes and cost effectiveness of the services provided by doctors of chiropractic, private coverage for chiropractic services has evolved and State licensure for chiropractors has advanced to meet patient needs and health outcomes.\n**(4)**\nThis Act would bring Medicare chiropractic coverage more in line with that provided with the Department of Veterans Affairs, Department of Defense, the Federal Employee Health Benefits Program, and private health insurance coverage.\n##### (b) Purpose\nIt is the purpose of this Act to expand recognition and coverage of a doctor of chiropractic as a physician under the Medicare program in connection with the performance of any function or action, including current service of manual manipulation of the spine to correct a subluxation , as is legally authorized by the State in which such doctor performs such function or action.\n#### 3. Providing Medicare coverage for all physicians\u2019 services furnished by doctors of chiropractic within the scope of their license\n##### (a) In general\nSection 1861(r)(5) of the Social Security Act ( 42 U.S.C. 1395x(r)(5) ) is amended by striking a chiropractor who is licensed as such by the State (or in a State which does not license chiropractors as such, is legally authorized to perform the services of a chiropractor in the jurisdiction in which he performs such services), and who meets uniform minimum standards promulgated by the Secretary, but only for the purpose of sections 1861(s)(1) and 1861(s)(2)(A) and only with respect to treatment by means of manual manipulation of the spine (to correct a subluxation) which he is legally authorized to perform by the State or jurisdiction in which such treatment is provided and inserting a doctor of chiropractic who is licensed as a doctor of chiropractic or a chiropractor by the State in which the function or action is performed and whose license provides legal authorization to perform such function or action in such State or in the jurisdiction in which the function or action is performed .\n##### (b) Certain coverage limits\nSection 1833 of the Social Security Act ( 42 U.S.C. 1395l ) is amended by adding at the end the following new subsection:\n(ee) Limitation on payment of services provided by certain doctors of chiropractic Notwithstanding any other provision of this part, in the case of services of a doctor of chiropractic described in section 1861(r)(5), payment may only be made under this part for such services if\u2014 (1) such services are furnished by a doctor of chiropractic who is verified once, by a process designed by the Secretary, as attending an educational documentation webinar, or other similar electronic product, designed by the Secretary or an updated modified version of such webinar, as designed by the Secretary; or (2) such services are treatment by means of manual manipulation of the spine to correct a subluxation. .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "539",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Chiropractic Medicare Coverage Modernization Act of 2025",
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
            "name": "Alternative treatments",
            "updateDate": "2025-02-26T16:38:47Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-02-26T16:38:47Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-02-26T16:38:47Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-02-26T16:38:47Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-02-26T16:38:47Z"
          },
          {
            "name": "Musculoskeletal and skin diseases",
            "updateDate": "2025-02-26T16:38:47Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-26T16:38:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-20T16:40:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s106",
          "measure-number": "106",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s106v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Chiropractic Medicare Coverage Modernization Act of 2025</strong><strong></strong></p><p>This bill expands Medicare coverage of chiropractic services to include all services provided by chiropractors, rather than only subluxation corrections through manual manipulation of the spine.</p>"
        },
        "title": "Chiropractic Medicare Coverage Modernization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s106.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Chiropractic Medicare Coverage Modernization Act of 2025</strong><strong></strong></p><p>This bill expands Medicare coverage of chiropractic services to include all services provided by chiropractors, rather than only subluxation corrections through manual manipulation of the spine.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119s106"
    },
    "title": "Chiropractic Medicare Coverage Modernization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Chiropractic Medicare Coverage Modernization Act of 2025</strong><strong></strong></p><p>This bill expands Medicare coverage of chiropractic services to include all services provided by chiropractors, rather than only subluxation corrections through manual manipulation of the spine.</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119s106"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s106is.xml"
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
      "title": "Chiropractic Medicare Coverage Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chiropractic Medicare Coverage Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide Medicare coverage for all physicians' services furnished by doctors of chiropractic within the scope of their license, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:28Z"
    }
  ]
}
```
