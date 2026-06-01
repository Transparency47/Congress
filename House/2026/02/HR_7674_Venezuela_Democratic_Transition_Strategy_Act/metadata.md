# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7674?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7674
- Title: Venezuela Democratic Transition Strategy Act
- Congress: 119
- Bill type: HR
- Bill number: 7674
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-23T19:04:18Z
- Update date including text: 2026-04-23T19:04:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 41 - 5.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 41 - 5.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7674",
    "number": "7674",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Venezuela Democratic Transition Strategy Act",
    "type": "HR",
    "updateDate": "2026-04-23T19:04:18Z",
    "updateDateIncludingText": "2026-04-23T19:04:18Z"
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
      "text": "Ordered to be Reported by the Yeas and Nays: 41 - 5.",
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
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
            "date": "2026-03-26T16:32:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-25T14:06:10Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7674ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7674\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Moskowitz introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of State to submit to Congress a strategy to support a democratic transition in Venezuela, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Venezuela Democratic Transition Strategy Act .\n#### 2. Strategy to support a democratic transition in Venezuela\n##### (a) Strategy\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees a comprehensive strategy to support a democratic transition in the Bolivarian Republic of Venezuela.\n**(2) Elements**\nThe strategy required under paragraph (1) shall include\u2014\n**(A)**\na description of United States diplomatic efforts to support a democratic transition in Venezuela;\n**(B)**\na plan to prioritize the release of all individuals arbitrarily detained in Venezuela, including through diplomatic engagement, coordination with international partners, and support for monitoring and documenting cases of political detention;\n**(C)**\na description of United States efforts to curb foreign authoritarian influence, including the influence of the Republic of Cuba, the Russian Federation, the Islamic Republic of Iran, and the People\u2019s Republic of China, within the military, security services, and Government of Venezuela;\n**(D)**\na plan for the use of United States foreign assistance to support the Venezuelan people, including humanitarian assistance, democracy and governance programming, and efforts to strengthen access to basic services; and\n**(E)**\na description of efforts to support Venezuelan civil society, including independent media, human rights defenders, independent journalists, and other nongovernmental actors working to advance democracy, the rule of law, and accountability for atrocities and gross violations of internationally recognized human rights.\n##### (b) Annual report\nNot later than 1 year after the date of the submission of the strategy required in subsection (a), and annually thereafter for 2 years, the Secretary shall submit to the appropriate congressional committees a report describing progress made in implementing such strategy and any recommended changes to such strategy.\n##### (c) Congressional consultation\nThe Secretary shall consult with the appropriate congressional committees on a semi-annual basis regarding the strategy required in subsection (a) and the implementation of such strategy.\n##### (d) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations of the Senate.",
      "versionDate": "2026-02-25",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Asia",
            "updateDate": "2026-04-23T19:03:39Z"
          },
          {
            "name": "China",
            "updateDate": "2026-04-23T19:03:30Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-23T19:04:18Z"
          },
          {
            "name": "Cuba",
            "updateDate": "2026-04-23T19:03:24Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2026-04-23T19:02:52Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-04-23T19:03:06Z"
          },
          {
            "name": "Europe",
            "updateDate": "2026-04-23T19:03:51Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2026-04-23T19:02:59Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2026-04-23T19:02:46Z"
          },
          {
            "name": "Iran",
            "updateDate": "2026-04-23T19:03:58Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2026-04-23T19:02:33Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2026-04-23T19:04:03Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2026-04-23T19:03:17Z"
          },
          {
            "name": "Russia",
            "updateDate": "2026-04-23T19:03:45Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2026-04-23T19:02:39Z"
          },
          {
            "name": "Venezuela",
            "updateDate": "2026-04-23T19:02:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-02-27T16:37:42Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7674ih.xml"
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
      "title": "Venezuela Democratic Transition Strategy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Venezuela Democratic Transition Strategy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State to submit to Congress a strategy to support a democratic transition in Venezuela, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T09:18:27Z"
    }
  ]
}
```
