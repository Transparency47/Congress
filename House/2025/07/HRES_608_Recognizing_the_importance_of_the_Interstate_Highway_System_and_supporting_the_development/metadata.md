# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/608?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/608
- Title: Recognizing the importance of the Interstate Highway System and supporting the development of an interstate through southern Ohio.
- Congress: 119
- Bill type: HRES
- Bill number: 608
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-10-07T08:05:15Z
- Update date including text: 2025-10-07T08:05:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-24 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-23: Submitted in House

## Actions

- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-24 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/608",
    "number": "608",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David J. [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Recognizing the importance of the Interstate Highway System and supporting the development of an interstate through southern Ohio.",
    "type": "HRES",
    "updateDate": "2025-10-07T08:05:15Z",
    "updateDateIncludingText": "2025-10-07T08:05:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:09:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-24T21:27:18Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres608ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 608\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Taylor submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nRecognizing the importance of the Interstate Highway System and supporting the development of an interstate through southern Ohio.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the importance of the Interstate Highway System;\n**(2)**\nrecognizes the economic boost and increased national security that an interstate could provide to a region; and\n**(3)**\nsupports the planning, designing, and development of an interstate in southern Ohio going south from Columbus, Ohio.",
      "versionDate": "2025-07-23",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-10T16:48:42Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres608ih.xml"
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
      "title": "Recognizing the importance of the Interstate Highway System and supporting the development of an interstate through southern Ohio.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:48:35Z"
    },
    {
      "title": "Recognizing the importance of the Interstate Highway System and supporting the development of an interstate through southern Ohio.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:06:36Z"
    }
  ]
}
```
