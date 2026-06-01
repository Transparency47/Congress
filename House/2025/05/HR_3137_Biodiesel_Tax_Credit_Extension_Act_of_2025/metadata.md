# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3137?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3137
- Title: Biodiesel Tax Credit Extension Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3137
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2025-06-04T13:37:31Z
- Update date including text: 2025-06-04T13:37:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3137",
    "number": "3137",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Biodiesel Tax Credit Extension Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-04T13:37:31Z",
    "updateDateIncludingText": "2025-06-04T13:37:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:07:20Z",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NY"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "SD"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NY"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IL"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "PA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "IA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "ME"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "IL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "IA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3137ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3137\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Carey (for himself, Mrs. Miller-Meeks , Ms. Tenney , Mr. Johnson of South Dakota , Mr. Garbarino , Mr. LaHood , and Mr. Kelly of Pennsylvania ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the biodiesel fuels credit and the biodiesel mixture credit.\n#### 1. Short title\nThis Act may be cited as the Biodiesel Tax Credit Extension Act of 2025 .\n#### 2. Extension of biofuel tax incentives\n##### (a) Extension of biodiesel and renewable diesel credit\n**(1) In general**\nSection 40A(g) of the Internal Revenue Code of 1986 is amended by striking 2024 and inserting 2026 .\n**(2) Denial of double benefit**\nSection 40A of such Code is amended\u2014\n**(A)**\nby redesignating subsection (g) (as amended) as subsection (h), and\n**(B)**\nby inserting after subsection (f) the following new subsection:\n(g) Denial of Double Benefit In the case of any fuel with respect to which a credit is allowed under section 45Z(a) for any taxable year, the amount determined under this section with respect to such fuel shall be zero. .\n##### (b) Extension of biodiesel mixture credit\n**(1) Extension of credit for fuels used for taxable purposes**\n**(A) In general**\nSection 6426(c)(6) of such Code is amended by striking 2024 and inserting 2026 .\n**(B) Denial of double benefit**\nSection 6426(c) of such Code is amended by adding at the end the following new paragraph:\n(7) Denial of double benefit In the case of any fuel with respect to which a credit is allowed under section 45Z(a) for any taxable year, the applicable amount determined under this paragraph (2) with respect to such fuel shall be zero. .\n**(2) Extension of credit for fuels not used for taxable purposes**\nSection 6427(e)(6)(B) of such Code is amended by striking 2024 and inserting 2026 .\n##### (c) Extension of alcohol fuel credit with respect to second generation biofuel production and coordination with clean fuel production credit\n**(1) Coordination with clean fuel production credit**\nSection 40(b) of such Code is amended by redesignating paragraph (6) as paragraph (7) and by inserting after paragraph (5) the following new paragraph:\n(6) Coordination with clean fuel production credit No credit shall be determined under this paragraph with respect to fuel with respect to which a credit was allowed under section 45Z(a). .\n**(2) Extension**\nSection 40(b)(7)(J)(i) of such Code (as so redesignated) is amended by striking January 1, 2025 and inserting January 1, 2027 .\n##### (d) Effective dates\n**(1) Biodiesels**\nThe amendments made subsections (a) and (b) shall apply to fuel sold or used after December 31, 2024.\n**(2) Second generation biofuels**\nThe amendments made by subsection (c) shall apply to qualified second generation biofuel (as defined in section 40(b)(6)(C) of such Code) production occurring after December 31, 2024.",
      "versionDate": "2025-05-01",
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
        "name": "Taxation",
        "updateDate": "2025-06-04T13:37:31Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3137ih.xml"
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
      "title": "Biodiesel Tax Credit Extension Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Biodiesel Tax Credit Extension Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend the biodiesel fuels credit and the biodiesel mixture credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:17Z"
    }
  ]
}
```
