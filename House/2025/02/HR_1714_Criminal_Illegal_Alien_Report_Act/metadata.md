# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1714?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1714
- Title: Criminal Illegal Alien Report Act
- Congress: 119
- Bill type: HR
- Bill number: 1714
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-03-18T14:40:40Z
- Update date including text: 2025-03-18T14:40:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1714",
    "number": "1714",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Criminal Illegal Alien Report Act",
    "type": "HR",
    "updateDate": "2025-03-18T14:40:40Z",
    "updateDateIncludingText": "2025-03-18T14:40:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-02-27T14:12:40Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1714ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1714\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Luttrell introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Secretary of Homeland Security to submit a report to Congress on crimes committed by individuals granted parole under the Immigration and Nationality Act.\n#### 1. Short title\nThis Act may be cited as the Criminal Illegal Alien Report Act .\n#### 2. Report on crimes committed by recipients of parole under the Immigration and Nationality Act\nNot later than 60 days after the date of enactment of this Act, the Secretary of Homeland Security shall submit to Congress a report on number of individuals who are present in the United States pursuant to a grant of parole under the Processes for Cubans, Haitians, Nicaraguans, and Venezuelans or any other grant of parole under section 212(d)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(5) ) who have committed crimes in the United States, including the nationalities of such individuals, and any ties of such individuals to terrorists and transnational criminal groups.",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-03-18T14:40:40Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1714ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Criminal Illegal Alien Report Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Criminal Illegal Alien Report Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Homeland Security to submit a report to Congress on crimes committed by individuals granted parole under the Immigration and Nationality Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:56Z"
    }
  ]
}
```
