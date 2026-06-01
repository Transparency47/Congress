# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7124
- Title: Realigning Mobile Phone Biometrics for American Privacy Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 7124
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-05-16T08:07:59Z
- Update date including text: 2026-05-16T08:07:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-01-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-01-16 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7124",
    "number": "7124",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "T000193",
        "district": "2",
        "firstName": "Bennie",
        "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
        "lastName": "Thompson",
        "party": "D",
        "state": "MS"
      }
    ],
    "title": "Realigning Mobile Phone Biometrics for American Privacy Protection Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:59Z",
    "updateDateIncludingText": "2026-05-16T08:07:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-16T21:02:58Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7124ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7124\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Thompson of Mississippi (for himself, Mr. Correa , Mr. Thanedar , Ms. Clarke of New York , Ms. Meng , and Mr. Espaillat ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo prohibit the use of facial recognition mobile phone applications outside ports of entry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Realigning Mobile Phone Biometrics for American Privacy Protection Act .\n#### 2. Prohibition on the use of facial recognition mobile phone applications outside ports of entry\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Homeland Security shall develop standards and guidelines for the Department of Homeland Security and its components\u2014\n**(1)**\nprohibiting the use of the Mobile Fortify Mobile Application, Mobile Identify Mobile Application, or successor applications, except for identification purposes at ports of entry;\n**(2)**\nprohibiting the Department and its components from sharing the Mobile Fortify Mobile Application, Mobile Identify Mobile Application, or successor applications with any other Federal agency or any State, local, Tribal, or territorial agency;\n**(3)**\nrequiring\u2014\n**(A)**\nthe removal of the Mobile Fortify Mobile Application, Mobile Identify Mobile Application, or any successor applications from Department and component information technology, except as necessary for identification purposes at ports of entry, in accordance with paragraph (1); and\n**(B)**\nthe Department to remotely render inoperable any such applications downloaded on non-Department information technology;\n**(4)**\nexcept as provided in paragraph (5), requiring the immediate destruction of any image, photograph, or fingerprint of any United States citizen captured through the use of the Mobile Fortify Mobile Application, Mobile Identify Mobile Application, any successor applications before such standards and guidelines are implemented, wherever such image, photograph, or fingerprint may be stored; and\n**(5)**\nrequiring the destruction of any image, photograph, or fingerprint of a United States citizen captured through the use of the Mobile Fortify Mobile Application, Mobile Identify Mobile Application, or successor applications for identification purposes at ports of entry pursuant to paragraph (1) not later than 12 hours after such image, photograph, or fingerprint is captured.",
      "versionDate": "2026-01-15",
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
        "updateDate": "2026-02-05T18:59:46Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7124ih.xml"
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
      "title": "Realigning Mobile Phone Biometrics for American Privacy Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Realigning Mobile Phone Biometrics for American Privacy Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T13:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of facial recognition mobile phone applications outside ports of entry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T13:03:38Z"
    }
  ]
}
```
