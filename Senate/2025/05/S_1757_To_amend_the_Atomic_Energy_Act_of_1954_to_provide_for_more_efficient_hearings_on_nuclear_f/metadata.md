# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1757?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1757
- Title: Efficient Nuclear Licensing Hearings Act
- Congress: 119
- Bill type: S
- Bill number: 1757
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1757",
    "number": "1757",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Efficient Nuclear Licensing Hearings Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-14",
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
            "date": "2025-05-14T16:29:01Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-14T16:29:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "DE"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "UT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "AZ"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1757is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1757\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Scott of South Carolina (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Atomic Energy Act of 1954 to provide for more efficient hearings on nuclear facility construction applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Efficient Nuclear Licensing Hearings Act .\n#### 2. Updating hearing procedures\n##### (a) Hearings and judicial review\nSection 189 a. of the Atomic Energy Act of 1954 ( 42 U.S.C. 2239(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the first sentence, by striking In any proceeding under this Act and inserting the following:\n(i) In any proceeding under this Act ; and\n**(ii)**\nin clause (i) (as so designated), by striking The Commission shall hold a hearing and all that follows through upon a determination by the Commission that the amendment involves no significant hazards consideration. and inserting the following:\n(ii) The Commission may, in the absence of a request for a hearing by any person whose interest may be affected, issue a construction permit, an operating license, a combined construction permit and operating license, an amendment to a construction permit, an amendment to an operating license, or an amendment to a combined construction permit and operating license under section 103, 104 b., 104 c., or 185 b. for a facility or a testing facility, without a hearing, but upon thirty days notice and publication once in the Federal Register of its intent to do so. The Commission may dispense with such thirty days notice and publication with respect to any application for an amendment to a construction permit, an amendment to an operating license, or an amendment to a combined construction permit and operating license upon a determination by the Commission that the amendment involves no significant hazards consideration. (iii) The Commission shall use informal adjudicatory procedures for any hearing held by the Commission pursuant to this subparagraph. ;\n**(B)**\nin subparagraph (B)(iv)\u2014\n**(i)**\nby inserting informal before hearing procedures ; and\n**(ii)**\nby striking , whether informal or formal adjudicatory, ; and\n**(2)**\nin paragraph (2)(A), in the second sentence, by striking required hearing and inserting hearing held by the Commission under this section .\n##### (b) Construction permits and operating licenses\nSection 185 b. of the Atomic Energy Act of 1954 ( 42 U.S.C. 2235(b) ) is amended by striking After holding a public hearing under section 189 a. (1)(A), and inserting After the thirty days notice and publication period or holding a hearing, as applicable, under section 189 a. (1)(A), .\n##### (c) Licensing of uranium enrichment facilities\nSection 193(b) of the Atomic Energy Act of 1954 ( 42 U.S.C. 2243(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking on the record ; and\n**(B)**\nby inserting if a person whose interest may be affected by such construction and operation has requested a hearing regarding the licensing of the construction and operation of the facility after and 63 ; and\n**(2)**\nin paragraph (2), by striking Such hearing and inserting If a hearing is held under paragraph (1), the hearing .\n##### (d) Applicability\nThe amendments made by this section shall apply to all applications and proceedings pending before the Nuclear Regulatory Commission on or after the date of enactment of this section.",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-09-23",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "5549",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Efficient Nuclear Licensing Hearings Act",
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
        "updateDate": "2025-05-30T14:05:57Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1757is.xml"
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
      "title": "Efficient Nuclear Licensing Hearings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Efficient Nuclear Licensing Hearings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Atomic Energy Act of 1954 to provide for more efficient hearings on nuclear facility construction applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:29Z"
    }
  ]
}
```
