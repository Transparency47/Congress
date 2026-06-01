# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/112
- Title: Expressing support for the designation of February 5, 2025, as "National Prosecutors Day".
- Congress: 119
- Bill type: HRES
- Bill number: 112
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-06-09T17:41:36Z
- Update date including text: 2025-06-09T17:41:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-05 - Committee: Submitted in House
- Latest action: 2025-02-05: Submitted in House

## Actions

- 2025-02-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-05 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/112",
    "number": "112",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of February 5, 2025, as \"National Prosecutors Day\".",
    "type": "HRES",
    "updateDate": "2025-06-09T17:41:36Z",
    "updateDateIncludingText": "2025-06-09T17:41:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-05T15:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NE"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres112ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 112\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Panetta (for himself, Mr. Bacon , Mr. Neguse , and Mr. Baird ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nExpressing support for the designation of February 5, 2025, as National Prosecutors Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of a National Prosecutors Day ;\n**(2)**\ncalls upon all residents to join in recognizing the vital work these public servants partake in to maintain justice and ensure safety among our communities; and\n**(3)**\nurges State, Tribal, and local governments to\u2014\n**(A)**\nspread awareness and promote the existence of National Prosecutors Day and appreciation for the role of prosecutors in our communities; and\n**(B)**\neducate the public about the integral role of prosecutors and the judicial system as a whole play in ensuring community safety and prosperity.",
      "versionDate": "2025-02-05",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-09T17:41:26Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-09T17:41:36Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-06-09T17:41:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-14T13:50:24Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres112ih.xml"
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
      "title": "Expressing support for the designation of February 5, 2025, as \"National Prosecutors Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T12:33:18Z"
    },
    {
      "title": "Expressing support for the designation of February 5, 2025, as \"National Prosecutors Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T09:06:10Z"
    }
  ]
}
```
