# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7272
- Title: Pipeline Cybersecurity Preparedness Act
- Congress: 119
- Bill type: HR
- Bill number: 7272
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-05-27T18:41:27Z
- Update date including text: 2026-05-27T18:41:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-27 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-27 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7272",
    "number": "7272",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "W000814",
        "district": "14",
        "firstName": "Randy",
        "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
        "lastName": "Weber",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Pipeline Cybersecurity Preparedness Act",
    "type": "HR",
    "updateDate": "2026-05-27T18:41:27Z",
    "updateDateIncludingText": "2026-05-27T18:41:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:31:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T22:42:55Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-04T22:42:11Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-27T22:41:17Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MI"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7272ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7272\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Weber of Texas (for himself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Energy to carry out a program relating to physical security and cybersecurity for pipelines and liquefied natural gas facilities.\n#### 1. Short title\nThis Act may be cited as the Pipeline Cybersecurity Preparedness Act .\n#### 2. Physical security and cybersecurity for pipelines and liquefied natural gas facilities\nThe Secretary of Energy, in carrying out the Department of Energy\u2019s functions pursuant to the Department of Energy Organization Act ( 42 U.S.C. 7101 et seq. ), and in consultation with appropriate Federal agencies, representatives of the energy sector, the States, and other stakeholders, shall carry out a program\u2014\n**(1)**\nto establish policies and procedures that improve coordination among Federal agencies, States, and the energy sector, including through councils or other entities engaged in sharing, analysis, or sector coordinating, to ensure the security, resiliency, and survivability of natural gas pipelines (including natural gas transmission and distribution pipelines), hazardous liquid pipelines, and liquefied natural gas facilities;\n**(2)**\nto lead the coordinated response and recovery by Federal agencies, States, and the energy sector, to physical incidents and cyber incidents impacting the energy sector;\n**(3)**\nto develop, for voluntary use, advanced cybersecurity applications and technologies for natural gas pipelines (including natural gas transmission and distribution pipelines), hazardous liquid pipelines, and liquefied natural gas facilities;\n**(4)**\nto perform pilot demonstration projects relating to physical security and cybersecurity for natural gas pipelines (including natural gas transmission and distribution pipelines), hazardous liquid pipelines, and liquefied natural gas facilities with representatives of the energy sector;\n**(5)**\nto develop workforce development curricula for the energy sector relating to physical security and cybersecurity for natural gas pipelines (including natural gas transmission and distribution pipelines), hazardous liquid pipelines, and liquefied natural gas facilities; and\n**(6)**\nto provide technical tools to help the energy sector voluntarily evaluate, prioritize, and improve physical security and cybersecurity capabilities of natural gas pipelines (including natural gas transmission and distribution pipelines), hazardous liquid pipelines, and liquefied natural gas facilities.\n#### 3. Savings clause\nNothing in this Act shall be construed to modify the authority of any Federal agency other than the Department of Energy relating to physical security or cybersecurity for natural gas pipelines (including natural gas transmission and distribution pipelines), hazardous liquid pipelines, or liquefied natural gas facilities.",
      "versionDate": "2026-01-27",
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
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-25T17:41:57Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-02-25T17:41:57Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-02-25T17:41:57Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2026-02-25T17:41:57Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-25T17:41:57Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2026-02-25T17:41:57Z"
          },
          {
            "name": "Pipelines",
            "updateDate": "2026-02-25T17:41:57Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-25T17:41:57Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2026-02-25T17:41:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-02-02T14:59:30Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7272ih.xml"
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
      "title": "Pipeline Cybersecurity Preparedness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pipeline Cybersecurity Preparedness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Energy to carry out a program relating to physical security and cybersecurity for pipelines and liquefied natural gas facilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:27Z"
    }
  ]
}
```
