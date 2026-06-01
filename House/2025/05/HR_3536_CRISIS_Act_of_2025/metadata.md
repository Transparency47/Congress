# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3536?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3536
- Title: CRISIS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3536
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2025-05-29T15:32:58Z
- Update date including text: 2025-05-29T15:32:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3536",
    "number": "3536",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "CRISIS Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-29T15:32:58Z",
    "updateDateIncludingText": "2025-05-29T15:32:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:01:15Z",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3536ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3536\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Foster (for himself and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the Secretary of Homeland Security to provide certain nationals of Russia with special immigrant status, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Countering Russian Innovation and Safeguarding Individual Scientists Act of 2025 or the CRISIS Act of 2025 .\n#### 2. Special immigrant status for certain Russian nationals\n##### (a) In general\nSubject to subsection (e), the Secretary of Homeland Security, or, notwithstanding any other provision of law, the Secretary of State in consultation with the Secretary of Homeland Security, may provide an alien described in subsection (b) with the status of a special immigrant under section 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ) if the alien\u2014\n**(1)**\nsubmits a classification petition under section 204(a)(1)(G)(i) of such Act ( 8 U.S.C. 1154(a)(1)(G)(i) );\n**(2)**\nis otherwise eligible to receive and immigrant visa;\n**(3)**\nis otherwise admissible to the United States for permanent residence; and\n**(4)**\nclears a background check and appropriate screening, as determined by the Secretary of Homeland Security and in accordance with subsection (d).\n##### (b) Aliens described\n**(1) Principal alien**\nAn alien is described in this subsection if the alien\u2014\n**(A)**\nis a national of Russia;\n**(B)**\nhas earned a doctoral degree in the United States or an equivalent foreign degree in a field involving science, technology, engineering, or mathematics; and\n**(C)**\nis seeking admission to engage in work in the United States in such a field.\n**(2) Spouse or child**\nAn alien is described in this subparagraph if the alien\u2014\n**(A)**\nis the spouse or child of the a principal alien described in paragraph (1); and\n**(B)**\nis accompanying or following to join the principal alien in the United States.\n##### (c) Processing and numerical limitations\n**(1) In general**\nThe total number of aliens described under subsection (b) who may be provided special immigrant status under this section may not exceed 3,000 per year for each of the fiscal years 2026, 2027, 2028, and 2029.\n**(2) Processing**\nNotwithstanding any other provision of law, the Secretary of Homeland Security shall, to the extent practicable, process petitions described in subsection (a) not later than 90 days after the date on which the Secretary of Homeland Security receives all required documentation and information to render a decision on such petition.\n**(3) Numerical limitations**\nAliens admitted to the United States pursuant to subsection (a) shall be exempt from the numerical limitations described in sections 201, 202, and 203 of the Immigration and Nationality Act ( 8 U.S.C. 1151 , 1152, and 1153).\n##### (d) Interview and vetting requirements\n**(1) Vetting requirements**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Homeland Security shall establish vetting requirements for applicants seeking special immigrant status under this section that are equivalent to the vetting requirements for refugees admitted to the United States through the United States Refugee Admissions Program, including an interview.\n**(2) Record requirements**\nThe Secretary of Homeland Security, in consultation with the Secretary of Defense, shall maintain records that contain, for each applicant under this section for the duration of the pendency of their application for special immigrant status\u2014\n**(A)**\npersonal biographic information, including name and date of birth;\n**(B)**\nbiometric information;\n**(C)**\nany criminal conviction occurring after the date on which the applicant entered the United States; and\n**(D)**\nthe history of the United States Government vetting to which the applicant has submitted, including whether the individual has undergone in-person vetting.\n**(3) Rule of Construction**\nNothing in this subsection may be construed to limit the authority of the Secretary of Homeland Security to maintain records in accordance with any other provision of law.\n##### (e) Termination\nThe authority of the Secretary of Homeland Security to admit aliens to the United States pursuant to subsection (a) shall terminate on the date that is the last day of the fourth full fiscal year after the date of enactment of this Act, except that petitions under subsection (a) that are approved on or before such date continue to form the basis for an application for an immigrant visa under section 221 of the Immigration and Nationality Act ( 8 U.S.C. 1201 ) or an application for adjustment of status under section 245 of such Act ( 8 U.S.C. 1255 ) after such date.\n##### (f) Definition\nThe term field involving science, technology, engineering, and mathematics includes advanced computing, advanced engineering materials, advanced gas turbine engine technologies, advanced manufacturing, advanced and networked sensing and signature management, advanced nuclear energy technologies, advanced particle accelerator and detector technologies, artificial intelligence, autonomous systems and robotics, biotechnologies, communication and networking technologies, cybersecurity, directed energy, financial technologies, human-machine interfaces, hypersonics, advanced missile propulsion technologies, networked sensors and sensing, quantum information technologies, renewable energy generation and storage, semiconductors and microelectronics, and space technologies and systems.\n##### (g) Rule of construction\nNothing in this Act shall be construed to require an alien described in subsection (b) to have an offer of employment from a United States employer to be eligible to be admitted as a special immigrant pursuant to subsection (a).",
      "versionDate": "2025-05-21",
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
        "updateDate": "2025-05-29T15:32:58Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3536ih.xml"
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
      "title": "CRISIS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CRISIS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Countering Russian Innovation and Safeguarding Individual Scientists Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Homeland Security to provide certain nationals of Russia with special immigrant status, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:44Z"
    }
  ]
}
```
