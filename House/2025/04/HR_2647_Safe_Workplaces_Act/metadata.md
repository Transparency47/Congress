# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2647?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2647
- Title: Safe Workplaces Act
- Congress: 119
- Bill type: HR
- Bill number: 2647
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2647",
    "number": "2647",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
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
    "title": "Safe Workplaces Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2647ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2647\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Neguse introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Labor to issue nonmandatory guidance on reducing the threat of violence in the workplace, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Workplaces Act .\n#### 2. OSHA guidance on reducing the threat of violence in the workplace\n##### (a) Study\nThe Director of the National Institute for Occupational Safety and Health shall conduct a study on reducing the threat of violence in the workplace.\n##### (b) Report\nNot later than 15 months after the date of the enactment of this Act, the Director shall submit to the Secretary of Labor, the Committee on Education and Labor of the House of Representatives, and the Committee on Health, Education, Labor, and Pensions of the Senate a report on the results of the study conducted under subsection (a), which shall include recommendations that the Secretary of Labor shall consider when issuing the guidance described in subsection (c).\n##### (c) Guidance\n**(1) In general**\nNot later than 4 years after the date of enactment of this Act, the Secretary of Labor, acting through the Occupational Safety and Health Administration, shall issue nonmandatory guidance on activities and work practice controls that can be implemented by workplaces to reduce workplace violence. Such guidance shall be differentiated to the extent necessary to account for the unique characteristics of, and the potential for threats of violence at, of each variety of workplace, including grocery stores, retail stores, movie theatres, hospitals, office buildings, restaurants and bars, religious facilities, manufacturing facilities, mail distribution centers, community centers, child care centers, and schools.\n**(2) Consideration**\nIn issuing the guidance required under paragraph (1), the Secretary shall\u2014\n**(A)**\nconsider the recommendations included in the report required under subsection (b); and\n**(B)**\ntake into account engineering controls, dangerous weapons, and environmental risk factors that may impact a workplace.\n##### (d) Definitions\nIn this Act:\n**(1) Dangerous weapon**\nThe term dangerous weapon means an instrument capable of inflicting death or serious bodily injury, without regard to whether such instrument was designed for that purpose.\n**(2) Engineering controls**\n**(A) In general**\nThe term engineering controls means an aspect of the built space or a device that removes a hazard from the workplace or creates a barrier between an employee and the hazard.\n**(B) Inclusions**\nFor purposes of reducing workplace violence hazards, the term engineering controls includes electronic access controls to employee occupied areas, weapon detectors (installed or handheld), enclosed work\u00adstations with shatter-resistant glass, deep service counters, locks on doors, removing access to or securing items that could be used as weapons, furniture affixed to the floor, opaque glass, closed-circuit television monitoring and video recording, sight-aids, and personal alarm devices.\n**(3) Environmental risk factors**\n**(A) In general**\nThe term environmental risk factors means factors in the facility or area in which a service is performed that may contribute to the likelihood or severity of a workplace violence incident.\n**(B) Clarification**\nEnvironmental risk factors may be associated with the specific task being performed or the work area, such as working in an isolated area, poor illumination or blocked visibility, and lack of physical barriers between individuals and persons at risk of committing workplace violence.\n**(4) Threat of Violence**\nThe term threat of violence means a statement or conduct that\u2014\n**(A)**\ncauses an individual to fear for such individual\u2019s safety because there is a reasonable possibility the individual might be physically injured; and\n**(B)**\nserves no legitimate purpose.\n**(5) Work practice controls**\n**(A) In general**\nThe term work practice controls means procedures and rules that are used to effectively reduce workplace violence hazards.\n**(B) Inclusions**\nThe term work practice controls includes\u2014\n**(i)**\nassigning and placing sufficient numbers of staff to reduce workplace violence directed at employees by customers, clients, patients, students, inmates, or any individual for whom the workplace provides services or for whom the employee performs services;\n**(ii)**\na provision of dedicated and available safety personnel such as security guards;\n**(iii)**\nemployee training on workplace violence prevention methods and techniques to de-escalate and minimize violent behavior; and\n**(iv)**\nemployee training on procedures for response in the event of a workplace violence incident and for post-incident response.\n**(6) Workplace violence**\n**(A) In general**\nThe term workplace violence means any act of violence or threat of violence, without regard to intent, that occurs at a workplace or while an employee performs a service.\n**(B) Exclusions**\nThe term workplace violence does not include lawful acts of self-defense or lawful acts of defense of others.\n**(C) Inclusions**\nThe term workplace violence includes\u2014\n**(i)**\nthe threat or use of physical force against a employee that results in or has a high likelihood of resulting in injury, psychological trauma, or stress, without regard to whether the employee sustains an injury, psychological trauma, or stress; and\n**(ii)**\nan incident involving the threat or use of a firearm or a dangerous weapon, including the use of common objects as weapons, without regard to whether the employee sustains an injury, psychological trauma, or stress.",
      "versionDate": "2025-04-03",
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
        "name": "Labor and Employment",
        "updateDate": "2025-05-02T12:22:59Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2647ih.xml"
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
      "title": "Safe Workplaces Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Workplaces Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Labor to issue nonmandatory guidance on reducing the threat of violence in the workplace, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T02:48:18Z"
    }
  ]
}
```
