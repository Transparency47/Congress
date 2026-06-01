# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1945?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1945
- Title: Energy Choice Act
- Congress: 119
- Bill type: S
- Bill number: 1945
- Origin chamber: Senate
- Introduced date: 2025-06-04
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in Senate
- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-06-04: Introduced in Senate

## Actions

- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1945",
    "number": "1945",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "J000312",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Justice, James C. [R-WV]",
        "lastName": "Justice",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Energy Choice Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-04",
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
        "item": [
          {
            "date": "2025-06-04T17:34:37Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-04T17:34:37Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "AL"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "WV"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "FL"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "KS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "ID"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1945is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1945\nIN THE SENATE OF THE UNITED STATES\nJune 4, 2025 Mr. Justice (for himself, Mr. Tuberville , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo prohibit States and local governments from prohibiting or limiting the connection, reconnection, modification, installation, transportation, distribution, or expansion of an energy service based on the type or source of energy to be delivered, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energy Choice Act .\n#### 2. Definition of energy\nIn this Act, the term energy includes\u2014\n**(1)**\nnatural gas;\n**(2)**\nrenewable natural gas;\n**(3)**\nhydrogen;\n**(4)**\nliquified petroleum gas;\n**(5)**\nrenewable liquified petroleum gas;\n**(6)**\nother liquid petroleum products;\n**(7)**\nbiomass-based diesel fuels and renewable fuels; and\n**(8)**\nelectricity.\n#### 3. Limitation on regulation of energy choice\nA State or local government, including any instrumentality or regulatory agency of a State or local government, may not adopt, implement, or enforce a law, regulation, ordinance, building code, standard, or policy that prohibits or limits, or has the effect of directly or indirectly prohibiting or limiting, the connection, reconnection, modification, installation, transportation, distribution, or expansion of, or access to, an energy service based on the type or source of energy sold in interstate commerce to be delivered to an end-user of that energy service.",
      "versionDate": "2025-06-04",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2025-12-10T18:36:55Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2025-12-10T18:36:55Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-12-10T18:36:55Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-12-10T18:36:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-06-23T14:17:50Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1945is.xml"
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
      "title": "Energy Choice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Energy Choice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit States and local governments from prohibiting or limiting the connection, reconnection, modification, installation, transportation, distribution, or expansion of an energy service based on the type or source of energy to be delivered, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T02:48:22Z"
    }
  ]
}
```
