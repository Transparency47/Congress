# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7616?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7616
- Title: Transatlantic Academic Security and Risk Mitigation Act
- Congress: 119
- Bill type: HR
- Bill number: 7616
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-04-08T19:20:20Z
- Update date including text: 2026-04-08T19:20:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 27 - 19.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 27 - 19.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7616",
    "number": "7616",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Transatlantic Academic Security and Risk Mitigation Act",
    "type": "HR",
    "updateDate": "2026-04-08T19:20:20Z",
    "updateDateIncludingText": "2026-04-08T19:20:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 27 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
        "item": [
          {
            "date": "2026-03-26T16:36:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-20T16:33:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
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
      "sponsorshipDate": "2026-03-02",
      "state": "NY"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7616ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7616\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Jackson of Texas (for himself and Mr. Fine ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of State to develop a strategy to identify and mitigate relationships that pose a risk to United States foreign policy interests between certain European institutions and certain covered entities of concern, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transatlantic Academic Security and Risk Mitigation Act .\n#### 2. Strategy\n##### (a) Strategy required\nNot later than 180 days after the date of the enactment of this Act, the Under Secretary of State for Political Affairs shall submit to the appropriate congressional committees a strategy regarding covered European institutions that maintain academic, financial, research, governance, programmatic, data-sharing, or other relevant direct or indirect relationships with covered entities of concern. Such strategy shall also include each of the following:\n**(1)**\nThe manner in which the Department of State will identify, evaluate, and mitigate the relationships that pose a risk to United States foreign policy interests between European institutions and covered entities of concern.\n**(2)**\nAn assessment of the scale, scope, and activities of covered entities of concern in Europe, disaggregated by country and including any other relevant operational or financial details.\n**(3)**\nAn evaluation of the vulnerabilities, threats, and national security risks posed to the United States and to European allies and partners arising from the presence, activities, or influence efforts of covered entities of concern in European countries.\n**(4)**\nA list of recommendations for bilateral and multilateral United States diplomatic engagement with European governments and covered European institutions aimed at mitigating risks associated with covered entities of concern.\n**(5)**\nAny other matters the Under Secretary of State for Political Affairs determines relevant.\n##### (b) Form\nThe strategy required by subsection (a) shall be submitted in unclassified form but may contain a classified annex.\n##### (c) Briefing\nConcurrently with the submission of the strategy required by subsection (a), the Under Secretary of State for Political Affairs shall submit to the appropriate congressional committees a briefing on that strategy.\n##### (d) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations of the Senate.\n**(2) Covered entity of concern**\nThe term covered entity of concern means\u2014\n**(A)**\nany entity of the People\u2019s Republic of China that\u2014\n**(i)**\nis involved in the implementation of military-civil fusion;\n**(ii)**\nparticipates in the Chinese defense industrial base;\n**(iii)**\nis affiliated with the Chinese State Administration for Science, Technology and Industry for the National Defense;\n**(iv)**\nreceives funding from any organization subordinate to the Central Military Commission of the Chinese Communist Party;\n**(v)**\nprovides support to any security, defense, police, or intelligence organization of the Government of the People\u2019s Republic of China or the Chinese Communist Party;\n**(vi)**\nengages in coordinated activities or provides material support intended to undermine the United States relationship with Taiwan;\n**(vii)**\naids, abets, or enables the detention, imprisonment, persecution, or forced labor of Uyghur Muslims in the People\u2019s Republic of China; or\n**(viii)**\nis affiliated with the Chinese Academy of Sciences or the Chinese People\u2019s Political Consultative Conference;\n**(B)**\nany entity that participates, directly or indirectly, in a foreign talent recruitment program of the People\u2019s Republic of China or has participated in such a program at any time in the 10-year period ending on the date of the submission of the report required by subsection (a);\n**(C)**\nany entity that directs support or coordination of student groups, language or cultural centers, or other on-campus entities (including Confucius Institutes or Chinese Student and Scholars Associations directed or funded, directly or indirectly, by the Government of the People\u2019s Republic of China); or\n**(D)**\nany entity that engages in foreign malign influence or interference involving subversive, undeclared, coercive, or criminal activities, which may include propaganda, information manipulation, or efforts to influence academic, political, or civic institutions, whether conducted directly by foreign governments, state-linked entities, or through affiliated non-state actors, or their proxies, including through and by the United Front Work Department.\n**(3) Covered European institution**\nThe term covered European institution means an institution of higher education or a research institution located in Europe.",
      "versionDate": "2026-02-20",
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
        "name": "International Affairs",
        "updateDate": "2026-02-27T16:43:26Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7616ih.xml"
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
      "title": "Transatlantic Academic Security and Risk Mitigation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T08:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transatlantic Academic Security and Risk Mitigation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T08:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State to develop a strategy to identify and mitigate relationships that pose a risk to United States foreign policy interests between certain European institutions and certain covered entities of concern, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T08:48:40Z"
    }
  ]
}
```
