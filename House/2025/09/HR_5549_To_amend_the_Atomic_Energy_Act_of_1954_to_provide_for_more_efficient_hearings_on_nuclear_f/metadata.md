# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5549?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5549
- Title: Efficient Nuclear Licensing Hearings Act
- Congress: 119
- Bill type: HR
- Bill number: 5549
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2026-05-13T08:06:27Z
- Update date including text: 2026-05-13T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-23: Introduced in House

## Actions

- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5549",
    "number": "5549",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "G000568",
        "district": "9",
        "firstName": "H.",
        "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
        "lastName": "Griffith",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Efficient Nuclear Licensing Hearings Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:27Z",
    "updateDateIncludingText": "2026-05-13T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "WA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "TX"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MO"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "TN"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "WA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "GA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "OH"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "VA"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "WA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "OK"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "NC"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5549ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5549\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Mr. Griffith (for himself, Ms. Schrier , and Mr. Veasey ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Atomic Energy Act of 1954 to provide for more efficient hearings on nuclear facility construction applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Efficient Nuclear Licensing Hearings Act .\n#### 2. Updating Hearing Procedures\n##### (a) Hearings and judicial review\nSection 189 a. of the Atomic Energy Act of 1954 ( 42 U.S.C. 2239(a) ) is amended\u2014\n**(1)**\nin paragraph (1)(A)\u2014\n**(A)**\nby striking In any proceeding under this Act and inserting the following:\n(i) In any proceeding under this Act ; and\n**(B)**\nin clause (i) (as so designated), by striking The Commission shall hold a hearing and all that follows through upon a determination by the Commission that the amendment involves no significant hazards consideration. and inserting the following:\n(ii) The Commission may, in the absence of a request for a hearing by any person whose interest may be affected, issue a construction permit, an operating license, a combined construction permit and operating license, an amendment to a construction permit, an amendment to an operating license, or an amendment to a combined construction permit and operating license under section 103, 104 b., 104 c., or 185 b. for a facility or a testing facility, without a hearing, but upon thirty days notice and publication once in the Federal Register of its intent to do so. The Commission may dispense with such thirty days notice and publication with respect to any application for an amendment to a construction permit, an amendment to an operating license, or an amendment to a combined construction permit and operating license upon a determination by the Commission that the amendment involves no significant hazards consideration. (iii) The Commission shall use informal adjudicatory procedures for any hearing held by the Commission pursuant to this subparagraph. ;\n**(2)**\nin paragraph (1)(B)(iv)\u2014\n**(A)**\nby inserting informal before hearing procedures ; and\n**(B)**\nby striking , whether informal or formal adjudicatory, ; and\n**(3)**\nin the second sentence of paragraph (2)(A), by striking required hearing and inserting hearing held by the Commission under this section .\n##### (b) Construction permits and operating licenses\nSection 185 b. of the Atomic Energy Act of 1954 ( 42 U.S.C. 2235(b) ) is amended by striking After holding a public hearing under section 189 a. (1)(A), and inserting After the thirty days notice and publication period or holding a hearing, as applicable, under section 189 a. (1)(A), .\n##### (c) Licensing of uranium enrichment facilities\nSection 193(b) of the Atomic Energy Act of 1954 ( 42 U.S.C. 2243(b) ) is amended by\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking on the record ; and\n**(B)**\nby inserting if a person whose interest may be affected by such construction and operation has requested a hearing regarding the licensing of the construction and operation of the facility after and 63 ; and\n**(2)**\nin paragraph (2), by striking Such hearing and inserting If a hearing is held under paragraph (1), the hearing .\n##### (d) Applicability\nThe amendments made by this section shall apply to all applications and proceedings pending before the Nuclear Regulatory Commission on or after the date of enactment of this section.",
      "versionDate": "2025-09-23",
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
        "actionDate": "2025-05-14",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "1757",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Efficient Nuclear Licensing Hearings Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-11-18T18:06:33Z"
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
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5549ih.xml"
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
      "title": "Efficient Nuclear Licensing Hearings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Efficient Nuclear Licensing Hearings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Atomic Energy Act of 1954 to provide for more efficient hearings on nuclear facility construction applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:33Z"
    }
  ]
}
```
