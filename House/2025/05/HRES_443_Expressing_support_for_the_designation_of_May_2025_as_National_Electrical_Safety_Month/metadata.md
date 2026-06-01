# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/443?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/443
- Title: Expressing support for the designation of May 2025 as "National Electrical Safety Month".
- Congress: 119
- Bill type: HRES
- Bill number: 443
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-06-20T13:15:31Z
- Update date including text: 2025-06-20T13:15:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-23 - IntroReferral: Submitted in House
- 2025-05-23 - IntroReferral: Submitted in House
- Latest action: 2025-05-23: Submitted in House

## Actions

- 2025-05-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-23 - IntroReferral: Submitted in House
- 2025-05-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/443",
    "number": "443",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001326",
        "district": "5",
        "firstName": "Janelle",
        "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
        "lastName": "Bynum",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Expressing support for the designation of May 2025 as \"National Electrical Safety Month\".",
    "type": "HRES",
    "updateDate": "2025-06-20T13:15:31Z",
    "updateDateIncludingText": "2025-06-20T13:15:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres443ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 443\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Ms. Bynum (for herself and Mr. Bresnahan ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of May 2025 as National Electrical Safety Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Electrical Safety Month to raise awareness of electrical hazards in homes, schools, and workplaces and actions citizens may take to protect against such hazards;\n**(2)**\nencourages all citizens to observe the importance of establishing and practicing electrical safety habits in the home, school, and workplace to reduce the number of electrically related fires, injuries, and deaths;\n**(3)**\nsupports the efforts of the Electrical Safety Foundation to provide necessary and fundamental understanding of electrical hazards associated with emerging technologies; and\n**(4)**\nrequests that the President issue a proclamation calling upon citizens to observe the month with appropriate programs and activities.",
      "versionDate": "2025-05-23",
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
        "name": "Energy",
        "updateDate": "2025-06-20T13:15:31Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres443ih.xml"
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
      "title": "Expressing support for the designation of May 2025 as \"National Electrical Safety Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T10:03:19Z"
    },
    {
      "title": "Expressing support for the designation of May 2025 as \"National Electrical Safety Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-24T08:05:46Z"
    }
  ]
}
```
