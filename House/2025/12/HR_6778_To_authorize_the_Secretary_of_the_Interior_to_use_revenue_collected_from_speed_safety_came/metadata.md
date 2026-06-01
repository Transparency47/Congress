# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6778?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6778
- Title: Parkway Safety and Reinvestment Act
- Congress: 119
- Bill type: HR
- Bill number: 6778
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-04-02T18:17:35Z
- Update date including text: 2026-04-02T18:17:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-19 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-26 - Committee: Subcommittee Hearings Held
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-19 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-26 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6778",
    "number": "6778",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Parkway Safety and Reinvestment Act",
    "type": "HR",
    "updateDate": "2026-04-02T18:17:35Z",
    "updateDateIncludingText": "2026-04-02T18:17:35Z"
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
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:07:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-26T19:33:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-19T14:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6778ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6778\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Beyer introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize the Secretary of the Interior to use revenue collected from speed safety cameras on highways in the National Park System for maintenance and construction purposes.\n#### 1. Short title\nThis Act may be cited as the Parkway Safety and Reinvestment Act .\n#### 2. Speed safety cameras in the National Park System\n##### (a) Citation authority\nSubject to subsection (d), if a vehicle is recorded by a speed safety camera while being operated in violation of an applicable traffic regulation for a covered highway, the Secretary may, with respect to the responsible party\u2014\n**(1)**\nissue a citation; and\n**(2)**\nafter providing the responsible party with notice and opportunity for a hearing on the record, assess a civil penalty.\n##### (b) Maintenance and construction purposes\nNotwithstanding section 1402 of the Victims of Crime Act of 1984 ( 34 U.S.C. 20101 ), the Secretary may collect and expend, without subsequent appropriation, any revenues obtained by the Federal Government from speed safety camera citations issued pursuant to subparagraph (a) for\u2014\n**(1)**\nthe construction and maintenance of the covered highways and parking facilities of the unit of the National Park System in which the citation was issued; and\n**(2)**\nthe installation, repair, and maintenance of speed safety cameras.\n##### (c) Authorization To enter into agreements\nIn carrying out this Act, the Secretary may enter into a contract or other appropriate agreement with a person for the purposes of installing, repairing, maintaining, or replacing speed safety cameras.\n##### (d) State law\nIn carrying out this Act, the Secretary may only use a speed safety camera in accordance with the State law of the State in which the applicable portion of covered highway is located.\n#### 3. Definitions\nIn this Act:\n**(1) Covered highway**\nThe term covered highway means a highway\u2014\n**(A)**\nadministered by the Secretary of the Interior; and\n**(B)**\nlocated within a unit of the National Park System.\n**(2) Highway**\nThe term highway has the meaning given the term in subparagraphs (A) and (B) of section 101(a)(11) of title 23, United States Code.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(4) Speed safety camera**\nThe term speed safety camera means a camera that captures a still or moving image of a vehicle for the purpose of traffic enforcement, and does not include handheld radar and other devices operated by law enforcement officers to make an on-the-scene traffic stop, issue a traffic citation, or other enforcement action at the time of the violation.\n**(5) Speed safety camera citation**\nThe term speed safety camera citation means a traffic citation processed by an automated traffic enforcement system owned or operated by the National Park Service for a traffic violation occurring on the covered highway.\n**(6) State**\nThe term State has the meaning given such term in section 31 of title 18, United States Code.",
      "versionDate": "2025-12-17",
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
            "name": "Civil actions and liability",
            "updateDate": "2026-04-02T18:17:15Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-04-02T18:17:34Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2026-04-02T18:17:08Z"
          },
          {
            "name": "Transportation programs funding",
            "updateDate": "2026-04-02T18:17:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-01-21T16:13:25Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6778ih.xml"
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
      "title": "Parkway Safety and Reinvestment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parkway Safety and Reinvestment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of the Interior to use revenue collected from speed safety cameras on highways in the National Park System for maintenance and construction purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:41Z"
    }
  ]
}
```
