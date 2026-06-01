# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1307?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1307
- Title: Commemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.
- Congress: 119
- Bill type: HRES
- Bill number: 1307
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-29T16:37:50Z
- Update date including text: 2026-05-29T16:37:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - IntroReferral: Submitted in House
- Latest action: 2026-05-20: Submitted in House

## Actions

- 2026-05-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1307",
    "number": "1307",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Commemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.",
    "type": "HRES",
    "updateDate": "2026-05-29T16:37:50Z",
    "updateDateIncludingText": "2026-05-29T16:37:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
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
          "date": "2026-05-20T15:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "HI"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "MP"
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
      "sponsorshipDate": "2026-05-20",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1307ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1307\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2026 Ms. Tokuda (for herself, Mr. Case , Ms. King-Hinds , and Mr. Moylan ) submitted the following resolution; which was referred to the Committee on Agriculture\nRESOLUTION\nCommemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.\nThat the House of Representatives\u2014\n**(1)**\ncommemorates the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry (referred to in this resolution as the IPIF );\n**(2)**\nrecognizes the vital contributions that the research conducted and data produced by the IPIF have provided to the United States in understanding the ecosystems of the Pacific region;\n**(3)**\nacknowledges the importance of having the IPIF located on Hawaii Island; and\n**(4)**\nreaffirms the strong support of the House of Representatives for the critical ongoing operations of the IPIF and its staff.",
      "versionDate": "2026-05-20",
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
        "name": "Environmental Protection",
        "updateDate": "2026-05-29T16:37:50Z"
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
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1307ih.xml"
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
      "title": "Commemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T02:33:34Z"
    },
    {
      "title": "Commemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:07:49Z"
    }
  ]
}
```
