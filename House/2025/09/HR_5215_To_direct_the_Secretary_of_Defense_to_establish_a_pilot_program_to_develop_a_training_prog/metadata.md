# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5215?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5215
- Title: SHIELD Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5215
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2025-09-19T19:35:45Z
- Update date including text: 2025-09-19T19:35:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5215",
    "number": "5215",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "SHIELD Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-19T19:35:45Z",
    "updateDateIncludingText": "2025-09-19T19:35:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
          "date": "2025-09-08T16:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5215ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5215\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Ms. Stevens introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to establish a pilot program to develop a training program that teaches members of the Armed Forces to interact with digital information in a safe and responsible manner, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the The Strategic Homeland Information Education and Learning Defense Act of 2025 or the SHIELD Act of 2025 .\n#### 2. Pilot program for digital information training for members of the Armed Forces\n##### (a) Pilot program\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Defense shall establish a pilot program (in this section referred to as the pilot program ) to develop a training program that teaches members of the Armed Forces to interact with digital information in a safe and responsible manner.\n##### (b) Elements\nIn carrying out the pilot program, the Secretary shall\u2014\n**(1)**\ndevelop and carry out a curriculum that includes instruction on\u2014\n**(A)**\nhow to identify\u2014\n**(i)**\nfact-based journalism;\n**(ii)**\nopinion-based journalism;\n**(iii)**\ndisinformation;\n**(iv)**\nconspiracy theories; and\n**(v)**\nhate-based ideologies, including antisemitism and white supremacy;\n**(B)**\nhow to assess the credibility of digital news and other digital sources of information;\n**(C)**\nthe effects of online actions on the actor and others, including the effects of posting or sharing personal, incorrect, or bias-based information;\n**(D)**\nthe importance of protecting personal information and how to protect personal information with respect to online activities;\n**(E)**\nhow to recognize and avoid common information-based threats that could harm\u2014\n**(i)**\nan individual targeted by such threats;\n**(ii)**\nthe property of the individual; or\n**(iii)**\nthe security, property, or goals of the Department of Defense when the individual is a member of the Armed Forces; and\n**(F)**\nin the case that the individual is a member of the Armed Forces, methodologies\u2014\n**(i)**\nthat the individual can use when locating, evaluating, and using digital information; and\n**(ii)**\nwhich are designed reduce insider threats to, and vulnerabilities of, the Armed Forces with respect to conspiracy theories and hate-based ideology;\n**(2)**\nselect as participants a geographically and demographically diverse sample of members of the Armed Forces in such number as is necessary to collect meaningful feedback about the training program; and\n**(3)**\nuse in-person, virtual, and hybrid training delivery methods in equal amounts.\n##### (c) Termination\nThe authority of Secretary to carry out the pilot program shall terminate on the date that is one year after the date on which the pilot program begins.\n##### (d) Consultation\nIn carrying out the pilot program, the Secretary may consult with organizations that specialize in teaching or providing information to individuals about interacting with digital information in a safe and responsible manner.\n##### (e) Survey\nAfter the date on which the pilot program terminates pursuant to subsection (c), the Secretary shall survey participants and instructors to identify\u2014\n**(1)**\nways to improve the training program and curriculum;\n**(2)**\nways to improve participant engagement during the training program; and\n**(3)**\nthe extent to which participants retained, over time, the information taught during the training program.\n##### (f) Report\nNot later than 180 days after the termination of the pilot program, the Secretary shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report summarizing the results of the pilot program, including\u2014\n**(1)**\na comparison of the in-person, virtual, and hybrid training delivery methods, considering\u2014\n**(A)**\nthe engagement of participants during the training program;\n**(B)**\nthe extent to which participants retained, over time, the information taught during the training program; and\n**(C)**\nother notable differences, as determined by the Secretary;\n**(2)**\na determination, based on such comparison, about which training delivery method is most effective for teaching the curriculum developed under subsection (b)(1);\n**(3)**\na recommendation about how often a member of the Armed Forces should be required to attend a permanent training program about interacting with digital information in a safe and responsible manner, if established, considering the extent to which participants of the pilot program retained information taught during the training program; and\n**(4)**\na recommendation about how often the curriculum of any such permanent training program should be updated.",
      "versionDate": "2025-09-08",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T19:35:45Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5215ih.xml"
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
      "title": "SHIELD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T04:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHIELD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-12T04:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "The Strategic Homeland Information Education and Learning Defense Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-12T04:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to establish a pilot program to develop a training program that teaches members of the Armed Forces to interact with digital information in a safe and responsible manner, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T04:33:25Z"
    }
  ]
}
```
