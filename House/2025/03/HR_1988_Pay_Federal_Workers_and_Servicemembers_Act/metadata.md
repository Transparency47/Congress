# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1988?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1988
- Title: Pay Federal Workers and Servicemembers Act
- Congress: 119
- Bill type: HR
- Bill number: 1988
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-01-09T09:07:07Z
- Update date including text: 2026-01-09T09:07:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1988",
    "number": "1988",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Pay Federal Workers and Servicemembers Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:07:07Z",
    "updateDateIncludingText": "2026-01-09T09:07:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "WA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NJ"
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
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "AL"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "WI"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "OH"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "DC"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "LA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OR"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "AL"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "DE"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "WA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "FL"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "MD"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MI"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "MO"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1988ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1988\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mrs. Dingell (for herself, Ms. DelBene , Ms. Tlaib , Mrs. McIver , Ms. Vel\u00e1zquez , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend chapter 85 of title 5, United States Code, to clarify that Federal civilian and military personnel excepted from a furlough during a Government shutdown are eligible for unemployment compensation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pay Federal Workers and Servicemembers Act .\n#### 2. Eligibility for unemployment compensation for Federal civilian and military personnel excepted from furlough during Government shutdown\n##### (a) Federal civilian employees\n**(1) In general**\nSubchapter I of chapter 85 of title 5, United States Code, is amended by adding at the end the following:\n8510. Eligibility for unemployment compensation for Federal personnel excepted from furlough during Government shutdown (a) In general With respect to any lapse in appropriations beginning on or after March 14, 2025, each covered employee shall be, solely for the purpose of determining eligibility for unemployment compensation under this subchapter or subchapter II (as the case may be), deemed for the duration of the lapse in appropriations to be\u2014 (1) totally separated from Federal service; and (2) eligible for unemployment compensation benefits under the applicable subchapter with no waiting period for such eligibility to accrue. (b) Covered employee defined In this section, the term covered employee means any of the following Federal personnel who are excepted from furlough and are not being paid due to a lapse in appropriations: (1) Any member of the Armed Forces or the Commissioned Corps of the National Oceanic and Atmospheric Administration. (2) Any Federal civilian employee who is an excepted employee or an employee performing emergency work, as such terms are defined by the Office of Personnel Management. .\n**(2) Clerical amendment**\nThe table of sections for such subchapter is amended by adding at the end the following:\n8510. Eligibility for unemployment compensation for Federal personnel excepted from furlough during Government shutdown. .\n##### (a) Application\nThe amendment made by subsection (a) shall apply to weeks of unemployment beginning on or after March 14, 2025.",
      "versionDate": "2025-03-10",
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
      "congress": "118",
      "latestAction": {
        "actionDate": "2023-09-19",
        "text": "Referred to the Committee on Education and the Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5572",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Civilian Climate Corps for Jobs and Justice Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T02:43:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
    "originChamber": "House",
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
          "measure-id": "id119hr1988",
          "measure-number": "1988",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-10-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1988v00",
            "update-date": "2025-10-01"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pay Federal Workers and Servicemembers Act</strong></p><p>This bill makes federal civilian and military personnel who are excepted from furlough during a government shutdown eligible for unemployment compensation benefits.\u00a0</p><p>During a government shutdown due to a lapse in appropriations, federal employees who are excepted from furlough are required to report for work and perform duties, but their pay is delayed until appropriations legislation is enacted. Under guidance issued by the Department of Labor, excepted employees who are performing services (but whose payment for that work is delayed) are generally ineligible for unemployment compensation benefits based on states' definitions of unemployment.\u00a0</p><p>This bill provides that, for the purpose of determining eligibility for unemployment compensation during a government shutdown, excepted employees are deemed to be (1) totally separated from federal service, and (2) eligible for unemployment compensation benefits with no waiting period for the eligibility to accrue.\u00a0</p><p>The bill applies to the following federal personnel who are excepted from furlough and are not being paid due to a government shutdown: (1) any member of the Armed Forces or the Commissioned Corps of the National Oceanic and Atmospheric Administration, and (2) any federal civilian employee who is an excepted employee or an employee performing emergency work.\u00a0</p>"
        },
        "title": "Pay Federal Workers and Servicemembers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1988.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pay Federal Workers and Servicemembers Act</strong></p><p>This bill makes federal civilian and military personnel who are excepted from furlough during a government shutdown eligible for unemployment compensation benefits.\u00a0</p><p>During a government shutdown due to a lapse in appropriations, federal employees who are excepted from furlough are required to report for work and perform duties, but their pay is delayed until appropriations legislation is enacted. Under guidance issued by the Department of Labor, excepted employees who are performing services (but whose payment for that work is delayed) are generally ineligible for unemployment compensation benefits based on states' definitions of unemployment.\u00a0</p><p>This bill provides that, for the purpose of determining eligibility for unemployment compensation during a government shutdown, excepted employees are deemed to be (1) totally separated from federal service, and (2) eligible for unemployment compensation benefits with no waiting period for the eligibility to accrue.\u00a0</p><p>The bill applies to the following federal personnel who are excepted from furlough and are not being paid due to a government shutdown: (1) any member of the Armed Forces or the Commissioned Corps of the National Oceanic and Atmospheric Administration, and (2) any federal civilian employee who is an excepted employee or an employee performing emergency work.\u00a0</p>",
      "updateDate": "2025-10-01",
      "versionCode": "id119hr1988"
    },
    "title": "Pay Federal Workers and Servicemembers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pay Federal Workers and Servicemembers Act</strong></p><p>This bill makes federal civilian and military personnel who are excepted from furlough during a government shutdown eligible for unemployment compensation benefits.\u00a0</p><p>During a government shutdown due to a lapse in appropriations, federal employees who are excepted from furlough are required to report for work and perform duties, but their pay is delayed until appropriations legislation is enacted. Under guidance issued by the Department of Labor, excepted employees who are performing services (but whose payment for that work is delayed) are generally ineligible for unemployment compensation benefits based on states' definitions of unemployment.\u00a0</p><p>This bill provides that, for the purpose of determining eligibility for unemployment compensation during a government shutdown, excepted employees are deemed to be (1) totally separated from federal service, and (2) eligible for unemployment compensation benefits with no waiting period for the eligibility to accrue.\u00a0</p><p>The bill applies to the following federal personnel who are excepted from furlough and are not being paid due to a government shutdown: (1) any member of the Armed Forces or the Commissioned Corps of the National Oceanic and Atmospheric Administration, and (2) any federal civilian employee who is an excepted employee or an employee performing emergency work.\u00a0</p>",
      "updateDate": "2025-10-01",
      "versionCode": "id119hr1988"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1988ih.xml"
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
      "title": "Pay Federal Workers and Servicemembers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pay Federal Workers and Servicemembers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 85 of title 5, United States Code, to clarify that Federal civilian and military personnel excepted from a furlough during a Government shutdown are eligible for unemployment compensation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:20Z"
    }
  ]
}
```
