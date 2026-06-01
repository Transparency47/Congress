# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3472?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3472
- Title: Housing Stability for Dreamers Act
- Congress: 119
- Bill type: HR
- Bill number: 3472
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-12-12T09:07:13Z
- Update date including text: 2025-12-12T09:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3472",
    "number": "3472",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "V000130",
        "district": "52",
        "firstName": "Juan",
        "fullName": "Rep. Vargas, Juan [D-CA-52]",
        "lastName": "Vargas",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Housing Stability for Dreamers Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:13Z",
    "updateDateIncludingText": "2025-12-12T09:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T15:41:10Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "A000371",
      "district": "33",
      "firstName": "Pete",
      "fullName": "Rep. Aguilar, Pete [D-CA-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Aguilar",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IL"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "DC"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "AZ"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3472ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3472\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Vargas (for himself, Mr. Aguilar , Ms. Garcia of Texas , Ms. Brownley , Mr. Carbajal , Mr. Castro of Texas , Mr. Garc\u00eda of Illinois , Mr. Gomez , Ms. Norton , Mr. Menendez , Ms. Tlaib , Ms. Vel\u00e1zquez , Ms. Ansari , Mr. Peters , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the National Housing Act and title 38, United States Code.\n#### 1. Short title\nThis Act may be cited as the Housing Stability for Dreamers Act .\n#### 2. DACA recipient eligibility\n##### (a) FHA\nSection 203 of the National Housing Act ( 12 U.S.C. 1709 ) is amended by inserting after subsection (h) the following:\n(i) DACA recipient eligibility (1) In general The Secretary may not\u2014 (A) prescribe terms that limit the eligibility of a single family mortgage for insurance under this title based in whole or in part on the status of the mortgagor as a DACA recipient; or (B) issue any limited denial of participation in the program for such insurance based in whole or in part on the status of the mortgagor as a DACA recipient. (2) DACA recipient defined For the purposes of this subsection, the term DACA recipient means an alien who, on the date of the enactment of this Act, is the recipient of deferred action pursuant to the memorandum of the Department of Homeland Security entitled Exercising Prosecutorial Discretion with Respect to Individuals Who Came to the United States as Children\u2019 issued on June 15, 2012 . .\n##### (b) Rural Housing Service\nSection 501 of the Housing Act of 1949 ( 42 U.S.C. 1472 ) is amended by adding at the end the following:\n(k) DACA recipient eligibility (1) In general The Secretary may not prescribe terms that limit eligibility for a single family mortgage made, insured, or guaranteed under this title because of the status of the mortgagor as a DACA recipient. (2) DACA recipient defined For the purposes of this paragraph, the term DACA recipient means an alien who, on the date of the enactment of this Act, is the recipient of deferred action pursuant to the memorandum of the Department of Homeland Security entitled Exercising Prosecutorial Discretion with Respect to Individuals Who Came to the United States as Children issued on June 15, 2012. .\n##### (c) Fannie Mae\nSection 302(b) of the National Housing Act ( 12 U.S.C. 1717(b) ) is amended by adding at the end the following:\n(8) DACA recipient eligibility (A) In general The corporation may not condition purchase of a single-family residence mortgage by the corporation under this subsection on the status of the borrower as a DACA recipient. (B) DACA recipient defined For the purposes of this paragraph, the term DACA recipient means an alien who, on the date of the enactment of this Act, is the recipient of deferred action pursuant to the memorandum of the Department of Homeland Security entitled Exercising Prosecutorial Discretion with Respect to Individuals Who Came to the United States as Children issued on June 15, 2012. .\n##### (d) Freddie Mac\nSection 305(a) of the Federal Home Loan Mortgage Corporation Act ( 12 U.S.C. 1454 ) is amended by adding at the end the following:\n(6) DACA recipient eligibility (A) In general The Corporation may not condition purchase of a single-family residence mortgage by the corporation under this subsection on the status of the borrower as a DACA recipient. (B) DACA recipient defined For the purposes of this subsection, the term DACA recipient means an alien who, on the date of the enactment of this Act, is the recipient of deferred action pursuant to the memorandum of the Department of Homeland Security entitled Exercising Prosecutorial Discretion with Respect to Individuals Who Came to the United States as Children issued on June 15, 2012. .\n#### 3. DACA recipient eligibility\nSection 214(a) of the Housing and Community Development Act of 1980 ( 42 U.S.C. 1436a ) is amended\u2014\n**(1)**\nin paragraph (6), by striking or at the end;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(8) an alien who, on the date of the enactment of this Act, is the recipient of deferred action pursuant to the memorandum of the Department of Homeland Security entitled Exercising Prosecutorial Discretion with Respect to Individuals Who Came to the United States as Children issued on June 15, 2012. .\n#### 4. Clarification of eligibility of a veteran who is a DACA recipient for a housing loan guaranteed by the Secretary of Veterans Affairs\nSection 3702(a) of title 38, United States Code, is amended by adding at the end the following new paragraph:\n(5) Whether a veteran described in paragraph (2) is a DACA recipient (as such term is defined in section 203 of the National Housing Act ( 12 U.S.C. 1709 )) shall not affect the veteran\u2019s entitlement to housing loan benefits under this chapter. .",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in House"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-06-03T15:47:27Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3472ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Housing Act and title 38, United States Code.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T08:05:58Z"
    },
    {
      "title": "Housing Stability for Dreamers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Stability for Dreamers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:17Z"
    }
  ]
}
```
