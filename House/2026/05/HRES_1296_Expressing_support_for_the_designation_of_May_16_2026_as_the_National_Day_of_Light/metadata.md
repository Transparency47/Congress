# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1296?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1296
- Title: Expressing support for the designation of May 16, 2026, as the "National Day of Light".
- Congress: 119
- Bill type: HRES
- Bill number: 1296
- Origin chamber: House
- Introduced date: 2026-05-15
- Update date: 2026-05-22T10:18:33Z
- Update date including text: 2026-05-22T10:18:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-15: Introduced in House
- 2026-05-15 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2026-05-15 - IntroReferral: Submitted in House
- Latest action: 2026-05-15: Submitted in House

## Actions

- 2026-05-15 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2026-05-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-15",
    "latestAction": {
      "actionDate": "2026-05-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1296",
    "number": "1296",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M001206",
        "district": "25",
        "firstName": "Joseph",
        "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
        "lastName": "Morelle",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Expressing support for the designation of May 16, 2026, as the \"National Day of Light\".",
    "type": "HRES",
    "updateDate": "2026-05-22T10:18:33Z",
    "updateDateIncludingText": "2026-05-22T10:18:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-15",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-15",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
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
          "date": "2026-05-15T13:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1296ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1296\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2026 Mr. Morelle (for himself and Mr. Mast ) submitted the following resolution; which was referred to the Committee on Science, Space, and Technology\nRESOLUTION\nExpressing support for the designation of May 16, 2026, as the National Day of Light .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of a National Day of Light ;\n**(2)**\nrecognizes the continuing importance of the United States as the world leader in light-based science and technologies;\n**(3)**\nrecognizes the importance of inspiring the next generation of scientists, researchers, innovators, technicians, and entrepreneurs; and\n**(4)**\nencourages schools, community colleges, and universities to observe the day with appropriate activities.",
      "versionDate": "2026-05-15",
      "versionType": "IH"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1296ih.xml"
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
      "title": "Expressing support for the designation of May 16, 2026, as the \"National Day of Light\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:33Z"
    },
    {
      "title": "Expressing support for the designation of May 16, 2026, as the \"National Day of Light\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T08:08:35Z"
    }
  ]
}
```
