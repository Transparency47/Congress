# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1844?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1844
- Title: PAGER Act
- Congress: 119
- Bill type: HR
- Bill number: 1844
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-07-11T08:05:53Z
- Update date including text: 2025-07-11T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1844",
    "number": "1844",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PAGER Act",
    "type": "HR",
    "updateDate": "2025-07-11T08:05:53Z",
    "updateDateIncludingText": "2025-07-11T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:00:30Z",
          "name": "Referred To"
        }
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TN"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1844ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1844\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the availability of Federal funds to support the Armed Forces of Lebanon, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Armed Groups from Engaging in Radicalism or the PAGER Act .\n#### 2. Limitations on United States support for the Lebanese armed forces\nNotwithstanding any other provision of law, on and after the date that is 60 days after the date of the enactment of this Act, no Federal funds are authorized to be appropriated or otherwise made available to the armed forces of Lebanon until the date on which the Secretary of State certifies to the appropriate congressional committees that\u2014\n**(1)**\nthe Government of Lebanon, including the Chamber of Deputies, no longer recognizes the legitimacy as political parties of, nor permits its ministers or other cabinet-level officials to be from or claim alliance with\u2014\n**(A)**\nHezbollah;\n**(B)**\nLoyalty to the Resistance Bloc; and\n**(C)**\nAmal;\n**(2)**\nHezbollah no longer maintains any presence in Lebanon pursuant to action of the Lebanese Armed Forces and internal security forces to implement the clauses of United Nations Security Council Resolution 1559 (2004), which calls for the disbanding and disarmament of all Lebanese and non-Lebanese militias ;\n**(3)**\nsuch implementation of United Nations Security Council Resolution 1559 includes the expulsion of Hezbollah forces from known strongholds;\n**(4)**\nthe Lebanese Armed Forces and internal security forces have established an increased presence in areas known to be Hezbollah strongholds in order to prevent a resurgence of Hezbollah;\n**(5)**\nthe Lebanese Armed Forces do not maintain any coordination, collaboration, or support with Hezbollah, its affiliates, or any other group designated by the United States as a foreign terrorist organization that has a presence in Lebanon as of the date of such certification;\n**(6)**\nno member of the Lebanese Armed Forces maintains any coordination with or receives any support, either directly or indirectly, from any entity or organization that is an agent of, affiliated with, or owned or controlled by the Iranian Regime or Hezbollah;\n**(7)**\nany military aid previously received from Iran, whether in the form of weapons, ammunition, munitions, or equipment, is destroyed or disarmed; and\n**(8)**\nLebanese courts and military tribunals under the jurisdiction of the Lebanese armed forces dismiss all charges and arrest warrants against American citizens who have advocated against Hezbollah\u2019s influence over the Government of Lebanon, including American journalists who have appeared on Israeli news media or invited Israeli guests on their media programs.\n#### 3. Limitation on United States support to the United Nations Development Programme\nOn and after the date that is 60 days after the date of the enactment of this Act, no Federal funds authorized to be appropriated or otherwise made available to the United Nations Development Programme may be obligated or expended to support any livelihood support programs making assistance available to members of the Lebanese armed forces or the Lebanese internal security forces.\n#### 4. Designation as global terrorist\nSuhil Bahij Gharab is designated as a specially designated global terrorist organization under Executive Order 13224 ( 50 U.S.C. 1701 note; relating to blocking property and prohibiting transactions with persons who commit, threaten to commit, or support terrorism).\n#### 5. Report\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the Secretary of State, in consultation with the Secretary of Defense and the Director of the Central Intelligence Agency, shall submit to the appropriate congressional committees a report on the influences of Hezbollah and the Government of Iran throughout the Government of Lebanon, including the Lebanese Ministry of Defense.\n#### 6. Appropriate congressional committees defined\nIn this Act, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs and the Committee on Armed Services of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations and the Committee on Armed Services of the Senate.",
      "versionDate": "2025-03-05",
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
        "updateDate": "2025-05-13T14:19:52Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1844ih.xml"
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
      "title": "PAGER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PAGER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Armed Groups from Engaging in Radicalism",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the availability of Federal funds to support the Armed Forces of Lebanon, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:33Z"
    }
  ]
}
```
