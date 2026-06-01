# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3532?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3532
- Title: State Veterans Homes Inspection Simplification Act
- Congress: 119
- Bill type: S
- Bill number: 3532
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-03-30T18:26:28Z
- Update date including text: 2026-03-30T18:26:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3532",
    "number": "3532",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "State Veterans Homes Inspection Simplification Act",
    "type": "S",
    "updateDate": "2026-03-30T18:26:28Z",
    "updateDateIncludingText": "2026-03-30T18:26:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
            "date": "2025-12-17T19:21:50Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-17T19:21:50Z",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-12-17",
      "state": "ME"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "ID"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "UT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "TN"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "WV"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MT"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3532is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3532\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Crapo (for himself, Mr. King , Mr. Risch , Mr. Lee , Mrs. Blackburn , Mr. Justice , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to streamline the certification process for State Veterans Homes by allowing certain facilities certified by the Department of Veterans Affairs to be deemed in compliance with specified Medicare and Medicaid requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the State Veterans Homes Inspection Simplification Act .\n#### 2. Deeming of State Veterans Homes certified by the Department of Veterans Affairs as meeting Medicare conditions of participation\n##### (a) Medicare deeming authority\nSection 1819 of the Social Security Act ( 42 U.S.C. 1395i\u20133 ) is amended by adding at the end the following new subsection:\n(l) Special Rule for State Veterans Homes (1) Deemed compliance (A) In general A State home (as defined in section 101 of title 38, United States Code) that is inspected and certified by the Department of Veterans Affairs (in this subsection referred to as the VA ) in accordance with standards approved by the Secretary shall be deemed to meet the requirements of subsections (b) through (i) of this section if the Secretary determines that the following requirements are met: (i) The VA provides the Secretary, upon request, with documentation of inspection and certification, including survey findings, statements of deficiencies, and related corrective actions. (ii) Not less than once every 2 years, the VA submits its State home survey standards and inspection procedures for joint review with the Centers for Medicare & Medicaid Services to confirm continued alignment with Medicare Conditions of Participation, including oversight methodologies. (B) Requirements for approval of standards In approving standards under subparagraph (A), the Secretary shall\u2014 (i) consult with the Secretary of Veterans Affairs; and (ii) ensure that the inspection and certification process used by the VA, including both standards and enforcement practices\u2014 (I) includes, as a minimum, the survey protocols and enforcement expectations of the Centers for Medicare & Medicaid Services; and (II) upholds, at a minimum, the same standards of resident care, safety, transparency, and accountability required under this section. (2) Oversight and enforcement Nothing in paragraph (1) shall preclude the Secretary from doing any of the following: (A) Conducting complaint investigations or targeted surveys of any State home. (B) Imposing remedies under subsection (h), including civil monetary penalties or termination of participation under this title. (C) Revoking deemed status under paragraph (1) if the VA certification process is found to be inconsistent with Federal standards of transparency, data quality, or enforcement. (3) Public reporting Survey and certification data from VA inspections deemed valid under this subsection shall be reported publicly through the Nursing Home Care Compare website under subsection (i) or another publicly accessible platform in a format determined by the Secretary, in consultation with the Secretary of Veterans Affairs. .\n##### (b) Medicaid conforming amendment\nSection 1919 of the Social Security Act ( 42 U.S.C. 1396r ) is amended by adding at the end the following new subsection:\n(l) Special rule for State veterans homes The provisions of section 1819(l) shall apply with respect to a nursing facility that is a State home (as defined in section 101 of title 38, United States Code) and that is inspected and certified by the Department of Veterans Affairs in the same manner and to the same extent as such provisions apply under title XVIII. .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date that is 90 days after the date of enactment of this Act.\n#### 3. Alignment of data for public reporting\n##### (a) VA survey data on nursing home care compare\nThe Secretary of Health and Human Services shall coordinate with the Secretary of Veterans Affairs to ensure that inspection findings, deficiency statements, and quality metrics from Department of Veterans Affairs-certified State homes (as defined in section 101 of title 38, United States Code) are incorporated into the Nursing Home Care Compare website (or a successor website), to the extent feasible and consistent with section 1819(g)(5) of the Social Security Act ( 42 U.S.C. 1395i\u20133(g)(5) ).\n##### (b) Harmonization of survey processes\nNot later than 180 days after the date of enactment of this section, the Secretary of Health and Human Services, in consultation with the Secretary of Veterans Affairs, shall issue guidance to align certification and data reporting processes to ensure consistency and transparency in the public reporting of quality and compliance information for State homes (as so defined).",
      "versionDate": "2025-12-17",
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
        "actionDate": "2026-03-02",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7747",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "State Veterans Homes Inspection Simplification Act",
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
        "updateDate": "2026-01-14T16:20:34Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3532is.xml"
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
      "title": "State Veterans Homes Inspection Simplification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "State Veterans Homes Inspection Simplification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles XVIII and XIX of the Social Security Act to streamline the certification process for State Veterans Homes by allowing certain facilities certified by the Department of Veterans Affairs to be deemed in compliance with specified Medicare and Medicaid requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T05:18:17Z"
    }
  ]
}
```
