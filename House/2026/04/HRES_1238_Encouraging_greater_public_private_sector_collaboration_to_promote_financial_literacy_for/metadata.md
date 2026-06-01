# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1238
- Title: Encouraging greater public-private sector collaboration to promote financial literacy for students and young adults.
- Congress: 119
- Bill type: HRES
- Bill number: 1238
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-15T18:51:07Z
- Update date including text: 2026-05-15T18:51:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-30 - IntroReferral: Submitted in House
- Latest action: 2026-04-30: Submitted in House

## Actions

- 2026-04-30 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1238",
    "number": "1238",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Encouraging greater public-private sector collaboration to promote financial literacy for students and young adults.",
    "type": "HRES",
    "updateDate": "2026-05-15T18:51:07Z",
    "updateDateIncludingText": "2026-05-15T18:51:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionCode": "1025",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
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
          "date": "2026-04-30T13:02:20Z",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "OH"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "OR"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1238ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1238\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Foster (for himself, Ms. Vel\u00e1zquez , Mrs. Beatty , and Ms. Bynum ) submitted the following resolution; which was referred to the Committee on Financial Services\nRESOLUTION\nEncouraging greater public-private sector collaboration to promote financial literacy for students and young adults.\nThat the House of Representatives\u2014\n**(1)**\nemphasizes the importance of raising awareness of individual financial capability by providing relevant information, financial workshops, and other decision making tools to consumers of all ages;\n**(2)**\nreaffirms the purposes of section 342 of the Dodd-Frank Act ( 12 U.S.C. 5452 ), which directs Federal financial agencies to partner with organizations that are focused on developing opportunities for minorities and women to place talented young minorities and women in industry internships, summer employment, and full-time positions;\n**(3)**\nsupports the efforts of the Bureau of Consumer Finance Protection to provide consumers with relevant information and decision making tools regarding important financial decisions; and\n**(4)**\nurges the Department of the Treasury to consult with the Financial Industry Regulatory Authority and implement future national financial capability studies.",
      "versionDate": "2026-04-30",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-05-15T18:51:07Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1238ih.xml"
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
      "title": "Encouraging greater public-private sector collaboration to promote financial literacy for students and young adults.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-04T13:48:29Z"
    },
    {
      "title": "Encouraging greater public-private sector collaboration to promote financial literacy for students and young adults.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T08:09:00Z"
    }
  ]
}
```
