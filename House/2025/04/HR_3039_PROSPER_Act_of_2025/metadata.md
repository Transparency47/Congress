# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3039?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3039
- Title: PROSPER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3039
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2025-10-01T08:05:25Z
- Update date including text: 2025-10-01T08:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3039",
    "number": "3039",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "PROSPER Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-01T08:05:25Z",
    "updateDateIncludingText": "2025-10-01T08:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
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
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
          "date": "2025-04-28T16:00:20Z",
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
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "RI"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MO"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "WA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3039ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3039\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Mr. Goldman of New York (for himself, Mr. Johnson of Georgia , Mr. Magaziner , and Mr. Gomez ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Attorney General to authorize the youth gun violence prevention program.\n#### 1. Short title\nThis Act may be cited as the Prioritizing Resources for Outreach, Safety, Violence Prevention, Youth Empowerment and Resilience Act of 2025 or the PROSPER Act of 2025 .\n#### 2. Youth gun violence prevention program\n##### (a) In general\nThe Attorney General is authorized to award grants to eligible entities to carry out a program for youth gun violence prevention.\n##### (b) Activities\nGrants awarded under subsection (a) shall be used for the implementation of youth gun violence prevention programs that use strategies that are evidence-informed, culturally competent, trauma-informed, and linguistically and developmentally inclusive, and have a demonstrated ability to engage those at highest risk for involvement in gun violence and reduce their risk of violent victimization or engaging in violence, including strategies that\u2014\n**(1)**\nprioritize healing from past trauma and other life experiences that increase a young person\u2019s risk for involvement in gun violence;\n**(2)**\npromote youth empowerment through the development of skills and qualities such as empathy, pride in identity, leadership, conflict management, and communication;\n**(3)**\nconnect young people to mental health professionals, counselors, mentors, community leaders, crisis intervention professionals, community violence interrupters, or individuals trained in trauma-informed care and activities;\n**(4)**\nfoster meaningful community engagement, belonging, and the development of safe community environments;\n**(5)**\ndevelop and connect young people and their families with gun violence prevention resources, including but not limited to firearm safety education, safe storage techniques, and gun violence hotlines; and\n**(6)**\npromote resources that support the reintegration and resilience of young people with past exposure to gun violence or the juvenile justice system.\n##### (c) Authorization of appropriations\nOf the amounts otherwise appropriated for each of fiscal year 2026 though fiscal year 2030, for juvenile justice programs\u2014\n**(1)**\n$100,000,000 shall be made available for grants under title V of the Juvenile Justice and Delinquency Prevention Act of 1974 (34 U.S.C. note et seq.); and\n**(2)**\n$25,000,000 of the amount under paragraph (1) shall be made available to carry out a program for youth gun violence prevention.\n##### (d) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity includes\u2014\n**(A)**\ninstitutions of higher education;\n**(B)**\nIndian Tribe government agencies;\n**(C)**\nnon-governmental organizations serving Indian Tribes;\n**(D)**\ncommunity-based organizations; and\n**(E)**\na local government agency that is not a law enforcement agency.\n**(2) Community-based organization**\nThe term community-based organization includes a nonprofit community-based organization, a consortium of nonprofit community-based organizations, a national nonprofit organization acting as an intermediary for a community-based organization, or a community-based organization that has a fiscal sponsor that allows the organization to function as an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code.\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 under the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(5) Law enforcement agency**\nThe term law enforcement agency means any agency of the United States, a State or unit of local government authorized by law or by a government agency to engage in or supervise the prevention, detection, or investigation of any violation of criminal law.",
      "versionDate": "2025-04-28",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-21T12:45:47Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3039ih.xml"
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
      "title": "PROSPER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROSPER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prioritizing Resources for Outreach, Safety, Violence Prevention, Youth Empowerment and Resilience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Attorney General to authorize the youth gun violence prevention program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:21Z"
    }
  ]
}
```
