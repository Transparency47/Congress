# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1413?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1413
- Title: To amend title 38, United States Code, to require that domiciliary facilities of the Department of Veterans Affairs and State homes that provide housing to veterans have resident advocates.
- Congress: 119
- Bill type: HR
- Bill number: 1413
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2025-06-13T19:16:15Z
- Update date including text: 2025-06-13T19:16:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-21 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-21 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1413",
    "number": "1413",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To amend title 38, United States Code, to require that domiciliary facilities of the Department of Veterans Affairs and State homes that provide housing to veterans have resident advocates.",
    "type": "HR",
    "updateDate": "2025-06-13T19:16:15Z",
    "updateDateIncludingText": "2025-06-13T19:16:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-21T17:56:55Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1413ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1413\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require that domiciliary facilities of the Department of Veterans Affairs and State homes that provide housing to veterans have resident advocates.\n#### 1. Requirement of resident advocate in a domiciliary facility of the Department of Veterans Affairs or State home\n##### (a) Domiciliary facilities of the Department of Veterans Affairs\nSubchapter I of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section (and conforming the table of sections at the beginning of such chapter accordingly):\n1720M. Resident advocates in domiciliary facilities of the Department (a) Requirement The Secretary shall employ in each domiciliary facility of the Department a resident advocate. (b) Duties A resident advocate shall have duties that include the following: (1) To serve as a liaison between veterans in the domiciliary facility and the Secretary. (2) To receive complaints from such veterans, transmit such complaints to the director of such domiciliary facility, and respond to such complaints. (3) When the resident advocate determines it appropriate, to submit such a complaint to the Secretary, the Inspector General of the Department. .\n##### (b) State homes\nSection 1741 of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (g) as subsection (h); and\n**(2)**\nby inserting, after subsection (f), the following new subsection (g):\n(g) To be eligible for payment for domiciliary care provided to a veteran in a State home under this section, a State shall employ in such State home a resident advocate. A resident advocate shall have duties that include the following: (1) To serve as a liaison between veterans in such State home and the State. (2) To receive complaints from such veterans, transmit such complaints to the director of the State home, and respond to such complaints. (3) When the resident advocate determines it appropriate, to submit such a complaint to the Secretary, the Inspector General of the Department, or an appropriate State official. .",
      "versionDate": "2025-02-18",
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
            "name": "Disability assistance",
            "updateDate": "2025-06-13T19:15:55Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-06-13T19:16:06Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-13T19:16:11Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-06-13T19:16:00Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-06-13T19:15:49Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-13T19:16:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:50:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1413",
          "measure-number": "1413",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1413v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires the Department of Veterans Affairs (VA) to employ a resident advocate in each of its domiciliary facilities. The resident advocate must (1) serve as liaison between veterans in the facilities and the VA; (2) receive complaints from such veterans, transmit the complaints to the directors of the facilities, and respond to such complaints; and (3) submit complaints to the Office of Inspector General of the VA when appropriate.</p><p>Additionally, state homes must also employ a resident advocate in order to be eligible for payment from the VA for\u00a0domiciliary care provided to a veteran. A <em>state home</em> is a home established by a state or tribe for veterans who are disabled by age, disease, or otherwise and are incapable of earning a living because of such disability. The term also includes a home that furnishes nursing home care for veterans.</p>"
        },
        "title": "To amend title 38, United States Code, to require that domiciliary facilities of the Department of Veterans Affairs and State homes that provide housing to veterans have resident advocates."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1413.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Department of Veterans Affairs (VA) to employ a resident advocate in each of its domiciliary facilities. The resident advocate must (1) serve as liaison between veterans in the facilities and the VA; (2) receive complaints from such veterans, transmit the complaints to the directors of the facilities, and respond to such complaints; and (3) submit complaints to the Office of Inspector General of the VA when appropriate.</p><p>Additionally, state homes must also employ a resident advocate in order to be eligible for payment from the VA for\u00a0domiciliary care provided to a veteran. A <em>state home</em> is a home established by a state or tribe for veterans who are disabled by age, disease, or otherwise and are incapable of earning a living because of such disability. The term also includes a home that furnishes nursing home care for veterans.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1413"
    },
    "title": "To amend title 38, United States Code, to require that domiciliary facilities of the Department of Veterans Affairs and State homes that provide housing to veterans have resident advocates."
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Department of Veterans Affairs (VA) to employ a resident advocate in each of its domiciliary facilities. The resident advocate must (1) serve as liaison between veterans in the facilities and the VA; (2) receive complaints from such veterans, transmit the complaints to the directors of the facilities, and respond to such complaints; and (3) submit complaints to the Office of Inspector General of the VA when appropriate.</p><p>Additionally, state homes must also employ a resident advocate in order to be eligible for payment from the VA for\u00a0domiciliary care provided to a veteran. A <em>state home</em> is a home established by a state or tribe for veterans who are disabled by age, disease, or otherwise and are incapable of earning a living because of such disability. The term also includes a home that furnishes nursing home care for veterans.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1413"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1413ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require that domiciliary facilities of the Department of Veterans Affairs and State homes that provide housing to veterans have resident advocates.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:27Z"
    },
    {
      "title": "To amend title 38, United States Code, to require that domiciliary facilities of the Department of Veterans Affairs and State homes that provide housing to veterans have resident advocates.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T09:05:38Z"
    }
  ]
}
```
