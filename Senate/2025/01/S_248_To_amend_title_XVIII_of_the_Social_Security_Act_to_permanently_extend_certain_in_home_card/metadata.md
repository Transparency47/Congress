# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/248?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/248
- Title: Sustainable Cardiopulmonary Rehabilitation Services in the Home Act
- Congress: 119
- Bill type: S
- Bill number: 248
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2026-02-06T21:26:15Z
- Update date including text: 2026-02-06T21:26:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/248",
    "number": "248",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Sustainable Cardiopulmonary Rehabilitation Services in the Home Act",
    "type": "S",
    "updateDate": "2026-02-06T21:26:15Z",
    "updateDateIncludingText": "2026-02-06T21:26:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T19:34:36Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "MN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "NJ"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "NC"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s248is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 248\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mrs. Blackburn (for herself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to permanently extend certain in-home cardiopulmonary rehabilitation flexibilities established in response to COVID\u201319, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sustainable Cardiopulmonary Rehabilitation Services in the Home Act .\n#### 2. Codifying virtual cardiopulmonary rehabilitation flexibilities established in response to COVID\u201319\n##### (a) In general\nSection 1861(eee)(2) of the Social Security Act ( 42 U.S.C. 1395x(eee)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by inserting , including in the home of an individual when furnished as a telehealth service through audio-visual real-time communications technology, or when such home is designated as a provider-based location of a hospital outpatient department after outpatient basis ; and\n**(2)**\nin subparagraph (B), by inserting , including through the virtual presence of such physician, physician assistant, nurse practitioner, or clinical nurse specialist, through audio-visual real-time communications technology after under the program .\n##### (b) Expanding originating sites\nSection 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking and (9) and all that follows through (as defined in paragraph (4)(E)) and inserting , (9), and (10), the Secretary shall pay for telehealth services that are furnished via a telecommunications system by a physician (as defined in section 1861(r)) or a practitioner (as defined in paragraph (4)(E)), or by a hospital (as defined in section 1861(e)) ;\n**(2)**\nin paragraph (2)(A), by striking or practitioner each place that it appears and inserting , practitioner, or hospital ;\n**(3)**\nin paragraph (4)(A), by striking or practitioner and inserting , practitioner, or hospital ;\n**(4)**\nin paragraph (4)(C)\u2014\n**(A)**\nin clause (i), by striking and (7) and inserting (7), and (10) ; and\n**(B)**\nin clause (ii)(X), by striking paragraph (7) and inserting paragraphs (7) and (10) ;\n**(5)**\nin paragraph (4)(F)(i), by striking paragraph (8) and inserting paragraphs (8) and (10) ; and\n**(6)**\nby adding at the end the following new paragraph:\n(10) Treatment of cardiac rehabilitation program, intensive cardiac rehabilitation program, and pulmonary rehabilitation program visits furnished through telehealth In the case of items and services furnished on or after January 1, 2026, the geographic requirements described in paragraph (4)(C)(i) shall not apply with respect to telehealth services for cardiac rehabilitation programs and intensive cardiac rehabilitation programs (as such terms are defined in section 1861(eee)) and pulmonary rehabilitation programs (as defined in section 1861(fff)) at an originating site described in subclause (V) or (X) of paragraph (4)(C)(ii). .\n##### (c) Authority To establish standards and allow for certain programs To utilize telehealth services\n**(1) In general**\nNot later than 30 days after the date of enactment of this section, the Secretary of Health and Human Services shall\u2014\n**(A)**\nestablish standards for the designation of the home of an individual with status as a provider-based organization of a hospital consistent with waivers issued through the Hospital Without Walls program for cardiac rehabilitation, pulmonary rehabilitation, and intensive cardiac rehabilitation; and\n**(B)**\ninclude items and services furnished under a cardiac rehabilitation program or under an intensive cardiac rehabilitation program (as such terms are defined in section 1861(eee) of the Social Security Act ( 42 U.S.C. 1395x(eee) ), or under a pulmonary rehabilitation program (as defined in section 1861(fff) of such Act ( 42 U.S.C. 1395x(fff) ) among telehealth services to be specified under section 1834(m)(4)(F) of such Act ( 42 U.S.C. 1395m(m)(4)(F) ).\n**(2) Effective date**\nThe standards established under paragraph (1) shall apply to items and services furnished on or after January 1, 2026.\n##### (d) Implementation\nNotwithstanding any other provision of the law, the Secretary of Health and Human Services may implement the provisions of, and the amendments made by, this section by program instruction or otherwise.\n##### (e) Effective date\nThe amendments made by subsections (a) and (b) shall apply to items and services furnished on or after January 1, 2026.",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "783",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Sustainable Cardiopulmonary Rehabilitation Services in the Home Act",
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
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-03-27T14:43:20Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-27T14:47:18Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-27T14:47:32Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-03-27T14:47:22Z"
          },
          {
            "name": "Home and outpatient care",
            "updateDate": "2025-03-27T14:47:27Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-03-27T14:47:10Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-03-27T14:42:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T14:49:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119s248",
          "measure-number": "248",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s248v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Sustainable Cardiopulmonary Rehabilitation Services in the Home Act</b></p> <p>This bill permanently allows services relating to cardiac rehabilitation programs, intensive cardiac rehabilitation programs, and pulmonary rehabilitation programs to be furnished via telehealth at a beneficiary's home under Medicare. </p>"
        },
        "title": "Sustainable Cardiopulmonary Rehabilitation Services in the Home Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s248.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Sustainable Cardiopulmonary Rehabilitation Services in the Home Act</b></p> <p>This bill permanently allows services relating to cardiac rehabilitation programs, intensive cardiac rehabilitation programs, and pulmonary rehabilitation programs to be furnished via telehealth at a beneficiary's home under Medicare. </p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119s248"
    },
    "title": "Sustainable Cardiopulmonary Rehabilitation Services in the Home Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Sustainable Cardiopulmonary Rehabilitation Services in the Home Act</b></p> <p>This bill permanently allows services relating to cardiac rehabilitation programs, intensive cardiac rehabilitation programs, and pulmonary rehabilitation programs to be furnished via telehealth at a beneficiary's home under Medicare. </p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119s248"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s248is.xml"
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
      "title": "Sustainable Cardiopulmonary Rehabilitation Services in the Home Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T11:18:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sustainable Cardiopulmonary Rehabilitation Services in the Home Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to permanently extend certain in-home cardiopulmonary rehabilitation flexibilities established in response to COVID-19, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:58Z"
    }
  ]
}
```
