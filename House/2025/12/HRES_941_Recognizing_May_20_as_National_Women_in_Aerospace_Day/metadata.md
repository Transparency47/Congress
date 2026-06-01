# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/941?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/941
- Title: Recognizing May 20 as "National Women in Aerospace Day".
- Congress: 119
- Bill type: HRES
- Bill number: 941
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2025-12-15T16:33:45Z
- Update date including text: 2025-12-15T16:33:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-12-10 - IntroReferral: Submitted in House
- 2025-12-10 - IntroReferral: Submitted in House
- Latest action: 2025-12-10: Submitted in House

## Actions

- 2025-12-10 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-12-10 - IntroReferral: Submitted in House
- 2025-12-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/941",
    "number": "941",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Recognizing May 20 as \"National Women in Aerospace Day\".",
    "type": "HRES",
    "updateDate": "2025-12-15T16:33:45Z",
    "updateDateIncludingText": "2025-12-15T16:33:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:00:20Z",
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
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres941ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 941\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mrs. Foushee (for herself and Mr. Haridopolos ) submitted the following resolution; which was referred to the Committee on Science, Space, and Technology\nRESOLUTION\nRecognizing May 20 as National Women in Aerospace Day .\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the celebration of National Women in Aerospace Day as a time to reflect on the many notable contributions that women have made to the field of aerospace in the United States;\n**(2)**\nurges the people of the United States to observe National Women in Aerospace Day with appropriate programs and activities; and\n**(3)**\naffirms the commitment of the House of Representatives to ensuring that all women have equal access to opportunity in the aerospace field.",
      "versionDate": "2025-12-10",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-15T16:33:45Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres941ih.xml"
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
      "title": "Recognizing May 20 as \"National Women in Aerospace Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-12T13:04:21Z"
    },
    {
      "title": "Recognizing May 20 as \"National Women in Aerospace Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T09:07:33Z"
    }
  ]
}
```
