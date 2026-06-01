# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2684?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2684
- Title: United States - Taiwan Partnership in the Americas Act
- Congress: 119
- Bill type: S
- Bill number: 2684
- Origin chamber: Senate
- Introduced date: 2025-09-02
- Update date: 2026-05-19T11:03:44Z
- Update date including text: 2026-05-19T11:03:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in Senate
- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 242.
- Latest action: 2025-09-02: Introduced in Senate

## Actions

- 2025-09-02 - IntroReferral: Introduced in Senate
- 2025-09-02 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 242.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2684",
    "number": "2684",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "United States - Taiwan Partnership in the Americas Act",
    "type": "S",
    "updateDate": "2026-05-19T11:03:44Z",
    "updateDateIncludingText": "2026-05-19T11:03:44Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 242.",
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
      "actionDate": "2025-09-02",
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
      "actionDate": "2025-09-02",
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
            "date": "2025-10-30T15:36:35Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:53Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-02T20:36:20Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "UT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "VA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NE"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "CO"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OR"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2684is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2684\nIN THE SENATE OF THE UNITED STATES\nSeptember 2, 2025 Mr. Merkley (for himself, Mr. Curtis , Mr. Kaine , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo support countries in Latin America and the Caribbean that maintain official diplomatic relations with Taiwan, to counter efforts by the People's Republic of China to coerce or pressure governments into breaking such ties, to deepen coordination with Taiwan on diplomatic, development, and economic engagement in the Western Hemisphere, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States-Taiwan Partnership in the Americas Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nTaiwan is a democratic partner of the United States, and countries that maintain ties with Taiwan often share our Nation's commitment to transparency, good governance, and human rights.\n**(2)**\nThe People\u2019s Republic of China has pressured Taiwan\u2019s remaining 7 diplomatic allies in Latin America and the Caribbean to sever diplomatic relations with Taiwan by leveraging opaque development deals and backroom pressure.\n**(3)**\nThe United States has an interest in ensuring countries in Latin America and the Caribbean can make sovereign foreign policy decisions free from coercion or financial manipulation by the People's Republic of China.\n#### 3. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto support countries in Latin America and the Caribbean that maintain diplomatic relations with Taiwan;\n**(2)**\nto counter efforts by the People's Republic of China to coerce or pressure governments in the region into breaking diplomatic ties with Taiwan; and\n**(3)**\nto deepen coordination with Taiwan on its development and economic engagement in the Western Hemisphere.\n#### 4. Monitoring the economic influence of the People's Republic of China\n##### (a) Infrastructure influence risk mechanism\nThe Secretary of State shall establish a mechanism to track and respond to infrastructure and development projects by the People's Republic of China in countries that maintain diplomatic relations with Taiwan.\n##### (b) Functions\nThe mechanism required under subsection (a) shall\u2014\n**(1)**\nidentify projects referred to in such subsection that carry strategic risks or involve non-transparent financing;\n**(2)**\ncoordinate appropriate United States diplomatic or technical responses to such projects; and\n**(3)**\nshare relevant information with Congress and with United States allies.\n#### 5. Reporting requirements\n##### (a) Semiannual status report\nThe Secretary of State shall submit semiannual status reports to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives regarding governments in Latin America that have taken steps to discontinue diplomatic relations with Taiwan.\n##### (b) Diplomatic engagement plan\nIf the Secretary of State determines that a government in a country referred to in subsection (a) is taking steps to terminate diplomatic relations with Taiwan, the Secretary, not later than 30 days after such determination, shall submit a report to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives that includes a detailed plan to support the maintenance of official diplomatic relations between such government and Taiwan.\n##### (c) Annual report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for the following 5 years, the Secretary of State shall submit a report to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives that includes\u2014\n**(A)**\nan assessment of the goals, investments, and interests of the People\u2019s Republic of China in Latin America and the Caribbean that maintain diplomatic relations with Taiwan;\n**(B)**\nan overview of the pressure tactics and influence campaigns carried out by the People\u2019 s Republic of China in countries in Latin America and the Caribbean that maintain diplomatic relations with Taiwan; and\n**(C)**\nthe actions taken by the Department of State during the most recent 12-month period to implement this Act by\u2014\n**(i)**\nsupporting Taiwan\u2019s diplomatic partners in Latin America and the Caribbean; and\n**(ii)**\ncountering the efforts of the People\u2019s Republic of China to isolate Taiwan from its Latin American and Caribbean allies.\n**(2) Form**\nEach report required under paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n#### 6. Taiwan\u2013Americas strategic coordination\nThe Secretary of State should take steps to expand United States coordination with countries in Latin America and the Caribbean with respect to Taiwan by\u2014\n**(1)**\ncoordinating joint programming and technical cooperation with United States allies;\n**(2)**\naligning public diplomacy efforts; and\n**(3)**\nencouraging collaboration between United States embassies and Taiwan's representative offices in Latin America and the Caribbean.",
      "versionDate": "2025-09-02",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2684rs.xml",
      "text": "II\nCalendar No. 242\n119th CONGRESS\n1st Session\nS. 2684\nIN THE SENATE OF THE UNITED STATES\nSeptember 2, 2025 Mr. Merkley (for himself, Mr. Curtis , Mr. Kaine , Mr. Ricketts , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo support countries in Latin America and the Caribbean that maintain official diplomatic relations with Taiwan, to counter efforts by the People's Republic of China to coerce or pressure governments into breaking such ties, to deepen coordination with Taiwan on diplomatic, development, and economic engagement in the Western Hemisphere, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States-Taiwan Partnership in the Americas Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nTaiwan is a democratic partner of the United States, and countries that maintain ties with Taiwan often share our Nation's commitment to transparency, good governance, and human rights.\n**(2)**\nThe People\u2019s Republic of China has pressured Taiwan\u2019s remaining 7 diplomatic allies in Latin America and the Caribbean to sever diplomatic relations with Taiwan by leveraging opaque development deals and backroom pressure.\n**(3)**\nThe United States has an interest in ensuring countries in Latin America and the Caribbean can make sovereign foreign policy decisions free from coercion or financial manipulation by the People's Republic of China.\n#### 3. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto support countries in Latin America and the Caribbean that maintain diplomatic relations with Taiwan;\n**(2)**\nto counter efforts by the People's Republic of China to coerce or pressure governments in the region into breaking diplomatic ties with Taiwan; and\n**(3)**\nto deepen coordination with Taiwan on its development and economic engagement in the Western Hemisphere.\n#### 4. Monitoring the economic influence of the People's Republic of China\n##### (a) Infrastructure influence risk mechanism\nThe Secretary of State shall establish a mechanism to track and respond to infrastructure and development projects by the People's Republic of China in countries that maintain diplomatic relations with Taiwan.\n##### (b) Functions\nThe mechanism required under subsection (a) shall\u2014\n**(1)**\nidentify projects referred to in such subsection that carry strategic risks or involve non-transparent financing;\n**(2)**\ncoordinate appropriate United States diplomatic or technical responses to such projects; and\n**(3)**\nshare relevant information with Congress and with United States allies.\n#### 5. Reporting requirements\n##### (a) Semiannual status report\nThe Secretary of State shall submit semiannual status reports to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives regarding governments in Latin America that have taken steps to discontinue diplomatic relations with Taiwan.\n##### (b) Diplomatic engagement plan\nIf the Secretary of State determines that a government in a country referred to in subsection (a) is taking steps to terminate diplomatic relations with Taiwan, the Secretary, not later than 30 days after such determination, shall submit a report to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives that includes a detailed plan to support the maintenance of official diplomatic relations between such government and Taiwan.\n##### (c) Annual report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for the following 5 years, the Secretary of State shall submit a report to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives that includes\u2014\n**(A)**\nan assessment of the goals, investments, and interests of the People\u2019s Republic of China in Latin America and the Caribbean that maintain diplomatic relations with Taiwan;\n**(B)**\nan overview of the pressure tactics and influence campaigns carried out by the People\u2019 s Republic of China in countries in Latin America and the Caribbean that maintain diplomatic relations with Taiwan; and\n**(C)**\nthe actions taken by the Department of State during the most recent 12-month period to implement this Act by\u2014\n**(i)**\nsupporting Taiwan\u2019s diplomatic partners in Latin America and the Caribbean; and\n**(ii)**\ncountering the efforts of the People\u2019s Republic of China to isolate Taiwan from its Latin American and Caribbean allies.\n**(2) Form**\nEach report required under paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n#### 6. Taiwan\u2013Americas strategic coordination\nThe Secretary of State should take steps to expand United States coordination with countries in Latin America and the Caribbean with respect to Taiwan by\u2014\n**(1)**\ncoordinating joint programming and technical cooperation with United States allies;\n**(2)**\naligning public diplomacy efforts; and\n**(3)**\nencouraging collaboration between United States embassies and Taiwan's representative offices in Latin America and the Caribbean.",
      "versionDate": "2025-10-30",
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
            "name": "Asia",
            "updateDate": "2026-01-30T19:19:13Z"
          },
          {
            "name": "Caribbean area",
            "updateDate": "2026-01-30T19:19:35Z"
          },
          {
            "name": "China",
            "updateDate": "2026-01-30T19:20:43Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-30T19:20:01Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-01-30T19:19:43Z"
          },
          {
            "name": "Economic development",
            "updateDate": "2026-01-30T19:19:54Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2026-01-30T19:20:31Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2026-01-30T19:20:20Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-01-30T19:20:12Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2026-01-30T19:19:25Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2026-01-30T19:20:37Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2026-01-30T19:19:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-11T21:28:17Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2684is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2684rs.xml"
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
      "title": "United States - Taiwan Partnership in the Americas Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:44Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "United States - Taiwan Partnership in the Americas Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States-Taiwan Partnership in the Americas Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-05T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to support countries in Latin America and the Caribbean that maintain official diplomatic relations with Taiwan, to counter efforts by the People's Republic of China to coerce or pressure governments into breaking such ties, to deepen coordination with Taiwan on diplomatic, development, and economic engagement in the Western Hemisphere, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-05T04:18:24Z"
    }
  ]
}
```
