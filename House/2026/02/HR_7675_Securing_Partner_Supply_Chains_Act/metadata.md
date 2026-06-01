# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7675?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7675
- Title: Securing Partner Supply Chains Act
- Congress: 119
- Bill type: HR
- Bill number: 7675
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-22T20:35:34Z
- Update date including text: 2026-04-22T20:35:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 43 - 3.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 43 - 3.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7675",
    "number": "7675",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001091",
        "district": "20",
        "firstName": "Joaquin",
        "fullName": "Rep. Castro, Joaquin [D-TX-20]",
        "lastName": "Castro",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Securing Partner Supply Chains Act",
    "type": "HR",
    "updateDate": "2026-04-22T20:35:34Z",
    "updateDateIncludingText": "2026-04-22T20:35:34Z"
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
      "text": "Ordered to be Reported by the Yeas and Nays: 43 - 3.",
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
            "date": "2026-03-26T16:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-25T14:05:45Z",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7675ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7675\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Castro of Texas (for himself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of State to establish the Initiative on Foreign Investment Screening, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Partner Supply Chains Act .\n#### 2. Initiative on foreign investment screening\n##### (a) Findings\nCongress finds the following:\n**(1)**\nForeign investment can be beneficial to economic growth, but also presents risks to national security if critical infrastructure, sensitive technology, or supply chains are compromised.\n**(2)**\nMany foreign countries lack robust regulatory frameworks to screen foreign investments for national security concerns.\n**(3)**\nStrengthening investment screening mechanisms worldwide supports United States national security by enhancing allied and partner countries\u2019 resilience against malign foreign influence.\n**(4)**\nThe United States has expertise in investment screening which can be leveraged to assist allies and partners.\n##### (b) Initiative on foreign investment screening\n**(1) Establishment**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall establish the Initiative on Foreign Investment Screening (in this section referred to as the Initiative ) which shall terminate on the date that is 3 years after the date of such establishment.\n**(2) Coordination**\nThe Secretary shall coordinate with the heads of other government agencies, as appropriate, in the establishment and activities of the initiative.\n**(3) Designated official**\nThe Secretary shall designate the Under Secretary for Economic Growth, Energy, and the Environment or the designee of the Under Secretary to lead the initiative.\n**(4) Duties**\nThe Initiative shall\u2014\n**(A)**\nprovide technical assistance, training, and advisory services to foreign countries regarding best practices for screening foreign investments for national security risks to such countries;\n**(B)**\nfacilitate coordination among United States agencies, the private sector, partner countries, and civil society to promote investment security standards;\n**(C)**\nsupport the development and implementation of foreign investment screening mechanisms in partner countries through regulatory guidance and information sharing;\n**(D)**\nassess the progress of partner countries in establishing robust investment screening mechanisms; and\n**(E)**\nconduct outreach and capacity-building efforts to enhance global awareness of investment security risks.\n**(5) Annual report to Congress**\nNot later than one year after the date of enactment of this Act, and annually thereafter for 3 years, the Secretary shall submit to the appropriate congressional committees a report on the activities of the Initiative, including\u2014\n**(A)**\na summary of technical assistance and training provided to foreign countries;\n**(B)**\nan assessment of progress made by foreign countries in implementing investment screening mechanisms;\n**(C)**\nan evaluation of emerging national security risks related to foreign investment;\n**(D)**\nrecommendations for further United States engagement with foreign countries regarding investment security assistance; and\n**(E)**\nfor each country determined by the Secretary to be a partner country pursuant to subsection (c)(4)(C) and not included in a previous report required in this paragraph, a detailed description of the reasons for such determination.\n##### (c) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the following:\n**(A)**\nThe Committee on Foreign Affairs of the House of Representatives.\n**(B)**\nThe Committee on Foreign Relations of the Senate.\n**(2) Foreign investment**\nThe term foreign investment means direct or indirect investment in the economy of a country by\u2014\n**(A)**\nan individual who is not a citizen or national of such country; or\n**(B)**\nan entity that is not organized under the laws of such country or any jurisdiction within such country.\n**(3) National security risk**\nThe term national security risk means a risk related to critical infrastructure, sensitive technology, supply chain vulnerabilities, or malign foreign influence.\n**(4) Partner country**\nThe term partner country means the following:\n**(A)**\nA country with which the United States has entered into a bilateral or multilateral free trade agreement.\n**(B)**\nA country with which the United States has entered into a mutual defense agreement by treaty.\n**(C)**\nAny other country, as determined by the Secretary.",
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-04-22T20:35:13Z"
          },
          {
            "name": "Business investment and capital",
            "updateDate": "2026-04-22T20:34:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-22T20:35:33Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2026-04-22T20:35:01Z"
          },
          {
            "name": "Free trade and trade barriers",
            "updateDate": "2026-04-22T20:35:26Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-22T20:34:33Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2026-04-22T20:34:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-02-27T16:37:57Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7675ih.xml"
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
      "title": "Securing Partner Supply Chains Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Partner Supply Chains Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State to establish the Initiative on Foreign Investment Screening, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T09:18:24Z"
    }
  ]
}
```
