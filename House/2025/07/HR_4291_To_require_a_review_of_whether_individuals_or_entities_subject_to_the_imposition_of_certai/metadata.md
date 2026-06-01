# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4291?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4291
- Title: Sanctions Lists Harmonization Act
- Congress: 119
- Bill type: HR
- Bill number: 4291
- Origin chamber: House
- Introduced date: 2025-07-02
- Update date: 2026-05-27T17:46:56Z
- Update date including text: 2026-05-27T17:46:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-02: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-02 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 49 - 0.
- Latest action: 2025-07-02: Introduced in House

## Actions

- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-02 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 49 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-02",
    "latestAction": {
      "actionDate": "2025-07-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4291",
    "number": "4291",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Sanctions Lists Harmonization Act",
    "type": "HR",
    "updateDate": "2026-05-27T17:46:56Z",
    "updateDateIncludingText": "2026-05-27T17:46:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "text": "Ordered to be Reported by the Yeas and Nays: 49 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-07-02",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-02",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-02",
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
            "date": "2025-12-03T16:04:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-02T13:02:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-02T13:02:40Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "FL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "MI"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "GA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "GU"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
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
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4291ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4291\nIN THE HOUSE OF REPRESENTATIVES\nJuly 2, 2025 Mr. Fine (for himself and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require a review of whether individuals or entities subject to the imposition of certain sanctions through inclusion on certain sanctions lists should also be subject to the imposition of other sanctions and included on other sanctions lists.\n#### 1. Short title\nThis Act may be cited as the Sanctions Lists Harmonization Act .\n#### 2. Requirements to include individuals and entities subject to united states sanctions on certain other sanctions lists\n##### (a) Notification to other Federal officials\nNot later than 30 days after the date on which an individual or entity is included on one of the lists described in subsection (d), the Federal official responsible for administering such list shall notify the Federal officials responsible for administering the other lists described in subsection (d) of the inclusion of the individual or entity on such list.\n##### (b) Determination and other requirements of other Federal official\n**(1) Review**\nNot later than 30 days after the date on which a Federal official receives a notification under subsection (a) of the inclusion of an individual or entity on one of the lists described in subsection (d), such Federal official shall initiate a review regarding whether such individual or entity warrants inclusion on such other lists.\n**(2) Determination**\nNot later than 90 days after the date on which a Federal official receives a notification under subsection (a) of the inclusion of an individual or entity on one of the lists described in subsection (d), such Federal official shall make a determination of whether to include such individual or entity on such other lists.\n##### (c) Report\n**(1) In general**\nNot later than 1 year after the enactment of this Act, each Federal agency maintaining a list described in subsection (d) shall submit to the appropriate congressional committees a report\u2014\n**(A)**\ncertifying compliance with subsections (a) and (b) of this section;\n**(B)**\nexplaining the agency\u2019s deliberative process to meet the requirements in subsections (a) and (b); and\n**(C)**\nenumerating any instances in which the requirements in subsections (a) and (b) led to the inclusion of additional individuals or entities to one of the lists described in subsection (d).\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form, but may contain a classified annex.\n##### (d) Lists described\nThe lists described in this subsection are the following:\n**(1)**\nThe list of specially designated nationals and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury.\n**(2)**\nThe list maintained and set forth in Supplement No. 4 to part 744 of the Export Administration Regulations (commonly known as the Entity List ).\n**(3)**\nThe Department of Defense\u2019s list maintained and published under 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 10 U.S.C. 113 note).\n**(4)**\nThe Non-SDN Chinese Military-Industrial Complex Companies (NS\u2013CMIC) List of the Office of Foreign Assets Control of the Department of the Treasury.\n**(5)**\nThe Sectoral Sanctions List of the Office of Foreign Assets Control of the Department of the Treasury.\n**(6)**\nThe Military End User List of the Bureau of Industry and Security of the Department of Commerce.\n##### (e) Definitions\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs, the Committee on Armed Services, the Permanent Select Committee on Intelligence, and the Committee on Financial Services of the House of Representatives; and\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs, the Committee on Armed Services, the Select Committee on Intelligence, the Committee on Foreign Relations, and the Committee on Finance of the Senate.\n**(2) Export Administration Regulations**\nThe term Export Administration Regulations means the regulations set forth in subchapter C of chapter VII of title 15, Code of Federal Regulations, or successor regulations.",
      "versionDate": "2025-07-02",
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
            "name": "Congressional oversight",
            "updateDate": "2026-05-27T17:46:37Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2026-05-27T17:46:43Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2026-05-27T17:46:56Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-05-27T17:46:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-08-01T17:20:14Z"
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
      "date": "2025-07-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4291ih.xml"
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
      "title": "Sanctions Lists Harmonization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sanctions Lists Harmonization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a review of whether individuals or entities subject to the imposition of certain sanctions through inclusion on certain sanctions lists should also be subject to the imposition of other sanctions and included on other sanctions lists.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:33:35Z"
    }
  ]
}
```
