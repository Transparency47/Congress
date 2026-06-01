# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2924?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2924
- Title: NATO Burden Sharing Enforcement Act
- Congress: 119
- Bill type: HR
- Bill number: 2924
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-05-20T14:06:44Z
- Update date including text: 2025-05-20T14:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2924",
    "number": "2924",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "NATO Burden Sharing Enforcement Act",
    "type": "HR",
    "updateDate": "2025-05-20T14:06:44Z",
    "updateDateIncludingText": "2025-05-20T14:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
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
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:34:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2924ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2924\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the Secretary of State to discontinue granting visas to nationals of countries failing to meet their North Atlantic Treaty Organization obligations to spend at least 2 percent of its gross domestic product on national defense, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NATO Burden Sharing Enforcement Act .\n#### 2. Discontinuing granting visas to nationals of country failing to meet NATO obligations\nSection 243(d) of the Immigration and Nationality Act ( 8 U.S.C. 1253(d) ) is amended\u2014\n**(1)**\nin the heading, by inserting or failing to meet NATO obligations after Accepting Aliens ;\n**(2)**\nby striking Attorney General each place it appears and inserting Secretary of Homeland Security ;\n**(3)**\nby inserting after the alien under this section, the following: or that the government of a foreign country that is a member of the North Atlantic Treaty Organization does not spend at least 2 percent of its gross domestic product on national defense, ; and\n**(4)**\nby striking Secretary that and inserting Secretary of State that .",
      "versionDate": "2025-04-17",
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
        "updateDate": "2025-05-20T14:06:44Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2924ih.xml"
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
      "title": "NATO Burden Sharing Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NATO Burden Sharing Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of State to discontinue granting visas to nationals of countries failing to meet their North Atlantic Treaty Organization obligations to spend at least 2 percent of its gross domestic product on national defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:37Z"
    }
  ]
}
```
