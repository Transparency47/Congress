# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/865?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/865
- Title: Lobbying Disclosure Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 865
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2025-12-18T12:48:41Z
- Update date including text: 2025-12-18T12:48:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2025-11-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 258.
- 2025-12-16 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8794; text: CR S8794)
- 2025-12-16 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-17 - Floor: Message on Senate action sent to the House.
- 2025-12-17 09:59:00 - Floor: Received in the House.
- 2025-12-17 10:22:02 - Floor: Held at the desk.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2025-11-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 258.
- 2025-12-16 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8794; text: CR S8794)
- 2025-12-16 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-17 - Floor: Message on Senate action sent to the House.
- 2025-12-17 09:59:00 - Floor: Received in the House.
- 2025-12-17 10:22:02 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/865",
    "number": "865",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Lobbying Disclosure Improvement Act",
    "type": "S",
    "updateDate": "2025-12-18T12:48:41Z",
    "updateDateIncludingText": "2025-12-18T12:48:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-17",
      "actionTime": "10:22:02",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-17",
      "actionTime": "09:59:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S8794; text: CR S8794)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 258.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-11-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-11-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
            "date": "2025-11-03T22:05:11Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-05T18:38:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s865is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 865\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Peters (for himself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend the Lobbying Disclosure Act of 1995 to require certain disclosures by registrants regarding exemptions under the Foreign Agents Registration Act of 1938, as amended.\n#### 1. Short title\nThis Act may be cited as the Lobbying Disclosure Improvement Act .\n#### 2. Registrant disclosure regarding foreign agent registration exemption\nSection 4(b) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1603(b) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) a statement as to whether the registrant is exempt under section 3(h) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 613(h) ). .",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s865rs.xml",
      "text": "II\nCalendar No. 258\n119th CONGRESS\n1st Session\nS. 865\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Peters (for himself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nNovember 3, 2025 Reported by Mr. Paul , without amendment\nA BILL\nTo amend the Lobbying Disclosure Act of 1995 to require certain disclosures by registrants regarding exemptions under the Foreign Agents Registration Act of 1938, as amended.\n#### 1. Short title\nThis Act may be cited as the Lobbying Disclosure Improvement Act .\n#### 2. Registrant disclosure regarding foreign agent registration exemption\nSection 4(b) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1603(b) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) a statement as to whether the registrant is exempt under section 3(h) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 613(h) ). .",
      "versionDate": "2025-11-03",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s865es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 865\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Lobbying Disclosure Act of 1995 to require certain disclosures by registrants regarding exemptions under the Foreign Agents Registration Act of 1938, as amended.\n#### 1. Short title\nThis Act may be cited as the Lobbying Disclosure Improvement Act .\n#### 2. Registrant disclosure regarding foreign agent registration exemption\nSection 4(b) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1603(b) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) a statement as to whether the registrant is exempt under section 3(h) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 613(h) ). .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-03-05",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1887",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lobbying Disclosure Improvement Act",
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
            "name": "Government information and archives",
            "updateDate": "2025-08-07T17:51:18Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-08-07T17:51:18Z"
          },
          {
            "name": "Public participation and lobbying",
            "updateDate": "2025-08-07T17:51:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-09T19:12:03Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s865is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-11-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s865rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s865es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Lobbying Disclosure Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Lobbying Disclosure Improvement Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-17T06:28:13Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Lobbying Disclosure Improvement Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-05T04:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lobbying Disclosure Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Lobbying Disclosure Act of 1995 to require certain disclosures by registrants regarding exemptions under the Foreign Agents Registration Act of 1938, as amended.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T16:33:25Z"
    }
  ]
}
```
