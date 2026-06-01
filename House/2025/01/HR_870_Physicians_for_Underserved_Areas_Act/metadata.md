# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/870?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/870
- Title: Physicians for Underserved Areas Act
- Congress: 119
- Bill type: HR
- Bill number: 870
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-12-05T21:58:09Z
- Update date including text: 2025-12-05T21:58:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/870",
    "number": "870",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000590",
        "district": "3",
        "firstName": "Susie",
        "fullName": "Rep. Lee, Susie [D-NV-3]",
        "lastName": "Lee",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Physicians for Underserved Areas Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:58:09Z",
    "updateDateIncludingText": "2025-12-05T21:58:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:03:40Z",
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
          "date": "2025-01-31T15:03:35Z",
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
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr870ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 870\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. Lee of Nevada (for herself and Mr. Balderson ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to make improvements to the redistribution of residency slots under the Medicare program after a hospital closes.\n#### 1. Short title\nThis Act may be cited as the Physicians for Underserved Areas Act .\n#### 2. Improvements to the redistribution of residency slots under the Medicare program after a hospital closes\n##### (a) In general\nSection 1886(h)(4)(H)(vi) of the Social Security Act ( 42 U.S.C. 1395ww(h)(4)(H)(vi) ) is amended\u2014\n**(1)**\nin subclause (II)\u2014\n**(A)**\nby striking item (cc) and redesignating item (dd) as item (cc); and\n**(B)**\nin item (cc), as redesignated under subparagraph (A)\u2014\n**(i)**\nby striking Fourth and inserting Third ; and\n**(ii)**\nby striking item (cc) and inserting item (bb) ; and\n**(2)**\nin subclause (III), by striking likelihood of filling and all that follows and inserting the following: \u201clikelihood of\u2014\n(aa) starting to utilize the positions made available under this clause within 2 years; and (bb) filling the positions made available under this clause within 5 years. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to the redistribution of residency slots with respect to hospitals that close on or after the date of enactment of this Act.",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1044",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Physicians for Underserved Areas Act",
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
            "name": "Employee hiring",
            "updateDate": "2025-04-07T13:37:50Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-04-07T13:37:50Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-04-07T13:37:50Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-04-07T13:37:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-04T17:27:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr870",
          "measure-number": "870",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr870v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Physicians for Underserved Areas Act</b></p> <p>This bill modifies how a hospital's residency positions are redistributed after it closes for purposes of graduate medical education payments under Medicare.</p> <p>Under current law, if a hospital with an approved medical residency program closes, the Centers for Medicare & Medicaid Services (CMS) must redistribute the hospital's residency positions to other hospitals in the following order: (1) hospitals in the same core-based statistical area as the closed hospital, (2) hospitals in the same state as the closed hospital, (3) hospitals in the same region of the country as the closed hospital, and (4) other remaining hospitals. In order to receive the additional positions, hospitals must demonstrate a likelihood of filling the positions within three years.</p> <p>The bill removes the requirement that the CMS prioritize hospitals in the same region of the country as the closed hospital. It also requires hospitals to demonstrate a likelihood of (1) starting to use the positions within two years, and (2) filling the positions within five years.</p>"
        },
        "title": "Physicians for Underserved Areas Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr870.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Physicians for Underserved Areas Act</b></p> <p>This bill modifies how a hospital's residency positions are redistributed after it closes for purposes of graduate medical education payments under Medicare.</p> <p>Under current law, if a hospital with an approved medical residency program closes, the Centers for Medicare & Medicaid Services (CMS) must redistribute the hospital's residency positions to other hospitals in the following order: (1) hospitals in the same core-based statistical area as the closed hospital, (2) hospitals in the same state as the closed hospital, (3) hospitals in the same region of the country as the closed hospital, and (4) other remaining hospitals. In order to receive the additional positions, hospitals must demonstrate a likelihood of filling the positions within three years.</p> <p>The bill removes the requirement that the CMS prioritize hospitals in the same region of the country as the closed hospital. It also requires hospitals to demonstrate a likelihood of (1) starting to use the positions within two years, and (2) filling the positions within five years.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr870"
    },
    "title": "Physicians for Underserved Areas Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Physicians for Underserved Areas Act</b></p> <p>This bill modifies how a hospital's residency positions are redistributed after it closes for purposes of graduate medical education payments under Medicare.</p> <p>Under current law, if a hospital with an approved medical residency program closes, the Centers for Medicare & Medicaid Services (CMS) must redistribute the hospital's residency positions to other hospitals in the following order: (1) hospitals in the same core-based statistical area as the closed hospital, (2) hospitals in the same state as the closed hospital, (3) hospitals in the same region of the country as the closed hospital, and (4) other remaining hospitals. In order to receive the additional positions, hospitals must demonstrate a likelihood of filling the positions within three years.</p> <p>The bill removes the requirement that the CMS prioritize hospitals in the same region of the country as the closed hospital. It also requires hospitals to demonstrate a likelihood of (1) starting to use the positions within two years, and (2) filling the positions within five years.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr870"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr870ih.xml"
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
      "title": "Physicians for Underserved Areas Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Physicians for Underserved Areas Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to make improvements to the redistribution of residency slots under the Medicare program after a hospital closes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:31Z"
    }
  ]
}
```
