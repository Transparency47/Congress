# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3072?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3072
- Title: No Coffee Tax Act
- Congress: 119
- Bill type: S
- Bill number: 3072
- Origin chamber: Senate
- Introduced date: 2025-10-29
- Update date: 2025-12-09T20:01:49Z
- Update date including text: 2025-12-09T20:01:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-29: Introduced in Senate
- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-10-29: Introduced in Senate

## Actions

- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-29",
    "latestAction": {
      "actionDate": "2025-10-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3072",
    "number": "3072",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "No Coffee Tax Act",
    "type": "S",
    "updateDate": "2025-12-09T20:01:49Z",
    "updateDateIncludingText": "2025-12-09T20:01:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-29",
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
          "date": "2025-10-29T18:13:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "KY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "NH"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3072is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3072\nIN THE SENATE OF THE UNITED STATES\nOctober 29, 2025 Ms. Cortez Masto (for herself and Mr. Paul ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo prohibit the imposition of additional tariffs on coffee imported from countries to which the United States has extended normal trade relations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Coffee Tax Act .\n#### 2. Prohibition on additional tariffs on coffee products from countries with which the United States has normal trade relations\n##### (a) Maintenance of tariff rate for coffee products\nNotwithstanding any other provision of law or regulation imposing tariffs on a country-by-country basis, including any authority with respect to the imposition of tariffs under emergency situations, no tariff or other duty may be imposed in excess of the rate assessed as of January 19, 2025, with respect to any article described in subsection (b) that is imported to the United States from a country to which the United States has extended normal trade relations.\n##### (b) Article described\nAn article described in this subsection is any of the following:\n**(1)**\nCoffee, whether or not roasted or decaffeinated.\n**(2)**\nCoffee husks and skins.\n**(3)**\nCoffee substitutes containing coffee in any proportion.",
      "versionDate": "",
      "versionType": "Introduced in Senate"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-12-09T20:01:48Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3072is.xml"
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
      "title": "No Coffee Tax Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Coffee Tax Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the imposition of additional tariffs on coffee imported from countries to which the United States has extended normal trade relations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:20Z"
    }
  ]
}
```
