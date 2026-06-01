# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8776?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8776
- Title: Officer Wellness and Peer Support Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8776
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-27T05:53:26Z
- Update date including text: 2026-05-27T05:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8776",
    "number": "8776",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "G000602",
        "district": "4",
        "firstName": "Laura",
        "fullName": "Rep. Gillen, Laura [D-NY-4]",
        "lastName": "Gillen",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Officer Wellness and Peer Support Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-27T05:53:26Z",
    "updateDateIncludingText": "2026-05-27T05:53:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
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
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:00:35Z",
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
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8776ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8776\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Ms. Gillen (for herself and Mr. Rutherford ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require a report by the Attorney General on effective strategies and best practices to reduce stigma related to mental health among law enforcement officers.\n#### 1. Short title\nThis Act may be cited as the Officer Wellness and Peer Support Act of 2026 .\n#### 2. Report required\n##### (a) In general\nNot later than 270 days after the date of enactment of this Act, the Attorney General, in consultation with the Director of the Office of Community Oriented Policing Services, the Director of the Federal Bureau of Investigation, and the Director of the National Institute of Justice, shall submit to the Committees on the Judiciary of the House of Representatives and of the Senate a report setting forth\u2014\n**(1)**\neffective strategies and best practices to\u2014\n**(A)**\nreduce stigma related to mental health among law enforcement officers;\n**(B)**\nencourage law enforcement officers to access mental health screening, peer-to-peer counseling, and other resources related to mental health; and\n**(C)**\nensure the confidentiality of mental health services, including peer-to-peer counseling, critical incident stress debriefings, peer crisis lines, and employee assistance programs, for law enforcement officers; and\n**(2)**\nrecommendations for action to implement such strategies and best practices.\n##### (b) Consultation\nIn preparing the report under this section, the Attorney General, the Director of the Office of Community Oriented Policing Services, the Director of the Federal Bureau of Investigation, and the Director of the National Institute of Justice shall consult with relevant stakeholders including\u2014\n**(1)**\nFederal, State, Tribal and local law enforcement agencies; and\n**(2)**\nprofessional law enforcement organizations, local law enforcement labor and representative organizations, academic organizations, mental health and suicide prevention organizations, or such other entities as the Attorney General may determine appropriate.\n##### (c) Definition\nFor purposes of this Act, the term law enforcement officer means an individual involved in crime and juvenile delinquency control or reduction, or enforcement of the criminal laws (including juvenile delinquency), including, but not limited to, police, corrections, probation, parole, and judicial officers.",
      "versionDate": "2026-05-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8776ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Officer Wellness and Peer Support Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T05:53:26Z"
    },
    {
      "title": "Officer Wellness and Peer Support Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T05:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a report by the Attorney General on effective strategies and best practices to reduce stigma related to mental health among law enforcement officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T05:48:29Z"
    }
  ]
}
```
