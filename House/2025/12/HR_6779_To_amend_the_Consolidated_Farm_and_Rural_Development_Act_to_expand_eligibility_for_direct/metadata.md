# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6779?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6779
- Title: USDA Loan Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 6779
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-22T08:08:48Z
- Update date including text: 2026-05-22T08:08:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6779",
    "number": "6779",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "USDA Loan Modernization Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:48Z",
    "updateDateIncludingText": "2026-05-22T08:08:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:28:26Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "TN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6779ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6779\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Bost (for himself, Ms. Budzinski , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to expand eligibility for direct loans to individuals or entity members that hold at least a 50 percent interest and that are or will become bona fide operators of the farm real estate acquired, improved, or supported with farm ownership, operating, or emergency loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the USDA Loan Modernization Act .\n#### 2. Persons eligible for real estate loans\nSection 302(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1922(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking a majority and inserting at least a 50 percent ; and\n**(B)**\nin subparagraph (C), by striking a majority and inserting at least a 50 percent ; and\n**(2)**\nin paragraph (2), by striking subparagraphs (A) and (B) and inserting the following:\n(A) Eligibility of qualified operators Qualified operators, as defined by the Secretary, shall be considered to meet the operator requirement of paragraph (1). (B) Eligibility of certain operating-only entities An applicant that is or will become only the operator of farm real estate acquired, improved, or supported with funds under this subtitle shall be considered to meet the owner-operator requirements of paragraph (1) if 1 or more of the individuals who is an owner of the farm real estate owns at least 50 percent (or such other percentage as the Secretary determines is appropriate) of the applicant. (C) Eligibility of certain embedded entities An entity that is an owner-operator described in paragraph (1), or an operator described in subparagraph (B) of this paragraph that is owned, in whole or in part, by 1 or more other entities, shall be considered to meet the direct ownership requirement imposed under paragraph (1) if at least 75 percent of the total ownership interests of the embedded entity, or of the other entities, is owned, directly or indirectly, by qualified operators of the farm acquired, improved, or supported with funds under this subtitle. .\n#### 3. Persons eligible for operating loans\nSection 311(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1941 ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking a majority and inserting at least a 50 percent ; and\n**(B)**\nin subparagraph (C), by striking a majority and inserting at least a 50 percent ; and\n**(2)**\nby amending paragraph (2) to read as follows:\n(2) Special rules (A) Eligibility of qualified operators Qualified operators, as defined by the Secretary, shall be considered to meet the operator requirement of paragraph (1). (B) Eligibility of certain operating-only entities An entity that is an operator described in paragraph (1) that is owned, in whole or in part, by other entities, shall be considered to meet the direct ownership requirement imposed under paragraph (1) if at least 75 percent of the total ownership interests of the embedded entity, or of the other entities, is owned, directly or indirectly, by qualified operators of the farm improved or supported with funds under this subtitle. .\n#### 4. Persons eligible for emergency loans\nSection 321 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1961 ) is amended\u2014\n**(1)**\nby striking all that precedes shall make and insure and inserting the following:\n321. Eligibility for loans (a) In general (1) Eligibility requirements The Secretary ; and\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin the 1st sentence\u2014\n**(i)**\nby striking (1) and inserting (A) ;\n**(ii)**\nby striking (2) and inserting (B) ;\n**(iii)**\nby striking (A) the 1st place it appears and inserting (i) ;\n**(iv)**\nby striking (B) the 1st place it appears and inserting (ii) ; and\n**(v)**\nby striking a majority each place it appears and inserting at least a 50 percent ;\n**(B)**\nby striking the 5th sentence; and\n**(C)**\nby adding at the end the following:\n(2) Special rules (A) Eligibility of qualified operators Qualified operators, as defined by the Secretary, shall be considered to meet the operator requirement of paragraph (1). (B) Eligibility of certain operating-only entities An applicant that is or will become only the operator of farm real estate acquired, improved, or supported with funds under this subtitle shall be considered to meet the owner-operator requirements of paragraph (1) if 1 or more of the individuals who is an owner of the real estate owns at least 50 percent (or such other percentage as the Secretary determines is appropriate) of the applicant. (C) Eligibility of certain embedded entities An entity that is an owner-operator described in paragraph (1), or an operator described in subparagraph (B) of this paragraph that is owned, in whole or in part, by 1 or more other entities, shall be considered to meet the direct ownership requirement imposed under paragraph (1) if at least 75 percent of the total ownership interests of the embedded entity, or of the other entities, is owned, directly or indirectly, by qualified operators of the farm acquired, improved, or supported with funds under this subtitle. .",
      "versionDate": "2025-12-17",
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
        "actionDate": "2026-05-19",
        "text": "Received in the Senate."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-21T16:10:46Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6779ih.xml"
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
      "title": "USDA Loan Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USDA Loan Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Farm and Rural Development Act to expand eligibility for direct loans to individuals or entity members that hold at least a 50 percent interest and that are or will become bona fide operators of the farm real estate acquired, improved, or supported with farm ownership, operating, or emergency loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:33:42Z"
    }
  ]
}
```
