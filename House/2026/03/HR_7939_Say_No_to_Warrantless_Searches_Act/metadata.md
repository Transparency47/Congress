# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7939?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7939
- Title: Say No to Warrantless Searches Act
- Congress: 119
- Bill type: HR
- Bill number: 7939
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-04-02T19:20:10Z
- Update date including text: 2026-04-02T19:20:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7939",
    "number": "7939",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000581",
        "district": "34",
        "firstName": "Vicente",
        "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
        "lastName": "Gonzalez",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Say No to Warrantless Searches Act",
    "type": "HR",
    "updateDate": "2026-04-02T19:20:10Z",
    "updateDateIncludingText": "2026-04-02T19:20:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
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
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:01:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7939ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7939\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Vicente Gonzalez of Texas introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo ensure rights under the Fourth Amendment to the Constitution are protected during immigration enforcement actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Say No to Warrantless Searches Act .\n#### 2. Fourth amendment protections\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended by adding at the end the following:\n(i) (1) A Federal law enforcement officer engaging in immigration enforcement activity may not conduct a search of private property without obtaining a judicial warrant prior to such search, except as provided in paragraph (2). (2) Paragraph (1) shall not apply in the case of\u2014 (A) lawfully obtained consent; or (B) exigent circumstances. (3) Nothing in this subsection shall be used to establish that the protections of the Fourth Amendment to the Constitution did not apply to enforcement activity conducted pursuant to this section before the date of enactment of this subsection. .",
      "versionDate": "2026-03-16",
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
        "updateDate": "2026-04-02T19:20:10Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7939ih.xml"
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
      "title": "Say No to Warrantless Searches Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Say No to Warrantless Searches Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure rights under the Fourth Amendment to the Constitution are protected during immigration enforcement actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-01T07:18:24Z"
    }
  ]
}
```
