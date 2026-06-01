# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1237?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1237
- Title: STOP Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 1237
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-20T08:08:16Z
- Update date including text: 2026-05-20T08:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-04-30 - IntroReferral: Submitted in House
- Latest action: 2026-04-30: Submitted in House

## Actions

- 2026-04-30 - IntroReferral: Referred to the House Committee on House Administration.
- 2026-04-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1237",
    "number": "1237",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000246",
        "district": "4",
        "firstName": "Pat",
        "fullName": "Rep. Fallon, Pat [R-TX-4]",
        "lastName": "Fallon",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "STOP Resolution",
    "type": "HRES",
    "updateDate": "2026-05-20T08:08:16Z",
    "updateDateIncludingText": "2026-05-20T08:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
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
          "date": "2026-04-30T13:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "AR"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1237ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1237\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Fallon (for himself and Mr. Crawford ) submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nRequiring certain Members, officers, and employees of the House of Representatives to complete a program of training in counterintelligence and classified information protection each Congress, and for other purposes.\n#### 1. Short title\nThis resolution may be cited as the Stop Telling other People Resolution or the STOP Resolution .\n#### 2. Mandatory completion of program of training in counterintelligence and classified information protection\n##### (a) Requiring training for certain Members, officers, and employees\n**(1) Requirement**\nNot later than 90 days after the date of the adoption of this resolution, the Committee on House Administration shall issue regulations to provide that during each Congress each Member (including each Delegate or Resident Commissioner to the Congress), officer, and employee of the House of Representatives described in subsection (b) shall complete a program of training with respect to counterintelligence and the protection of classified information administered by the Sergeant-at-Arms of the House.\n**(2) Inclusion of fellows and detailees**\nFor purposes of this resolution, an individual serving in an office of the House of Representatives as a participant in a fellowship program or a detailee from another office of the Federal Government shall be considered an employee of the House.\n**(3) Exception for participants in new Member orientation programs**\nIf an individual completed a program of training required under paragraph (1) during the new Member orientation program administered by the Committee on House Administration prior to the beginning of a Congress, the individual is not required to complete the program during that Congress.\n##### (b) Covered Members, officers, and employees described\nA Member (including each Delegate or Resident Commissioner to the Congress), officer, or employee of the House of Representatives described in this subsection is\u2014\n**(1)**\nin the case of a Member, any Member who receives access to classified information as a result of the Member\u2019s service in the House of Representatives; and\n**(2)**\nin the case of an officer or employee, each officer or employee who holds a security clearance and receives access to classified information as a result of the individual\u2019s service in the House of Representatives.\n##### (c) Deadline\n**(1) In general**\nUnder the regulations issued by the Committee on House Administration under subsection (a) , an individual shall complete the program of training required under subsection (a)(1) and file a certificate of completion of such training not later than\u2014\n**(A)**\nin the case of an individual who is serving as a Member, officer, or employee of the House as of the date on which the Committee first certifies that the program is in operation for a Congress, not later than 90 days after such date; or\n**(B)**\nin the case of any other individual, not later than 90 days after the individual first becomes a Member, officer, or employee of the House.\n**(2) Alternative deadlines**\nThe Committee on House Administration may include in the regulations issued under subsection (a) \u2014\n**(A)**\nan alternative deadline for individuals serving as participants in fellowship programs to take into account the duration of their service; and\n**(B)**\nan alternative deadline for individuals who first become Members, officers, or employees of the House towards the end of a Congress to take into account the amount of time remaining in the Congress.\n**(3) Special rule for One Hundred Nineteenth Congress**\nIn the case of the One Hundred Nineteenth Congress, an individual described in subparagraph (A) of paragraph (1) shall complete the program required under subsection (a) not later than 90 days after the date of the adoption of this resolution.\n##### (d) Prohibition with respect to access to classified information for noncompliance\nIf an individual does not meet deadline for completion of the training under subsection (c) \u2014\n**(1)**\nin the case of a Member, such Member may not be granted access to any classified information until such date as the Member completes the training and files a certificate of completion; and\n**(2)**\nin the case of an officer or employee, such officer or employee may not be granted access to any classified information until the date that is 180 days after the date the officer or employee completes the training and files a certificate of completion.\n##### (e) Additional mechanisms\nThe Committee on House Administration shall consider additional mechanisms to ensure compliance with the training requirement under subsection (a) .",
      "versionDate": "2026-04-30",
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
        "updateDate": "2026-05-15T18:56:44Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1237ih.xml"
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
      "title": "STOP Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-04T13:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Telling other People Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-04T13:53:25Z"
    },
    {
      "title": "STOP Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-04T13:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Requiring certain Members, officers, and employees of the House of Representatives to complete a program of training in counterintelligence and classified information protection each Congress, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-04T13:48:29Z"
    }
  ]
}
```
