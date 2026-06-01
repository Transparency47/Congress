# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5995?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5995
- Title: Have You Served Act
- Congress: 119
- Bill type: HR
- Bill number: 5995
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-01-09T09:06:45Z
- Update date including text: 2026-01-09T09:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-09 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-09 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5995",
    "number": "5995",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Have You Served Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:45Z",
    "updateDateIncludingText": "2026-01-09T09:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T14:05:56Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "MI"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "AL"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "MA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "MI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5995ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5995\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Ms. Brownley (for herself and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to make grants to eligible entities for the purpose of carrying out Ask the Question Campaigns, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Have You Served Act .\n#### 2. Grants for Ask the Question Campaigns\n##### (a) Grant program\nThe Secretary of Veterans Affairs shall make grants to eligible entities for the purpose of carrying out campaigns, to be known as Ask the Question Campaigns , to encourage human services professionals, State and local governments, and community providers to ask consumers whether they or a loved one have served in the Armed Forces.\n##### (b) Use of funds\nAn eligible entity that receives a grant under subsection (a) shall use the grant\u2014\n**(1)**\nto develop or expand an Ask the Question Campaign, under which the entity shall provide training to human services professionals, State and local governments, and community providers about\u2014\n**(A)**\nhow to appropriately ask consumers whether they or a loved one have served in the Armed Forces; and\n**(B)**\nresources available for members of the Armed Forces and veterans in their community through the Department of Veterans Affairs and other service providers to encourage the recipients of such training to refer consumers to the Department and other service providers, as appropriate; and\n**(2)**\nfor associated program costs, including staffing, technology, marketing and outreach materials, and convenings.\n##### (c) Eligible entity\nFor purposes of this section, an eligible entity is a State or an American Indian or Alaska Native tribe\u2014\n**(1)**\nthat\u2014\n**(A)**\nin the case of a State, develops a veteran suicide prevention plan, known as a Governors Challenge Action Plan ; or\n**(B)**\nin the case of an American Indian or Alaska Native tribe, develops a veteran suicide prevention plan; and\n**(2)**\nthat submits to the Secretary a proposal for the implementation of such plan that contains such information and assurances as the Secretary may require.\n##### (d) Technical assistance\nThe Secretary shall provide technical assistance to eligible entities that receive grants under this section to support the development and implementation of Ask the Question Campaigns. Such assistance shall include\u2014\n**(1)**\nthe provision of best practices acquired from the experiences of other eligible entities carrying out Ask the Question Campaigns;\n**(2)**\nthe provision of information on veterans resources in the State where the eligible entity is located;\n**(3)**\nthe provision of information about screening protocols used by the Department for assessing suicide risk and social determinants of health; and\n**(4)**\nestablishing key performance indicators for the training provided under the Campaigns.\n##### (e) Amount of grant\nThe Secretary may make up to 25 grants under this section for each of fiscal years 2026 through 2030. Each such grant shall be in an amount that does not exceed $200,000 .\n##### (f) Reporting\n**(1) Grant recipients**\nAs a condition of a grant under this section, an eligible entity shall agree to submit, by not later than the last day of each fiscal year during which the entity receives a grant, to the Secretary a report on the key performance indicators for the training provided using the grant funds.\n**(2) Implementation report**\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to Congress a report on the implementation of this section.\n**(3) Annual report**\nNot later than 30 days after the last day of a fiscal year for which the Secretary makes a grant under this section, the Secretary shall submit to Congress a report on the key performance indicators for the training provided under such grants.\n##### (g) Ask the Question Campaigns for Federal Agencies\nThe Secretary, in coordination with the Director of the Office of Management and Budget, shall develop a plan to work with each Federal department and agency to implement Ask the Question Campaigns, where appropriate, through any social service or health care programs of the department or agency through which employees of the department or agency interact with individuals receiving services and benefits.\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary of Veterans Affairs to carry out this section $6,000,000 for each of fiscal years 2026 through 2030.\n##### (i) State defined\nIn this section, the term State means each of the several States, Territories, and possessions of the United States, the District of Columbia, and the Commonwealth of Puerto Rico.",
      "versionDate": "2025-11-10",
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
        "updateDate": "2025-12-04T21:59:51Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5995ih.xml"
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
      "title": "Have You Served Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Have You Served Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to make grants to eligible entities for the purpose of carrying out Ask the Question Campaigns, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T04:33:26Z"
    }
  ]
}
```
