# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8414?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8414
- Title: DAIRY PRIDE Act
- Congress: 119
- Bill type: HR
- Bill number: 8414
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-05-16T08:08:03Z
- Update date including text: 2026-05-16T08:08:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8414",
    "number": "8414",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000302",
        "district": "13",
        "firstName": "John",
        "fullName": "Rep. Joyce, John [R-PA-13]",
        "lastName": "Joyce",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "DAIRY PRIDE Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:03Z",
    "updateDateIncludingText": "2026-05-16T08:08:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
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
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:03:40Z",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "PA"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "ID"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "MN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "WI"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "WI"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "WI"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8414ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8414\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Mr. Joyce of Pennsylvania (for himself and Mr. Riley of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require enforcement against misbranded milk alternatives.\n#### 1. Short title\nThis Act may be cited as the Defending Against Imitations and Replacements of Yogurt, milk, and cheese to Promote Regular Intake of Dairy Everyday Act or the DAIRY PRIDE Act .\n#### 2. Purpose\nIt is the purpose of this Act to establish that no food may be introduced or delivered for introduction into interstate commerce using a name for a standardized dairy product if the food does not meet the criterion set forth for dairy products under paragraph (z)(2) of section 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) (as added by section 3(a)) or the requirements for imitation of another food under paragraph (c) of section 403 of such Act.\n#### 3. Enforcement of definition\n##### (a) In general\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) (1) If it uses the name for a standardized dairy product described in subparagraph (3) and the food does not meet\u2014 (A) the criterion for being a dairy product, as described in subparagraph (2); or (B) the requirements for imitation of another food under paragraph (c). (2) For purposes of this paragraph, a food is a dairy product only if the food is, contains as a primary ingredient, or is derived from, the lacteal secretion, practically free from colostrum, obtained by the complete milking of one or more hooved mammals. (3) A name for a standardized dairy product described in this subparagraph means the dairy product terms described in parts 131 and 133 of subchapter B of chapter I of title 21, Code of Federal Regulations, and sections 135.110, 135.115, and 135.140 of title 21, Code of Federal Regulations (or any successor regulations), or any other term for which the Secretary has promulgated a standard of identity with respect to a food that is formulated with a dairy product (as described in subparagraph (2)) as the primary ingredient. .\n##### (b) Guidance\n**(1) New guidance**\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall\u2014\n**(A)**\nnot later than 90 days after the date of enactment of this Act, issue draft guidance on how enforcement of the amendment made by subsection (a) will be carried out; and\n**(B)**\nnot later than 180 days after the date of enactment of this Act, issue final guidance on such enforcement.\n**(2) Effect on certain previous guidance**\nEffective on the date of enactment of this Act, any guidance issued by the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, that is not consistent with paragraph (z) of section 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ), as added by subsection (a), shall have no force or effect.\n##### (c) Report to Congress\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall report to Congress on enforcement actions taken under paragraph (z) of section 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ), as added by subsection (a), including warnings issued pursuant to such paragraph and penalties assessed under section 303 of such Act ( 21 U.S.C. 333 ) with respect to such paragraph. If food that is misbranded under section 403(z) of such Act is offered for sale in interstate commerce at the time of such report, the Commissioner of Food and Drugs shall include in such report an updated plan for enforcement with respect to such food.",
      "versionDate": "2026-04-21",
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2507",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DAIRY PRIDE Act",
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
        "name": "Health",
        "updateDate": "2026-04-27T20:18:57Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8414ih.xml"
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
      "title": "DAIRY PRIDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DAIRY PRIDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defending Against Imitations and Replacements of Yogurt, milk, and cheese to Promote Regular Intake of Dairy Everyday Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require enforcement against misbranded milk alternatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T03:18:21Z"
    }
  ]
}
```
