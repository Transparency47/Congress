# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/244?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/244
- Title: ROUTERS Act
- Congress: 119
- Bill type: S
- Bill number: 244
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2025-12-06T06:36:53Z
- Update date including text: 2025-12-06T06:36:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- 2025-06-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-25.
- 2025-06-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-25.
- 2025-06-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 87.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.
- 2025-06-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-25.
- 2025-06-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-25.
- 2025-06-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 87.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/244",
    "number": "244",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "ROUTERS Act",
    "type": "S",
    "updateDate": "2025-12-06T06:36:53Z",
    "updateDateIncludingText": "2025-12-06T06:36:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 87.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-25.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with amendments. With written report No. 119-25.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-06-02T20:59:35Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-12T14:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-24T17:43:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "NM"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s244is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 244\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mrs. Blackburn (for herself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Secretary of Commerce, acting through the Assistant Secretary of Commerce for Communications and Information, to conduct a study of the national security risks posed by consumer routers, modems, and devices that combine a modem and router, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Removing Our Unsecure Technologies to Ensure Reliability and Security Act or the ROUTERS Act .\n#### 2. Study of national security risks posed by certain routers and modems\n##### (a) In general\nThe Secretary shall conduct a study of the national security risks posed by consumer routers, modems, and devices that combine a modem and router that are designed, developed, manufactured, or supplied by persons owned by, controlled by, or subject to the influence of a covered country.\n##### (b) Report to Congress\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the results of the study conducted under subsection (a).\n##### (c) Definitions\nIn this section:\n**(1) Covered country**\nThe term covered country means a country specified in section 4872(d)(2) of title 10, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Commerce, in consultation with the Assistant Secretary of Commerce for Communications and Information.",
      "versionDate": "2025-01-24",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s244rs.xml",
      "text": "II\nCalendar No. 87\n119th CONGRESS\n1st Session\nS. 244\n[Report No. 119\u201325]\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mrs. Blackburn (for herself, Mr. Luj\u00e1n , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nJune 2, 2025 Reported by Mr. Cruz , with amendments Omit the part struck through and insert the parts printed in italic\nA BILL\nTo direct the Secretary of Commerce, acting through the Assistant Secretary of Commerce for Communications and Information, to conduct a study of the national security risks posed by consumer routers, modems, and devices that combine a modem and router, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Removing Our Unsecure Technologies to Ensure Reliability and Security Act or the ROUTERS Act .\n#### 2. Study of national security risks posed by certain routers and modems\n##### (a) In general\nThe Secretary shall conduct a study of the national security risks and cybersecurity vulnerabilities posed by consumer routers, modems, and devices that combine a modem and router that are designed, developed, manufactured, or supplied by persons owned by, controlled by, or subject to the influence of a covered country.\n##### (b) Report to Congress\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the results of the study conducted under subsection (a).\n##### (c) Definitions\nIn this section:\n**(1) Covered country**\nThe term covered country means a country specified in section 4872(d)(2) 4872(f)(2) of title 10, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Commerce, in consultation with the Assistant Secretary of Commerce for Communications and Information.",
      "versionDate": "2025-06-02",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-29",
        "text": "Received in the Senate."
      },
      "number": "866",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ROUTERS Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
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
            "updateDate": "2025-03-18T17:16:08Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-03-18T17:16:08Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-18T17:16:08Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-03-18T17:16:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-01T13:30:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
    "originChamber": "Senate",
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
          "measure-id": "id119s244",
          "measure-number": "244",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s244v00",
            "update-date": "2025-03-04"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Removing Our Unsecure Technologies to Ensure Reliability and Security Act or the ROUTERS Act</strong></p><p>This bill requires the Department of Commerce, in consultation with the National Telecommunications and Information Administration, to conduct a study on the national security risks posed by consumer routers and modems (including devices that combine a modem and router) and provide the results of the study to Congress. The study must address devices developed, manufactured, or supplied\u00a0by persons (i.e., individuals and entities)\u00a0owned by, controlled by, or subject to the influence of China, Iran, North Korea, or Russia.\u00a0</p><p>\u00a0</p>"
        },
        "title": "ROUTERS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s244.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Removing Our Unsecure Technologies to Ensure Reliability and Security Act or the ROUTERS Act</strong></p><p>This bill requires the Department of Commerce, in consultation with the National Telecommunications and Information Administration, to conduct a study on the national security risks posed by consumer routers and modems (including devices that combine a modem and router) and provide the results of the study to Congress. The study must address devices developed, manufactured, or supplied\u00a0by persons (i.e., individuals and entities)\u00a0owned by, controlled by, or subject to the influence of China, Iran, North Korea, or Russia.\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119s244"
    },
    "title": "ROUTERS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Removing Our Unsecure Technologies to Ensure Reliability and Security Act or the ROUTERS Act</strong></p><p>This bill requires the Department of Commerce, in consultation with the National Telecommunications and Information Administration, to conduct a study on the national security risks posed by consumer routers and modems (including devices that combine a modem and router) and provide the results of the study to Congress. The study must address devices developed, manufactured, or supplied\u00a0by persons (i.e., individuals and entities)\u00a0owned by, controlled by, or subject to the influence of China, Iran, North Korea, or Russia.\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119s244"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s244is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s244rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "ROUTERS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T11:03:20Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "ROUTERS Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-04T03:23:23Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Removing Our Unsecure Technologies to Ensure Reliability and Security Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-04T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ROUTERS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Removing Our Unsecure Technologies to Ensure Reliability and Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Commerce, acting through the Assistant Secretary of Commerce for Communications and Information, to conduct a study of the national security risks posed by consumer routers, modems, and devices that combine a modem and router, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:24Z"
    }
  ]
}
```
