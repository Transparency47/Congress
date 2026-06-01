# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6774?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6774
- Title: FHA Small-Dollar Mortgages Act
- Congress: 119
- Bill type: HR
- Bill number: 6774
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-04-24T20:12:30Z
- Update date including text: 2026-04-24T20:12:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Financial Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6774",
    "number": "6774",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000187",
        "district": "43",
        "firstName": "Maxine",
        "fullName": "Rep. Waters, Maxine [D-CA-43]",
        "lastName": "Waters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FHA Small-Dollar Mortgages Act",
    "type": "HR",
    "updateDate": "2026-04-24T20:12:30Z",
    "updateDateIncludingText": "2026-04-24T20:12:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:05:45Z",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6774ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6774\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Waters introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo authorize the Secretary of Housing and Urban Development, acting through the Federal Housing Commissioner, to establish a pilot program to increase access to small-dollar mortgages, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FHA Small-Dollar Mortgages Act .\n#### 2. FHA small-dollar mortgages\n##### (a) In general\nNot later than 1 year after the date of the enactment of this section, the Secretary of Housing and Urban Development, acting through the Federal Housing Commissioner, may establish a pilot program to increase access to small-dollar mortgages for mortgagors which may include\u2014\n**(1)**\nauthorizing direct payments to mortgagees to incentivize the origination of small-dollar mortgages;\n**(2)**\nadjusting terms and costs imposed by the Federal Housing Administration with respect to small-dollar mortgages;\n**(3)**\nproviding direct grants for mortgagors who obtain small-dollar mortgages to cover costs associated with\u2014\n**(A)**\ndown payments;\n**(B)**\nclosing costs;\n**(C)**\nappraisals; and\n**(D)**\ntitle insurance;\n**(4)**\nconducting outreach to potential mortgagors about the availability of small-dollar mortgages; and\n**(5)**\nproviding technical assistance for mortgagees that originate small-dollar mortgages.\n##### (b) Report\nBeginning not later than 1 year after the establishment of the pilot program under subsection (a) and ending 1 year after the sunset of the pilot program, the Federal Housing Commissioner shall submit to the Congress an annual report that\u2014\n**(1)**\ntracks and evaluates the outcomes of small-dollar mortgages originated by mortgagees as a result of support provided under subsection (a);\n**(2)**\nanalyzes risks of the pilot program to the solvency of the Mutual Mortgage Insurance Fund;\n**(3)**\nincludes data with respect to\u2014\n**(A)**\nthe number of small-dollar mortgages originated in the 10-year period preceding the date of the enactment of this section, including small-dollar mortgages insured or guaranteed by the Federal Government and small-dollar mortgages not insured by the Federal Government;\n**(B)**\nthe original principal balance of each small-dollar mortgage identified under subparagraph (A);\n**(C)**\ndemographic information about the mortgagors associated with each such small-dollar mortgage; and\n**(D)**\nthe number and type of mortgagees that offer small-dollar mortgages;\n**(4)**\nprovides a description of the fixed costs that are associated with mortgages and the impact of such costs on the ability of lenders to earn a market rate return on small-dollar mortgages; and\n**(5)**\nincludes analysis, by regions of the United States, including rural regions, that identifies regions with the greatest need for, and the highest likelihood of, the origination of small-dollar mortgages and regions that could benefit the most from increased availability of small-dollar mortgages.\n##### (c) Sunset\nThe pilot program established under subsection (a) shall terminate on the date that is 4 years after the date on which the pilot program is established under subsection (a).\n##### (d) Expiration of authority\nAfter the expiration of the 3-year period beginning on the date of enactment of this section, neither the Federal Housing Commissioner nor the Secretary of Housing and Urban Development may newly establish a pilot program to increase access to small-dollar mortgages for mortgagors.\n##### (e) Small-Dollar mortgage defined\nThe term small-dollar mortgage means a mortgage that\u2014\n**(1)**\nhas an original principal balance of $100,000 or less; and\n**(2)**\nis secured by a 1- to 4-unit property that is the principal residence of the mortgagor.",
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
        "actionDate": "2026-03-16",
        "text": "Message on Senate action sent to the House."
      },
      "number": "6644",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "21st Century ROAD to Housing Act",
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
        "updateDate": "2026-04-24T20:12:30Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6774ih.xml"
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
      "title": "To authorize the Secretary of Housing and Urban Development, acting through the Federal Housing Commissioner, to establish a pilot program to increase access to small-dollar mortgages, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T08:01:12Z"
    },
    {
      "title": "FHA Small-Dollar Mortgages Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FHA Small-Dollar Mortgages Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T07:53:23Z"
    }
  ]
}
```
