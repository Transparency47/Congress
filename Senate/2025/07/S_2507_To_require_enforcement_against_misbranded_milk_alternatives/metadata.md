# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2507?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2507
- Title: DAIRY PRIDE Act
- Congress: 119
- Bill type: S
- Bill number: 2507
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-04-27T20:18:50Z
- Update date including text: 2026-04-27T20:18:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2507",
    "number": "2507",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "DAIRY PRIDE Act",
    "type": "S",
    "updateDate": "2026-04-27T20:18:50Z",
    "updateDateIncludingText": "2026-04-27T20:18:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
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
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T18:47:20Z",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "ID"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "ME"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-29",
      "state": "ME"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "ID"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "SD"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NE"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "KS"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2507is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2507\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Ms. Baldwin (for herself, Mr. Risch , Ms. Collins , Mr. Welch , Ms. Klobuchar , Mr. King , Mr. Fetterman , Mrs. Gillibrand , Mr. Crapo , Mr. Rounds , Mr. Ricketts , Mr. Marshall , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require enforcement against misbranded milk alternatives.\n#### 1. Short title\nThis Act may be cited as the Defending Against Imitations and Replacements of Yogurt, milk, and cheese to Promote Regular Intake of Dairy Everyday Act or the DAIRY PRIDE Act .\n#### 2. Purpose\nIt is the purpose of this Act to establish that no food may be introduced or delivered for introduction into interstate commerce using a name for a standardized dairy product if the food does not meet the criterion set forth for dairy products under paragraph (z)(2) of section 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) (as added by section 3(a)) or the requirements for imitation of another food under paragraph (c) of section 403 of such Act.\n#### 3. Enforcement of definition\n##### (a) In general\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) (1) If it uses the name for a standardized dairy product described in subparagraph (3) and the food does not meet\u2014 (A) the criterion for being a dairy product, as described in subparagraph (2); or (B) the requirements for imitation of another food under paragraph (c). (2) For purposes of this paragraph, a food is a dairy product only if the food is, contains as a primary ingredient, or is derived from, the lacteal secretion, practically free from colostrum, obtained by the complete milking of one or more hooved mammals. (3) A name for a standardized dairy product described in this subparagraph means the dairy product terms described in parts 131 and 133 of subchapter B of chapter I of title 21, Code of Federal Regulations, and sections 135.110, 135.115, and 135.140 of title 21, Code of Federal Regulations (or any successor regulations), or any other term for which the Secretary has promulgated a standard of identity with respect to a food that is formulated with a dairy product (as described in subparagraph (2)) as the primary ingredient. .\n##### (b) Guidance\n**(1) New guidance**\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall\u2014\n**(A)**\nnot later than 90 days after the date of enactment of this Act, issue draft guidance on how enforcement of the amendment made by subsection (a) will be carried out; and\n**(B)**\nnot later than 180 days after the date of enactment of this Act, issue final guidance on such enforcement.\n**(2) Effect on certain previous guidance**\nEffective on the date of enactment of this Act, any guidance issued by the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, that is not consistent with paragraph (z) of section 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ), as added by subsection (a), shall have no force or effect.\n##### (c) Report to Congress\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall report to Congress on enforcement actions taken under paragraph (z) of section 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ), as added by subsection (a), including warnings issued pursuant to such paragraph and penalties assessed under section 303 of such Act ( 21 U.S.C. 333 ) with respect to such paragraph. If food that is misbranded under section 403(z) of such Act is offered for sale in interstate commerce at the time of such report, the Commissioner of Food and Drugs shall include in such report an updated plan for enforcement with respect to such food.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2026-04-21",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8414",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DAIRY PRIDE Act",
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
        "updateDate": "2025-09-18T19:58:09Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2507is.xml"
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
      "title": "DAIRY PRIDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DAIRY PRIDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Defending Against Imitations and Replacements of Yogurt, milk, and cheese to Promote Regular Intake of Dairy Everyday Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require enforcement against misbranded milk alternatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:03:17Z"
    }
  ]
}
```
