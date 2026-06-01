# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/27?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/27
- Title: Expressing opposition to Central Business District Tolling Program of New York City.
- Congress: 119
- Bill type: HRES
- Bill number: 27
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-01-13T12:51:00Z
- Update date including text: 2025-01-13T12:51:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - Committee: 
- 2025-01-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-09 - Committee: Submitted in House
- 2025-01-09 - IntroReferral: Submitted in House
- Latest action: 2025-01-09: Submitted in House

## Actions

- 2025-01-09 - Committee: 
- 2025-01-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-09 - Committee: Submitted in House
- 2025-01-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/27",
    "number": "27",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Expressing opposition to Central Business District Tolling Program of New York City.",
    "type": "HRES",
    "updateDate": "2025-01-13T12:51:00Z",
    "updateDateIncludingText": "2025-01-13T12:51:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres27ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 27\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. LaLota (for himself, Mr. Garbarino , Ms. Malliotakis , and Mr. Lawler ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing opposition to Central Business District Tolling Program of New York City.\nThat the House of Representatives\u2014\n**(1)**\ndisapproves of Central Business District Tolling Program of New York City;\n**(2)**\nacknowledges the severe economic burden the proposed Central Business District Tolling Program would pose on small businesses and strongly recommends the State of New York conducts, and makes publicly available, an economic impact report on such Program; and\n**(3)**\nstrongly recommends that relevant Federal agencies and the State of New York halt implementation of the Central Business District Tolling Program.",
      "versionDate": "2025-01-09",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-01-10T15:20:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hres27",
          "measure-number": "27",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-01-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres27v00",
            "update-date": "2025-01-13"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution disapproves of the Central Business District Tolling Program of New York City and strongly recommends that (1) New York conduct an economic impact report on the program, and (2) relevant federal agencies and New York halt the program's implementation. The tolling program, also known as congestion pricing, will charge drivers a toll to enter an area designated as Manhattan's central business district.</p>"
        },
        "title": "Expressing opposition to Central Business District Tolling Program of New York City."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres27.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution disapproves of the Central Business District Tolling Program of New York City and strongly recommends that (1) New York conduct an economic impact report on the program, and (2) relevant federal agencies and New York halt the program's implementation. The tolling program, also known as congestion pricing, will charge drivers a toll to enter an area designated as Manhattan's central business district.</p>",
      "updateDate": "2025-01-13",
      "versionCode": "id119hres27"
    },
    "title": "Expressing opposition to Central Business District Tolling Program of New York City."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution disapproves of the Central Business District Tolling Program of New York City and strongly recommends that (1) New York conduct an economic impact report on the program, and (2) relevant federal agencies and New York halt the program's implementation. The tolling program, also known as congestion pricing, will charge drivers a toll to enter an area designated as Manhattan's central business district.</p>",
      "updateDate": "2025-01-13",
      "versionCode": "id119hres27"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres27ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing opposition to Central Business District Tolling Program of New York City.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-10T09:18:17Z"
    },
    {
      "title": "Expressing opposition to Central Business District Tolling Program of New York City.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:16Z"
    }
  ]
}
```
