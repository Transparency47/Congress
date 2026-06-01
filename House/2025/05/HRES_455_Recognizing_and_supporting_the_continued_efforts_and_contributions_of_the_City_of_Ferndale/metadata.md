# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/455?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/455
- Title: Recognizing and supporting the continued efforts and contributions of the City of Ferndale to the LGBTQIA+ community of the State of Michigan.
- Congress: 119
- Bill type: HRES
- Bill number: 455
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-06-02T13:43:33Z
- Update date including text: 2025-06-02T13:43:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House
- Latest action: 2025-05-29: Submitted in House

## Actions

- 2025-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/455",
    "number": "455",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Recognizing and supporting the continued efforts and contributions of the City of Ferndale to the LGBTQIA+ community of the State of Michigan.",
    "type": "HRES",
    "updateDate": "2025-06-02T13:43:33Z",
    "updateDateIncludingText": "2025-06-02T13:43:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:02:10Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres455ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 455\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Ms. Stevens submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing and supporting the continued efforts and contributions of the City of Ferndale to the LGBTQIA+ community of the State of Michigan.\nThat the House of Representatives recognizes the City of Ferndale, its residents, businesses, and community support organizations for their significance in the LGBTQIA+ movement and for its continued dedication to creating a more equitable society.",
      "versionDate": "2025-05-29",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-06-02T13:43:33Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres455ih.xml"
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
      "title": "Recognizing and supporting the continued efforts and contributions of the City of Ferndale to the LGBTQIA+ community of the State of Michigan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T08:18:19Z"
    },
    {
      "title": "Recognizing and supporting the continued efforts and contributions of the City of Ferndale to the LGBTQIA+ community of the State of Michigan.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T08:05:25Z"
    }
  ]
}
```
