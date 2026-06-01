# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2742?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2742
- Title: DOGE Accountability and Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 2742
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-05-08T17:59:54Z
- Update date including text: 2025-05-08T17:59:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2742",
    "number": "2742",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001190",
        "district": "10",
        "firstName": "Bradley",
        "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
        "lastName": "Schneider",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "DOGE Accountability and Transparency Act",
    "type": "HR",
    "updateDate": "2025-05-08T17:59:54Z",
    "updateDateIncludingText": "2025-05-08T17:59:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MA"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "VA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2742ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2742\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Schneider (for himself and Mr. Lynch ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prevent fraud, waste, and abuse by requiring the Administrator of the United States Department of Government Efficiency Service to provide weekly reports to Congress regarding changes DOGE has made to any Federal agency and the realized impacts of such changes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DOGE Accountability and Transparency Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress has a responsibility to review, monitor, supervise, and evaluate the actions of the executive branch to provide effective oversight as a co-equal branch of Government.\n**(2)**\nThe authority of the Congress to provide oversight and obtain information from the executive branch is firmly established and essential to its legislative function derived from Article I of the Constitution.\n**(3)**\nThe Legislative Reorganization Act of 1946 established that \u201ceach standing committee of the Senate and the House of Representatives shall exercise continuous watchfulness of the execution by the administrative agencies concerned of any laws, the subject matter of which is within the jurisdiction of such committee; and, for that purpose, shall study all pertinent reports and data submitted to the Congress by the agencies in the executive branch of the Government.\u201d\n**(4)**\nOn January 20, 2025, President Donald Trump issued an executive order to reorganize the U.S. Digital Service as the U.S. Department of Government Efficiency (DOGE) Service and directs DOGE to \u201cimplement the President\u2019s DOGE Agenda, by monitoring Federal technology and software to maximize governmental efficiency and productivity.\u201d\n**(5)**\nDOGE has pushed for large-scale reductions in force and office closures (often arbitrarily and capriciously), which will have a significant adverse impact on the ability of agencies to serve citizens of the United States.\n**(6)**\nReductions in Force (RIFs) and scaling back, or completely eliminating programs at Federal agencies should be based on real and transparent analysis and formal, deliberate program evaluation, not for the purposes of pursuing personal vendettas or yielding personal financial gain for well-connected individuals.\n**(7)**\nThe illogical and erratic, chainsaw approach of DOGE has sown confusion and chaos for employees at Federal agencies and the citizens of the United States alike.\n**(8)**\nThe citizens of the United States expect and deserve ongoing transparency of the actions of the Federal Government, particularly when their personal, private data is concerned.\n#### 3. Department of Government Efficiency activity and impact reports\n##### (a) Weekly report\nNot later than 1 week after the date of the enactment of this Act, and weekly thereafter, the Administrator of the United States Department of Government Efficiency Service shall provide to Congress a report regarding any action DOGE has taken with respect to each Federal agency and the cumulative impact of actions taken to date, including the following:\n**(1)**\nEach statutory authorization supporting each such change.\n**(2)**\nAny change in the number of employees at the respective Federal agency, including any employee that has resigned, been removed, or had their position eliminated.\n**(3)**\nA description of each specific change DOGE has made to the respective Federal agency, including to an office within such agency.\n**(4)**\nAny cost-saving measure.\n**(5)**\nAny policy change.\n**(6)**\nAny physical change to a Federal agency structure or location, including moving a Federal agency to a different building and relocating employees.\n**(7)**\nA description of any Federal agency data accessed by DOGE, the name of the individual who accessed such data, the purpose for such access, and what was done with such data.\n**(8)**\nThe realized versus expected benefits of DOGE actions to date.\n##### (b) Initial report\nNot later than 1 week after the date of the enactment of this Act, the Administrator shall submit to Congress a report of any DOGE activity listed under subsection (a) that occurred between January 20, 2025, and the date of the enactment of this Act.\n##### (c) Definitions\nIn this section:\n**(1) DOGE**\nThe term DOGE means the United States DOGE Service (commonly referred to as the Department of Government Efficiency).\n**(2) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code.",
      "versionDate": "2025-04-08",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-08T17:59:54Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2742ih.xml"
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
      "title": "DOGE Accountability and Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T09:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DOGE Accountability and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T09:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent fraud, waste, and abuse by requiring the Administrator of the United States Department of Government Efficiency Service to provide weekly reports to Congress regarding changes DOGE has made to any Federal agency and the realized impacts of such changes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T09:48:19Z"
    }
  ]
}
```
