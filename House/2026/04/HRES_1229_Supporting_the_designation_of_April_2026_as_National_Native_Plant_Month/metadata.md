# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1229
- Title: Supporting the designation of April 2026 as "National Native Plant Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1229
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-14T18:50:07Z
- Update date including text: 2026-05-14T18:50:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-29 - IntroReferral: Submitted in House
- Latest action: 2026-04-29: Submitted in House

## Actions

- 2026-04-29 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1229",
    "number": "1229",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000604",
        "district": "2",
        "firstName": "Maggie",
        "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
        "lastName": "Goodlander",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Supporting the designation of April 2026 as \"National Native Plant Month\".",
    "type": "HRES",
    "updateDate": "2026-05-14T18:50:07Z",
    "updateDateIncludingText": "2026-05-14T18:50:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
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
          "date": "2026-04-29T13:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "OH"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "LA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "GU"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
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
      "sponsorshipDate": "2026-04-30",
      "state": "HI"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "OH"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1229ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1229\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Ms. Goodlander (for herself, Mr. Joyce of Ohio , Mr. Carter of Louisiana , Mr. Moylan , and Mr. Neguse ) submitted the following resolution; which was referred to the Committee on Natural Resources\nRESOLUTION\nSupporting the designation of April 2026 as National Native Plant Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Native Plant Month ; and\n**(2)**\nrecognizes the benefits of native plants to the environment and economy of the United States.",
      "versionDate": "2026-04-29",
      "versionType": "IH"
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
        "actionDate": "2025-03-21",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "233",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the designation of April 2025 as \"National Native Plant Month\".",
      "type": "HRES"
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-14T18:50:07Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1229ih.xml"
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
      "title": "Supporting the designation of April 2026 as \"National Native Plant Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T06:48:32Z"
    },
    {
      "title": "Supporting the designation of April 2026 as \"National Native Plant Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T08:06:50Z"
    }
  ]
}
```
