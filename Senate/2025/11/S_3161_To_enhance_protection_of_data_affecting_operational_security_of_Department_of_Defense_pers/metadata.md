# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3161?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3161
- Title: Protecting DOD Data Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3161
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2025-11-25T19:02:36Z
- Update date including text: 2025-11-25T19:02:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3161",
    "number": "3161",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001208",
        "district": "",
        "firstName": "Elissa",
        "fullName": "Sen. Slotkin, Elissa [D-MI]",
        "lastName": "Slotkin",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Protecting DOD Data Act of 2025",
    "type": "S",
    "updateDate": "2025-11-25T19:02:36Z",
    "updateDateIncludingText": "2025-11-25T19:02:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T21:18:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3161is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3161\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Ms. Slotkin (for herself and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo enhance protection of data affecting operational security of Department of Defense personnel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting DOD Data Act of 2025 .\n#### 2. Enhanced protection of data affecting operational security of Department of Defense personnel\n##### (a) Priorities for protection of personal data for operational security\nIn carrying out the duties of the Secretary of Defense, the Secretary shall identify and prioritize the protection of personal data that is related to or may have impacts on the operational security of members of the Armed Forces and civilian employees of the Department of Defense through the prevention of collection, use, dissemination, or retention of such data that does not conform with provisions of law and practices relating to privacy that were in effect on the day before the date of the enactment of this Act.\n##### (b) Review and issuance of new guidance related to protection of personal data related to operational security\nNot later than June 1, 2026, the Secretary of Defense shall review all applicable guidance and policy relating to the protection of personal data that is related to or may have impacts on the operational security of Department personnel and, if necessary, issue revised or new guidance for enhanced protection measures for such data. Such guidance shall cover provisions of law and practices relating to privacy and personnel security that were in effect on the day before the date of the enactment of this Act.\n##### (c) Storage of data\n**(1) Limitation**\nThe Secretary shall ensure that no Department personal data related to or that may have impacts on the operational security of Department personnel is stored on a non-Department server or cloud service except pursuant to a contract or other agreement entered into by the Secretary and a contractor or subcontractor of the Department or, for personnel data, with the permission of the data subject.\n**(2) Waivers**\nThe Secretary may waive paragraph (1) in a case in which the Secretary certifies in writing that such waiver\u2014\n**(A)**\nappropriately considers the operational security risks to an employee of the Department with respect to whom such data may relate;\n**(B)**\ndoes not pose a risk to national security; and\n**(C)**\nis necessary in the interest of national security.\n##### (d) Congressional notification of changes to Departmental issuances\n**(1) In general**\nNot later than 30 days after the date on which the Secretary changes a Department issuance relating to the protection of personal data that is related to or may have impacts on the operational security of Department personnel, the Secretary shall submit to Congress notice of the change.\n**(2) Sunset**\nThe requirement of paragraph (1) shall terminate on the date that is five years after the date of the enactment of this Act.\n##### (e) Congressional notification of events\n**(1) In general**\nNot later than 30 days after the date of the occurrence of an event described in paragraph (2), the Secretary shall submit to Congress notice of the event.\n**(2) Events described**\nAn event described in this paragraph is an occurrence of an event in which\u2014\n**(A)**\nthe Secretary issues a waiver under subsection (c)(2);\n**(B)**\npersonal data related to or that may have an impact on operational security of Department personnel is not stored according to Department regulations or exfiltrated in violation of Department regulations;\n**(C)**\npersonal data related to or that may have an impact on operational security of Department personnel is stored on a non-Department server or cloud service that has not undergone an authorization process in accordance with Department regulations; or\n**(D)**\npersonal data related to or that may have an impact on operational security of Department of Defense personnel is exposed in any cybersecurity incident.\n##### (f) Standards, training, and reporting processes for system owners\n**(1) In general**\nThe Secretary shall develop standards, training, reporting, and security debriefing requirements for Department personnel who receive write or read access privileges as system owners across more than one platform of Department information systems that hosts personal data related to or that may have an impact on operational security of Department personnel.\n**(2) Security debriefings**\nThe Secretary shall ensure that personnel described in paragraph (1) are provided regular security debriefings, including after departing the Department.\n**(3) Notification of congress under certain circumstances**\nNot later than 30 days after the completion of the development of the standards, training, reporting, and security debriefing requirements in paragraph (1) the Secretary shall submit to Congress details of the requirements.",
      "versionDate": "2025-11-07",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T19:02:36Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3161is.xml"
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
      "title": "Protecting DOD Data Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting DOD Data Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enhance protection of data affecting operational security of Department of Defense personnel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:18:32Z"
    }
  ]
}
```
