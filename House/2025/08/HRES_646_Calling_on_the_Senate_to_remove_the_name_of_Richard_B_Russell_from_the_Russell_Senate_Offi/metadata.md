# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/646?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/646
- Title: Calling on the Senate to remove the name of Richard B. Russell from the Russell Senate Office Building.
- Congress: 119
- Bill type: HRES
- Bill number: 646
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-10-07T08:05:35Z
- Update date including text: 2025-10-07T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-08 - IntroReferral: Submitted in House
- 2025-08-08 - IntroReferral: Submitted in House
- 2025-08-09 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-08-08: Submitted in House

## Actions

- 2025-08-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-08 - IntroReferral: Submitted in House
- 2025-08-08 - IntroReferral: Submitted in House
- 2025-08-09 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/646",
    "number": "646",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Calling on the Senate to remove the name of Richard B. Russell from the Russell Senate Office Building.",
    "type": "HRES",
    "updateDate": "2025-10-07T08:05:35Z",
    "updateDateIncludingText": "2025-10-07T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-09",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:32:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-09T21:34:15Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres646ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 646\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Green of Texas submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nCalling on the Senate to remove the name of Richard B. Russell from the Russell Senate Office Building.\nThat the House of Representatives\u2014\n**(1)**\nonce again rejects White nationalism and White supremacy as hateful expressions of intolerance that are contradictory to the values that define the people of the United States;\n**(2)**\ncondemns the use of captions, statutes, memorials, and artwork used or erected to memorialize Senator Richard B. Russell, or any other lawmaker who intentionally disavowed the Declaration of Independence\u2019s exhortation that all persons are created equal; and\n**(3)**\ncalls on the Senate to remove the name of Richard B. Russell from the Russell Senate Office Building and to revert to using the building\u2019s original name, the Old Senate Office Building, until the Senate finds a suitable honoree.",
      "versionDate": "2025-08-08",
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
        "name": "Congress",
        "updateDate": "2025-09-18T19:39:40Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres646ih.xml"
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
      "title": "Calling on the Senate to remove the name of Richard B. Russell from the Russell Senate Office Building.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T08:19:09Z"
    },
    {
      "title": "Calling on the Senate to remove the name of Richard B. Russell from the Russell Senate Office Building.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T08:05:36Z"
    }
  ]
}
```
