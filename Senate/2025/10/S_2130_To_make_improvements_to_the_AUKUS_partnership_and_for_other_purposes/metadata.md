# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2130
- Title: AUKUS Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2130
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-04-01T20:08:05Z
- Update date including text: 2026-04-01T20:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 235.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 235.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2130",
    "number": "2130",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "AUKUS Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-04-01T20:08:05Z",
    "updateDateIncludingText": "2026-04-01T20:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 235.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
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
      "actionDate": "2025-10-30",
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
      "actionDate": "2025-10-22",
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
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
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
            "date": "2025-10-30T15:05:57Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:41Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-18T18:48:16Z",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "VA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "TX"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "DE"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "NE"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "CT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "FL"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "AK"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "IA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CO"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NV"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2130is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2130\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Ricketts (for himself, Mr. Kaine , Mr. Cornyn , Mr. Coons , Mrs. Fischer , Mr. Murphy , Mr. Scott of Florida , and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo make improvements to the AUKUS partnership, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AUKUS Improvement Act of 2025 .\n#### 2. Flexibility with respect to certain Arms Export control Act and other arms transfer requirements\nSection 38(l) of the Arms Export Control Act ( 22 U.S.C. 2778(l) ) is amended by adding at the end the following new paragraph:\n(8) Exemption from certain requirements (A) In general Defense articles sold by the United States under this Act may be reexported, retransferred or temporarily imported exclusively between the Government of Australia, the Government of the United Kingdom, or entities eligible under section 126.7(b)(2) of title 22 of the Code of Federal Regulations, or successor regulations. Such transfers shall not require the consent of the President under section 3(a)(2) of this Act, or under section 505(a)(1) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2314(a)(1)(B) ). (B) Intra-company, intra-organizational, and intra-governmental transfers Intra-company, intra-organization, and intra-governmental transfers related to defense articles and defense services described under subparagraph (A) are authorized between officers, employees, and agents who satisfy section 120.64 of title 22 of the Code of Federal Regulations, or successor regulations, including dual or third country nationals who satisfy section 126.18 of title 22 of the Code of Federal Regulations, or successor regulations. .\n#### 3. Elimination of certification requirement for commercial technical assistance or manufacturing license agreements involving Australia and the United Kingdom\nSection 36(d)(2) of the Arms Export Control Act ( 22 U.S.C. 2776(d)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively;\n**(2)**\nby striking A certification and inserting (A) A certification ;\n**(3)**\nin clause (i), as redesignated by paragraph (1), by striking North Atlantic Treaty Organization or Australia, Japan and inserting North Atlantic Treaty Organization (excluding the United Kingdom) or Japan ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(B) A certification under this subsection shall not be required in the case of an agreement for or in Australia or the United Kingdom. .",
      "versionDate": "2025-06-18",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2130rs.xml",
      "text": "II\nCalendar No. 235\n119th CONGRESS\n1st Session\nS. 2130\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Ricketts (for himself, Mr. Kaine , Mr. Cornyn , Mr. Coons , Mrs. Fischer , Mr. Murphy , Mr. Scott of Florida , Mr. Sullivan , Ms. Ernst , Mr. Bennet , Ms. Rosen , and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo make improvements to the AUKUS partnership, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AUKUS Improvement Act of 2025 .\n#### 2. Flexibility with respect to certain Arms Export control Act and other arms transfer requirements\nSection 38(l) of the Arms Export Control Act ( 22 U.S.C. 2778(l) ) is amended by adding at the end the following new paragraph:\n(8) Exemption from certain requirements (A) In general Defense articles sold by the United States under this Act may be reexported, retransferred or temporarily imported exclusively between the Government of Australia, the Government of the United Kingdom, or entities eligible under section 126.7(b)(2) of title 22 of the Code of Federal Regulations, or successor regulations. Such transfers shall not require the consent of the President under section 3(a)(2) of this Act, or under section 505(a)(1) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2314(a)(1)(B) ). (B) Intra-company, intra-organizational, and intra-governmental transfers Intra-company, intra-organization, and intra-governmental transfers related to defense articles and defense services described under subparagraph (A) are authorized between officers, employees, and agents who satisfy section 120.64 of title 22 of the Code of Federal Regulations, or successor regulations, including dual or third country nationals who satisfy section 126.18 of title 22 of the Code of Federal Regulations, or successor regulations. .\n#### 3. Elimination of certification requirement for commercial technical assistance or manufacturing license agreements involving Australia and the United Kingdom\nSection 36(d)(2) of the Arms Export Control Act ( 22 U.S.C. 2776(d)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively;\n**(2)**\nby striking A certification and inserting (A) A certification ;\n**(3)**\nin clause (i), as redesignated by paragraph (1), by striking North Atlantic Treaty Organization or Australia, Japan and inserting North Atlantic Treaty Organization (excluding the United Kingdom) or Japan ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(B) A certification under this subsection shall not be required in the case of an agreement for or in Australia or the United Kingdom. .",
      "versionDate": "2025-10-30",
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
        "actionDate": "2025-08-22",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "5013",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AUKUS Improvement Act of 2025",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-01T20:07:43Z"
          },
          {
            "name": "Alliances",
            "updateDate": "2026-04-01T20:07:58Z"
          },
          {
            "name": "Australia",
            "updateDate": "2026-04-01T20:07:04Z"
          },
          {
            "name": "Europe",
            "updateDate": "2026-04-01T20:07:24Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-04-01T20:08:05Z"
          },
          {
            "name": "Military assistance, sales, and agreements",
            "updateDate": "2026-04-01T20:07:51Z"
          },
          {
            "name": "Oceania",
            "updateDate": "2026-04-01T20:07:17Z"
          },
          {
            "name": "United Kingdom",
            "updateDate": "2026-04-01T20:07:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-17T21:11:00Z"
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
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2130is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2130rs.xml"
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
      "title": "AUKUS Improvement Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:53:13Z"
    },
    {
      "title": "AUKUS Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AUKUS Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to make improvements to the AUKUS partnership, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-03T04:18:23Z"
    }
  ]
}
```
