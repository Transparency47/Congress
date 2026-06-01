# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/488?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/488
- Title: A resolution expressing the sense of the Senate regarding the European Union's actions to diversify from Russian energy sources.
- Congress: 119
- Bill type: SRES
- Bill number: 488
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-11-19T17:21:08Z
- Update date including text: 2025-11-19T17:21:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Referred to the Committee on Foreign Relations.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/488",
    "number": "488",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "A resolution expressing the sense of the Senate regarding the European Union's actions to diversify from Russian energy sources.",
    "type": "SRES",
    "updateDate": "2025-11-19T17:21:08Z",
    "updateDateIncludingText": "2025-11-19T17:21:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T20:55:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "NC"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "MS"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "DE"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "MD"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "IA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CO"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "KY"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "VA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "UT"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "TX"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres488is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 488\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mrs. Shaheen (for herself, Mr. Tillis , Mr. Wicker , Mr. Coons , Mr. Van Hollen , Mr. Grassley , Mr. Bennet , Mr. McConnell , Mr. Kaine , Mr. Curtis , Mr. Cornyn , and Ms. Rosen ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate regarding the European Union\u2019s actions to diversify from Russian energy sources.\nThat the Senate\u2014\n**(1)**\nwelcomes the European Union\u2019s commitment and actions\u2014\n**(A)**\nto end its dependence on Russian fossil fuels; and\n**(B)**\nto deny Vladimir Putin a critical source of revenue to continue funding Russia's war campaign in Ukraine;\n**(2)**\nwelcomes the Trump Administration\u2019s recent decision to sanction Rosneft and Lukoil and calls on United States allies and partners to terminate all contracts associated with both companies to avoid potential exposure to secondary sanctions;\n**(3)**\nencourages continued coordinated action among the United States and the Group of Seven countries, in addition to concerted action with the European Union and the United Kingdom to apply additional sanctions on Russian energy sources;\n**(4)**\nexpresses concern that Hungary has shown no sign of reducing its dependence on Russian fossil fuels;\n**(5)**\ncalls on Hungary and remaining consumers of Russian energy to fully adhere to the timeline agreed to in the REPowerEU initiative; and\n**(6)**\nunderscores continued bipartisan opposition to the Nord Stream I and II pipeline projects and any effort to revive them, regardless of the home country of individuals or entities involved.",
      "versionDate": "2025-11-06",
      "versionType": "IS"
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
        "name": "International Affairs",
        "updateDate": "2025-11-19T17:21:08Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres488is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing the sense of the Senate regarding the European Union's actions to diversify from Russian energy sources.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:27Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate regarding the European Union's actions to diversify from Russian energy sources.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T11:56:23Z"
    }
  ]
}
```
