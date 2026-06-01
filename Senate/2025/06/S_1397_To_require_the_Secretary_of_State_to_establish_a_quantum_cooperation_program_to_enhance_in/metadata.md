# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1397?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1397
- Title: International Quantum Research Exchange Act
- Congress: 119
- Bill type: S
- Bill number: 1397
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2025-10-09T03:26:15Z
- Update date including text: 2025-10-09T03:26:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 92.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 92.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1397",
    "number": "1397",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "International Quantum Research Exchange Act",
    "type": "S",
    "updateDate": "2025-10-09T03:26:15Z",
    "updateDateIncludingText": "2025-10-09T03:26:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 92.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
            "date": "2025-06-18T18:17:23Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-05T14:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-09T20:44:51Z",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "IN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "DE"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1397is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1397\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mrs. Shaheen (for herself and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require the Secretary of State to establish a quantum cooperation program to enhance international cooperation in quantum information science.\n#### 1. Short title\nThis Act may be cited as the International Quantum Research Exchange Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the following:\n**(A)**\nThe Committee on Foreign Relations of the Senate.\n**(B)**\nThe Committee on Foreign Affairs of the House of Representatives.\n**(C)**\nThe Committee on Commerce, Science, and Transportation of the Senate.\n**(D)**\nThe Committee on Energy and Commerce of the House of Representatives.\n**(2) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n**(3) Quantum Information Science**\nThe term quantum information science means the use of the laws of quantum physics for the storage, transmission, manipulation, computing, or measurement of information.\n#### 3. Department of State International Quantum Cooperation Program\n##### (a) In general\nThe Secretary of State shall establish and carry out a program\u2014\n**(1)**\nto enhance international cooperation in quantum information science through the competitive award of matching grants to institutions of higher education or eligible nonprofit organizations (or consortia thereof) engaged in international collaborative research; and\n**(2)**\nto support international scientist exchange programs, including exchange programs that vary in length from multi-day to multi-year visits.\n##### (b) Program Alignment\n**(1) Coordination**\nIn carrying out the program under subsection (a), the Secretary of State shall coordinate with\u2014\n**(A)**\nthe Director of the Office of Science and Technology Policy;\n**(B)**\nthe Director of the National Quantum Coordination Office (established under section 102(a) of the National Quantum Initiative Act ( 15 U.S.C. 8812(a) ));\n**(C)**\nthe Co-Chairs of the Subcommittee on Quantum Information Science of the National Science and Technology Council (established under section 103(a) of the National Quantum Initiative Act ( 15 U.S.C. 8813(a) ); and\n**(D)**\nthe Co-Chairs of the Subcommittee on the Economic and Security Implications of Quantum Information Science of the National Science and Technology Council (established under section 105(a) of the National Quantum Initiative Act ( 15 U.S.C. 8814a(a) ).\n**(2) Strategic alignment**\nIn carrying out the program under subsection (a), the Secretary of State shall\u2014\n**(A)**\nensure alignment with the National Quantum Information Science Strategy; and\n**(B)**\nonly fund collaborative research programs with countries who have signed quantum cooperation statements with the United States.\n**(3) Research Security**\nThe activities authorized under this section shall be carried out in a manner consistent with the following:\n**(A)**\nSubtitle D of title VI of the Research and Development, Competition, and Innovation Act (division B of Public Law 117\u2013167 ; 42 U.S.C. 19231 et seq. ).\n**(B)**\nNational Security Presidential Memorandum\u201333 (relating to supported research and development national policy), issued January 2021, and its implementation guidance on research security and research integrity, issued January 2022, or any successor policy document or guidance related to strengthening protections on research and development, funded by the Federal Government, against the influence and exploitation of foreign governments.\n##### (c) Consultation\nIn developing and operating the program required under subsection (a), the Secretary of State shall consult with\u2014\n**(1)**\nthe appropriate congressional committees;\n**(2)**\nthe Special Envoy for Critical and Emerging Technologies;\n**(3)**\nUnited States industry leaders;\n**(4)**\nany technology experts the Secretary considers relevant, including experts from academia; and\n**(5)**\nrepresentatives from any United States Government agency the Secretary considers relevant.\n##### (d) Annual report\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter, the Secretary shall submit to the appropriate congressional committees a report that contains the following elements:\n**(1)**\nA description of the activities pursued under the authorities of this section during the prior year.\n**(2)**\nA list of priority countries with which the Department of State seeks to pursue increased collaboration on quantum information science.\n##### (e) Authorization of Appropriations\nThere is authorized to be appropriated to carry out the program required by subsection (a) $20,000,000 for fiscal year 2026.\n##### (f) Sunset\nThe authorities under this section shall terminate on the date that is 10 years after the date of the enactment of this title.",
      "versionDate": "2025-04-09",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1397rs.xml",
      "text": "II\nCalendar No. 92\n119th CONGRESS\n1st Session\nS. 1397\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mrs. Shaheen (for herself, Mr. Young , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nJune 18, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the Secretary of State to establish a quantum cooperation program to enhance international cooperation in quantum information science.\n#### 1. Short title\nThis Act may be cited as the International Quantum Research Exchange Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the following:\n**(A)**\nThe Committee on Foreign Relations of the Senate.\n**(B)**\nThe Committee on Foreign Affairs of the House of Representatives.\n**(C)**\nThe Committee on Commerce, Science, and Transportation of the Senate.\n**(D)**\nThe Committee on Energy and Commerce of the House of Representatives.\n**(2) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n**(3) Quantum Information Science**\nThe term quantum information science means the use of the laws of quantum physics for the storage, transmission, manipulation, computing, or measurement of information.\n#### 3. Department of State International Quantum Cooperation Program\n##### (a) In general\nThe Secretary of State shall establish and carry out a program\u2014\n**(1)**\nto enhance international cooperation in quantum information science through the competitive award of matching grants to institutions of higher education or eligible nonprofit organizations (or consortia thereof) engaged in international collaborative research; and\n**(2)**\nto support international scientist exchange programs, including exchange programs that vary in length from multi-day to multi-year visits.\n##### (b) Program Alignment\n**(1) Coordination**\nIn carrying out the program under subsection (a), the Secretary of State shall coordinate with\u2014\n**(A)**\nthe Director of the Office of Science and Technology Policy;\n**(B)**\nthe Director of the National Quantum Coordination Office (established under section 102(a) of the National Quantum Initiative Act ( 15 U.S.C. 8812(a) ));\n**(C)**\nthe Co-Chairs of the Subcommittee on Quantum Information Science of the National Science and Technology Council (established under section 103(a) of the National Quantum Initiative Act ( 15 U.S.C. 8813(a) ); and\n**(D)**\nthe Co-Chairs of the Subcommittee on the Economic and Security Implications of Quantum Information Science of the National Science and Technology Council (established under section 105(a) of the National Quantum Initiative Act ( 15 U.S.C. 8814a(a) ).\n**(2) Strategic alignment**\nIn carrying out the program under subsection (a), the Secretary of State shall\u2014\n**(A)**\nensure alignment with the National Quantum Information Science Strategy; and\n**(B)**\nonly fund collaborative research programs with countries who have signed quantum cooperation statements with the United States.\n**(3) Research Security**\nThe activities authorized under this section shall be carried out in a manner consistent with the following:\n**(A)**\nSubtitle D of title VI of the Research and Development, Competition, and Innovation Act (division B of Public Law 117\u2013167 ; 42 U.S.C. 19231 et seq. ).\n**(B)**\nNational Security Presidential Memorandum\u201333 (relating to supported research and development national policy), issued January 2021, and its implementation guidance on research security and research integrity, issued January 2022, or any successor policy document or guidance related to strengthening protections on research and development, funded by the Federal Government, against the influence and exploitation of foreign governments.\n##### (c) Consultation\nIn developing and operating the program required under subsection (a), the Secretary of State shall consult with\u2014\n**(1)**\nthe appropriate congressional committees;\n**(2)**\nthe Special Envoy for Critical and Emerging Technologies;\n**(3)**\nUnited States industry leaders;\n**(4)**\nany technology experts the Secretary considers relevant, including experts from academia; and\n**(5)**\nrepresentatives from any United States Government agency the Secretary considers relevant.\n##### (d) Annual report\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter, the Secretary shall submit to the appropriate congressional committees a report that contains the following elements:\n**(1)**\nA description of the activities pursued under the authorities of this section during the prior year.\n**(2)**\nA list of priority countries with which the Department of State seeks to pursue increased collaboration on quantum information science.\n##### (e) Authorization of Appropriations\nThere is authorized to be appropriated to carry out the program required by subsection (a) $20,000,000 for fiscal year 2026.\n##### (f) Sunset\nThe authorities under this section shall terminate on the date that is 10 years after the date of the enactment of this title.",
      "versionDate": "2025-06-18",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-06-12T20:11:55Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-12T20:11:39Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-12T20:11:27Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-06-12T20:11:04Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-06-12T20:12:04Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-06-12T20:10:47Z"
          },
          {
            "name": "International scientific cooperation",
            "updateDate": "2025-06-12T20:10:56Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-06-12T20:12:12Z"
          },
          {
            "name": "Science and engineering education",
            "updateDate": "2025-06-12T20:12:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-22T20:37:48Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1397is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1397rs.xml"
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
      "title": "International Quantum Research Exchange Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-02T21:33:19Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "International Quantum Research Exchange Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "International Quantum Research Exchange Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of State to establish a quantum cooperation program to enhance international cooperation in quantum information science.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:25Z"
    }
  ]
}
```
