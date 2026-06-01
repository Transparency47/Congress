# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2828?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2828
- Title: VA DATA Access Transparency and Accountability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2828
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2025-12-12T09:07:12Z
- Update date including text: 2025-12-12T09:07:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-08 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-08 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2828",
    "number": "2828",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001136",
        "district": "3",
        "firstName": "Herbert",
        "fullName": "Rep. Conaway, Herbert [D-NJ-3]",
        "lastName": "Conaway",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "VA DATA Access Transparency and Accountability Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:12Z",
    "updateDateIncludingText": "2025-12-12T09:07:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:11:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-08T15:35:57Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2828ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2828\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Conaway (for himself, Mr. Carbajal , and Ms. Houlahan ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to restrict the access and use of veterans\u2019 data by the US DOGE Service and special Government employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA DATA Access Transparency and Accountability Act of 2025 or the VA DATA Act of 2025 .\n#### 2. Restrictions on access of DOGE Service to personal information about veterans\n##### (a) Restriction on access\nThe Secretary of Veterans Affairs may not provide to the Administrator of the United States DOGE Service (commonly referred to as the Department of Government Efficiency or DOGE ) access to any veteran\u2019s data in the possession of the Department of Veterans Affairs.\n##### (b) Restriction on use of information\nNo special Government employee may access or exfiltrate any veteran\u2019s data in the possession of the Department of Veterans Affairs for the purpose of using such data\u2014\n**(1)**\nfor commercial gain; or\n**(2)**\nfor any reason other than a governmental purpose authorized by the Secretary.\n##### (c) Termination of access\nIf any special Government employee acquires access to any system of the Department of Veterans Affairs that contains any veteran\u2019s data, the Secretary shall ensure that upon the termination of the period of service of the special Government employee, such employee\u2014\n**(1)**\nreturns all such data to the Department of Veterans Affairs; and\n**(2)**\ndoes not retain a copy of any such data.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term special Government employee has the meaning given such term in section 202(a) of title 18, United States Code.\n**(2)**\nThe term veteran\u2019s data mean data relating to an individual veteran, including personal health information, personal identifying information, and financial information.\n**(3)**\nThe term personal health information means, with respect to a veteran, any information, whether oral or recorded in any form or medium, that is related to\u2014\n**(A)**\nthe health of the veteran, including past, present, or future health;\n**(B)**\nthe medical treatment of the veteran, including past, present or future such treatment; or\n**(C)**\nany payment made or charged to a veteran related to the health or medical treatment of the veteran, including any past, present or future such payment.\n**(4)**\nThe term personal identifying information means, with respect to a veteran, any information, whether oral or recorded in any form or medium, that can be used to uncover the identity of the veteran, including\u2014\n**(A)**\nthe name, signature, or initials of the veteran;\n**(B)**\nthe social security number of the veteran;\n**(C)**\nthe drivers license number or passport number of the veteran;\n**(D)**\nthe home or mailing address of the veteran;\n**(E)**\nthe date of birth of the veteran;\n**(F)**\nany medical record of the veteran;\n**(G)**\nany financial account or credit card number of the veteran; and\n**(H)**\nany biometric records.",
      "versionDate": "2025-04-10",
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
        "updateDate": "2025-05-12T20:11:53Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2828ih.xml"
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
      "title": "VA DATA Access Transparency and Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA DATA Access Transparency and Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to restrict the access and use of veterans' data by the US DOGE Service and special Government employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T04:48:29Z"
    }
  ]
}
```
