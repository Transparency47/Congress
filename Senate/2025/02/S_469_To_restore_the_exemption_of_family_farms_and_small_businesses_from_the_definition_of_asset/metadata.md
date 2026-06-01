# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/469?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/469
- Title: Family Farm and Small Business Exemption Act
- Congress: 119
- Bill type: S
- Bill number: 469
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-12-11T16:47:00Z
- Update date including text: 2025-12-11T16:47:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/469",
    "number": "469",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Family Farm and Small Business Exemption Act",
    "type": "S",
    "updateDate": "2025-12-11T16:47:00Z",
    "updateDateIncludingText": "2025-12-11T16:47:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T22:03:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "KS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WV"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "KS"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ND"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "SD"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AR"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NE"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "AL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s469is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 469\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Ms. Ernst (for herself, Mr. Bennet , Mr. Grassley , Mr. Marshall , Mr. Justice , Mr. Moran , Mr. Hoeven , Mr. Rounds , Mr. Boozman , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo restore the exemption of family farms and small businesses from the definition of assets under title IV of the Higher Education Act of 1965.\n#### 1. Short title\nThis Act may be cited as the Family Farm and Small Business Exemption Act .\n#### 2. Exempting family farms and small businesses from assets under the Higher Education Act of 1965\n##### (a) In general\nSection 480(f)(2) of the Higher Education Act of 1965 ( 20 U.S.C. 1087vv(f)(2) ) is amended\u2014\n**(1)**\nby striking net value of the and inserting the following:\nnet value of\u2014 (A) the ;\n**(2)**\nby striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(B) a family farm on which the family resides; or (C) a small business with not more than 100 full-time or full-time equivalent employees (or any part of such a small business) that is owned and controlled by the family. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply to need analysis conducted under part F of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1087kk et seq. ) for award years beginning on or after the date of the enactment of this Act.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-07",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1131",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Family Farm and Small Business Exemption Act",
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
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-04-23T17:11:28Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-04-23T17:11:28Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-04-23T17:11:28Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-04-23T17:11:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-21T11:24:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s469",
          "measure-number": "469",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s469v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Family Farm and Small Business Exemption Act</strong></p><p>This bill restores an exemption for certain family farms and small businesses on the Free Application for Federal Student Aid (FAFSA) form. The bill applies to the net worth of (1) a family farm on which the family resides, or (2) a small business with not more than 100 full-time or full-time equivalent employees that is owned and controlled by the family.</p><p>Prior to recent changes made to the FAFSA, the net worth of these family farms and small businesses were excluded as assets when calculating a student's financial need to determine federal student aid eligibility. Beginning with the 2024-2025 academic year, the net worth of these farms and businesses are treated as an asset and therefore included in the calculation. This bill restores the exemption to exclude such net worth from the calculation.</p>"
        },
        "title": "Family Farm and Small Business Exemption Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s469.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Family Farm and Small Business Exemption Act</strong></p><p>This bill restores an exemption for certain family farms and small businesses on the Free Application for Federal Student Aid (FAFSA) form. The bill applies to the net worth of (1) a family farm on which the family resides, or (2) a small business with not more than 100 full-time or full-time equivalent employees that is owned and controlled by the family.</p><p>Prior to recent changes made to the FAFSA, the net worth of these family farms and small businesses were excluded as assets when calculating a student's financial need to determine federal student aid eligibility. Beginning with the 2024-2025 academic year, the net worth of these farms and businesses are treated as an asset and therefore included in the calculation. This bill restores the exemption to exclude such net worth from the calculation.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119s469"
    },
    "title": "Family Farm and Small Business Exemption Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Family Farm and Small Business Exemption Act</strong></p><p>This bill restores an exemption for certain family farms and small businesses on the Free Application for Federal Student Aid (FAFSA) form. The bill applies to the net worth of (1) a family farm on which the family resides, or (2) a small business with not more than 100 full-time or full-time equivalent employees that is owned and controlled by the family.</p><p>Prior to recent changes made to the FAFSA, the net worth of these family farms and small businesses were excluded as assets when calculating a student's financial need to determine federal student aid eligibility. Beginning with the 2024-2025 academic year, the net worth of these farms and businesses are treated as an asset and therefore included in the calculation. This bill restores the exemption to exclude such net worth from the calculation.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119s469"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s469is.xml"
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
      "title": "Family Farm and Small Business Exemption Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Family Farm and Small Business Exemption Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restore the exemption of family farms and small businesses from the definition of assets under title IV of the Higher Education Act of 1965.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:02Z"
    }
  ]
}
```
