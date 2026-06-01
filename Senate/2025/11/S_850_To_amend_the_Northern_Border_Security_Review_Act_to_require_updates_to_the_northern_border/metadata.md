# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/850?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/850
- Title: Northern Border Security Enhancement and Review Act
- Congress: 119
- Bill type: S
- Bill number: 850
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2025-11-05T03:53:12Z
- Update date including text: 2025-11-05T03:53:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2025-11-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 256.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul without amendment. Without written report.
- 2025-11-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 256.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/850",
    "number": "850",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Northern Border Security Enhancement and Review Act",
    "type": "S",
    "updateDate": "2025-11-05T03:53:12Z",
    "updateDateIncludingText": "2025-11-05T03:53:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 256.",
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
            "date": "2025-11-03T22:06:58Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-05T17:09:03Z",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "ND"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "ME"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s850is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 850\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Ms. Hassan (for herself, Mr. Cramer , Mrs. Gillibrand , and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend the Northern Border Security Review Act to require updates to the northern border threat analysis and northern border strategy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Northern Border Security Enhancement and Review Act .\n#### 2. Northern border threat analysis and strategy\n##### (a) Northern border threat analysis\nSection 3(a) of the Northern Border Security Review Act ( Public Law 114\u2013267 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking 180 days after the date of enactment of this Act and inserting September 2, 2025, and every 3 years thereafter ;\n**(2)**\nby redesignating paragraphs (2), (3), and (4) as paragraphs (3), (4), and (5), respectively; and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) an assessment of recent changes in the amount and demographics of apprehensions at the Northern Border, including an analysis of apprehension changes at the sector level. .\n##### (b) Northern border strategy updates\nSection 3 of the Northern Border Security Review Act ( Public Law 114\u2013267 ) is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Northern border strategy updates The Secretary of Homeland Security shall update the Department of Homeland Security\u2019s Northern Border strategy not later than September 2, 2026, and every 5 years thereafter, and shall incorporate the results of the most recent threat analysis in each such update. .\n##### (c) Classified briefings\nSection 3 of the Northern Border Security Review Act, as amended by subsections (a) and (b), is further amended by adding at the end the following:\n(e) Classified briefings Not later than 30 days after the submission of each threat analysis pursuant to subsection (a), the Secretary of Homeland Security shall provide a classified briefing regarding such analysis to the appropriate congressional committees. .\n##### (d) Implementation of certain Government Accountability Office recommendations\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Homeland Security, acting through the Executive Assistant Commissioner of Air and Marine Operations of U.S. Customs and Border Protection, shall develop performance measures to assess the effectiveness of Air and Marine Operations at securing the northern border between ports of entry in the air and maritime environments.\n#### 3. No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act or the amendments made by this Act.",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s850rs.xml",
      "text": "II\nCalendar No. 256\n119th CONGRESS\n1st Session\nS. 850\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Ms. Hassan (for herself, Mr. Cramer , Mrs. Gillibrand , Ms. Collins , and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nNovember 3, 2025 Reported by Mr. Paul , without amendment\nA BILL\nTo amend the Northern Border Security Review Act to require updates to the northern border threat analysis and northern border strategy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Northern Border Security Enhancement and Review Act .\n#### 2. Northern border threat analysis and strategy\n##### (a) Northern border threat analysis\nSection 3(a) of the Northern Border Security Review Act ( Public Law 114\u2013267 ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking 180 days after the date of enactment of this Act and inserting September 2, 2025, and every 3 years thereafter ;\n**(2)**\nby redesignating paragraphs (2), (3), and (4) as paragraphs (3), (4), and (5), respectively; and\n**(3)**\nby inserting after paragraph (1) the following:\n(2) an assessment of recent changes in the amount and demographics of apprehensions at the Northern Border, including an analysis of apprehension changes at the sector level. .\n##### (b) Northern border strategy updates\nSection 3 of the Northern Border Security Review Act ( Public Law 114\u2013267 ) is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Northern border strategy updates The Secretary of Homeland Security shall update the Department of Homeland Security\u2019s Northern Border strategy not later than September 2, 2026, and every 5 years thereafter, and shall incorporate the results of the most recent threat analysis in each such update. .\n##### (c) Classified briefings\nSection 3 of the Northern Border Security Review Act, as amended by subsections (a) and (b), is further amended by adding at the end the following:\n(e) Classified briefings Not later than 30 days after the submission of each threat analysis pursuant to subsection (a), the Secretary of Homeland Security shall provide a classified briefing regarding such analysis to the appropriate congressional committees. .\n##### (d) Implementation of certain Government Accountability Office recommendations\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Homeland Security, acting through the Executive Assistant Commissioner of Air and Marine Operations of U.S. Customs and Border Protection, shall develop performance measures to assess the effectiveness of Air and Marine Operations at securing the northern border between ports of entry in the air and maritime environments.\n#### 3. No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act or the amendments made by this Act.",
      "versionDate": "2025-11-03",
      "versionType": "Reported in Senate"
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-05-13T14:55:50Z"
          },
          {
            "name": "Canada",
            "updateDate": "2025-05-13T14:55:50Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-13T14:55:50Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-13T14:55:50Z"
          },
          {
            "name": "North America",
            "updateDate": "2025-05-13T14:55:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-05-12T16:43:29Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s850is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-11-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s850rs.xml"
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
      "title": "Northern Border Security Enhancement and Review Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-05T03:53:12Z"
    },
    {
      "title": "Northern Border Security Enhancement and Review Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-04T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Northern Border Security Enhancement and Review Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Northern Border Security Review Act to require updates to the northern border threat analysis and the northern border strategy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T16:18:19Z"
    }
  ]
}
```
