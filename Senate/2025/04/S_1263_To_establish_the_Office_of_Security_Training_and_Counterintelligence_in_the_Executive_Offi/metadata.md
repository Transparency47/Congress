# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1263?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1263
- Title: Operational Security Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1263
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2025-05-28T14:18:45Z
- Update date including text: 2025-05-28T14:18:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2141-2142: 2)
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2141-2142: 2)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1263",
    "number": "1263",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Operational Security Act of 2025",
    "type": "S",
    "updateDate": "2025-05-28T14:18:45Z",
    "updateDateIncludingText": "2025-05-28T14:18:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S2141-2142: 2)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-02",
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
        "item": {
          "date": "2025-04-02T20:26:01Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1263is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1263\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Schumer (for himself, Mr. Schiff , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish the Office of Security Training and Counterintelligence in the Executive Office of the President, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Operational Security Act of 2025 .\n#### 2. Office of Security Training and Counterintelligence of Executive Office of the President\n##### (a) Office of Security Training and Counterintelligence\nThere is in the Executive Office of the President an Office of Security Training and Counterintelligence (in this section referred to as the Office ).\n##### (b) Director\n**(1) In general**\nThere shall be at the head of the Office a Director of the Office of Security Training and Counterintelligence (in this section referred to as the Director ) who shall be appointed by the President, by and with the advice and consent of the Senate.\n**(2) Initial appointment**\nThe President shall make an initial appointment of the Director not later than the date that is 30 days after the date of the enactment of this Act.\n**(3) Qualifications of the Director**\nThe Director shall\u2014\n**(A)**\nbe a recognized security expert, including expertise in cybersecurity, physical security, or counterintelligence; and\n**(B)**\nbe eligible to access classified information at the level of Top Secret and be eligible to access sensitive compartmented information.\n##### (c) Detailees\n**(1) In general**\nSubject to paragraph (3), the Office shall be staffed by career security and counterintelligence professionals detailed from Federal agencies.\n**(2) From Office of Director of National Intelligence**\nSubject to paragraph (3), the Director of National Intelligence may detail to the Office any of the personnel of the Office of the Director of National Intelligence to assist in carrying out the functions of the Office under subsection (e).\n**(3) Clearance**\nAny personnel detailed to the Office under this subsection shall possess a security clearance in accordance with applicable laws and regulations concerning the handling of classified information.\n##### (d) Functions\nThe primary functions of the Office are to provide, within the Executive Office of the President, advice on the following:\n**(1) Security training**\nTraining, education, and research activities to equip and prepare personnel of the Executive Office of the President through the development and management of on-line and in-person courses, curricula, conferences, and other products.\n**(2) Counterintelligence and insider threat**\nActivities to identify, assess, deter, and mitigate foreign and insider threats to the Executive Office of the President, both directly and through collaborative engagement with other intelligence and law enforcement organizations.\n**(3) Protection of classified information**\nProtection and preservation of classified information and other sensitive information, including with regard to the use by personnel of the Executive Office of the President of unclassified commercially available messaging applications, as well as preservation of such information through collaborative engagement with the National Archives and Records Administration.\n##### (e) Advisory Board\n**(1) Establishment**\n**(A) In general**\nThere is hereby established an advisory board to advise the President, the Assistant to the President for National Security Affairs, the Director of the Office, and such other personnel of the Executive Office of the President as the Board considers appropriate on best practices in security training, counterintelligence and insider threats, and protection of classified information.\n**(B) Designation**\nThe advisory board established by subparagraph (A) shall be known as the Security Training and Counterintelligence Advisory Board (in this section referred to as the Board ).\n**(2) Membership**\n**(A) Composition**\nSubject to subparagraph (B), the Board shall be composed of 4 members, appointed as follows:\n**(i)**\nOne member appointed by the Democratic leader of the Senate.\n**(ii)**\nOne member appointed by the Republican leader of the Senate.\n**(iii)**\nOne member appointed by the Democratic leader of the House of Representatives.\n**(iv)**\nOne member appointed by the Republican leader of the House of Representatives.\n**(B) Criteria**\nThe members appointed under subparagraph (A) shall meet the following criteria:\n**(i)**\nEach member shall be a recognized expert in security, including expertise in cybersecurity, physical security, or counterintelligence.\n**(ii)**\nEach member shall be eligible to access classified information at the level of Top Secret and be eligible to access sensitive compartmented information.\n**(C) Terms**\n**(i) In general**\nEach member appointed to the Board, including the Chairperson selected under paragraph (3), shall be appointed or elected, as applicable, for a 2-year term and members of the Board may be reappointed for additional terms of service as members of the Board. Members may continue to serve until they are either reappointed or replaced.\n**(ii) Annual reports**\nThe Board shall submit to the congressional intelligence committees (as defined in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )), in writing, an annual report which shall set forth the recommendations of the Board for improving security training, counterintelligence and insider threat awareness, and the protection of classified information and other sensitive information used by personnel of the Executive Office of the President.\n**(3) Chairperson**\n**(A) In general**\nDuring the first meeting of the Board, the members of the Board shall elect a Chairperson of the Board.\n**(B) Limitation**\nIn addition to meeting the criteria under paragraph (2)(B), the Chairperson may not be an employee, or former employee, of the Executive Office of the President.",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T14:18:45Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1263is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Operational Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Operational Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Office of Security Training and Counterintelligence in the Executive Office of the President, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:18:49Z"
    }
  ]
}
```
