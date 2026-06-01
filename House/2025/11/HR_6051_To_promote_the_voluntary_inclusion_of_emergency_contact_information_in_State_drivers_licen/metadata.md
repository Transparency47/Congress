# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6051?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6051
- Title: To Inform Families First Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6051
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-01-07T09:05:40Z
- Update date including text: 2026-01-07T09:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-18 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-18 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6051",
    "number": "6051",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To Inform Families First Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:40Z",
    "updateDateIncludingText": "2026-01-07T09:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
          "date": "2025-11-17T17:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-18T18:19:18Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6051ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6051\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mr. Buchanan introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo promote the voluntary inclusion of emergency contact information in State driver\u2019s license and identification systems and to provide support to States for implementation of such systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the To Inform Families First Act of 2025 .\n#### 2. National Highway Traffic Safety Administration grant program for emergency contact information system\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration, shall establish a program (in this section referred to as the program ) to provide assistance to States to develop and implement systems to collect emergency contact information for inclusion in the driver\u2019s license and identification records of such States.\n##### (b) Forms of assistance\nAssistance provided under the program section may be in the form of a grant or technical assistance.\n##### (c) Requirements\nAs a condition of receiving assistance under the program, a State shall use such assistance to develop an emergency contact information system described in subsection (a) and such State shall\u2014\n**(1)**\nensure that the provision of emergency contact information by an individual under such system is voluntary;\n**(2)**\ninclude robust data security protections in such system;\n**(3)**\nrestrict access to information provided under such system to authorized emergency personnel for use only during an emergency; and\n**(4)**\nensure that there is no requirement to display such emergency contact information on a physical driver\u2019s license or identification card.\n##### (d) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to Congress an annual report on the implementation of this section and include in such report information on any technical assistance provided under this section.\n##### (e) State defined\nIn this section, the term State means any of the 50 States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.",
      "versionDate": "2025-11-17",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-20T16:39:35Z"
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
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6051ih.xml"
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
      "title": "To Inform Families First Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To Inform Families First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T10:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote the voluntary inclusion of emergency contact information in State driver's license and identification systems and to provide support to States for implementation of such systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T10:03:17Z"
    }
  ]
}
```
