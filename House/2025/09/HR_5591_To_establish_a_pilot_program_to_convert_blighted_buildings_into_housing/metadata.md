# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5591?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5591
- Title: RESIDE Act
- Congress: 119
- Bill type: HR
- Bill number: 5591
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-01-31T03:36:14Z
- Update date including text: 2026-01-31T03:36:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5591",
    "number": "5591",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000607",
        "district": "16",
        "firstName": "Sam",
        "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
        "lastName": "Liccardo",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "RESIDE Act",
    "type": "HR",
    "updateDate": "2026-01-31T03:36:14Z",
    "updateDateIncludingText": "2026-01-31T03:36:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:03:00Z",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "FL"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "MD"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "PA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5591ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5591\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Liccardo (for himself, Ms. Salazar , Mr. Olszewski , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo establish a pilot program to convert blighted buildings into housing.\n#### 1. Short title\nThis Act may be cited as the Revitalizing Empty Structures Into Desirable Environments Act or the RESIDE Act .\n#### 2. Blighted Building to Housing Conversion Program\n##### (a) Definitions\nIn this section:\n**(1) Attainable housing**\nThe term attainable housing means housing that\u2014\n**(A)**\nserves households earning not more than 100 percent of the area median income, if a majority of the housing units are affordable to households earning not more than 80 percent of the area median income; or\n**(B)**\nserves households earning not more than 120 percent of the area median income, if the majority of the housing units are affordable to households earning not more than 60 percent of the area median income.\n**(2) Converted housing unit**\nThe term converted housing unit means a housing unit that is created using a covered grant.\n**(3) Covered grant**\nThe term covered grant means a grant awarded under the Pilot Program.\n**(4) Eligible entity**\nThe term eligible entity means a participating jurisdiction, as that term is defined in section 104 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 ).\n**(5) HOME Investment Partnerships Program**\nThe term HOME Investment Partnerships Program means the program under subtitle A of title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12741 et seq. ).\n**(6) Pilot Program**\nThe term Pilot Program means the Blighted Building to Housing Conversion Program carried out under subsection (b).\n**(7) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(8) Vacant and abandoned building**\nThe term vacant and abandoned building means a property\u2014\n**(A)**\nthat was constructed for use as a warehouse, factory, mall, strip mall, or hotel, or for another industrial or commercial use; and\n**(B)**\n**(i)**\nwith respect to which\u2014\n**(I)**\na code enforcement inspection has determined that the property is not safe; and\n**(II)**\nnot less than 90 days have elapsed since the owner was notified of the deficiencies in the property and the owner has taken no corrective action; or\n**(ii)**\nthat is subject to a court-ordered receivership or nuisance abatement related to abandonment pursuant to State or local law or otherwise meets the definition of an abandoned property under State law.\n##### (b) Grant program\nFor each of fiscal years 2027 through 2031, if the amounts made available to carry out the HOME Investment Partnerships Program exceed $1,350,000,000, the Secretary may use not more than $100,000,000 of the excess amounts to carry out a pilot program, to be known as the Blighted Building to Housing Conversion Program , under which the Secretary awards grants on a competitive basis to eligible entities to convert vacant and abandoned buildings into attainable housing.\n##### (c) Amount of grant\n**(1) In general**\nFor any fiscal year for which $100,000,000 is available to carry out the Pilot Program pursuant to subsection (b), the amount of a covered grant shall be not less than $1,000,000 and not more than $10,000,000.\n**(2) Fiscal years with lower funding**\nFor any fiscal year for which less than $100,000,000 is available to carry out the Pilot Program pursuant to subsection (b), the Secretary shall seek to maximize the number of covered grants awarded.\n##### (d) Relation to HOME Investment Partnerships Program formula allocation\nA covered grant awarded to an eligible entity shall be in addition to, and shall not affect, the formula allocation for the eligible entity under the HOME Investment Partnerships Program.\n##### (e) Priority\nIn awarding covered grants, the Secretary shall give priority to an eligible entity that\u2014\n**(1)**\nwill use the covered grant in a community that is experiencing economic distress;\n**(2)**\nwill use the covered grant in a qualified opportunity zone (as defined in section 1400Z\u20131(a) of the Internal Revenue Code of 1986);\n**(3)**\nwill use the covered grant to construct housing that will serve a need identified in the comprehensive housing affordability strategy and community development plan of the eligible entity under part 91 of title 24, Code of Federal Regulations, or any successor regulation (commonly referred to as a consolidated plan ); or\n**(4)**\nhas enacted ordinances to reduce regulatory barriers to conversion of commercial or industrial properties to housing, which shall not include any alteration of an ordinance that governs safety and habitability.\n##### (f) Use of funds\nAn eligible entity may use a covered grant for\u2014\n**(1)**\nproperty acquisition;\n**(2)**\ndemolition;\n**(3)**\nhealth hazard remediation;\n**(4)**\nsite preparation;\n**(5)**\nconstruction, renovation, or rehabilitation; or\n**(6)**\nthe establishment, maintenance, or expansion of community land trusts.\n##### (g) Applicability of HOME requirements\nThe requirements for rental, sale, and resale of housing under the HOME Investment Partnerships Program shall apply to rental, sale, and resale of converting housing units under the Pilot Program.\n##### (h) Waiver authority\nIn administering covered grants, the Secretary may waive, or specify alternative requirements for, any statute or regulation that the Secretary administers in connection with the obligation by the Secretary or the use by eligible entities of covered grant funds (except for requirements related to fair housing, nondiscrimination, labor standards, or the environment) if the Secretary makes a public finding that good cause exists for the waiver or alternative requirement.\n##### (i) Study; report\nNot later than 180 days after the termination of the Pilot Program, the Secretary shall study and submit a report to Congress on the impact of the Pilot Program on\u2014\n**(1)**\nimproving the tax base of local communities;\n**(2)**\nincreasing access to affordable housing, especially for elderly individuals, disabled individuals, and veterans;\n**(3)**\nincreasing homeownership; and\n**(4)**\nremoving blight.",
      "versionDate": "2025-09-26",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2460",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RESIDE Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-12-16T16:29:23Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5591ih.xml"
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
      "title": "RESIDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T07:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESIDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T07:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Revitalizing Empty Structures Into Desirable Environments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T07:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a pilot program to convert blighted buildings into housing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T07:33:28Z"
    }
  ]
}
```
