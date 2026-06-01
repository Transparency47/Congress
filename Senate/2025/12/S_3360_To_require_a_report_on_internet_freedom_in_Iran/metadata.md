# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3360?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3360
- Title: FREEDOM Act
- Congress: 119
- Bill type: S
- Bill number: 3360
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2026-04-15T17:20:06Z
- Update date including text: 2026-04-15T17:20:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 328.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 328.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3360",
    "number": "3360",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "FREEDOM Act",
    "type": "S",
    "updateDate": "2026-04-15T17:20:06Z",
    "updateDateIncludingText": "2026-04-15T17:20:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 328.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
            "date": "2026-02-10T16:34:07Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-29T14:30:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-04T20:33:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-04T20:33:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "PA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "AZ"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3360is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3360\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Ms. Rosen (for herself and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require a report on internet freedom in Iran.\n#### 1. Short title\nThis Act may be cited as the Feasibility Review of Emerging Equipment for Digital Open Media Act or the FREEDOM Act .\n#### 2. Report on internet freedom in Iran\n##### (a) In general\nNot later than 120 days after the date of the enactment of the Act, the Secretary of State, in consultation with the Federal Communications Commission and the Department of the Treasury, shall prepare and submit to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a report that updates and supplements the report required under section 5124 of the National Defense Authorization Act for Fiscal Year 2025 ( 22 U.S.C. 8754a ).\n##### (b) Additional matters To be included\nUpdates to the strategy required in section 5124 of the National Defense Authorization Act for Fiscal Year 2025 ( 22 U.S.C. 8754a ), shall also include the following:\n**(1)**\nAn assessment of the feasibility of using direct-to-cell wireless communications technologies to expand internet access for the people of Iran, including technical, regulatory, and security considerations.\n**(2)**\nAn analysis of how drone-based platforms, signal jamming technologies, and related countermeasures could impact the feasibility, security, economics, and resilience of such direct-to-cell wireless communications.\n**(3)**\nA survey of terrestrial and non-terrestrial telecommunications service providers currently active in Iran, including\u2014\n**(A)**\nwhether such providers are state-owned or state-controlled;\n**(B)**\nthe extent of foreign participation or investment in such providers; and\n**(C)**\nthe implications of such ownership and control for communications freedom and censorship.\n**(4)**\nAny other relevant information to assess the opportunities and risks associated with terrestrial and non-terrestrial communications technologies in Iran.\n##### (c) Form\nThe report required by subsection (a) shall be submitted in unclassified form, but may include a classified annex.",
      "versionDate": "2025-12-04",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3360rs.xml",
      "text": "II\nCalendar No. 328\n119th CONGRESS\n2d Session\nS. 3360\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Ms. Rosen (for herself, Mr. McCormick , Mr. Gallego , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nFebruary 10, 2026 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require a report on internet freedom in Iran.\n#### 1. Short title\nThis Act may be cited as the Feasibility Review of Emerging Equipment for Digital Open Media Act or the FREEDOM Act .\n#### 2. Report on internet freedom in Iran\n##### (a) In general\nNot later than 120 days after the date of the enactment of the Act, the Secretary of State, in consultation with the Federal Communications Commission and the Department of the Treasury, shall prepare and submit to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a report that updates and supplements the report required under section 5124 of the National Defense Authorization Act for Fiscal Year 2025 ( 22 U.S.C. 8754a ).\n##### (b) Additional matters To be included\nUpdates to the strategy required in section 5124 of the National Defense Authorization Act for Fiscal Year 2025 ( 22 U.S.C. 8754a ), shall also include the following:\n**(1)**\nAn assessment of the feasibility of using direct-to-cell wireless communications technologies to expand internet access for the people of Iran, including technical, regulatory, and security considerations.\n**(2)**\nAn analysis of how drone-based platforms, signal jamming technologies, and related countermeasures could impact the feasibility, security, economics, and resilience of such direct-to-cell wireless communications.\n**(3)**\nA survey of terrestrial and non-terrestrial telecommunications service providers currently active in Iran, including\u2014\n**(A)**\nwhether such providers are state-owned or state-controlled;\n**(B)**\nthe extent of foreign participation or investment in such providers; and\n**(C)**\nthe implications of such ownership and control for communications freedom and censorship.\n**(4)**\nAny other relevant information to assess the opportunities and risks associated with terrestrial and non-terrestrial communications technologies in Iran.\n##### (c) Form\nThe report required by subsection (a) shall be submitted in unclassified form, but may include a classified annex.",
      "versionDate": "2026-02-10",
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
        "actionDate": "2025-12-04",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "6469",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FREEDOM Act",
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
            "name": "Aviation and airports",
            "updateDate": "2026-04-15T17:19:59Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-15T17:19:46Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-15T17:19:37Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-04-15T17:19:29Z"
          },
          {
            "name": "Iran",
            "updateDate": "2026-04-15T17:19:14Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2026-04-15T17:19:21Z"
          },
          {
            "name": "Spacecraft and satellites",
            "updateDate": "2026-04-15T17:20:06Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-04-15T17:19:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-01-08T16:42:27Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3360is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3360rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "FREEDOM Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-12T04:38:20Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Feasibility Review of Emerging Equipment for Digital Open Media Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-12T04:38:20Z"
    },
    {
      "title": "FREEDOM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FREEDOM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Feasibility Review of Emerging Equipment for Digital Open Media Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-30T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a report on internet freedom in Iran.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-30T05:33:25Z"
    }
  ]
}
```
