# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4117
- Title: Fuel Emissions Freedom Act
- Congress: 119
- Bill type: HR
- Bill number: 4117
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-04-02T15:57:32Z
- Update date including text: 2026-04-02T15:57:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4117",
    "number": "4117",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000816",
        "district": "25",
        "firstName": "Roger",
        "fullName": "Rep. Williams, Roger [R-TX-25]",
        "lastName": "Williams",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Fuel Emissions Freedom Act",
    "type": "HR",
    "updateDate": "2026-04-02T15:57:32Z",
    "updateDateIncludingText": "2026-04-02T15:57:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:02:35Z",
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
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "TX"
    },
    {
      "bioguideId": "S000929",
      "district": "5",
      "firstName": "Victoria",
      "fullName": "Rep. Spartz, Victoria [R-IN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Spartz",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "IN"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4117ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4117\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Williams of Texas (for himself, Mr. Cloud , and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Clean Air Act to repeal the establishment of motor vehicle emission and fuel standards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fuel Emissions Freedom Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nFuel emissions regulations increase costs for consumers and manufacturers.\n**(2)**\nOverlapping and ever-changing fuel emissions standards, whether imposed by the Environmental Protection Agency, the State of California, or through Corporate Average Fuel Economy regulations, create long-term uncertainty for manufacturers.\n**(3)**\nThis fragmented regulatory environment stifles innovation, disrupts supply chains, and burdens manufacturers and businesses, especially small and medium-sized auto suppliers.\n**(4)**\nConflicting fuel emissions standards force manufacturers to comply with multiple sets of costly and inconsistent regulations, further reducing efficiency and raising production costs, which are ultimately passed onto the consumer.\n**(5)**\nEliminating fuel emissions standards at the Federal and State level will help restore regulatory certainty, lower costs for families, and strengthen manufacturing in the United States to ensure economic freedom.\n#### 3. Repeal and preemption of certain emission standards\n##### (a) Motor vehicle emission and fuel standards under Clean Air Act\n**(1) Repeal of standards**\nSection 202 of the Clean Air Act ( 42 U.S.C. 7521 ) is repealed.\n**(2) Preemption of State standards**\nSection 209 of the Clean Air Act ( 42 U.S.C. 7543 ) is amended\u2014\n**(A)**\nin subsection (a), by striking subject to this part ;\n**(B)**\nby striking subsection (b);\n**(C)**\nin subsection (c), by striking The preceding sentence shall not apply in the case of a State with respect to which a waiver is in effect under subsection (b). ;\n**(D)**\nin subsection (e), by striking Subsection (b) shall not apply for purposes of this paragraph and all that follows through The Administrator shall issue and inserting the following:\n(2) Regulations The Administrator shall issue ; and\n**(E)**\nby redesignating subsections (c), (d), and (e) as subsections (b), (c), and (d), respectively.\n##### (b) Automobile fuel economy\n**(1) Repeal of standards**\nSections 32902 through 32918 of title 49, United States Code, are repealed.\n**(2) Preemption of State standards**\nSection 32919 of title 49, United States Code, is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking (a) General. \u2014When an average fuel economy standard prescribed under this chapter is in effect, a State and inserting A State ; and\n**(ii)**\nby striking covered by an average fuel economy standard under this chapter ; and\n**(B)**\nby striking subsections (b) and (c).\n**(3) Table of sections amendment**\nThe table of sections for chapter 329 of title 49, United States Code, is amended by striking the items relating to sections 32902 through 32918.\n##### (c) Nullification of standards\nAny Federal regulation issued pursuant to section 202 of the Clean Air Act ( 42 U.S.C. 7543(b) ) or sections 32902 through 32918 of title 49, United States Code, or any State law, regulation, or executive order issued pursuant to section 209(b) of such Act, as each such section was in effect on the day before the date of enactment of this Act, is hereby nullified and shall have no force or effect.\n##### (d) References\nAny reference in any other Federal law, Executive order, rule, regulation, or delegation of authority, or any document of or pertaining to a standard established under section 202 or 209(b) of the Clean Air Act ( 42 U.S.C. 7521 ; 7543(b)) or section 32902 through 32918 of title 49, United States Code, is deemed void and unenforceable.\n#### 4. Prohibition on fuel emission standards\n##### (a) Federal preemption\nNotwithstanding any other law, the Federal Government may not establish, enforce, or maintain fuel emission standard for motor vehicles.\n##### (b) State prohibition\nA State, or political subdivision thereof, may not enforce or maintain any fuel emission standards for motor vehicles.\n##### (c) Preemption of standards\nAny Federal or State law, regulation, or executive order that establishes fuel emissions standards for motor vehicles is hereby nullified and shall have no force or effect.",
      "versionDate": "2025-06-24",
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-02T15:57:32Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4117ih.xml"
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
      "title": "Fuel Emissions Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fuel Emissions Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Clean Air Act to repeal the establishment of motor vehicle emission and fuel standards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-09T04:18:22Z"
    }
  ]
}
```
