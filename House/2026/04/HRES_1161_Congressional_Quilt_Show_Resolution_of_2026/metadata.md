# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1161?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1161
- Title: Congressional Quilt Show Resolution of 2026
- Congress: 119
- Bill type: HRES
- Bill number: 1161
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-04-14T19:01:56Z
- Update date including text: 2026-04-14T19:01:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-04-09 - IntroReferral: Submitted in House
- Latest action: 2026-04-09: Submitted in House

## Actions

- 2026-04-09 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-04-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1161",
    "number": "1161",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Congressional Quilt Show Resolution of 2026",
    "type": "HRES",
    "updateDate": "2026-04-14T19:01:56Z",
    "updateDateIncludingText": "2026-04-14T19:01:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
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
          "date": "2026-04-09T15:32:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1161ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1161\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Ms. Perez (for herself, Mr. Moran , and Ms. Van Duyne ) submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nExpressing support for the establishment of a Congressional Quilt Show to recognize and honor American quilters and their craftsmanship in the Nation for over 250 years.\n#### 1. Short title\nThis resolution may be cited as the Congressional Quilt Show Resolution of 2026 .\n#### 2. Findings\nThe House of Representatives finds the following:\n**(1)**\nThe American quilting community are persistent, inter-generational stewards of craft, memory, and skill in our Nation.\n**(2)**\nSince before the Nation\u2019s founding, the rigor and joy of quilting and needlework have ushered Americans, predominantly women and girls, to learn the muscle and union of beauty and function and embody the utility and necessity of visual and mathematical intelligence.\n**(3)**\nCongressional investment will aid American quilters in their work to uphold high standards of skill and ingenuity, and build community across the country.\n**(4)**\nIt is the intent of the House of Representatives to celebrate the important role American quilters play is keeping our Nation warm, sharp, self-sufficient, and generous.\n**(5)**\nBringing together Members of Congress and their constituents to participate in activities that will result in a deeper appreciation for quilting will foster cultural pride and affirm the value of craftsmanship as a national asset.\n#### 3. Congressional quilt show\n##### (a) Establishment of showcase\nThere is hereby established a congressional quilting showcase, which shall be administered by lottery and held each year among eligible constituents in each congressional district.\n##### (b) Regulations\nThe showcase under this resolution shall be carried out in accordance with such regulations as may be prescribed by the Committee on House Administration.\n##### (c) Display\nThe Architect of the Capitol shall display each quilt outside the respective congressional office in the House of Representatives.\n##### (d) Eligible constituent defined\nIn this section, the term eligible constituent means an individual who has won a ribbon from a county fair, or received similar recognition, within their respective congressional district.",
      "versionDate": "2026-04-09",
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
        "name": "Congress",
        "updateDate": "2026-04-14T19:01:56Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1161ih.xml"
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
      "title": "Congressional Quilt Show Resolution of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Quilt Show Resolution of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the establishment of a Congressional Quilt Show to recognize and honor American quilters and their craftsmanship in the Nation for over 250 years.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T08:18:37Z"
    }
  ]
}
```
