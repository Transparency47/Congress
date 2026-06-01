# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3607
- Title: Access to Genetic Counselor Services Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3607
- Origin chamber: Senate
- Introduced date: 2026-01-08
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in Senate
- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S116-117)
- Latest action: 2026-01-08: Introduced in Senate

## Actions

- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S116-117)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3607",
    "number": "3607",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Access to Genetic Counselor Services Act of 2026",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S116-117)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T19:55:31Z",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "VT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "WV"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NV"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3607is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3607\nIN THE SENATE OF THE UNITED STATES\nJanuary 8 (legislative day, January 7), 2026 Mr. Barrasso (for himself, Mr. Welch , Mrs. Capito , and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide for expanded coverage of services furnished by genetic counselors under part B of the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Access to Genetic Counselor Services Act of 2026 .\n#### 2. Medicare coverage of genetic counseling services\n##### (a) In general\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)\u2014\n**(A)**\nby striking and at the end of subparagraph (II);\n**(B)**\nby adding and at the end of subparagraph (JJ); and\n**(C)**\nby adding at the end the following new subparagraph:\n(KK) covered genetic counseling services (as defined in subsection (nnn)(1)); ; and\n**(2)**\nby adding at the end the following new subsection:\n(nnn) Covered Genetic Counseling Services (1) The term covered genetic counseling services means genetic counseling services furnished on or after January 1, 2027, by a genetic counselor (as defined in paragraph (2)) and such services and supplies furnished as an incident to the provision of such services which the genetic counselor is legally authorized to perform under State law (or the State regulatory mechanism provided by State law) as would otherwise be covered if furnished by a physician (or as incident to a physician\u2019s service). (2) The term genetic counselor means an individual who\u2014 (A) is licensed as a genetic counselor by the State in which the individual furnishes genetic counseling services; or (B) in the case of an individual practicing in a State that does not license genetic counselors, is certified by the American Board of Genetic Counseling and meets such other criteria as the Secretary establishes. .\n##### (b) Balance billing\nSection 1842(b)(18)(C) of the Social Security Act ( 42 U.S.C. 1395u(b)(18)(C) ) is amended by adding at the end the following new clause:\n(ix) A genetic counselor (as defined in section 1861(nnn)(2)). .\n##### (c) Payment\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(1)**\nby striking and (HH) and inserting (HH) ; and\n**(2)**\nby inserting before the semicolon at the end the following: , and (II) with respect to covered genetic counseling services (as defined in section 1861(nnn)(1)), the amount paid shall be equal to 80 percent of the lesser of (i) the actual charge for the services or (ii) 85 percent of the fee schedule amount provided under section 1848 that would have applied had the genetic counseling services been furnished by a physician .\n##### (d) Conforming amendment\nSection 1862(a)(14) of the Social Security Act (42 U.S.C. 1395(y)(a)(14)) is amended by inserting covered genetic counseling services, after qualified psychologist services, .\n##### (e) Rule of construction\nThe amendments made by this section shall not be construed as preventing physicians and health care providers other than genetic counselors from billing for genetic counseling services under the Medicare program which are otherwise covered under such program.\n##### (f) Implementation\nNotwithstanding any other provision of law, the Secretary of Health and Human Services may implement the amendments made by this section by interim final rule with comment period.",
      "versionDate": "2026-01-08",
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
        "actionDate": "2025-11-21",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6280",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Access to Genetic Counselor Services Act of 2025",
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
        "name": "Health",
        "updateDate": "2026-01-26T14:39:17Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3607is.xml"
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
      "title": "Access to Genetic Counselor Services Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to Genetic Counselor Services Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-24T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide for expanded coverage of services furnished by genetic counselors under part B of the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-24T03:48:20Z"
    }
  ]
}
```
