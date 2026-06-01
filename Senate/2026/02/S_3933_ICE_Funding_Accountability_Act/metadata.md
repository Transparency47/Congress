# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3933?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3933
- Title: ICE Funding Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 3933
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-03-24T11:03:18Z
- Update date including text: 2026-03-24T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3933",
    "number": "3933",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "ICE Funding Accountability Act",
    "type": "S",
    "updateDate": "2026-03-24T11:03:18Z",
    "updateDateIncludingText": "2026-03-24T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": [
          {
            "name": "Energy and Natural Resources Committee",
            "systemCode": "sseg00"
          },
          {
            "name": "Homeland Security and Governmental Affairs Committee",
            "systemCode": "ssga00"
          }
        ]
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T18:00:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3933is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3933\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Mr. Kim introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit funds from the One Big Beautiful Bill Act from being used to recruit or hire new immigration enforcement agents or officers at ICE or CBP.\n#### 1. Short title\nThis Act may be cited as the ICE Funding Accountability Act .\n#### 2. Spending limitation\nNotwithstanding any other provision of law, amounts appropriated or otherwise made available under Public Law 119\u201321 may not be expended\u2014\n**(1)**\nto pay the salaries of agents or officers of U.S. Immigration and Customs Enforcement or U.S. Customs and Border Protection who were hired on or after the date of the enactment of this Act; or\n**(2)**\nto recruit, advertise for hiring, or pay retention or sign on bonuses to such agents or officers.",
      "versionDate": "2026-02-26",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2026-03-16T18:39:43Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3933is.xml"
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
      "title": "ICE Funding Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ICE Funding Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-14T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit funds from the One Big Beautiful Bill Act from being used to recruit or hire new immigration enforcement agents or officers at ICE or CBP.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-14T03:48:26Z"
    }
  ]
}
```
