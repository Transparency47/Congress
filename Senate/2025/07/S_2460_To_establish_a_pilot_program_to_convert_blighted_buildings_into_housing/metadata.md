# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2460?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2460
- Title: RESIDE Act
- Congress: 119
- Bill type: S
- Bill number: 2460
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2025-12-16T16:29:18Z
- Update date including text: 2025-12-16T16:29:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2460",
    "number": "2460",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "RESIDE Act",
    "type": "S",
    "updateDate": "2025-12-16T16:29:18Z",
    "updateDateIncludingText": "2025-12-16T16:29:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T18:41:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2460is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2460\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Banks (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish a pilot program to convert blighted buildings into housing.\n#### 1. Short title\nThis Act may be cited as the Revitalizing Empty Structures Into Desirable Environments Act or the RESIDE Act .\n#### 2. Blighted Building to Housing Conversion Program\n##### (a) Definitions\nIn this section:\n**(1) Attainable housing**\nThe term attainable housing means housing that\u2014\n**(A)**\nserves households earning not more than 100 percent of the area median income, if a majority of the housing units are affordable to households earning not more than 80 percent of the area median income; or\n**(B)**\nserves households earning not more than 120 percent of the area median income, if the majority of the housing units are affordable to households earning not more than 60 percent of the area median income.\n**(2) Converted housing unit**\nThe term converted housing unit means a housing unit that is created using a covered grant.\n**(3) Covered grant**\nThe term covered grant means a grant awarded under the Pilot Program.\n**(4) Eligible entity**\nThe term eligible entity means a participating jurisdiction, as that term is defined in section 104 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 ).\n**(5) HOME Investment Partnerships Program**\nThe term HOME Investment Partnerships Program means the program under subtitle A of title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12741 et seq. ).\n**(6) Pilot Program**\nThe term Pilot Program means the Blighted Building to Housing Conversion Program carried out under subsection (b).\n**(7) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(8) Vacant and abandoned building**\nThe term vacant and abandoned building means a property\u2014\n**(A)**\nthat was constructed for use as a warehouse, factory, mall, strip mall, or hotel, or for another industrial or commercial use; and\n**(B)**\n**(i)**\nwith respect to which\u2014\n**(I)**\na code enforcement inspection has determined that the property is not safe; and\n**(II)**\nnot less than 90 days have elapsed since the owner was notified of the deficiencies in the property and the owner has taken no corrective action; or\n**(ii)**\nthat is subject to a court-ordered receivership or nuisance abatement related to abandonment pursuant to State or local law or otherwise meets the definition of an abandoned property under State law.\n##### (b) Grant program\nFor each of fiscal years 2027 through 2031, if the amounts made available to carry out the HOME Investment Partnerships Program exceed $1,350,000,000, the Secretary may use not more than $100,000,000 of the excess amounts to carry out a pilot program, to be known as the Blighted Building to Housing Conversion Program , under which the Secretary awards grants on a competitive basis to eligible entities to convert vacant and abandoned buildings into attainable housing.\n##### (c) Amount of grant\n**(1) In general**\nFor any fiscal year for which $100,000,000 is available to carry out the Pilot Program pursuant to subsection (b), the amount of a covered grant shall be not less than $1,000,000 and not more than $10,000,000.\n**(2) Fiscal years with lower funding**\nFor any fiscal year for which less than $100,000,000 is available to carry out the Pilot Program pursuant to subsection (b), the Secretary shall seek to maximize the number of covered grants awarded.\n##### (d) Relation to HOME Investment Partnerships Program formula allocation\nA covered grant awarded to an eligible entity shall be in addition to, and shall not affect, the formula allocation for the eligible entity under the HOME Investment Partnerships Program.\n##### (e) Priority\nIn awarding covered grants, the Secretary shall give priority to an eligible entity that\u2014\n**(1)**\nwill use the covered grant in a community that is experiencing economic distress;\n**(2)**\nwill use the covered grant in a qualified opportunity zone (as defined in section 1400Z\u20131(a) of the Internal Revenue Code of 1986);\n**(3)**\nwill use the covered grant to construct housing that will serve a need identified in the comprehensive housing affordability strategy and community development plan of the eligible entity under part 91 of title 24, Code of Federal Regulations, or any successor regulation (commonly referred to as a consolidated plan ); or\n**(4)**\nhas enacted ordinances to reduce regulatory barriers to conversion of commercial or industrial properties to housing, which shall not include any alteration of an ordinance that governs safety and habitability.\n##### (f) Use of funds\nAn eligible entity may use a covered grant for\u2014\n**(1)**\nproperty acquisition;\n**(2)**\ndemolition;\n**(3)**\nhealth hazard remediation;\n**(4)**\nsite preparation;\n**(5)**\nconstruction, renovation, or rehabilitation; or\n**(6)**\nthe establishment, maintenance, or expansion of community land trusts.\n##### (g) Applicability of HOME requirements\nThe requirements for rental, sale, and resale of housing under the HOME Investment Partnerships Program shall apply to rental, sale, and resale of converting housing units under the Pilot Program.\n##### (h) Waiver authority\nIn administering covered grants, the Secretary may waive, or specify alternative requirements for, any statute or regulation that the Secretary administers in connection with the obligation by the Secretary or the use by eligible entities of covered grant funds (except for requirements related to fair housing, nondiscrimination, labor standards, or the environment) if the Secretary makes a public finding that good cause exists for the waiver or alternative requirement.\n##### (i) Study; report\nNot later than 180 days after the termination of the Pilot Program, the Secretary shall study and submit a report to Congress on the impact of the Pilot Program on\u2014\n**(1)**\nimproving the tax base of local communities;\n**(2)**\nincreasing access to affordable housing, especially for elderly individuals, disabled individuals, and veterans;\n**(3)**\nincreasing homeownership; and\n**(4)**\nremoving blight.",
      "versionDate": "2025-07-24",
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
        "actionDate": "2025-09-26",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "5591",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RESIDE Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-18T18:07:50Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2460is.xml"
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
      "title": "RESIDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RESIDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Revitalizing Empty Structures Into Desirable Environments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a pilot program to convert blighted buildings into housing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:43Z"
    }
  ]
}
```
