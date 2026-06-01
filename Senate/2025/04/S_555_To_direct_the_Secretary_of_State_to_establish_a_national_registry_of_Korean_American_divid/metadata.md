# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/555?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/555
- Title: Korean American Divided Families National Registry Act
- Congress: 119
- Bill type: S
- Bill number: 555
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2025-09-05T11:03:18Z
- Update date including text: 2025-09-05T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 51.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 51.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/555",
    "number": "555",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Korean American Divided Families National Registry Act",
    "type": "S",
    "updateDate": "2025-09-05T11:03:18Z",
    "updateDateIncludingText": "2025-09-05T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 51.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-28",
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
      "actionDate": "2025-04-28",
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
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
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
            "date": "2025-04-28T20:37:27Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-27T17:57:30Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-12T22:43:44Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
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
      "sponsorshipDate": "2025-02-12",
      "state": "DE"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "AZ"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s555is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 555\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Kaine (for himself, Mr. Cruz , Mr. Coons , Mr. Kelly , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo direct the Secretary of State to establish a national registry of Korean American divided families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Korean American Divided Families National Registry Act .\n#### 2. National registry of Korean American divided families\n##### (a) In general\nThe Secretary of State, acting through the Special Envoy on North Korean Human Rights Issues, the Assistant Secretary of State for Consular Affairs, or such other individual as the Secretary may designate, shall\u2014\n**(1)**\nidentify Korean American families who wish to be reunited with family members residing in North Korea from which such Korean American families were divided after the signing of the Agreement Concerning a Military Armistice in Korea, signed at Panmunjom July 27, 1953 (commonly referred to as the Korean War Armistice Agreement ), in anticipation of future reunions for such families and family members, including in-person and video reunions; and\n**(2)**\nestablish a national registry of the names and other relevant information of such Korean American families\u2014\n**(A)**\nto facilitate such future reunions; and\n**(B)**\nto provide for a repository of information about such Korean American families and family members in North Korea, including information about individuals who may be deceased.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary of State $1,000,000 to carry out this section.\n#### 3. Actions to facilitate dialogue between the United States and North Korea\n##### (a) In general\nThe Secretary of State should take such actions as may be necessary to ensure that any direct dialogue between the United States and North Korea includes progress towards holding future reunions for Korean American families and their family members in North Korea.\n##### (b) Consultations\nThe Secretary of State should consult with the Government of the Republic of Korea, as appropriate, in carrying out this section.\n##### (c) Reporting requirement\n**(1) In general**\nThe Secretary of State, acting through the Special Envoy on North Korean Human Rights Issues, shall include in each report required under section 107(d) of the North Korean Human Rights Act of 2004 ( 22 U.S.C. 7817(d) ) a description of the consultations described in subsection (b) conducted during the year preceding the submission of the report.\n**(2) Elements**\nThe reporting required under paragraph (1) should include\u2014\n**(A)**\nthe status of the national registry established pursuant to section 2(a)(2);\n**(B)**\nthe number of individuals included on the registry who\u2014\n**(i)**\nhave met their family members in North Korea during previous reunions; and\n**(ii)**\nhave yet to meet their family members in North Korea during previous reunions;\n**(C)**\na summary of responses by North Korea to requests to hold reunions of divided families; and\n**(D)**\na description of actions taken by North Korea that prevent the emigration of family members of Korean American families.\n##### (d) Appropriate congressional committees defined\nIn this Act, the term appropriate congressional committees means the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2025-02-12",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s555rs.xml",
      "text": "II\nCalendar No. 51\n119th CONGRESS\n1st Session\nS. 555\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Kaine (for himself, Mr. Cruz , Mr. Coons , Mr. Kelly , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nApril 28, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo direct the Secretary of State to establish a national registry of Korean American divided families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Korean American Divided Families National Registry Act .\n#### 2. National registry of Korean American divided families\n##### (a) In general\nThe Secretary of State, acting through the Special Envoy on North Korean Human Rights Issues, the Assistant Secretary of State for Consular Affairs, or such other individual as the Secretary may designate, shall\u2014\n**(1)**\nidentify Korean American families who wish to be reunited with family members residing in North Korea from which such Korean American families were divided after the signing of the Agreement Concerning a Military Armistice in Korea, signed at Panmunjom July 27, 1953 (commonly referred to as the Korean War Armistice Agreement ), in anticipation of future reunions for such families and family members, including in-person and video reunions; and\n**(2)**\nestablish a national registry of the names and other relevant information of such Korean American families\u2014\n**(A)**\nto facilitate such future reunions; and\n**(B)**\nto provide for a repository of information about such Korean American families and family members in North Korea, including information about individuals who may be deceased.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary of State $1,000,000 to carry out this section.\n#### 3. Actions to facilitate dialogue between the United States and North Korea\n##### (a) In general\nThe Secretary of State should take such actions as may be necessary to ensure that any direct dialogue between the United States and North Korea includes progress towards holding future reunions for Korean American families and their family members in North Korea.\n##### (b) Consultations\nThe Secretary of State should consult with the Government of the Republic of Korea, as appropriate, in carrying out this section.\n##### (c) Reporting requirement\n**(1) In general**\nThe Secretary of State, acting through the Special Envoy on North Korean Human Rights Issues, shall include in each report required under section 107(d) of the North Korean Human Rights Act of 2004 ( 22 U.S.C. 7817(d) ) a description of the consultations described in subsection (b) conducted during the year preceding the submission of the report.\n**(2) Elements**\nThe reporting required under paragraph (1) should include\u2014\n**(A)**\nthe status of the national registry established pursuant to section 2(a)(2);\n**(B)**\nthe number of individuals included on the registry who\u2014\n**(i)**\nhave met their family members in North Korea during previous reunions; and\n**(ii)**\nhave yet to meet their family members in North Korea during previous reunions;\n**(C)**\na summary of responses by North Korea to requests to hold reunions of divided families; and\n**(D)**\na description of actions taken by North Korea that prevent the emigration of family members of Korean American families.\n##### (d) Appropriate congressional committees defined\nIn this Act, the term appropriate congressional committees means the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives.",
      "versionDate": "2025-04-28",
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
            "updateDate": "2025-05-14T13:04:06Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-14T13:04:33Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-05-14T13:04:24Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-05-14T13:04:06Z"
          },
          {
            "name": "Family services",
            "updateDate": "2025-05-14T13:04:06Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-14T13:04:06Z"
          },
          {
            "name": "North Korea",
            "updateDate": "2025-05-14T13:04:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-08T15:32:28Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s555is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s555rs.xml"
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
      "title": "Korean American Divided Families National Registry Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-05T11:03:18Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Korean American Divided Families National Registry Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-01T02:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Korean American Divided Families National Registry Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of State to establish a national registry of Korean American divided families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:32Z"
    }
  ]
}
```
