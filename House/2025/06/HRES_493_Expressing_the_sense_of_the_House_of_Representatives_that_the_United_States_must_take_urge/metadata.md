# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/493?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/493
- Title: Expressing the sense of the House of Representatives that the United States must take urgent, coordinated action to address the national housing crisis through preservation and production of affordable housing.
- Congress: 119
- Bill type: HRES
- Bill number: 493
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2026-01-22T09:06:13Z
- Update date including text: 2026-01-22T09:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-06-10 - IntroReferral: Submitted in House
- 2025-06-10 - IntroReferral: Submitted in House
- Latest action: 2025-06-10: Submitted in House

## Actions

- 2025-06-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-06-10 - IntroReferral: Submitted in House
- 2025-06-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/493",
    "number": "493",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001313",
        "district": "11",
        "firstName": "Shontel",
        "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
        "lastName": "Brown",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Expressing the sense of the House of Representatives that the United States must take urgent, coordinated action to address the national housing crisis through preservation and production of affordable housing.",
    "type": "HRES",
    "updateDate": "2026-01-22T09:06:13Z",
    "updateDateIncludingText": "2026-01-22T09:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
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
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-06-10T14:00:15Z",
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
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
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
      "sponsorshipDate": "2025-06-23",
      "state": "DC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "AZ"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CT"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "OH"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NV"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres493ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 493\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Ms. Brown (for herself and Mrs. Beatty ) submitted the following resolution; which was referred to the Committee on Financial Services\nRESOLUTION\nExpressing the sense of the House of Representatives that the United States must take urgent, coordinated action to address the national housing crisis through preservation and production of affordable housing.\nThat the House of Representatives\u2014\n**(1)**\naffirms that housing is a foundational human need and economic necessity, and that the housing crisis is a national emergency;\n**(2)**\nsupports comprehensive Federal, State, and local efforts to increase the supply of deeply affordable rental housing and preserve existing units;\n**(3)**\nurges Congress to prioritize supporting rental assistance, housing preservation, and affordable housing development programs;\n**(4)**\nencourages private and nonprofit sector partners to invest in sensible housing solutions and collaborate on innovative, community-based models that are responsive to community needs;\n**(5)**\ncalls on policy makers across all levels of government to align housing, zoning, and infrastructure policies in support of affordability, availability, and preservation; and\n**(6)**\ncommits to advancing solutions that ensure safe, affordable housing for all individuals, families, and communities across the United States.",
      "versionDate": "2025-06-10",
      "versionType": "IH"
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
        "updateDate": "2025-07-31T11:41:53Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres493ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Expressing the sense of the House of Representatives that the United States must take urgent, coordinated action to address the national housing crisis through preservation and production of affordable housing.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing the sense of the House of Representatives that the United States must take urgent, coordinated action to address the national housing crisis through preservation and production of affordable housing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T08:18:25Z"
    }
  ]
}
```
