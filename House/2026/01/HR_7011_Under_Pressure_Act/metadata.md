# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7011?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7011
- Title: Under Pressure Act
- Congress: 119
- Bill type: HR
- Bill number: 7011
- Origin chamber: House
- Introduced date: 2026-01-12
- Update date: 2026-04-24T19:14:44Z
- Update date including text: 2026-04-24T19:14:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-12: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-01-12: Introduced in House

## Actions

- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Introduced in House
- 2026-01-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-12",
    "latestAction": {
      "actionDate": "2026-01-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7011",
    "number": "7011",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Under Pressure Act",
    "type": "HR",
    "updateDate": "2026-04-24T19:14:44Z",
    "updateDateIncludingText": "2026-04-24T19:14:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-12",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-01-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-12",
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
          "date": "2026-01-12T17:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7011ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7011\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 12, 2026 Mr. Deluzio (for himself and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Administrator of the Federal Railroad Administration to submit to Congress a report on the rate and causes of rail tank car pressure relief device failures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Under Pressure Act .\n#### 2. Report on rail tank car pressure relief device failures\n##### (a) Report to Congress\nNot later than 18 months after the date of enactment of this Act, the Administrator of the Federal Railroad Administration shall submit to Congress a report that includes\u2014\n**(1)**\nthe rate and causes of rail tank car pressure relief device failures in a derailment event including information and variables relating to each event, including\u2014\n**(A)**\nthe number of tank cars involved in such derailment;\n**(B)**\nwhether or not the event included a fire;\n**(C)**\nin the case of a fire, the temperature and duration of the fire;\n**(D)**\nthe length of the time before, and circumstances of, the failure of a pressure relief device; and\n**(E)**\nwith respect to each pressure relief device that failed\u2014\n**(i)**\nan assessment of the compatibility of the device with each tank car commodity involved in such derailment;\n**(ii)**\nan assessment of the survivability of, and thermal protection for high heat conditions used on, the device; and\n**(iii)**\nidentification of each orientation of the device, including whether the orientation is\u2014\n**(I)**\nabove or below the vapor line; or\n**(II)**\nin the liquid space;\n**(2)**\nrecommendations to prevent rail tank car pressure relief device failures; and\n**(3)**\nthe status of any recommendations issued by the National Transportation Safety Board, including any recommendations issued during the period beginning on the date of enactment of this Act and ending on the date on which the Administrator initiates the report, on rail tank cars for which the respondent has not provided an acceptable response.\n##### (b) Consultation required\nIn developing the report under subsection (a), the Administrator shall consult with\u2014\n**(1)**\nthe Administrator of the Pipeline and Hazardous Materials Safety Administration;\n**(2)**\nrail employers;\n**(3)**\norganizations representing rail employees; and\n**(4)**\nrail tank car builders, shippers, and owners.",
      "versionDate": "2026-01-12",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-24T19:14:43Z"
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
      "date": "2026-01-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7011ih.xml"
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
      "title": "Under Pressure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T09:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Under Pressure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Federal Railroad Administration to submit to Congress a report on the rate and causes of rail tank car pressure relief device failures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T09:18:58Z"
    }
  ]
}
```
