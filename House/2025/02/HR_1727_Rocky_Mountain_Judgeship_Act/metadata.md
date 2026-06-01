# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1727?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1727
- Title: Rocky Mountain Judgeship Act
- Congress: 119
- Bill type: HR
- Bill number: 1727
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-02-11T15:03:45Z
- Update date including text: 2026-02-11T15:03:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1727",
    "number": "1727",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Rocky Mountain Judgeship Act",
    "type": "HR",
    "updateDate": "2026-02-11T15:03:45Z",
    "updateDateIncludingText": "2026-02-11T15:03:45Z"
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
          "date": "2025-02-27T14:12:35Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "ID"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1727ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1727\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Neguse (for himself, Mr. Simpson , and Mr. Fulcher ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize additional district judgeships for the districts of Colorado and Idaho.\n#### 1. Short title\nThis Act may be cited as the Rocky Mountain Judgeship Act .\n#### 2. Additional district judgeships for the districts of Colorado and Idaho\n##### (a) Colorado\nThe President shall appoint, by and with the advice and consent of the Senate, 2 additional district judges for the district of Colorado.\n##### (b) Idaho\nThe President shall appoint, by and with the advice and consent of the Senate, 1 additional district judges for the district of Idaho.\n##### (c) Technical and conforming amendments\nThe table in section 133(a) of title 28, United States Code, is amended\u2014\n**(1)**\nby striking the item relating to Colorado and inserting the following:\nColorado 9 ; and\n**(2)**\nby striking the item relating to Idaho and inserting the following:\nIdaho 3 .\n#### 3. Colorado\nSection 85 of title 28, United States Code, is amended by striking and Sterling and inserting Sterling, and Fort Collins .",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Colorado",
            "updateDate": "2026-02-11T15:03:26Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2026-02-11T15:03:44Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2026-02-11T15:03:32Z"
          },
          {
            "name": "Judges",
            "updateDate": "2026-02-11T15:03:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-03-21T13:38:02Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1727ih.xml"
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
      "title": "Rocky Mountain Judgeship Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T15:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rocky Mountain Judgeship Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize additional district judgeships for the districts of Colorado and Idaho.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T15:18:22Z"
    }
  ]
}
```
